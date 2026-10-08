# -*- coding: utf-8 -*-
"""ESP32 系列产品页 中英对照核实
用法: python outputs/check_esp32_product_pages.py
"""
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EN = os.path.join(ROOT, "docs", "en", "products")
ZH = os.path.join(ROOT, "docs", "zh", "products")

RE_TITLE = re.compile(r"^title:\s*(.+)$", re.M)
RE_DESC = re.compile(r"^description:\s*(.+)$", re.M)
RE_H1 = re.compile(r"^#\s+(.+)$", re.M)


def info(path):
    raw = open(path, "rb").read()
    txt = raw.decode("utf-8", "replace")
    fm = txt.startswith("---")
    m_title = RE_TITLE.search(txt)
    m_desc = RE_DESC.search(txt)
    m_h1 = RE_H1.search(txt)
    return {
        "fm": fm,
        "title": m_title.group(1).strip() if m_title else None,
        "desc": m_desc.group(1).strip() if m_desc else None,
        "h1": m_h1.group(1).strip() if m_h1 else None,
        "crlf": raw.count(b"\r\n") > 0,
    }


def esp32_dirs(base):
    out = {}
    if not os.path.isdir(base):
        return out
    for name in sorted(os.listdir(base)):
        if not name.startswith("esp32") or name == "esp32":
            continue
        p = os.path.join(base, name)
        if not os.path.isdir(p):
            continue
        idx = os.path.join(p, "index.md")
        out[name] = info(idx) if os.path.isfile(idx) else None
    return out


def main():
    en = esp32_dirs(EN)
    zh = esp32_dirs(ZH)
    en_pages = [k for k, v in en.items() if v]
    zh_pages = [k for k, v in zh.items() if v]

    print("EN ESP32 系列产品页: %d" % len(en_pages))
    print("ZH ESP32 系列产品页: %d" % len(zh_pages))
    print("-" * 78)

    miss = [k for k in en_pages if k not in zh]
    print(">>> ZH 缺失 = %d" % len(miss))
    for i, k in enumerate(miss, 1):
        v = en[k]
        print("%2d. %s" % (i, k))
        print("      H1  : %s" % v["h1"])
        print("      FM  : %s | title:%s | desc:%s" % (
            "有" if v["fm"] else "无",
            "有" if v["title"] else "无",
            "有" if v["desc"] else "无",
        ))
    print("-" * 78)

    print(">>> ZH 已有 = %d" % len(zh_pages))
    for k in zh_pages:
        v = zh[k]
        e = en.get(k)
        print("  [%s] %s" % ("中英齐全" if e else "EN 无", k))
        print("      ZH H1: %s" % v["h1"])
        print("      ZH FM: %s | title:%s | desc:%s" % (
            "有" if v["fm"] else "无",
            "有" if v["title"] else "无",
            "有" if v["desc"] else "无",
        ))
        if e:
            print("      EN FM: %s | title:%s | desc:%s" % (
                "有" if e["fm"] else "无",
                "有" if e["title"] else "无",
                "有" if e["desc"] else "无",
            ))
        print("      ZH 行尾: %s" % ("CRLF" if v["crlf"] else "LF"))
    print("-" * 78)

    empty = [k for k, v in en.items() if v is None]
    print(">>> 英文侧「目录存在但无 index.md」= %d: %s" % (len(empty), empty or "(无)"))
    print(">>> 英文侧 FM 覆盖率: %d / %d" % (sum(1 for k in en_pages if en[k]["fm"]), len(en_pages)))
    print(">>> 中文侧 FM 覆盖率: %d / %d" % (sum(1 for k in zh_pages if zh[k]["fm"]), len(zh_pages)))


if __name__ == "__main__":
    main()
