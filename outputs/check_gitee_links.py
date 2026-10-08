#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
核验 docs/{zh,en} 下 VIEWESMART 仓库链接在目标平台上的等价地址是否存在。

用途：中文页把 GitHub 链接换成 Gitee 之前/之后，逐条实探真伪。两平台仓库内容
      并不总是一致（已发现 ESP32-P4-Pi 的 examples/esp-idf 编号与数量都不同）。

判定口径（踩坑后修正，勿改回「contents API + 状态码」）
  1. Gitee contents API 对**不存在的路径返回 200 + []**，不是 404
     → 用状态码判定会得到「全部存在」的假阳性。已弃用该接口。
  2. Gitee 匿名 API 请求几十次即 403 Rate Limit Exceeded，且是**小时级**窗口
     → 主要判据改用下面第 3 条，API 仅作目录判定的补充。
  3. **raw 地址 HTTP 状态码**：302 = 存在，404 = 不存在（文件，权威）。
     目录没有 raw 地址，改为：先查 Gitee git/trees 全量树（权威）；
     树取不到（限流 403）时退回「目录内探针文件」，全部不命中则报「无法判定」，
     不报 MISS，避免把「目录里只有子目录」误判成「不存在」。
  4. URL 里的 `%20` 等转义**必须先 unquote 再 quote**，否则二次编码成 %2520 → 假 404。
  5. 链接尾部可能粘上反引号/右括号等 markdown 噪音，需先清洗。

用法
    python outputs/check_gitee_links.py                        # GitHub 链接 → 查 Gitee
    python outputs/check_gitee_links.py --host gitee --against gitee   # 查 Gitee 链接自身
    python outputs/check_gitee_links.py --all                  # 输出全部条目
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36"}

# 目录探针：任一命中即判定目录存在（仅在拿不到 git tree 时使用）
DIR_PROBES = ("CMakeLists.txt", "main/CMakeLists.txt", "README.md", "README_CN.md",
              "index.md", "sdkconfig.defaults", ".gitignore")

_TREE_CACHE = {}


def make_re(host):
    return re.compile(
        rf"https?://{host}\.com/([A-Za-z0-9_.\-]+)/([A-Za-z0-9_.\-]+)"
        r"((?:/(?:tree|blob)/[^)\s\"'<>\]]+)?)"
    )


def http_code(url, timeout=20):
    req = urllib.request.Request(url, headers=UA, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:  # noqa: BLE001
        return -1


def api_json(url, timeout=25):
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, json.loads(r.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as e:
        return e.code, None
    except Exception as e:  # noqa: BLE001
        return -1, str(e)


def gitee_tree(owner, repo):
    """返回 (files:set, dirs:set) 或 None（限流/取不到，无法判定）。"""
    if repo in _TREE_CACHE:
        return _TREE_CACHE[repo]
    code, body = api_json(f"https://gitee.com/api/v5/repos/{owner}/{repo}"
                          "/git/trees/main?recursive=1")
    res = None
    if code == 200 and isinstance(body, dict) and "tree" in body:
        paths = {t["path"] for t in body["tree"]}
        dirs = set()
        for p in paths:
            parts = p.split("/")
            for i in range(1, len(parts)):
                dirs.add("/".join(parts[:i]))
        res = (paths, dirs)
    _TREE_CACHE[repo] = res
    return res


def raw_url(host, owner, repo, path, ref="main"):
    q = urllib.parse.quote(urllib.parse.unquote(path), safe="/")
    if host == "gitee":
        return f"https://gitee.com/{owner}/{repo}/raw/{ref}/{q}"
    return f"https://raw.githubusercontent.com/{owner}/{repo}/{ref}/{q}"


def exists(host, owner, repo, path, kind):
    """返回 True / False / None（无法判定）。"""
    if not path:
        return http_code(raw_url(host, owner, repo, "README.md")) in (200, 206, 302)

    if host == "gitee":
        tree = gitee_tree(owner, repo)
        if tree is not None:
            files, dirs = tree
            return (path in files) if kind == "blob" else (path in dirs)

    if kind == "blob":
        return http_code(raw_url(host, owner, repo, path)) in (200, 206, 302)

    # 目录 + 拿不到 tree：用探针文件，全不命中则判为「无法判定」
    for probe in DIR_PROBES:
        c = http_code(raw_url(host, owner, repo, f"{path}/{probe}"))
        time.sleep(0.3)
        if c in (200, 206, 302):
            return True
    return None


def clean(rest):
    """清洗 markdown 噪音：尾部反引号、右括号、句末标点、冗余斜杠。"""
    rest = rest.split("`")[0].strip()
    rest = rest.rstrip(".,;:)]}）》。，、")
    return rest.rstrip("/")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default="docs/zh")
    ap.add_argument("--host", default="github", choices=("github", "gitee"))
    ap.add_argument("--against", default="gitee", choices=("github", "gitee"))
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--sleep", type=float, default=0.4)
    args = ap.parse_args()
    RE_LINK = make_re(args.host)

    seen = {}
    for root, _, files in os.walk(args.dir):
        for fn in files:
            if not fn.endswith(".md"):
                continue
            fp = os.path.join(root, fn).replace("\\", "/")
            txt = open(fp, encoding="utf-8", errors="replace").read()
            for m in RE_LINK.finditer(txt):
                owner, repo, rest = m.group(1), m.group(2), clean(m.group(3) or "")
                if owner != "VIEWESMART":
                    continue  # 第三方仓库（esp-arduino-libs 等）不参与替换
                if rest.endswith(".git"):
                    rest = ""
                seen.setdefault(f"{owner}/{repo}{rest}", set()).add(fp)

    ok, bad, unknown = [], [], []
    print(f"发现 {len(seen)} 条去重后的 {args.host}::VIEWESMART 链接，"
          f"开始实探 {args.against} …\n")
    for i, key in enumerate(sorted(seen), 1):
        seg = key.split("/", 3)
        owner, repo = seg[0], seg[1]
        kind, path = "", ""
        if len(seg) > 3 and seg[2] in ("tree", "blob"):
            kind = seg[2]
            parts = seg[3].split("/", 1)
            path = parts[1] if len(parts) > 1 else ""
        r = exists(args.against, owner, repo, path, kind)
        tag = {True: "OK  ", False: "MISS", None: "????"}[r]
        print(f"  [{i:>2}/{len(seen)}] {tag} {args.against}.com/{key}")
        (ok if r is True else bad if r is False else unknown).append(key)

        if args.all:
            for f in sorted(seen[key]):
                print(f"          ← {f}")
        time.sleep(args.sleep)

    print(f"\n>>> {args.against} 存在 {len(ok)} / 不存在 {len(bad)} / 无法判定 {len(unknown)}")
    for title, group in (("不存在", bad), ("无法判定（多为限流，需人工看一眼）", unknown)):
        if group:
            print(f"\n### {title}")
            for key in group:
                print(f"  - {args.against}.com/{key}")
                for f in sorted(seen[key]):
                    print(f"      ← {f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
