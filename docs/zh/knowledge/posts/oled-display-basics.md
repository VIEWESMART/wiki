---
title: "OLED 显示结构、工作原理及与 LCD 的对比"
description: "一篇面向工程师的 OLED 入门指南：覆盖 OLED 自发光原理、层结构与载流子机制、AMOLED / PMOLED / QD-OLED 分类、与 LCD 在图像质量、功耗、响应速度、户外可视性、烧屏等维度的横向对比，并给出选型建议。"
date: 2026-09-01
categories:
  - 显示技术
tags:
  - 显示技术
  - OLED
  - 工程应用
authors:
  - viewe_expert
keywords:
  - LCD
  - OLED
  - 工作原理及与
  - 工程应用
  - 显示技术
  - 显示结构
  - 的对比
og:type: article
og:image: ./oled-display-basics-the-oled-layer-structure.jpeg
twitter:card: summary_large_image
canonical: https://www.displaywiki.com/zh/knowledge/posts/oled-display-basics
lastmod: 2026-09-02
cover: ./oled-display-basics-the-oled-layer-structure.jpeg
---


# OLED 显示结构、工作原理及与 LCD 的对比


<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "OLED 和 LCD 到底哪个更护眼？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "没有\"绝对护眼\"。OLED 在相同亮度下蓝光占比一般比 LCD 低，但 OLED 多用 PWM 调光，低亮度时若 PWM 频率太低会引发视疲劳；LCD 高亮方案在直射阳光下反而更省力护眼。结论是调好亮度 + 控制时长比\"OLED vs LCD\"更重要。"
      }
    },
    {
      "@type": "Question",
      "name": "AMOLED 和 PMOLED 的本质区别是什么？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "AMOLED 给每个像素配一组 TFT，能独立精准控光，可放大尺寸并保持均匀性；PMOLED 用行列扫描直接驱动，结构和驱动简单，但尺寸一大难以保证寿命与均匀度。当前手机与电视全是 AMOLED。"
      }
    },
    {
      "@type": "Question",
      "name": "QD-OLED、QLED、OLED 是不是同一种？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "不是。OLED 是自发光大类；QD-OLED 是\"OLED + 量子点\"组合（蓝光 OLED 激发量子点）；QLED 通常指\"量子点 + LCD 背光\"（量子点仅做色转换层，本身不发光）。"
      }
    },
    {
      "@type": "Question",
      "name": "OLED 在户外为什么常常不够亮？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "OLED 的最大瞬时电流受寿命制约，全屏高亮难度高；同时为了补偿有机材料衰减，厂商会保留降额空间。LCD（特别是高亮方案 + 半透半反）户外可视性仍是强项。"
      }
    },
    {
      "@type": "Question",
      "name": "工控 / 数字标牌适合用 OLED 吗？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "谨慎。长时间显示同一菜单或 Logo 是烧屏温床。如果必须用 OLED，应配合像素位移、自动息屏、Logo 透明度变化等策略，并预留亮度衰减预算。"
      }
    }
  ]
}
</script>

!!! abstract "快速结论"
    OLED 是自发光器件，单像素独立控光，因此能做到纯黑、高对比、广视角、超薄和可弯曲。这是它替代 LCD 成为高端手机与电视首选的根本原因，代价是成本相对较高、长期使用存在烧屏风险、最大亮度暂时低于 LCD。

## 核心要点

- OLED 与 LCD 的本质差别是"是否需要背光"：LCD 靠背光 + 液晶调制，OLED 由有机材料直接发光。
- OLED 的层结构包括阴极、阳极、发射层、导电层，电子与空穴在发射层复合后释放光子。
- OLED 分为 AMOLED、PMOLED、QD-OLED 等子类，AMOLED 是手机与电视的主流。
- 与 LCD 相比，OLED 真实黑、对比度极高、响应更快、可弯折，但成本更高、最大亮度偏低，长期高亮显示存在烧屏风险。
- 选型决策应结合分辨率、寿命要求、户外可视性、预算四个维度共同决定是否选 OLED。

## 1. OLED 是什么

OLED 全称 Organic Light Emitting Diode（有机发光二极管），也称 Organic Electroluminescent Device（有机电致发光器件）。它由含碳的有机化合物构成，当电流通过时有机层直接发光，不再依赖额外的背光模组。

由于是自发光，OLED 显示器天然具有：

- **真实黑色**：不发光即纯黑，对比度可超过 1,000,000 : 1。
- **更薄的厚度**：无需背光模组，整机厚度可压缩到毫米级。
- **可弯折性**：把玻璃基板换成柔性基材即可制成曲面 / 折叠 / 卷曲屏。
- **更低功耗**：显示深色画面时几乎不耗电。

LCD 必须依赖背光模组照亮整片液晶层，因此无法关闭单个像素的灯，黑色永远是"灰黑色"。

## 2. OLED 层结构

OLED 显示器的核心组成是**阴极、阳极、发射层、导电层**，它们被封装在上下基板之间：

<figure markdown="span" class="displaywiki-figure">
  [![OLED 层结构](oled-display-basics-the-oled-layer-structure.jpeg){ width="760" loading="lazy" }](oled-display-basics-the-oled-layer-structure.jpeg){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 2-1 OLED 层结构示意</figcaption>
</figure>

- **基板**：玻璃或柔性塑料，作为底层支撑。
- **阳极（Anode）**：通常为透明 ITO，接正电。
- **空穴注入层（HIL）/ 空穴传输层（HTL）**：把阳极的空穴送到发射层。
- **发射层（EML）**：有机发光材料，是真正的发光场所。
- **电子传输层（ETL）/ 电子注入层（EIL）**：把阴极的电子送到发射层。
- **阴极（Cathode）**：金属或合金薄层，接负电，反射光与注入电子。
- **封装层**：隔绝水氧，寿命关键。

## 3. OLED 工作原理

OLED 的电致发光过程是：电子从阴极向阳极运动，空穴从阳极向阴极运动；两者在**发射层**相遇并复合，把多余能量以光子的形式释放。

<figure markdown="span" class="displaywiki-figure">
  [![从阴极到阳极的电流流](oled-display-basics-electrical-current-flows-from-the-cathode-to-the-anode-through-the-org.jpeg){ width="760" loading="lazy" }](oled-display-basics-electrical-current-flows-from-the-cathode-to-the-anode-through-the-org.jpeg){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 3-1 载流子在 OLED 各层中的流动</figcaption>
</figure>

具体步骤：

1. 电压加载在阴极与阳极之间。
2. 阴极释放电子，电子经 ETL 进入发射层。
3. 阳极从 HTL 抽取电子，HTL 留下"空穴"并迁移到发射层。
4. 电子与空穴在 EML 内复合，激发有机分子到激发态。
5. 激发态分子回到基态时释放光子，光子穿过透明阳极与基板射出。
6. 发光颜色由有机分子本身的能带决定，常见主发光材料是蓝色与黄绿色，其余颜色通过色阻层转换。

<figure markdown="span" class="displaywiki-figure">
  [![OLED 显示器是如何工作的](oled-display-basics-how-does-an-oled-display-work.png){ width="760" loading="lazy" }](oled-display-basics-how-does-an-oled-display-work.png){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 3-2 OLED 单像素发光原理</figcaption>
</figure>

## 4. OLED 与 LCD 的对比

OLED 与 LCD 同为平板显示器主流，但因"自发光 vs 背光"差别，性能维度表现差异明显。

<figure markdown="span" class="displaywiki-figure">
  [![LCD 与 OLED 的对比](oled-display-basics-lcd-and-oled-comparison.png){ width="760" loading="lazy" }](oled-display-basics-lcd-and-oled-comparison.png){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 4-1 LCD 与 OLED 直观对比</figcaption>
</figure>

下表是工程角度的常见指标对比：

| 维度 | OLED | LCD（带背光） |
| --- | --- | --- |
| 黑场亮度 | 几乎为 0（纯黑） | 受背光漏光限制 |
| 对比度 | 1,000,000 : 1 量级 | 1000 : 1 量级 |
| 视角 | 近 180° | 视角外偏色 / 亮度下降 |
| 响应时间 | 微秒级 | 毫秒级 |
| 厚度 | 极薄（无背光） | 受背光厚度限制 |
| 弯曲 / 折叠 | 天然支持 | 难 |
| 蓝光占比 | 较低 | 较高 |
| 最大亮度 | 偏低（高端例外） | 高，适合户外 |
| 寿命 | 有机材料衰减，烧屏风险 | 背光长寿命 |
| 成本 | 较高 | 低 |
| 能耗 | 暗画面极省电 | 背光常亮功耗稳定 |

## 5. OLED 的细分类型

OLED 是一个大类，下面还会按驱动方式、发光材料、色彩合成方式细分。

### 5.1 AMOLED 与 PMOLED

- **AMOLED（Active Matrix OLED）**：用 TFT 作为每个像素的开关，能独立精准控光，是手机、电视的主流方案。
- **PMOLED（Passive Matrix OLED）**：把行列扫描信号直接施加到 OLED，结构和驱动简单，但尺寸一大刷新率与均匀性便难以保证，多用于小尺寸如手表、早期 MP3。

### 5.2 QD-OLED / PLED

- **QD-OLED（Quantum Dot OLED）**：以蓝光 OLED 为基底激发量子点层得到红 / 绿，色域更高，常见于高端电视。
- **PLED（Polymer Light Emitting Diode）**：用高分子聚合物作发光层，可用于溶液法制程（如喷墨打印），适合大尺寸柔性屏。
- 其它还有高分子 / 小分子之分、印刷 / 蒸镀之分，不再展开。

## 6. OLED 适用场景

### 6.1 高端消费电子

- 智能手机、笔记本电脑、平板电脑、VR / AR 头盔。
- 高端电视，特别是 QD-OLED 路线。

### 6.2 工控 / 车载 / 可穿戴

- 智能手表：黑色深、对比高、厚度小。
- 车载仪表：宽温、宽视角越来越被 OLED 替代。
- 工业控制面板：部分强光场景仍是 LCD（含高亮）的强项，要按场景选。

### 6.3 不适合 OLED 的场景

- **长期显示同一静态画面**（如控制台菜单、加油机面板）：烧屏风险高。
- **超亮户外强光场景**：LCD（Transflective / 高亮）仍然是首选。
- **预算极敏感的中低端消费类**：LCD 仍有 3 到 5 倍价差。

## 7. 关于蓝光与眼健康

OLED 的发光是电致发光，机理上没有"必须全程发蓝光"的限制。实验室测试常给出 OLED 蓝光占比在 30% 出头，明显低于 LCD 背光的 60%+ 水平。这并不直接等同于"不伤眼"，但在同一亮度下，OLED 蓝光剂量更低。

需要注意的是，眼健康与亮度、色温、使用时长同样密切相关，无论 OLED 还是 LCD 都应使用合适的亮度并定期休息。

## 8. 烧屏：成因与应对

### 8.1 什么是烧屏

OLED 烧屏是指某些像素长时间高亮工作后，发光效率下降，在切换到其它画面后依然留下残影。

### 8.2 缓解措施

- **像素位移**：每隔一段时间整体像素微移 1–2 个像素，分散点亮时间。
- **亮屏时限**：UI 上的高亮元素（Logo、状态栏）做透明度变化或定期移动。
- **自动亮度 / 自动息屏**：长时间无操作自动息屏，对工控 / 数字标牌尤其重要。
- **寿命预估**：主流厂商商用 OLED 在每天 6 小时高亮工作下寿命可超过 15 年。

## 9. 选型建议

- **选 OLED**：追求高对比、广视角、可弯折、薄机身、不在意最大亮度、不长期显示相同静态内容。
- **选 LCD**：预算紧、强光户外、长期显示相同画面、对最大亮度有刚需。
- **选 QD-OLED / 高亮 LCD**：对色彩或亮度某一维度有极致要求时再考虑特殊子类。

## 10. FAQ

??? question "Q1：OLED 和 LCD 到底哪个更护眼？"
    没有"绝对护眼"。OLED 在相同亮度下蓝光占比一般比 LCD 低，但 OLED 多用 PWM 调光，低亮度时若 PWM 频率太低会引发视疲劳；LCD 高亮方案在直射阳光下反而更省力护眼。结论是**调好亮度 + 控制时长**比"OLED vs LCD"更重要。

??? question "Q2：AMOLED 和 PMOLED 的本质区别是什么？"
    AMOLED 给每个像素配一组 TFT，能独立精准控光，可放大尺寸并保持均匀性；PMOLED 用行列扫描直接驱动，结构和驱动简单，但尺寸一大难以保证寿命与均匀度。当前手机与电视全是 AMOLED。

??? question "Q3：QD-OLED、QLED、OLED 是不是同一种？"
    不是。**OLED** 是自发光大类；**QD-OLED** 是"OLED + 量子点"组合（蓝光 OLED 激发量子点）；**QLED** 通常指"量子点 + LCD 背光"（量子点仅做色转换层，本身不发光）。

??? question "Q4：OLED 在户外为什么常常不够亮？"
    OLED 的最大瞬时电流受寿命制约，全屏高亮难度高；同时为了补偿有机材料衰减，厂商会保留降额空间。LCD（特别是高亮方案 + 半透半反）户外可视性仍是强项。

??? question "Q5：工控 / 数字标牌适合用 OLED 吗？"
    谨慎。长时间显示同一菜单或 Logo 是烧屏温床。如果必须用 OLED，应配合像素位移、自动息屏、Logo 透明度变化等策略，并预留亮度衰减预算。

## 相关阅读

- [IPS、TN、VA 与 FFS TFT 面板技术对比](tft-panel-technologies.md)
- [a-Si、LTPS 与 IGZO TFT 背板技术对比](tft-backplane-technologies.md)
- [透射型、反射式与半反半透式 LCD 对比](transmissive-reflective-transflective.md)

## 参考数据来源

本文涉及的标准、规格、应用笔记与官方资料：

- [OLED 寿命与残影（burn-in）讨论](https://www.oled-info.com/oled-lifetime-and-burn-in-faq)
- [AMOLED 驱动 IC 设计指南（Omdia 摘要）](https://www.oled-a.org/)


!!! info "没有找到您需要的内容？"
    如果您需要更多产品、资源或技术支持，欢迎联系我们的团队：

    [**:material-archive-arrow-down: 知识库**](../../knowledge/tags.md){ .md-button .md-button--primary }
    [**:material-archive-arrow-down: 产品与解决方案**](https://www.chinasunyee.com){ .md-button }
    [**:material-email: 联系技术支持**](mailto:info@chinasunyee.com){ .md-button }
