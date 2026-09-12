---
title: "如何读懂显示屏规格参数"
description: "系统了解如何读懂显示屏规格参数，包括关键原理、优缺点、应用场景和工程选型要点。"
date: 2026-09-01
categories:
  - 显示技术
tags:
  - 工程应用
  - 显示技术
authors:
  - viewe_expert
keywords:
  - LCD
  - TFT
  - 如何读懂显示屏规格参数
  - 工程应用
og:type: article
og:image: ./display-specifications-use-the-formula.png
twitter:card: summary_large_image
canonical: https://www.displaywiki.com/zh/knowledge/posts/display-specifications
lastmod: 2026-09-02
cover: ./display-specifications-use-the-formula.png
---


# 如何读懂显示屏规格参数

!!! abstract "快速结论"
    本指南解释显示规格的核心读法、相关设计权衡，以及在选型时工程师应当逐项验证的点。读完本文，你将能够独立看懂数据表上的每一项参数，并判断它对你的产品是否够用。

## 核心要点

- 显示规格不是孤立的数字，它们共同决定画面在不同环境下的可读性、色彩准确度与寿命。
- 工程选型时通常要先确认五件事：光学表现、电气接口、结构尺寸、环境可靠性和量产可行性。
- 本文按从"几何"到"光学"再到"环境"的顺序逐项展开：尺寸与对角线 → 分辨率与 PPI → 亮度 → 亮度均匀性 → 对比度 → 颜色色域 → 视角。

## 1. 显示尺寸与对角线

显示屏的尺寸通常指对角线长度，行业默认以英寸表达。

### 如何计算屏幕对角线

**第一步：测量宽度与高度。**

查阅显示模组的数据表，或用卡尺直接测量显示区域（AA 区）的宽度 W 与高度 H，单位可以是英寸也可以是厘米。

**第二步：用勾股定理计算对角线长度。**

<figure markdown="span" class="displaywiki-figure">
  [![使用公式](display-specifications-use-the-formula.png){ width="760" loading="lazy" }](display-specifications-use-the-formula.png){ .displaywiki-image-link title="查看原图" }
  <figcaption>使用公式</figcaption>
</figure>

### 举例

假设一块屏的宽度是 16 英寸、高度是 9 英寸，则对角线约为 18.36 英寸。

<figure markdown="span" class="displaywiki-figure">
  [![因此，显示屏的对角线长度约为 18.36 英寸](display-specifications-therefore-the-diagonal-length-of-the-display-screen-is-approximately-1.png){ width="760" loading="lazy" }](display-specifications-therefore-the-diagonal-length-of-the-display-screen-is-approximately-1.png){ .displaywiki-image-link title="查看原图" }
  <figcaption>因此，显示屏的对角线长度约为 18.36 英寸</figcaption>
</figure>

### 单位换算

如果给的是厘米，先换算成英寸（1 英寸 = 2.54 厘米），再用上面的方法计算。

<figure markdown="span" class="displaywiki-figure">
  [![然后用同样的方法计算对角线](display-specifications-then-use-the-same-method-as-above-to-calculate-the-diagonal-length.png){ width="760" loading="lazy" }](display-specifications-then-use-the-same-method-as-above-to-calculate-the-diagonal-length.png){ .displaywiki-image-link title="查看原图" }
  <figcaption>然后用同样的方法计算对角线</figcaption>
</figure>

### 其他考虑因素

- **宽高比**：不同显示器的宽高比不同，常见的有 16:9、4:3 等。
- **实际测量**：很多显示器边框较厚，测量时只算可见显示区域，不要把边框算进去。

## 2. 分辨率与像素结构

### 什么是液晶显示器的"原生分辨率"

要理解原生分辨率，需要先理解像素，以及 LCD（尤其是 TFT LCD）是怎么把像素点亮起来的。

### 像素是什么

像素（Pixel，Picture Element）是数字显示设备上能表示的最小图像单元。每个像素由 RGB（红、绿、蓝）三个子像素组成，三个子像素可以独立控制开关与亮度。三者全关表现为黑色，三者全开 100% 表现为白色，通过调节三色的比例可以复现数百万种颜色。

<figure markdown="span" class="displaywiki-figure">
  [![有 RGB 子像素的 LCD 像素](display-specifications-lcd-pixel-with-rgb-sub-pixels.png){ width="760" loading="lazy" }](display-specifications-lcd-pixel-with-rgb-sub-pixels.png){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 1有 RGB 子像素的 LCD 像素</figcaption>
</figure>

LCD 不是 CRT，不会用电子束扫描荧光屏。它由按矩形网格排列的独立像素构成，每个子像素背后有一个 TFT（Thin Film Transistor，薄膜晶体管）元件，电极与 TFT 都沉积在玻璃基板上，构成整个显示器堆叠的一部分。所有平板显示器（LCD、OLED、Plasma 等）都只有"原生分辨率"这一种分辨率，CRT 才有扫描分辨率的概念。

参考量级：

- HD 电视：1280 × 720 = 921,600 像素
- Full HD 电视：1920 × 1080 ≈ 2,073,600 像素
- 8K 电视：7680 × 4320 ≈ 33,177,600 像素（K 代表 Kilo，即 1000）

### PPI：每英寸像素数

PPI 是 Pixels Per Inch 的缩写，量化的是一英寸表面上排列的像素数量。可以把一英寸想象成一张网格，网格里的每个格子就是一个像素。

<figure markdown="span" class="displaywiki-figure">
  [![每英寸像素数（PPI）示意](display-specifications-also-known-as-pixels-tells-you-the-ppi.jpeg){ width="760" loading="lazy" }](display-specifications-also-known-as-pixels-tells-you-the-ppi.jpeg){ .displaywiki-image-link title="查看原图" }
  <figcaption>每英寸像素数（PPI）示意</figcaption>
</figure>

<figure markdown="span" class="displaywiki-figure">
  [![每英寸像素数（PPI）示意](display-specifications-also-known-as-pixels-tells-you-the-ppi-2.jpeg){ width="760" loading="lazy" }](display-specifications-also-known-as-pixels-tells-you-the-ppi-2.jpeg){ .displaywiki-image-link title="查看原图" }
  <figcaption>PPI与清晰度</figcaption>
</figure>

PPI 常用来描述显示器、笔记本、电视、手机等任意显示设备的像素密度。

### 计算 PPI 的三个步骤

**第一步：测量屏幕对角线长度（英寸）。**

屏幕、显示器、电视一般都按对角线尺寸销售，可以安装上文的显示尺寸来计算。

**第二步：用勾股定理求对角线上的像素数。**

已知屏幕分辨率（宽 × 高），可以算出对角线像素数 dp：

<figure markdown="span" class="displaywiki-figure">
  [![第二步：用勾股定理求对角线像素数](display-specifications-step-two-find-the-diagonal-pixels.jpeg){ width="760" loading="lazy" }](display-specifications-step-two-find-the-diagonal-pixels.jpeg){ .displaywiki-image-link title="查看原图" }
  <figcaption>第二步：用勾股定理求对角线像素数</figcaption>
</figure>

例如 1920 × 1080 屏，dp = √(1920² + 1080²)。

**第三步：用 PPI 公式。**

```
PPI = dp / 屏幕对角线英寸数
```

### 视网膜屏（Retina）

视网膜屏是指人眼在该观看距离下分辨不出单个像素的像素密度。实际阈值取决于眼睛离屏幕的距离，通常观看笔记本屏幕（约 12 英寸 / 30 cm）时 PPI ≈ 300 就够细腻。

## 3. 亮度

显示屏亮度指显示表面辐射出的光强度，常见单位是 cd/m²，也叫 nits。亮度越高，在明亮环境下的可读性越好，整体视觉体验也更通透。

<figure markdown="span" class="displaywiki-figure">
  [![两块相同工业显示屏在强日光下的亮度对比：左侧低亮度屏受反射影响而发灰，右侧高亮度屏仍清晰可读](../../../assets/images/Post/display-specifications-brightness-comparison.png){ width="960" loading="lazy" }](../../../assets/images/Post/display-specifications-brightness-comparison.png){ .displaywiki-image-link title="查看原图" }
  <figcaption>亮度对比：在相同的强环境光下，左侧较低亮度的显示屏更易受眩光影响；右侧较高亮度的显示屏仍能保持良好的画面可读性。</figcaption>
</figure>

### 关键概念

- **亮度**：单位面积显示表面发出的光强度。
- **单位**：cd/m²（或 nits）。
- **典型值**：常见显示器在 200–500 cd/m² 之间，高亮屏可到 1000 cd/m² 及以上。

### 为什么亮度重要

- **可读性**：在户外或明亮室内，高亮度让画面保持可读。
- **画质**：合适的亮度水平能提升对比度与色彩精度。
- **舒适度**：恰当的亮度能减轻长时间使用的眼睛疲劳。

### 亮度测试方法

测量亮度需要专业工具与流程，常用工具有：

- **亮度计（Light Meter）**：例如 TOPCON BM-7 等，专门用于显示器亮度测量。

#### 在暗室中测亮度的流程

1. **准备显示器**：将显示器恢复出厂设置或标准测试图；测试前至少预热 30 分钟，让器件达到稳定工作温度。
2. **架设测量设备**：把亮度计或光谱仪垂直对准屏幕中心，距离参照设备厂家建议；保证测量区域落在屏幕中心。
3. **采集数据**：屏幕显示全屏白色（用校准软件或加载白色测试图）；在中心、四角、边缘等多个点测量亮度，评估亮度均匀性与平均值。
4. **记录结果**：记录每个点的亮度读数；如有多点测量，给出平均亮度并标注屏内最大偏差。

### 亮度测试标准

- **VESA FPDM（Flat Panel Display Measurements）**：平板显示测量标准，含亮度等指标。
- **ISO 9241-307**：人机工效学标准，规定电子视觉显示器的测试方法。
- **IEC 61966-2-1**：多媒体系统颜色测量与管理标准，覆盖显示亮度。

## 4. 亮度均匀性

亮度均匀性指屏幕不同区域亮度的一致性。均匀性越好，屏内亮度差异越小，视觉体验越自然。

### 计算亮度均匀性的步骤

**第一步：测量多个点的亮度。**

在屏幕上选取若干固定点测量亮度，常见网格是 3 × 3（九点）或 5 × 5（二十五点），点位一般包含中心、四角，以及需要关注的中间位置。

**第二步：记录亮度值。**

每个点读到的亮度通常以 cd/m² 为单位记录下来。

**第三步：计算最暗与最亮点的比例。**

用下面的公式计算亮度均匀性：

<figure markdown="span" class="displaywiki-figure">
  [![用公式计算亮度均匀性](display-specifications-use-the-following-formula-to-calculate-luminance-uniformity.png){ width="760" loading="lazy" }](display-specifications-use-the-following-formula-to-calculate-luminance-uniformity.png){ .displaywiki-image-link title="查看原图" }
  <figcaption>计算公式</figcaption>
</figure>

最终值用最暗点亮度与最亮点亮度的比值表示（百分比）。

### 举例

假设一块屏的 9 个测量点（3 × 3）亮度（cd/m²）如下：

<figure markdown="span" class="displaywiki-figure">
  [![根据这些测量值](display-specifications-from-these-measurements.png){ width="760" loading="lazy" }](display-specifications-from-these-measurements.png){ .displaywiki-image-link title="查看原图" }
  <figcaption>测试数据</figcaption>
</figure>

<figure markdown="span" class="displaywiki-figure">
  [![高亮度均匀性的重要性](display-specifications-importance-of-high-luminance-uniformity.png){ width="760" loading="lazy" }](display-specifications-importance-of-high-luminance-uniformity.png){ .displaywiki-image-link title="查看原图" }
  <figcaption>计算结果</figcaption>
</figure>

### 为什么亮度均匀性重要

- **视觉舒适**：高均匀性的屏幕亮度一致，眼睛不容易疲劳。
- **色彩准确**：对图形设计、视频编辑等需要精确色彩表达的应用至关重要。
- **专业应用**：医疗影像、航空航天等领域要求高均匀性以保证显示精确可靠。

## 5. 对比度（CR）

对比度（Contrast Ratio，CR）是显示屏的关键规格，指屏幕能产生的最亮白色与最暗黑色之间的亮度比。它直接影响画面清晰度、层次感和整体视觉体验。

### 定义

对比度 = 最亮白色亮度 / 最暗黑色亮度，常以 1000:1、3000:1 等形式表达。

<figure markdown="span" class="displaywiki-figure">
  [![两块相同显示屏显示夜景的对比：左侧低对比度屏黑色发灰且暗部层次较弱，右侧高对比度屏呈现更深黑色和更多暗部细节](../../../assets/images/Post/display-specifications-contrast-ratio-comparison.png){ width="960" loading="lazy" }](../../../assets/images/Post/display-specifications-contrast-ratio-comparison.png){ .displaywiki-image-link title="查看原图" }
  <figcaption>对比度对比：左侧较低对比度会抬高黑位、压缩暗部层次；右侧较高对比度可带来更深的黑色与更清晰的暗场细节。</figcaption>
</figure>

### 如何计算

测出全白画面与全黑画面的亮度值（cd/m²），再求两者比值即可。例如：

<figure markdown="span" class="displaywiki-figure">
  [![对比度的重要性](display-specifications-importance-of-contrast-ratio.png){ width="760" loading="lazy" }](display-specifications-importance-of-contrast-ratio.png){ .displaywiki-image-link title="查看原图" }
  <figcaption>对比度计算公式</figcaption>
</figure>

### 对比度为什么重要

- **画质**：对比度高，最亮与最暗部分的差异更明显，画面更生动、清晰、真实。
- **色深**：高对比度能呈现更丰富的色彩层次与细节，尤其在暗场景下。
- **用眼舒适**：对比度足够时，眼睛更容易区分不同视觉元素，不易疲劳。

### 不同面板的典型对比度

- **TN（Twisted Nematic）面板**：通常对比度较低，约 1000:1 左右。
- **IPS（In-Plane Switching）面板**：对比度一般优于 TN，常见 1000:1–1500:1。
- **VA（Vertical Alignment）面板**：以高对比度著称，常见 3000:1–6000:1。
- **OLED（Organic Light Emitting Diode）面板**：理论上可做到"无限对比度"，因为单个像素可完全关闭，呈现真正的黑色。

### 实际考虑

- **观看环境**：明亮房间因环境光反射，主观对比度会下降；暗室里显示器对比度更明显。
- **内容类型**：高对比度对影音、游戏和任何要求画面还原度的场景都尤其重要。
- **测量标准**：不同厂商使用的测量方法可能不同，尤其是"动态对比度"，实际可比性有限。

## 6. 颜色色域（NTSC）

评估 TFT（Thin Film Transistor，薄膜晶体管）显示器的色彩能力时，色域（Color Gamut）是核心指标之一。色域代表显示器能复现的色彩范围，更高的色域代表色彩更为鲜艳。NTSC（National Television System Committee，国家电视系统委员会）色域是评估显示器色彩覆盖度时常用的参考标准。

<figure markdown="span" class="displaywiki-figure">
  [![两块相同显示屏显示相同花卉和色卡：左侧较窄色域的颜色更平淡，右侧较宽色域可呈现更丰富鲜明的颜色](../../../assets/images/Post/display-specifications-color-gamut-comparison.png){ width="960" loading="lazy" }](../../../assets/images/Post/display-specifications-color-gamut-comparison.png){ .displaywiki-image-link title="查看原图" }
  <figcaption>色域对比：较宽色域可以复现更大的色彩范围；但色域更宽本身并不等同于颜色更准确。</figcaption>
</figure>

### NTSC 色域的定义

NTSC 色域是 1953 年 NTSC 为模拟电视广播制定的颜色标准。尽管 NTSC 标准本身已不再广泛用于现代数字显示，但 NTSC 色域仍是评估显示色彩能力的常用基准。

### 颜色覆盖率

色域覆盖率通常用 NTSC 色域的百分比表示。例如，某屏的 NTSC 色域覆盖率为 72%，意味着它能复现 NTSC 标准色谱中 72% 的颜色。

### 如何计算 NTSC 色域覆盖率

需要用色度图把显示器的色域和 NTSC 色域做比较，步骤如下：

1. **测量显示器的颜色范围**：用色彩分析仪或光谱仪测量屏幕的色域。
2. **绘制色度图**：把显示器的色域与 NTSC 色域都画在 CIE 1931 色度图上。
3. **计算覆盖率**：两者比对，得到 NTSC 色域百分比覆盖率。

### 常见色域覆盖水平

- **标准显示器**：约 72% NTSC 色域。适合一般办公与日常家用娱乐。
- **高端显示器**：85% NTSC 色域及以上，适合摄影、视频编辑、专业设计等要求更高的应用。
- **专业显示器**：可覆盖 100% 或以上 NTSC 色域，色彩鲜艳度高，能复现更丰富的色彩。

### 与其他色域标准的对比

除 NTSC 外，业内常用的色域标准还有 sRGB、Adobe RGB、DCI-P3，每个标准覆盖的色彩范围不同，适用场景也不同：

- **sRGB**：适合互联网与一般消费电子。
- **Adobe RGB**：用于专业摄影与印刷，覆盖更广的绿色与蓝色。
- **DCI-P3**：用于电影与 HDR 内容，覆盖更广的红色与绿色。

## 7. 视角

视角指屏幕在画面质量仍可接受的条件下，可观看的最大角度。角度越大时，色彩与对比度可能变化，画面会出现失真或色偏。了解视角有助于在不同观看场景下选择可见性与色彩精度合适的显示器。

<figure markdown="span" class="displaywiki-figure">
  [![从相同斜视角度观看两块工业显示屏：左侧窄视角屏变暗并失去饱和度，右侧宽视角屏仍保持亮度和色彩](../../../assets/images/Post/display-specifications-viewing-angle-comparison.png){ width="960" loading="lazy" }](../../../assets/images/Post/display-specifications-viewing-angle-comparison.png){ .displaywiki-image-link title="查看原图" }
  <figcaption>视角对比：在相同的离轴观看位置下，左侧窄视角显示屏更早出现亮度下降和色彩变化；右侧宽视角显示屏的画面保持更稳定。</figcaption>
</figure>

### 定义

**视角**：在色彩精度与对比度不发生显著下降的条件下，可以观看显示器的角度。详细规格请参考优奕视界显示数据表。

### 为什么视角重要

- **用户体验**：宽视角保证从多个位置观看时画面都好看，适合需要共享画面的场景。
- **应用适配**：不同应用对视角的要求不同。专业图形设计需要宽视角，而基本办公监看可能不需要。
- **技术对比**：了解不同显示技术的视角差异，有助于针对场景选型。

### 视角的测量

视角通常以屏幕中心为基准测得，一般用水平视角与垂直视角两个值表示：

- **水平视角**：屏幕中心向左、向右两侧，图像质量仍可接受的最大角度。
- **垂直视角**：屏幕中心向上、向下两侧，图像质量仍可接受的最大角度。

### 视角规格

厂家通常按下方顺序标注视角性能：

<figure markdown="span" class="displaywiki-figure">
  [![影响视角的因素](display-specifications-factors-affecting-viewing-angle.png){ width="760" loading="lazy" }](display-specifications-factors-affecting-viewing-angle.png){ .displaywiki-image-link title="查看原图" }
  <figcaption>视角规格图</figcaption>
</figure>

**显示技术对比**：OLED > MVA > IPS >> TN

**背光与偏光片**：背光模组质量以及偏光片的取向也会影响视角表现。

### 实际考虑

- **使用环境**：会议室电视与监控屏等公共/共享场景，需要宽视角以容纳多人观看。
- **使用目的**：图片与视频编辑等要求高色彩精度的任务，需要宽视角以保证不同观看位置下色彩一致。
- **成本**：视角更好的显示器（尤其是 IPS、OLED）通常比 TN 屏更贵。

## 相关阅读

- [LCD 基础知识：液晶显示器的工作原理](lcd-basics.md)
- [TFT LCD 基础知识：结构、原理与优势](tft-lcd-basics.md)
- [TFT LCD 模组的组成与结构](tft-lcd-module.md)

## 参考数据来源

本文涉及的标准、规格、应用笔记与官方资料：

- [VESA DisplayPort 标准（含 eDP）](https://vesa.org/vesa-standards/)
- [TFT LCD 通用规格书示例](../../../assets/datasheet/display/ALL-UE070WV-RB40-A092A.pdf)


!!! info "没有找到您需要的内容？"
    如果您需要更多产品、资源或技术支持，欢迎联系我们的团队：

    [**:material-archive-arrow-down: 知识库**](../../knowledge/tags.md){ .md-button .md-button--primary }
    [**:material-magnify: 产品与解决方案**](https://www.chinasunyee.com){ .md-button }
    [**:material-email: 联系技术支持**](mailto:info@chinasunyee.com){ .md-button }
