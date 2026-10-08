# -*- coding: utf-8 -*-
"""校验 6 个中文产品分类页：结构对照 / FM / CRLF / 品牌渠道 / 本地链接可达性。

用法：python outputs/verify_zh_category_pages.py
"""
import io
import os
import re
import sys
import urllib.parse

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENP = os.path.join(ROOT, "docs", "en", "products")
ZHP = os.path.join(ROOT, "docs", "zh", "products")

SLUGS = ["amoled", "embedded", "hdmi", "mipi", "tft", "transflective"]

RE_MD = re.compile(r"\]\(([^)\s]+)\)")
RE_HTML = re.compile(r'(?:src|href)\s*=\s*"([^"]+)"')
RE_TABTITLE = re.compile(r'^=== "(.*)"\s*$', re.M)
RE_COMMENT = re.compile(r"<!--.*?-->", re.S)


def read(p):
    return io.open(p, encoding="utf-8", errors="replace").read().replace("\r\n", "\n")


def counts(txt):
    lines = txt.split("\n")
    return {
        "h1": sum(1 for l in lines if l.startswith("# ")),
        "h2": sum(1 for l in lines if l.startswith("## ")),
        "h3": sum(1 for l in lines if l.startswith("### ")),
        "admon": sum(1 for l in lines if l.startswith("!!!")),
        "tab": sum(1 for l in lines if l.startswith("=== ")),
        "grid": txt.count("grid cards"),
        "card": sum(1 for l in lines if l.startswith("-   ") or l.startswith("    -   ")),
        "br": sum(1 for l in lines if l.strip() == "<br>"),
        "hr": sum(1 for l in lines if l.strip() == "---" and l == "---"),
        "table": sum(1 for l in lines if l.startswith("|")),
        "anchor": len(re.findall(r"\{:\s*#[^}]+\}", txt)),
    }


def check_links(txt, slug):
    """返回 (ok, fallback, dead)。fallback = 中文源缺但英文源有。"""
    base = os.path.join(ZHP, slug)
    en_base = os.path.join(ENP, slug)
    body = RE_COMMENT.sub("", txt)
    urls = []
    for m in RE_MD.finditer(body):
        urls.append(m.group(1))
    for m in RE_HTML.finditer(body):
        urls.append(m.group(1))

    ok, fb, dead = [], [], []
    for u in urls:
        if u.startswith(("http://", "https://", "mailto:", "#", "tel:")):
            continue
        z = u.split("#")[0]
        if not z:
            continue
        local = os.path.normpath(os.path.join(base, urllib.parse.unquote(z)))
        if os.path.isfile(local) or os.path.isdir(local):
            ok.append(u)
            continue
        rel = os.path.relpath(local, os.path.join(ROOT, "docs", "zh")).replace("\\", "/")
        en_try = os.path.normpath(os.path.join(ROOT, "docs", "en", rel))
        if os.path.isfile(en_try) or os.path.isdir(en_try):
            fb.append(u)
        else:
            dead.append(u)
    return ok, fb, dead


def main():
    print("=" * 96)
    print("A. 结构对照（ZH vs EN）")
    print("=" * 96)
    print("%-16s %-24s %s" % ("指标", "amoled/embedded/hdmi/mipi/tft/transflective", "判定"))
    bad = 0
    for slug in SLUGS:
        ep = os.path.join(ENP, slug, "index.md")
        zp = os.path.join(ZHP, slug, "index.md")
        if not os.path.isfile(zp):
            print("  [MISS] zh/products/%s/index.md" % slug)
            bad += 1
            continue
        e, z = counts(read(ep)), counts(read(zp))
        diffs = [k for k in e if e[k] != z[k]]
        flag = "OK" if not diffs else "DIFF %s" % {
            k: "%s->%s" % (e[k], z[k]) for k in diffs
        }
        if diffs:
            bad += 1
        print("  %-14s %s" % (slug, flag))
    print()

    print("=" * 96)
    print("B. front matter / 行尾 / 品牌渠道")
    print("=" * 96)
    for slug in SLUGS:
        zp = os.path.join(ZHP, slug, "index.md")
        raw = io.open(zp, "rb").read()
        crlf = raw.count(b"\r\n")
        lf_only = raw.count(b"\n") - crlf
        txt = raw.decode("utf-8", "replace").replace("\r\n", "\n")
        fm = txt.startswith("---\n")
        ti = re.search(r"^title:\s*(.+)$", txt.split("---\n")[1] if fm else "", re.M)
        leak = {
            "viewedisplay.com": len(re.findall(r"viewedisplay\.com", txt)),
            "github.com": len(re.findall(r"github\.com", txt)),
            "shop..taobao": len(re.findall(r"shop277726935\.taobao\.com", txt)),
            "chinasunyee": len(re.findall(r"chinasunyee\.com", txt)),
            "gitee": len(re.findall(r"gitee\.com", txt)),
        }
        # 裸 VIEWE（排除 URL / 型号）
        bare = [l for l in txt.split("\n") if "VIEWE" in l and "VIEWESMART" not in l]
        print("  %-14s FM=%-5s title=%-28s CRLF=%-4d LFonly=%-3d 裸VIEWE=%d" % (
            slug, fm, (ti.group(1).strip() if ti else "(缺)"), crlf, lf_only, len(bare)))
        print("     渠道: " + "  ".join("%s=%d" % kv for kv in leak.items()))
        for l in bare:
            print("       ! 裸 VIEWE: " + l.strip()[:100])
        if lf_only:
            bad += 1
    print()

    print("=" * 96)
    print("C. 本地链接可达性")
    print("=" * 96)
    for slug in SLUGS:
        zp = os.path.join(ZHP, slug, "index.md")
        txt = read(zp)
        ok, fb, dead = check_links(txt, slug)
        print("  %-14s  OK=%-3d fallback=%-3d dead=%-3d" % (slug, len(ok), len(fb), len(dead)))
        for u in fb:
            print("      [fallback 中文源缺] " + u)
        for u in dead:
            print("      [DEAD] " + u)
            bad += 1
    print()

    print("=" * 96)
    print("D. tab 标题内的 ASCII 双引号（会破坏 tabbed 语法）")
    print("=" * 96)
    for slug in SLUGS:
        txt = read(os.path.join(ZHP, slug, "index.md"))
        for m in RE_TABTITLE.finditer(txt):
            inner = m.group(1)
            if '"' in inner:
                print("  [BAD] %s -> %s" % (slug, m.group(0)))
                bad += 1
    print("  （无输出即全部通过）")
    print()

    print("=" * 96)
    print("E. 中文 nav 六项落地检查")
    print("=" * 96)
    for slug in SLUGS:
        zp = os.path.join(ZHP, slug, "index.md")
        site = os.path.join(ROOT, "site", "zh", "products", slug, "index.html")
        print("  源文件 %-14s %s   |  产物 %s" % (
            slug, "有" if os.path.isfile(zp) else "缺",
            "有" if os.path.isfile(site) else "缺(未构建)"))
    print()
    print("问题总数 = %d" % bad)


if __name__ == "__main__":
    main()
