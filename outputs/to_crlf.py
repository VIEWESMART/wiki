# -*- coding: utf-8 -*-
"""把指定文件（或目录下所有 .md）统一转换为 CRLF 行尾，无 BOM。
用法:
  python outputs/to_crlf.py <path> [<path> ...]
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")


def walk(paths):
    for p in paths:
        if os.path.isdir(p):
            for root, _dirs, files in os.walk(p):
                for f in files:
                    if f.endswith(".md"):
                        yield os.path.join(root, f)
        elif os.path.isfile(p):
            yield p


def main():
    paths = sys.argv[1:]
    if not paths:
        print("用法: python outputs/to_crlf.py <path> [...]")
        return
    changed = 0
    for fp in walk(paths):
        raw = open(fp, "rb").read()
        if raw.startswith(b"\xef\xbb\xbf"):
            raw = raw[3:]
        txt = raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
        new = txt.replace(b"\n", b"\r\n")
        if new != raw:
            open(fp, "wb").write(new)
            changed += 1
            print("  转换 -> %s" % os.path.relpath(fp, os.getcwd()))
        else:
            print("  已是 CRLF -> %s" % os.path.relpath(fp, os.getcwd()))
    print("-" * 60)
    print("共处理 %d 个文件，其中 %d 个发生转换" % (len(list(walk(paths))), changed))


if __name__ == "__main__":
    main()
