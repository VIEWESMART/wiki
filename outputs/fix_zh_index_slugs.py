# -*- coding: utf-8 -*-
"""修正 docs/zh/products/esp32/index.md 里写错的 slug（保持 CRLF）。
用法: python outputs/fix_zh_index_slugs.py [--check]
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET = os.path.join(ROOT, "docs", "zh", "products", "esp32", "index.md")

# 错误 slug -> 正确 slug（英文侧实际目录名）
MAP = {
    "esp32-s3-5inch-800x480": "esp32-s3-5inch-800x480-touch-uart-display-hmi",
    "esp32-s3-4.3inch-800x480": "esp32-s3-4.3inch-800x480-touch-uart-display-hmi",
    "esp32-s3-4.3inch-480x272": "esp32-s3-4.3inch-480x272-touch-uart-display-hmi",
    "esp32-s3-3.5inch-320x480": "esp32-s3-3.5inch-320x480-touch-uart-display-hmi",
    "esp32-s3-3.5inch-240x320": "esp32-s3-3.5inch-240x320-touch-uart-display-hmi",
    "esp32-s3-2.8inch-240x320": "esp32-s3-2.8inch-240x320-touch-uart-display-hmi",
    "esp32-s3-2.4inch-240x320": "esp32-s3-2.4inch-240x320-touch-uart-display-hmi",
    "esp32-s3-1.9inch-170x320": "esp32-s3-1.9inch-170x320-touch-uart-display-hmi",
    "esp32-s3-2.1-knob": "esp32-s3-2.1-touch-knob",
    "esp32-s3-1.5-knob": "esp32-UEDX46466015-MD50ET",
}


def main():
    check_only = "--check" in sys.argv
    raw = open(TARGET, "rb").read()
    txt = raw.decode("utf-8")
    crlf_before = txt.count("\r\n")
    lf_before = txt.count("\n")

    total = 0
    for bad, good in MAP.items():
        # 只替换相对链接里的 slug（以 "../slug/)" 为完整边界），避免误伤已正确的长 slug
        needle = "../%s/)" % bad
        n = txt.count(needle)
        if n:
            txt = txt.replace(needle, "../%s/)" % good)
            total += n
            print("  %-34s -> %-52s  x%d" % (bad, good, n))
        else:
            print("  %-34s -> (未命中)" % bad)

    print("-" * 70)
    print("共替换 %d 处" % total)
    print("行尾: 改前 CRLF=%d / LF=%d" % (crlf_before, lf_before))

    if check_only:
        print("[--check] 未写盘")
        return

    data = txt.encode("utf-8")
    print("行尾: 改后 CRLF=%d / LF=%d" % (data.count(b"\r\n"), data.count(b"\n")))
    open(TARGET, "wb").write(data)
    print("已写入 %s" % TARGET)


if __name__ == "__main__":
    main()
