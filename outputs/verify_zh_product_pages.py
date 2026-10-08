# -*- coding: utf-8 -*-
"""校验新建中文产品页：结构 + 行尾 + 链接规范 + 图片存在性。
用法: python outputs/verify_zh_product_pages.py
"""
import os
import re
import sys
from urllib.parse import unquote

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ZHP = os.path.join(ROOT, "docs", "zh", "products")
DOCS_ZH = os.path.join(ROOT, "docs", "zh")
ENP = os.path.join(ROOT, "docs", "en", "products")

SLUGS = [
    "esp32-UEDX46466015-MD50ET",
    "esp32-c3-1.3-knob",
    "esp32-s3-2.1-touch-knob",
    "esp32-s3-1.9inch-170x320-touch-uart-display-hmi",
    "esp32-s3-2.4inch-240x320-touch-uart-display-hmi",
    "esp32-s3-2.8inch-240x320-touch-uart-display-hmi",
    "esp32-s3-3.5inch-240x320-touch-uart-display-hmi",
    "esp32-s3-3.5inch-320x480-touch-uart-display-hmi",
    "esp32-s3-4.3inch-480x272-touch-uart-display-hmi",
    "esp32-s3-4.3inch-800x480-touch-uart-display-hmi",
    "esp32-s3-5inch-800x480-touch-uart-display-hmi",
]

RE_SRC = re.compile(r'src="([^"]+)"')
RE_H2 = re.compile(r"^##\s+(?!#)(.*)$", re.M)
RE_FAQ = re.compile(r'^\?\?\? question\s+"(.*)"\s*$', re.M)
RE_TITLE = re.compile(r"^title:\s*(.+)$", re.M)
RE_DESC = re.compile(r"^description:\s*(.+)$", re.M)

problems = []


def check(slug):
    fp = os.path.join(ZHP, slug, "index.md")
    row = {"slug": slug}
    if not os.path.isfile(fp):
        problems.append("%s：文件不存在" % slug)
        return row
    raw = open(fp, "rb").read()
    txt = raw.decode("utf-8")
    row["crlf"] = raw.count(b"\r\n")
    row["lf"] = raw.count(b"\n")
    row["bom"] = raw.startswith(b"\xef\xbb\xbf")
    row["lines"] = row["crlf"]
    row["fm"] = txt.startswith("---") and RE_TITLE.search(txt) and RE_DESC.search(txt)
    h2 = RE_H2.findall(txt)
    row["h2"] = len(h2)
    row["h2list"] = [h.strip() for h in h2]
    row["github"] = txt.count("github.com")
    row["taobao"] = txt.count("shop277726935.taobao.com")
    row["viewedisplay_product"] = txt.count("viewedisplay.com/product")
    row["gitee"] = len(re.findall(r"gitee\.com/VIEWESMART/[^\)\s]+", txt))
    # FAQ 标题内 ASCII 双引号
    bad_faq = []
    for m in RE_FAQ.finditer(txt):
        if '"' in m.group(1):
            bad_faq.append(m.group(1)[:40])
    row["badfaq"] = bad_faq
    # 图片/本地链接存在性
    miss = []
    fallback = []

    def probe(u):
        """返回 ('ok'|'fallback'|'miss', 原样 url)"""
        u2 = unquote(u.split("#")[0])
        if not u2:
            return ("ok", u)
        t = os.path.normpath(os.path.join(ZHP, slug, u2))
        if os.path.isfile(t) or os.path.isdir(t):
            return ("ok", u)
        # 中文源缺失但英文源存在 -> i18n fallback，不算死链
        rel = os.path.relpath(t, DOCS_ZH).replace("\\", "/")
        e = os.path.normpath(os.path.join(ROOT, "docs", "en", rel))
        if not rel.startswith("..") and (os.path.isfile(e) or os.path.isdir(e)):
            return ("fallback", u)
        return ("miss", u)

    for m in RE_SRC.finditer(txt):
        u = m.group(1)
        if not u or u.startswith(("http", "mailto:")):
            continue
        st, uu = probe(u)
        if st == "miss":
            miss.append(uu)
        elif st == "fallback":
            fallback.append(uu)
    for m in re.finditer(r"\]\(([^)#\s]+)\)", txt):
        u = m.group(1)
        if u.startswith(("http", "mailto:", "#")):
            continue
        st, uu = probe(u)
        if st == "miss":
            miss.append(uu)
        elif st == "fallback":
            fallback.append(uu)
    row["miss"] = miss
    row["fallback"] = sorted(set(fallback))

    # 判定
    if row["lf"] != row["crlf"]:
        problems.append("%s：行尾非纯 CRLF（LF=%d CRLF=%d）" % (slug, row["lf"], row["crlf"]))
    if row["bom"]:
        problems.append("%s：含 BOM" % slug)
    if not row["fm"]:
        problems.append("%s：front matter 不完整" % slug)
    if row["h2"] != 6:
        problems.append("%s：H2 数量 = %d（应为 6）" % (slug, row["h2"]))
    if row["github"]:
        problems.append("%s：出现 %d 处 github.com" % (slug, row["github"]))
    if row["taobao"] != 1:
        problems.append("%s：淘宝旗舰店链接 %d 处（应为 1）" % (slug, row["taobao"]))
    if row["viewedisplay_product"]:
        problems.append("%s：出现 viewedisplay.com/product %d 处" % (slug, row["viewedisplay_product"]))
    if row["gitee"] == 0:
        problems.append("%s：未见 Gitee 仓库链接" % slug)
    if bad_faq:
        problems.append("%s：FAQ 标题含 ASCII 双引号 %s" % (slug, bad_faq))
    if miss:
        problems.append("%s：引用了不存在的本地资源 %s" % (slug, miss))
    return row


def main():
    rows = [check(s) for s in SLUGS]
    print("=" * 100)
    print("%-56s %5s %4s %3s %4s %4s %3s %3s" % ("slug", "行数", "FM", "H2", "gh", "tb", "gt", "miss"))
    print("-" * 100)
    for r in rows:
        if "lines" not in r:
            continue
        print("%-56s %5d %4s %3d %4d %4d %3d %3d" % (
            r["slug"], r["lines"], "Y" if r["fm"] else "N", r["h2"],
            r["github"], r["taobao"], r["gitee"], len(r["miss"])))
    print("=" * 100)
    if problems:
        print("发现 %d 个问题：" % len(problems))
        for p in problems:
            print("  [!] %s" % p)
    else:
        print("全部 11 页通过结构校验")
    # 打印 H2 列表供人工核对
    print()
    for r in rows:
        if "h2list" in r:
            print("%s" % r["slug"])
            print("    " + " | ".join(r["h2list"]))


if __name__ == "__main__":
    main()
