# -*- coding: utf-8 -*-
"""
对比 docs/en/products 与 docs/zh/products 的目录与结构差异。
用法: python outputs/compare_products_i18n.py
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EN = os.path.join(ROOT, "docs", "en", "products")
ZH = os.path.join(ROOT, "docs", "zh", "products")

# 英文侧的一级「分类页」（非具体产品）
CATEGORY = {"amoled", "embedded", "esp32", "hdmi", "mipi", "tft", "transflective"}


def scan(base):
    """返回 {slug: 行数 or None}；None 表示目录存在但没有 index.md"""
    out = {}
    if not os.path.isdir(base):
        return out
    for name in sorted(os.listdir(base)):
        p = os.path.join(base, name)
        if not os.path.isdir(p):
            continue
        idx = os.path.join(p, "index.md")
        if os.path.isfile(idx):
            with open(idx, "rb") as f:
                n = f.read().count(b"\n")
            out[name] = n
        else:
            out[name] = None
    return out


def h2s(path):
    """抽取正文 H2 标题（跳过代码围栏）"""
    res = []
    if not os.path.isfile(path):
        return res
    fence = False
    with open(path, encoding="utf-8") as f:
        for line in f:
            s = line.rstrip("\r\n")
            if s.strip().startswith("```"):
                fence = not fence
                continue
            if fence:
                continue
            m = re.match(r"^##\s+(?!#)(.*)$", s)
            if m:
                res.append(m.group(1).strip())
    return res


def main():
    en = scan(EN)
    zh = scan(ZH)

    print("=" * 78)
    print("A. 一级目录对比")
    print("=" * 78)
    en_cat = sorted(s for s in en if s in CATEGORY)
    zh_cat = sorted(s for s in zh if s in CATEGORY)
    print(f"EN 分类页 ({len(en_cat)}): {', '.join(en_cat)}")
    print(f"ZH 分类页 ({len(zh_cat)}): {', '.join(zh_cat) or '(无)'}")
    miss_cat = [s for s in en_cat if s not in zh]
    print(f"→ ZH 缺分类页 {len(miss_cat)} 个: {', '.join(miss_cat) or '(无)'}")

    en_prod = sorted(s for s in en if s not in CATEGORY)
    zh_prod = sorted(s for s in zh if s not in CATEGORY)
    print()
    print(f"EN 产品页 ({len(en_prod)}):")
    for s in en_prod:
        flag = "" if en[s] is not None else "   <<< 目录存在但无 index.md"
        print(f"    - {s}  [{en[s] if en[s] is not None else '-'} 行]{flag}")
    print()
    print(f"ZH 产品页 ({len(zh_prod)}):")
    for s in zh_prod:
        print(f"    - {s}  [{zh[s]} 行]")

    miss_prod = [s for s in en_prod if s not in zh]
    print()
    print(f"→ ZH 缺产品页 {len(miss_prod)} 个:")
    for s in miss_prod:
        print(f"    [ ] {s}")

    print()
    print("=" * 78)
    print("B. 同名页结构对齐（H2 数量 + 标题）")
    print("=" * 78)
    both = [s for s in en_prod if s in zh]
    for s in both:
        eh = h2s(os.path.join(EN, s, "index.md"))
        zhh = h2s(os.path.join(ZH, s, "index.md"))
        mark = "OK " if len(eh) == len(zhh) else "!! "
        print(f"\n{mark}{s}: EN {len(eh)} 个 H2 / ZH {len(zhh)} 个 H2")
        for i in range(max(len(eh), len(zhh))):
            e = eh[i] if i < len(eh) else "(缺)"
            z = zhh[i] if i < len(zhh) else "(缺)"
            print(f"      {i+1:>2}. EN: {e}")
            print(f"          ZH: {z}")

    print()
    print("=" * 78)
    print("C. ZH 索引页 (products/esp32/index.md) 内链体检")
    print("=" * 78)
    idx = os.path.join(ZH, "esp32", "index.md")
    with open(idx, encoding="utf-8") as f:
        txt = f.read()
    links = sorted(set(re.findall(r"\]\(((?:\.\./)[^)\s]*)\)", txt)))
    zh_root = os.path.join(ROOT, "docs", "zh")
    en_root = os.path.join(ROOT, "docs", "en")
    base = os.path.join(ZH, "esp32")

    def exists(p):
        """路径存在：直接是文件，或目录下有 index.md"""
        if os.path.isfile(p):
            return True
        if os.path.isdir(p) and os.path.isfile(os.path.join(p, "index.md")):
            return True
        if os.path.isdir(p) and os.path.isfile(os.path.join(p, "index.html")):
            return True
        return False

    for l in links:
        target = os.path.normpath(os.path.join(base, l))
        rel = os.path.relpath(target, zh_root).replace("\\", "/")
        en_target = os.path.join(en_root, rel)
        if exists(target):
            state = "OK    中文源存在"
        elif exists(en_target):
            state = "WARN  仅英文源存在（中文 URL fallback 到英文内容）"
        else:
            state = "MISS  两平台都没有（真 404）"
        print(f"  {state:<46} {l}")


if __name__ == "__main__":
    main()
