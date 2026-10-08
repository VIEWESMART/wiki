# -*- coding: utf-8 -*-
"""检查英文产品页引用的本地资源是否存在。
用法: python outputs/check_product_assets.py
"""
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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
RE_MDLINK = re.compile(r"\]\(([^)#\s]+)\)")


def main():
    bad_total = 0
    for slug in SLUGS:
        p = os.path.join(ENP, slug, "index.md")
        if not os.path.isfile(p):
            print("[!] %s 不存在" % slug)
            continue
        txt = open(p, encoding="utf-8").read()
        print("=" * 74)
        print(slug)
        refs = []
        for m in RE_SRC.finditer(txt):
            refs.append(m.group(1))
        for m in RE_MDLINK.finditer(txt):
            u = m.group(1)
            if u.startswith(("http", "mailto:", "#")):
                continue
            refs.append(u)
        seen = set()
        for r in refs:
            r = r.split("#")[0]
            if not r or r in seen:
                continue
            seen.add(r)
            if r.startswith("../"):
                target = os.path.normpath(os.path.join(ENP, slug, r))
            else:
                target = os.path.normpath(os.path.join(ENP, slug, r))
            ok = os.path.isfile(target) or os.path.isdir(target)
            if not ok:
                bad_total += 1
                print("   MISS  %s" % r)
            else:
                print("   ok    %s" % r)
    print("=" * 74)
    print("缺失引用合计: %d" % bad_total)


if __name__ == "__main__":
    main()
