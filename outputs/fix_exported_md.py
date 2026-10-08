#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
修复被「导出/转义」工具破坏的 md 文件。

损坏特征（本次实测）：
  1) 前置元数据与列表项被转义：`\\---`、`\\- `、`\\_`、`\\&`
  2) 所有缩进被剥离（!!! / ??? 块体、卡片续行）
  3) EOL 被写成 CR + 若干空格 + LF（原为「两空格硬换行 + CRLF」）
  4) 行尾残留空格
  5) 末尾按钮块被额外套了一对 ``` 围栏
  6) 卡片（grid cards）里丢失了粗体标题行与 `---` 分隔线
用法：
  python outputs/fix_exported_md.py <file>            # 只体检，不改
  python outputs/fix_exported_md.py <file> --apply    # 修复并写回（CRLF）
"""
import argparse
import re
import sys

CARD_TITLE_SUFFIX = " · ESP32-S3 圆形开发板"


def unescape(lines):
    out = []
    for l in lines:
        l = l.replace("\\---", "---").replace("\\_", "_").replace("\\&", "&")
        l = re.sub(r"^\\- ", "- ", l)          # 行首列表项转义
        l = re.sub(r"^\\\* ", "* ", l)
        out.append(l)
    return out


def strip_fences(lines):
    """删掉包裹按钮块的那对多余围栏。"""
    removed = 0
    i = 0
    while i < len(lines):
        if lines[i].strip() == "```":
            j = i + 1
            while j < len(lines) and lines[j].strip() != "```":
                j += 1
            if j < len(lines):
                body = lines[i + 1:j]
                if body and all(b.lstrip().startswith("[**") or b.strip() == "" for b in body):
                    lines = lines[:i] + lines[i + 1:j] + lines[j + 1:]
                    removed += 2
                    continue
        i += 1
    return lines, removed


def reindent(lines):
    """把 !!! / ??? 块体补回 4 空格缩进。"""
    TERM = re.compile(r"^(#{1,6}\s|<|---|\||```|!!!|\?\?\?)")
    out = list(lines)
    i = 0
    while i < len(out):
        if re.match(r"^(!!!|\?\?\?)", out[i]):
            j = i + 1
            while j < len(out):
                if out[j].strip() == "":
                    k = j + 1
                    while k < len(out) and out[k].strip() == "":
                        k += 1
                    if k >= len(out) or TERM.match(out[k]):
                        break                     # 块结束
                    j = k
                    continue
                if TERM.match(out[j]):
                    break
                out[j] = "    " + out[j]
                j += 1
            i = j
        else:
            i += 1
    return out


def fix_card(lines):
    """重建 grid cards 的头部结构（标题行 + --- + 4 空格缩进）。"""
    try:
        s = next(i for i, l in enumerate(lines) if 'class="grid cards"' in l)
        e = next(i for i in range(s + 1, len(lines)) if lines[i].strip() == "</div>")
    except StopIteration:
        return lines, False
    block = lines[s + 1:e]
    body = [l for l in block if l.strip().startswith("- ")]
    btns = [l for l in block if l.strip().startswith("[")]
    if not body or not btns:
        return lines, False
    para = body[0].strip()[2:].strip()
    title = None
    m = re.search(r"([0-9.]+ 英寸 [0-9x]+ [A-Za-z]+)", para)
    if m:
        title = m.group(1) + CARD_TITLE_SUFFIX
    new = [""]
    if title:
        new += ["-   **" + title + "**", "    ---"]
    new += ["    " + para, ""]
    new += ["    " + b.strip() for b in btns]
    new += [""]
    return lines[:s + 1] + new + lines[e:], True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()

    raw = open(a.file, "rb").read()
    txt = raw.decode("utf-8")
    lines = txt.replace("\r", "").split("\n")
    n_esc = sum(1 for l in lines if "\\" in l)
    n_trail = sum(1 for l in lines if l != l.rstrip())
    print(f"体检 {a.file}")
    print(f"  含反斜杠行 {n_esc} / 行尾空格行 {n_trail} / 原 CR 数 {txt.count(chr(13))}")

    lines = unescape(lines)
    lines = [l.rstrip() for l in lines]
    lines, nf = strip_fences(lines)
    lines = reindent(lines)
    lines, ok = fix_card(lines)
    print(f"  去掉多余围栏 {nf} 行；卡片重建 {'成功' if ok else '跳过'}")

    out = "\r\n".join(lines).encode("utf-8")
    if b"\\" in out:
        print("  ⚠ 仍有反斜杠残留：" +
              str([l for l in lines if "\\" in l][:3]))
    if a.apply:
        open(a.file, "wb").write(out)
        print(f"  已写回（CRLF，{len(lines)} 行）")
    else:
        print("  （未写回，加 --apply 生效）")


if __name__ == "__main__":
    sys.exit(main())
