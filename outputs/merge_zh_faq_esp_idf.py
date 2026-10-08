# -*- coding: utf-8 -*-
"""把 faq-esp-idf 的两段中文片段合并成最终文件。"""
import io
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = r"D:\GitHub\wiki"
P1 = os.path.join(ROOT, "outputs", "_zh_faq_esp_idf_part1.md")
P2 = os.path.join(ROOT, "outputs", "_zh_faq_esp_idf_part2.md")
OUT = os.path.join(ROOT, "docs", "zh", "support", "faq-esp-idf.md")

a = io.open(P1, encoding="utf-8").read().replace("\r\n", "\n")
b = io.open(P2, encoding="utf-8").read().replace("\r\n", "\n")

a = a.rstrip("\n")
b = b.lstrip("\n").rstrip("\n")

merged = a + "\n\n" + b + "\n"

# 校验合并边界
if "## Firmware Update" in merged:
    print("!! 仍含英文标题 ## Firmware Update")
if "## 固件烧录" not in merged or "## 调试" not in merged:
    print("!! 缺少中文 H2")

io.open(OUT, "w", encoding="utf-8", newline="\n").write(merged)

print("已写出:", OUT)
print("总字符:", len(merged), " 总行数:", merged.count("\n"))
print("H2:", [l for l in merged.split("\n") if l.startswith("## ")])
print("H1:", [l for l in merged.split("\n") if l.startswith("# ")])
print("### 数:", sum(1 for l in merged.split("\n") if l.startswith("### ")))
print("!!! 数:", sum(1 for l in merged.split("\n") if l.startswith("!!!")))
print("``` 数:", sum(1 for l in merged.split("\n") if l.strip().startswith("```")))
