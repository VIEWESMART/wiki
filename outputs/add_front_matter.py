# -*- coding: utf-8 -*-
"""给缺 front matter 的中文产品页补 title/description（保持 CRLF）。
用法: python outputs/add_front_matter.py [--check]
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ZHP = os.path.join(ROOT, "docs", "zh", "products")

ITEMS = [
    (
        "esp32-p4-pi",
        "优奕视界 ESP32-P4-Pi 开发套件",
        "ESP32-P4-Pi 是一款基于 ESP32-P4-Core 模组（ESP32-P4 + ESP32-C6）的树莓派外形开发套件，"
        "配备 7 英寸 1024x600 MIPI DSI 触控显示屏，支持 Wi-Fi 6 与 H.264 硬件编码。",
    ),
    (
        "esp32-p4-wifi6-7inch-1024x600-touch-uart-display-hmi",
        "优奕视界 7 英寸 1024x600 ESP32-P4 WiFi6 触控智能屏",
        "UEP4S070H1024V600C-WBA 是一款 7 英寸 1024x600 的 ESP32-P4 + ESP32-C6 智能触控显示模组，"
        "采用 MIPI DSI 接口与电容触摸，支持 Wi-Fi 6 与 H.264 硬件编码，"
        "并提供 Arduino / ESP-IDF / PlatformIO 完整支持。",
    ),
    (
        "esp32-s3-7inch-800x480-touch-uart-display-hmi",
        "优奕视界 7 英寸 800x480 ESP32-S3 触控智能屏",
        "UEDX80480070E-WB-A 是一款 7 英寸 800x480 的 ESP32-S3 智能触控显示模组，"
        "采用 RGB 接口与 GT911 电容触摸，支持 Wi-Fi 与蓝牙 5 (LE)，"
        "并提供 Arduino / ESP-IDF / PlatformIO 完整支持。",
    ),
]


def main():
    check_only = "--check" in sys.argv
    for slug, title, desc in ITEMS:
        fp = os.path.join(ZHP, slug, "index.md")
        raw = open(fp, "rb").read()
        if raw.startswith(b"---"):
            print("  已有 FM，跳过 -> %s" % slug)
            continue
        fm = ("---\r\ntitle: %s\r\ndescription: %s\r\n---\r\n\r\n" % (title, desc)).encode("utf-8")
        new = fm + raw
        first = raw.split(b"\r\n", 1)[0].decode("utf-8", "replace")
        print("  %s" % slug)
        print("     原首行 : %s" % first)
        print("     新首行 : ---")
        print("     新 title: %s" % title)
        print("     CRLF 校验: 原 %d / 新 %d" % (raw.count(b"\r\n"), new.count(b"\r\n")))
        if not check_only:
            open(fp, "wb").write(new)
    print("-" * 60)
    print("[--check] 未写盘" if check_only else "已写盘")


if __name__ == "__main__":
    main()
