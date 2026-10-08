# -*- coding: utf-8 -*-
"""
盘点中文侧（docs/zh）在产品分类页 / 支持中心上的缺口。

三层判据：
  1. 目录结构差集：EN 有而 ZH 无（含分类页目录、support 文件）
  2. nav 引用检查：mkdocs.yml 里 zh nav 挂的路径，中文源是否存在
  3. 链接可达性：docs/zh 全部 md 的本地链接
       OK       -> 中文源存在
       FALLBACK -> 中文源缺失但英文源存在（i18n 渲染英文内容副本，不 404）
       MISS     -> 两平台都没有（真 404）
"""
import os
import re
import sys
import urllib.parse

sys.stdout.reconfigure(encoding="utf-8")

ROOT = r"D:\GitHub\wiki"
DOCS = os.path.join(ROOT, "docs")
EN = os.path.join(DOCS, "en")
ZH = os.path.join(DOCS, "zh")

MARKDOWN_LINK = re.compile(r"\]\(([^)\s]+)\)")
HTML_ATTR = re.compile(r'(?:src|href)\s*=\s*"([^"]+)"')
HTML_COMMENT = re.compile(r"<!--.*?-->", re.S)


def strip_comments(txt):
    """去掉 HTML 注释：注释内的链接不渲染，不应计入死链。"""
    return HTML_COMMENT.sub(lambda m: "\n" * m.group(0).count("\n"), txt)


def norm(base, url, cur_file):
    """把链接解析成绝对路径；返回 None 表示非本地目标"""
    u = url.split("#")[0].strip()
    if not u or u.startswith(("http://", "https://", "mailto:", "tel:", "#", "//")):
        return None
    u = urllib.parse.unquote(u)
    d = os.path.dirname(cur_file)
    p = os.path.normpath(os.path.join(d, u))
    return p


def resolve(p):
    """判定一个绝对路径目标的状态"""
    for cand in (p, p + ".md", os.path.join(p, "index.md")):
        if os.path.isfile(cand):
            return True, cand
    if os.path.isdir(p):
        return True, p
    return False, p


def state_of(target, cur_file):
    ok, real = resolve(target)
    if ok:
        return "OK", real
    # 换算成 docs 相对路径，用于找英文对应
    try:
        rel = os.path.relpath(target, DOCS).replace("\\", "/")
    except ValueError:
        return "MISS", target
    if rel.startswith("zh/"):
        en_rel = "en/" + rel[3:]
        en_abs = os.path.join(DOCS, en_rel)
        ok2, _ = resolve(en_abs)
        if ok2:
            return "FALLBACK", en_rel
    return "MISS", rel


def walk(base):
    s = set()
    for root, _dirs, files in os.walk(base):
        for f in files:
            s.add(os.path.relpath(os.path.join(root, f), base).replace("\\", "/"))
    return s


print("=" * 80)
print("① 产品分类页：EN 顶层目录 vs ZH 顶层目录")
print("=" * 80)
en_dirs = sorted(d for d in os.listdir(os.path.join(EN, "products"))
                 if os.path.isdir(os.path.join(EN, "products", d)))
zh_dirs = set(d for d in os.listdir(os.path.join(ZH, "products"))
              if os.path.isdir(os.path.join(ZH, "products", d)))
CAT = ["amoled", "embedded", "esp32", "hdmi", "mipi", "tft", "transflective"]
print("EN 分类页目录：%s" % ", ".join(CAT))
print()
print("%-16s %-10s %-12s %s" % ("分类", "ZH 源", "ZH 有 index", "状态"))
for c in CAT:
    in_zh = c in zh_dirs
    idx = os.path.isfile(os.path.join(ZH, "products", c, "index.md"))
    if idx:
        st = "OK 中文源存在"
    elif in_zh:
        st = "WARN 目录在但无 index.md"
    else:
        st = "MISS 无中文源 → /zh/ 下渲染英文副本"
    print("%-16s %-10s %-12s %s" % (c, "有" if in_zh else "无", "有" if idx else "无", st))

print()
print("=" * 80)
print("② 支持中心：EN vs ZH 文件级差集")
print("=" * 80)
en_all = walk(os.path.join(EN, "support"))
zh_all = walk(os.path.join(ZH, "support"))
en_files = sorted(f for f in en_all if not f.endswith(".bak") and not f.endswith(".bak260415"))
zh_files = sorted(zh_all)
print("EN support 有效文件 = %d ；ZH support 文件 = %d" % (len(en_files), len(zh_files)))
print()
print("--- ZH 缺失 ---")
for f in en_files:
    if f in zh_all:
        print("   OK        support/" + f)
    else:
        nav = "【zh nav 挂着】" if f in ("resource.md", "tutorials.md") else ""
        print("   MISSING   support/%-58s %s" % (f, nav))
print()
print("--- ZH 独有 ---")
for f in zh_files:
    if f not in en_all:
        print("   ONLY      support/" + f)

print()
print("=" * 80)
print("③ zh nav 引用路径可达性")
print("=" * 80)
nav_zh = [
    ("products/esp32/index.md", "ESP32 智能屏"),
    ("products/embedded/index.md", "嵌入式系统"),
    ("products/hdmi/index.md", "HDMI 显示屏"),
    ("products/mipi/index.md", "MIPI DSI 显示屏"),
    ("products/tft/index.md", "TFT 液晶屏"),
    ("products/amoled/index.md", "AMOLED 显示屏"),
    ("products/transflective/index.md", "半反半透屏"),
    ("support/resource.md", "资源中心"),
    ("support/tutorials.md", "教程指南"),
    ("knowledge/tags.md", "知识库"),
    ("support/faq.md", "常见问题"),
]
for rel, label in nav_zh:
    p = os.path.join(ZH, rel)
    ok, _ = resolve(p)
    if ok:
        st = "OK 中文源存在"
    else:
        ok2, _ = resolve(os.path.join(EN, rel))
        st = "FALLBACK 无中文源 → 渲染英文副本" if ok2 else "MISS 真 404"
    print("   %-34s %-14s %s" % (rel, label, st))

print()
print("=" * 80)
print("④ docs/zh 全库本地链接可达性（只列 FALLBACK 与 MISS）")
print("=" * 80)
fbs, misses = [], []
for root, _dirs, files in os.walk(ZH):
    for f in files:
        if not f.endswith(".md"):
            continue
        fp = os.path.join(root, f)
        txt = strip_comments(open(fp, encoding="utf-8", errors="replace").read())
        for url in set(MARKDOWN_LINK.findall(txt)) | set(HTML_ATTR.findall(txt)):
            t = norm(ZH, url, fp)
            if t is None:
                continue
            st, info = state_of(t, fp)
            relf = os.path.relpath(fp, ROOT).replace("\\", "/")
            if st == "FALLBACK":
                fbs.append((relf, url, info))
            elif st == "MISS":
                misses.append((relf, url, info))
print("--- FALLBACK（可开、内容是英文）：%d 处 / %d 个目标 ---" % (len(fbs), len({x[2] for x in fbs})))
for tgt in sorted({x[2] for x in fbs}):
    print("   %s" % tgt)
print()
print("--- MISS（真 404）：%d 处 ---" % len(misses))
for relf, url, info in sorted(set(misses)):
    print("   %-62s -> %s" % (relf.replace("docs/zh/", ""), url))
