---
title: "PCB 结构与制造流程"
description: "一篇面向硬件工程师的 PCB 制造入门指南：拆解 PCB 各功能层（基板 / 铜箔 / 半固化片 / 阻焊层 / 丝印 / 焊盘 / 过孔 / 金手指），并按 19 步标准流程梳理单 / 双 / 多层 PCB 的制造过程，覆盖 Lamination、沉铜、ENIG、QC 等关键工艺。"
date: 2026-09-01
categories:
  - 接口和电子
tags:
  - 工程应用
  - PCB
authors:
  - viewe_expert
---

# PCB 结构与制造流程

!!! abstract "快速结论"
    PCB 是几乎所有电子设备中"电路连通 + 元件固定"的基础载体，由基板、铜箔、阻焊、丝印、焊盘、过孔、金手指等功能层组成。多层板的制造核心是**层压（Lamination）+ 沉铜**两个步骤，前后辅以内 / 外层图形转移、AOI、阻焊、表面处理与电气测试。

## 核心要点

- PCB 按层数可分为单 / 双 / 多层，按基板材料可分为刚性、柔性、刚挠结合。
- 主要功能层：基板、铜箔、半固化片（Prepreg）、阻焊层（Solder Mask）、丝印（Silkscreen）、焊盘（Pad）、过孔（Via）、金手指（Gold Finger）。
- 标准 19 步制造流程以"内层图形 → 层压 → 钻孔沉铜 → 外层图形 → 阻焊 / 丝印 → 表面处理 → 成型与电气测试"为主线。
- **基板选择**（FR-4 / 高频 / 高速 / 铝基 / 陶瓷 / 柔性）是 PCB 设计的第一决策，直接影响成本、性能、可靠性。
- **表面处理**（HASL / ENIG / OSP / 沉银 / 沉锡 / 硬金）决定可焊性、信号完整性、寿命与成本。

## 1. 印刷电路板概述

印刷电路板（Printed Circuit Board，PCB）几乎应用于所有类型的电子设备，承担"为电子元器件提供电气连接和机械支撑"的核心作用。PCB 裸板上没有器件，故此通常也被称为**印制线路板（Printed Wiring Board，PWB）**。

在 PCB 普及之前，电子系统的连接靠手工布线与绝缘电缆完成。一旦线缆绝缘层老化破裂，就会引起开路或短路。PCB 通过"把导线做成铜箔图形并固化在绝缘基板上"把这两类故障的发生概率极大降低。

典型的成品 PCB 是绿色的，实际上颜色可以是蓝、黑、红、白、黄等多种。颜色源于阻焊层染料，对电气性能没有实质影响，仅影响外观与维修识别。

PCB 可按下列维度分类：

- **按层数**：单面板、双面板、多层板。
- **按频率 / 速率**：普通数字 / 高速数字 / 射频微波。
- **按基板材料**：刚性（FR-4 等）、柔性（PI / PET）、刚挠结合、铝基板、陶瓷基板。

PCB 的物理构成主要由**电路图形、基板、过孔、阻焊层、丝印、表面处理**六部分组成。

## 2. PCB 的功能层

### 2.1 基板（Substrate）

基板对线路和元件起支撑与绝缘作用，通常由电绝缘复合材料制成。基板的性能直接决定 PCB 的电学 / 力学 / 热学表现与成本，是制造 PCB 的第一步决策。

最常见的刚性基板是 **FR-4**：织造玻璃纤维布 + 环氧树脂的复合材料，具有良好的机械强度、电气绝缘与耐热性，成本相对友好。柔性基板用聚酰亚胺（PI）或聚酯（PET），可弯折或卷曲。

<figure markdown="span" class="displaywiki-figure">
  [![标准 PCB](pcb-construction-process-a-standard-printed-circuit-board.jpeg){ width="760" loading="lazy" }](pcb-construction-process-a-standard-printed-circuit-board.jpeg){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 2-1 标准 PCB 实物</figcaption>
</figure>

### 2.2 铜箔（Copper Foil）

基板上可见的"细线"就是铜。在 PCB 制造中，铜箔先整面敷在基板两面，然后通过图形转移与蚀刻保留需要的部分，形成导线和焊盘。铜的厚度以"盎司 / 平方英尺"为单位，常见规格 0.5 oz / 1 oz / 2 oz，约对应 17 µm / 35 µm / 70 µm。

在多层板中，铜还沉在钻孔孔壁上，作为不同层之间的电气连接。

### 2.3 半固化片（Prepreg，PP）

Prepreg 是用树脂浸渍过的玻璃纤维织物，处于"半固化"状态——既有一定粘性又能在加热加压下进一步固化。它像胶水一样把内层芯板与外层铜箔粘合在一起，是多层板层压（Lamination）的关键材料。

<figure markdown="span" class="displaywiki-figure">
  [![多层 PCB 结构](pcb-construction-process-a-multi-layer-printed-circuit-board.png){ width="760" loading="lazy" }](pcb-construction-process-a-multi-layer-printed-circuit-board.png){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 2-2 多层 PCB 结构示意</figcaption>
</figure>

### 2.4 阻焊层（Solder Mask）

阻焊层是覆盖在铜层之上的绝缘保护层，常见颜色是绿色。它防止铜线氧化、避免在焊接时桥接短路，焊盘位置开窗露出以供焊接。颜色可用绿、黑、蓝、红、白等。

### 2.5 丝印（Silkscreen / Legend）

丝印通常以白色油墨印在阻焊层上，标注元器件位号、极性、版本号、测试点等参考信息，方便装配与维修。

### 2.6 焊盘（Pad）

焊盘是 PCB 表面暴露出来的铜区，作为元件焊接的着陆区。焊盘分为两类：

- **通孔焊盘（Through-Hole Pad）**：带孔，主要用于插针元件（DIP 直插封装等）。
- **表贴焊盘（SMT Pad）**：不带孔，主要用于表面贴装元件（QFP、QFN、BGA 等）。

<figure markdown="span" class="displaywiki-figure">
  [![PCB 焊盘示意](pcb-construction-process-the-pad-of-printed-circuit-board.jpeg){ width="760" loading="lazy" }](pcb-construction-process-the-pad-of-printed-circuit-board.jpeg){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 2-3 PCB 焊盘示意</figcaption>
</figure>

### 2.7 过孔（Via）

过孔是贯穿多层板、用于在不同层之间导通的金属化孔。主要分三类：

- **镀通孔（PTH，Plated Through Hole）**：贯穿所有层，成本最低。
- **盲孔（Blind Via）**：从最外层连到相邻内层，从外部不可见。
- **埋孔（Buried Via）**：仅在内部层之间，从外部完全不可见。

过孔周围的铜环被称为**环形圈（Annular Ring）**，对钻孔对准与层间连接可靠性至关重要。HDI（高密度互连）板大量使用盲孔与埋孔来腾出表层走线空间。

<figure markdown="span" class="displaywiki-figure">
  [![PCB 过孔示意](pcb-construction-process-the-via-of-printed-circuit-board.jpeg){ width="760" loading="lazy" }](pcb-construction-process-the-via-of-printed-circuit-board.jpeg){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 2-4 PCB 过孔示意</figcaption>
</figure>

### 2.8 金手指（Gold Finger）

金手指是沿板边暴露的金属焊盘，表面镀硬金（Hard Gold），耐磨、抗氧化，用于金手指连接器（PCIe、内存条、AMR 板等子卡互连场景）。

<figure markdown="span" class="displaywiki-figure">
  [![PCB 金手指](pcb-construction-process-the-finger-of-printed-circuit-board.jpeg){ width="760" loading="lazy" }](pcb-construction-process-the-finger-of-printed-circuit-board.jpeg){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 2-5 PCB 金手指</figcaption>
</figure>

## 3. PCB 制造流程

下列 19 步流程是标准 PCB 工厂的实际作业顺序，特别适合"认识 4–10 层板从基板到成品"的全景。

### 步骤 1：开料（Cutting）

按订单尺寸把大片铜面板切成生产需要的"工作板"尺寸；为减少运输划伤并提高安全裕量，板四角做圆角处理。

### 步骤 2：内层贴干膜（Inner Layer Dry Film Lamination）

用热压方式把光致抗蚀干膜贴到内层芯板上。干膜对紫外光极度敏感，本工序必须在黄光室（避免短波紫外曝光）进行。

### 步骤 3：曝光（Exposure）

把电路图底片与板精准对位，用紫外灯曝光。**有电路的区域被紫外光照射，干膜硬化；无电路的区域被遮光，干膜仍柔软**，电路图形就此转移到干膜上。

### 步骤 4：显影（Developing）

用显影液洗去未硬化的干膜，露出下面的铜表面。

### 步骤 5：蚀刻（Etching）

用酸 / 碱性蚀刻液去除暴露出来的铜，剩余部分就是需要的电路图形。

### 步骤 6：退膜（Stripping）

用强碱液剥除已硬化的干膜，露出全部电路铜面。

### 步骤 7：内层 AOI（Automated Optical Inspection）

AOI 用高清摄像头快速扫描铜面，把实拍图与原始 Gerber 比对，检查短路、开路、缺口等缺陷。

### 步骤 8：棕化处理（Brown Oxide Treatment）

在内层铜面化学生成一层微观粗化 + 有机金属层，提升与 Prepreg 的层间结合力，防止层压后分层（delamination）。

### 步骤 9：层压（Lamination）

按图纸把多个芯板与 Prepreg 叠合（铜箔在最外），在高温高压下使 Prepreg 完全固化，冷却后形成整体多层板。

设计阶段必须关注：**铜分布均匀性、叠层对称性、盲孔与埋孔的布局**——这些都是层压后无法再改的物理边界。

### 步骤 10：钻孔（Drilling）

钻孔两个目的：插针元件的焊盘过孔 + 不同层铜之间的电气连接孔。**钻孔后的孔壁尚未金属化**，因此还没法导电。

### 步骤 11：沉铜 / 电镀铜（Electroless Copper + Panel Plating）

孔壁首先通过化学沉铜得到一层薄铜（孔壁从绝缘变为导电），然后通过电解电镀加厚到目标铜厚，使孔壁实现层间电气互连。这一步通常在化学与水洗槽中串联完成。

### 步骤 12：外层图形转移（Outer Layer Imaging）

外层图形转移的工序与内层类似：**贴干膜 → 曝光 → 显影 → 图形电镀 → 退膜**，但外层用的是**图形电镀**工艺，先镀一层薄铜再镀锡，锡作为后续蚀刻的抗蚀保护层。

### 步骤 13：外层蚀刻（Outer Layer Etching）

先剥除残留的干膜，再通过化学液蚀掉不需要的铜；锡保护的区域被留下，形成最终的电路图形。

### 步骤 14：阻焊（Soldev Mask Application）

用丝印或涂布方式在板面覆盖阻焊油墨，再经曝光 / 显影把焊盘与过孔开窗露出，其余地方被阻焊覆盖。

### 步骤 15：丝印（Silkscreen）

通过丝印方式在板面印上字符、位号、测试点标号等，再经紫外曝光固化。

### 步骤 16：表面处理（Surface Finish）

裸铜在大气中容易氧化，必须做表面处理才能保证可焊性、信号完整性、寿命。常用工艺对比见下表：

| 工艺 | 全称 | 特点 |
| --- | --- | --- |
| HASL（锡铅 / 无铅） | Hot Air Solder Leveling | 成本低、可焊性好，但不适用于小封装、BGA 与 HDI |
| ENIG | Electroless Nickel Immersion Gold | 镀镍 + 薄金层，平面好、寿命长，适合 BGA / 高频 |
| OSP | Organic Solderability Preservatives | 有机保护膜，环保低成本，但易划伤、多次回流受限 |
| 沉银 | Immersion Silver | 信号完整性好，但易硫化变色 |
| 沉锡 | Immersion Tin | 适合压接 / 多次回流，但易产生锡须 |
| 硬金 | Hard Gold（电镀厚金） | 用于金手指、按键触点，耐磨抗氧化 |

### 步骤 17：成型（Profiling / Routing）

按客户要求的成品外形，把板从工作板上锣（铣）出来或 V-cut 切出来。

### 步骤 18：电气测试（Electrical Test）

用飞针或针床测试设备的开通 / 短路，验证所有网络符合设计图。

### 步骤 19：最终 QC、包装与入库（Final QC, Packaging, Stocking）

外观、尺寸、孔径、厚度、丝印等项目按客户规格抽检或全检，合格品按包装规范入库。

## 4. 关键工艺的工程取舍

### 4.1 选基板：先定 FR-4 还是其它？

- **FR-4**：覆盖率最广，性价比高，普通数字逻辑与低速信号首选。
- **高 Tg FR-4**：耐热好，多层板 / 高密度首选。
- **PTFE / 改性树脂**：Dk / Df 稳定，毫米波、射频首选。
- **铝基板 / 陶瓷基板**：高功率 LED 与功率模块散热首选。
- **PI / PET**：柔性 / 刚挠结合首选。

### 4.2 选层数：先估算走线密度

- 单 / 双面：低成本家电、玩具、电源。
- 4 层：主流消费 / 工业 / 嵌入式产品。
- 6 / 8 层：典型 PCIe、USB 3.x、MIPI、HDMI、千兆网等高速场景。
- 10+ 层：高速服务器、交换机、雷达与复杂 SoC。

### 4.3 选表面处理：装配与可靠性决定

- 一次性消费 / 手工焊接：HASL 即可。
- BGA / QFN / 高频 / 长寿命：ENIG。
- 多次回流焊 / 压接：沉锡。
- 金手指 / 高频触点：硬金。
- 强信号完整性 / 散热敏感：**沉银**（注意硫化问题）。

## 5. FAQ

??? question "Q1：PCB 颜色为什么多数是绿色？"
    颜色来自阻焊层（通常是油墨或干膜感光层），绿色来自酞菁绿染料，对人眼敏感度低，工厂观感舒适，并不影响电气性能。蓝、黑、红、白、紫色都是阻焊染料配方问题，工厂侧都能批量供应。

??? question "Q2：通孔、盲孔、埋孔到底怎么选？"
    通孔最便宜、最可靠，但密度低；盲孔占表层走线空间少；埋孔可完全藏在内部且不占用表层空间，但需要压合前先做完、成本最高。**HDI 板常用 1 阶 / 2 阶盲埋组合**，关键还是看密度与成本。

??? question "Q3：ENIG 与 HASL 哪个更适合 BGA？"
    BGA 球距小、对平面度与共面性要求高，HASL 的锡面不平容易导致虚焊，**ENIG 是 BGA 的常规选择**。HASL 主要用在传统通孔或表贴封装为主的板。

??? question "Q4：为什么 PCB 还需要电气测试？"
    即使通过了 AOI 和过程控制，仍可能存在隐性缺陷：**内层开路、短路、短针、缺孔**。飞行探针或针床测试可以 100% 覆盖网络连通性，是出厂质量底线。

??? question "Q5：HDI 板是不是 HDI 等级越高越好？"
    不一定。HDI 阶数（1 / 2 / 3 阶）指的是"激光盲孔的最多叠层次数"，阶数越高密度越大、成本也剧增。选 HDI 等级前先评估设计密度：超过 4 层 ± 微孔的需求才考虑 2 阶以上。

## 相关阅读

- [PCB 类型与材料选择](pcb-types-materials.md)
- [PCB 设计、制造与互连方式选择](pcb-design-interconnections.md)
- [显示接口详解：MCU、RGB、LVDS、MIPI、SPI、UART 等](display-interface-guide.md)

!!! info "没有找到您需要的内容？"
    如果您需要更多产品、资源或技术支持，欢迎联系我们的团队：

    [**:material-archive-arrow-down: 知识库**](../../knowledge/tags.md){ .md-button .md-button--primary }
    [**:material-archive-arrow-down: 产品与解决方案**](https://www.chinasunyee.com){ .md-button }
    [**:material-email: 联系技术支持**](mailto:info@chinasunyee.com){ .md-button }
