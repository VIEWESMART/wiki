---
title: "PCB 设计、制造与互连方式选择"
description: "面向硬件工程师的 PCB 端到端实操指南：从原理图与 PCB CAD 设计的输入、Gerber / ODB++ / IPC-D-350 等制造数据格式、工厂端 CAM 与 AOI、双面板制造流程，到系统级设计取舍（时钟频率、电源分布、热管理、EMI、环境与成本）的工程权衡。"
date: 2026-09-01
categories:
  - 接口和电子
tags:
  - 工程应用
  - PCB
  - 接口协议
authors:
  - viewe_expert
---

# PCB 设计、制造与互连方式选择

!!! abstract "快速结论"
    PCB 设计不仅是画图，更是**为工厂提供一套可量产的物理规格**的过程：原理图、器件库、Gerber、叠层、SMD 焊盘、阻抗参数、表面处理、钻孔表、测试点。工厂用 CAM 软件接收这些数据，进入面板化 → 钻孔 → 沉铜 → 图形转移 → 蚀刻 → 阻焊 → 表面处理 → 成型 → 电气测试的标准化流程。系统端的设计取舍围绕**速度 / 功耗 / 热 / EMI / 环境 / 成本**六个维度展开。

## 核心要点

- 设计师先选元件库与封装（footprint）、再选材料（FR-4、高频、金属基板）、再叠层与阻抗控制，最后输出**Gerber / ODB++**等制造数据。
- 工厂端通过 CAM 把工程文件转为面板化、激光绘图（LDI）、钻孔与路由 NC、AOI 测试程序、电气测试网表。
- 双面板制造工艺顺序：开料 → 钻孔 → 去毛刺 → 沉铜 → 图形转移 → 蚀刻 → 阻焊 → 表面处理 → 丝印 → 成型 → 电气测试。
- 高速系统（≥ 100 MHz）的设计要点是**传输线阻抗、电源 / 地平面、回流路径、EMI 抑制、信号延迟匹配**。
- 成本与可靠性的平衡贯穿所有设计决策：装配设计良好的项目可降本 25%–35%。

## 1. 电路板设计流程

电子工程师先选择系统功能所需元件，再安排元件之间的电气连接与 PCB 物理布局。设计交付给制造商时需附带大量信息：

- **PCB 尺寸、孔大小与位置、机械外形定义**。
- **参考材料**：基板类型、铜厚、阻焊颜色、表面处理方式。
- **规格**：UL 阻燃等级、介电常数、阻抗规格、弯曲与弯曲半径。
- **测试要求**：电气测试网表、阻抗测试点、ICT / FCT 夹具接口。
- **附加要求**：阻抗匹配、阻抗连续性、阻抗对称、阻抗长度与过孔 stub 控制。

### 1.1 CAD：硬件建模工具

早年 PCB 在 Mylar 膜上手工贴图。今天的 PCB 设计依靠 **EDA / CAD** 软件自动布线、规则检查（DRC）、库管理、信号完整性仿真。

- **元件库（Footprint / Symbol）**：每个元件的物理焊盘图形与电气符号都从库中调用。
- **Footprint / 焊盘图形**：元件引脚与 PCB 焊盘接触的物理图形（如 QFN、QFP、BGA 的 footprint）。
- **设计规则**：最小线宽、最小间距、过孔规格、阻抗匹配规则、差分对规则。

### 1.2 材料选择

设计员必须明确基板与铜厚组合。常见可选：

- **FR-4**：成本低、综合性能好，是消费与工业电子的主流。
- **高频基板**（如 Rogers RO4000、RT/duroid、Taconic TLX）：Dk / Df 稳定，适合毫米波、雷达、射频。
- **金属基板（铝 / 铜基板）**：LED 照明与功率模块专用，强散热。
- **陶瓷基板**：高功率密度模块（IGBT / SiC），高温下绝缘性能好。
- **PI / PET 柔性基板**：折叠 / 弯曲 / 立体装配需求。

### 1.3 表面处理

铜面必须做金属处理以防氧化并保证可焊性。不同表面处理在价格、保质期、可靠性、加工良率上各有偏向：

| 表面处理 | 特点 | 典型应用 |
| --- | --- | --- |
| HASL（锡铅 / 无铅） | 成本低、可焊性好；不平整，BGA 慎用 | 消费类、电源、DIP |
| ENIG（化镍化金） | 平整、可焊性稳定、耐腐蚀 | BGA、QFN、高频、长期可靠性 |
| OSP | 环保、低成本、易划伤 | 单次回流、批量消费类 |
| 沉银 | 信号完整性佳、易硫化变色 | 高速信号、强趋肤效应场景 |
| 沉锡 | 易长锡须 | 压接、多次回流 |
| 硬金 | 耐磨、抗氧化 | 金手指、按键盘 |
| ENEPIG | ENIG + 薄钯层，适用铝线键合 | 元件键合、特殊封装 |

### 1.4 叠层（Stack-up）设计

作为制造前的最后一步，设计师需要给出**叠层表（Stack-up）**，明确每个层的铜厚、芯板厚度、Prepreg 张数、阻抗与对称性要求。

<figure markdown="span" class="displaywiki-figure">
  [![产生制造数据](pcb-design-interconnections-generating-manufacturing-data.png){ width="760" loading="lazy" }](pcb-design-interconnections-generating-manufacturing-data.png){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 1-1 PCB 制造数据生成</figcaption>
</figure>

典型 4 层 1.6 mm FR-4 叠层：

```
1.6 mm 总厚
├─ 35 µm 铜箔 + 介电
├─ 0.36 mm 介电（芯板）
├─ 35 µm 铜箔 + Prepreg
├─ 0.71 mm 介电（Prepreg）
├─ 35 µm 铜箔 + Prepreg
├─ 0.36 mm 介电（芯板）
├─ 35 µm 铜箔 + 介电
```

## 2. 工程数据交接（设计 → 工厂）

设计方与制造方通过制造数据文件传递信息，常用：

- **Gerber（RS-274X）**：最常见的 2D 图形描述，包括铜层、阻焊、丝印、钻孔、轮廓等。
- **ODB++**：含元件、网络、设计意图的完整数据库，多用于复杂多层板。
- **GenCAM**：机器驱动命令格式。
- **IPC-D-350**：工艺文档标准，部分高端工厂用。

同时附带的还有：

- **内 / 行业规范**：IPC-6012（刚性板）等。
- **UL 要求**：阻燃等级、UL 编号、日期码格式。
- **测试要求**：飞针 / 网表 / 测试点分布。
- **定制规格**：阻抗公差、镀镍 / 金厚度、特殊材料。

## 3. 工厂端 CAM 处理

制造从"接收工程数据"开始。工厂用 **CAM（Computer-Aided Manufacturing）** 软件完成三件事：

### 3.1 面板化与绘图

**面板化**是把多块 PCB 图像排进一张大生产板（panel）以提高材料利用率。CAM 在板上自动添加 UL 编号、测试 coupon、定位靶标。LDI（Laser Direct Imaging）用激光直接在感光膜上绘制电路图，省去传统银盐照相底片。

### 3.2 钻孔与成型 NC

CAM 输出数控（NC）钻孔与铣边（routing）数据，下发到钻机 / 锣机。

### 3.3 AOI 与测试数据

CAM 根据 Gerber 与 netlist 自动生成：

- **AOI 测试程序**：以原始设计图为参考，机器扫描与比对外层与内层铜面，识别短路、开路、缺口。
- **网表测试**：从 Gerber 提取所有网络（NET），与设计 netlist 比对。

**两种电气测试对比**：

- **Golden Board（样板）测试**：在没有 netlist 时，由样板上电探针对比；适合 2–6 层板。
- **网表测试**：用 Netlist 对每条线作"开 / 短路"判断，覆盖率 100%，是高可靠性板必经步骤。

## 4. 双面板制造过程

双面板（2-Layer PCB）正反面均有铜，中间一层介质。通过**过孔（Via）**在两面之间导通。

<figure markdown="span" class="displaywiki-figure">
  [![双面 PCB](pcb-design-interconnections-double-sided-pcb.png){ width="760" loading="lazy" }](pcb-design-interconnections-double-sided-pcb.png){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 4-1 双面板结构示意</figcaption>
</figure>

### 4.1 制造前规划

CAM 接收订单与 CAD 数据后做以下准备：

- **面板尺寸**：在材料利用率最优的前提下决定 panel 大小。
- **板面分布**：UL 标识、测试 coupon、层号、靶标、轮廓。
- **基板材料选择**：FR-4 等常规材料；高频用 Rogers 系列；LED 用金属基板。
- **钻孔规格**：孔径、孔位、孔数、孔类型（通孔 / 埋孔 / 盲孔）。
- **工具孔 / 靶标**：用于电镀、丝印、贴片的对位基准。

### 4.2 双面板生产流程

本节描述 SMOBC（Solder Mask over Bare Copper，裸铜上覆盖阻焊）、PTH（Plated Through Hole，镀通孔）、ENIG 接触面、丝印一体的标准双面板制造流程。

**步骤 1：开料（Cut to Size）**

使用"Traveler"工单与原料 CCL（Copper Clad Laminate），按设备允许尺寸把大板切割成工作板。多块 PCB 会拼在同张板上以提升材料利用率。

<figure markdown="span" class="displaywiki-figure">
  [![SMOBC / PTH 双面板制造示意](pcb-design-interconnections-electroless-copper-deposition-plating-through-holes-pth.png){ width="760" loading="lazy" }](pcb-design-interconnections-electroless-copper-deposition-plating-through-holes-pth.png){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 4-2 沉铜 / PTH 工序示意</figcaption>
</figure>

**步骤 2：钻孔（Drilling）**

自动钻机按 NC 数据完成所有通孔、过孔、安装孔。

**步骤 3：去毛刺（Deburring）**

机械刷 / 砂轮去除孔壁毛刺与孔缘铜箔烧灼层，同时清除指纹与氧化物，露出清洁铜面利于沉铜。

**步骤 4：沉铜 / 电镀（PTH）**

孔壁最初是绝缘基材。通过无电沉铜（Electroless Copper Deposition）让孔壁沉积一层薄铜，使其从绝缘变导电。然后电解电镀将铜加厚到目标厚度（典型 1 oz 或更多），实现两面 / 不同层之间的导通。

**步骤 5：图像转移（Imaging / Patterning）**

板面贴覆干膜（光致抗蚀剂），黄光房内经紫外曝光把"电路图"转移到干膜：曝光区硬化、未曝光区保留软态。

**步骤 6：图形电镀（Pattern Plating）**

显影去除未硬化的干膜，露出需要保留的铜面，进入电解槽：铜离子迁移到板表面 / 孔内沉积加厚，再在铜面镀锡（或锡合金）作为后续蚀刻的抗蚀层。

**步骤 7：蚀刻（Etching）**

剥膜后进入蚀刻液（氨基化合物系），未保护的铜被蚀掉，锡保护的区域被保留，最终露出需要的电路图形。最后剥除锡，完成电路成像。

**步骤 8：阻焊（Solder Mask）**

整板涂覆阻焊油墨，干燥后紫外曝光：焊盘开窗处不固化被洗去，其余固化作为永久阻焊。颜色通常是绿色。

**步骤 9：表面处理（Surface Finish）**

按产品要求做 HASL / ENIG / OSP / 沉银 / 沉锡 / 硬金之一。

**步骤 10：丝印（Legend / Silkscreen）**

油墨在板面印位号、字符、版本号、Logo 等，再用紫外固化。

**步骤 11：成型（Profiling / Routing）**

按客户外形锣（铣）出成品，V-cut 或邮票孔方便拼板分离。

**步骤 12：电气测试（Electrical Test）**

飞针测试是把多个探针压到焊盘上施加电流，验证每条网络的开路 / 短路关系。

<figure markdown="span" class="displaywiki-figure">
  [![双面 PCB 制造流程总览](pcb-design-interconnections-double-sided-pcb-manufacturing-process.png){ width="760" loading="lazy" }](pcb-design-interconnections-double-sided-pcb-manufacturing-process.png){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 4-3 双面板制造流程总览</figcaption>
</figure>

## 5. 系统级设计取舍（互连选型）

封装与互连方式的选择不仅取决于系统功能，还取决于**元件型号、系统运行参数、运行环境**。下面六个维度是工程上反复出现的取舍点。

### 5.1 运行速度

电子系统的运行速度是互连设计的核心技术参数。数字系统普遍工作在 100 MHz 以上，CPU、DDR、SerDes 等接口已进入 GHz 量级。

- 信号传播速度与基板材料 Dk 平方根成反比：**Dk 越低，信号越快，但通常成本也越高**。
- "飞行时间（Time of Flight）"与连接器长度成正比：**互连越短，高速性能越好**。
- 当系统速率 ≥ 25 MHz 时应按传输线处理：导线特征阻抗受控、线长匹配、必要时用差分对。
- PCB 上有两种基本传输线拓扑：**带状线（Stripline）** 与 **微带线（Microstrip）**。

### 5.2 功耗与电源分布

时钟频率上升、单芯片门数增长，单芯片功耗已可达 30 W 甚至 100 W。这对供电 / 接地提出更高要求：

- 多层板 MLB 的内层用于"电源 / 地平面"，降低 di/dt 噪声、地弹与回流阻抗。
- 通常 20%–25% 的芯片引脚用于电源与地；在高速系统中为抑制同步切换噪声（SSN），这一比例可上升到 50%。
- 高速芯片同时用 5 V、3.3 V、1.8 V、1.0 V 多档供电，需合理规划电源层分割与去耦。

### 5.3 热管理

封装的"全部供电能量都要从 IC 移走"是大功率系统的根本挑战：

- 服务器级芯片常配合空气 / 液冷冷却；芯片级热仿真、流道仿真已成必经环节。
- 便携 / 桌面系统同样需要关注热点。PCB 是热的不良导体，但可用以下技术增加散热：金属基板、热过孔（thermal via）、内嵌铜块、热管、导热界面材料（TIM）等。

### 5.4 电磁干扰（EMI）

高速 IC 与时钟本身就是辐射源，过量 EMI 会引起邻近设备失效。在 PCB 设计中抑制 EMI 的常用手段：

- 完整地平面（无割缝），避免跨越分区走线。
- 关键信号线包地（guard trace）、控制阻抗、缩短回流路径。
- 差分对保持长度匹配与对称。
- 高速 I/O 加共模扼流圈、TVS、屏蔽罩。
- I/O 滤波、连接器端接。

### 5.5 系统运行环境

电子产品的封装选择与应用场景强相关：

- **车规级**：发动机舱 -40 °C – 125 °C、强振动、EMI、油液腐蚀，对应 AEC-Q100 / Q104 / Q200 应力测试。
- **工控**：长时间运行、粉尘、宽温。
- **办公与消费**：环境稳定，成本优先。
- **医疗**：低漏电流、生物相容性。

IPC 把设备按环境严酷度分了三类（Class 1 / 2 / 3），对应不同程度的工艺与质量要求。

### 5.6 成本

所有工程取舍最终都要回到成本：

- **装配设计（DFA）** 良好可降本 25%–35%。
- **制造设计（DFM）** 良好可降本 20%–30%。
- 设计早期介入的成本节约远大于事后改板。

工程实践中所有"看似互斥"的取舍（速度 vs 成本、可靠性 vs 单板价、热管理 vs 高度），都应在 BOM 成本、产品周期、出货数量与售后维修成本之间做项目级平衡。

## 6. FAQ

??? question "Q1：Gerber 和 ODB++ 在工厂都能接受，怎么选？"
    一般 4 层以下简单板：Gerber 足够；6 层及以上、阻抗控制、HDI、盲埋孔板：优先给 ODB++。**Gerber 是图形，ODB++ 含网络与设计意图**，出错风险前者更高。

??? question "Q2：AOI 检测不到什么缺陷？"
    AOI 通过图像比对检测短路、开路、缺口，对内层有效；但对**内层短路、镀层缺陷、孔铜厚度不足、化学铜不均**等需要切片（Cross-section）或微电阻计（4-wire）测试。建议在出货报告里加 X-层抽样切片报告。

??? question "Q3：HASL / ENIG / OSP 各擅胜场，怎么选？"
    **HASL**（锡铅 / 无铅）：低成本、DIP 友好，BGA 慎用。**ENIG**：平整、稳定，BGA/QFN 首选。**OSP**：消费批量、低成本、不多次回流。**沉银**：高频 / 高速。**沉锡**：压接 / 多次回流（注意锡须）。

??? question "Q4：PCB 上跑 100 MHz 一定要做阻抗匹配吗？"
    当信号上升时间 ≤ 4 倍传输线延迟（"长线效应"）时必须做阻抗控制。简单经验：**走线物理长度 > 上升时间对应传播距离的 1/6** 就视为传输线，需 50 Ω（单端） / 90 Ω / 100 Ω（差分）匹配。100 MHz 看似不高，但很多接口（USB / HDMI / MIPI）边沿速率已达 GHz 级。

??? question "Q5：车规 PCB 与消费 PCB 工艺差异在哪？"
    车规（AEC-Q）需通过 -40 °C – 125 °C 温度循环 + 振动 + 寿命测试，对板材 Tg / Td、孔铜厚度、阻焊附着力、表面处理稳定性的要求显著提高。常见对策是选高 Tg FR-4、ENIG 表面、加厚孔铜、加强叠层对称与测试覆盖。

??? question "Q6：HDI 与传统多层板的本质区别是什么？"
    HDI 的核心是**激光盲孔 + 薄介质**，把线宽 / 线距 / 孔径压到更小；允许 BGA fanout 微孔、信号在高密度下走线。**传统多层板的通孔在 HDI 中会让位给 stagger / stacked 微孔**，但每阶压合都会推高成本。选 HDI 之前先评估密度与回报。

## 相关阅读

- [PCB 结构与制造流程](pcb-construction-process.md)
- [PCB 类型与材料选择](pcb-types-materials.md)
- [显示接口详解：MCU、RGB、LVDS、MIPI、SPI、UART 等](display-interface-guide.md)

!!! info "没有找到您需要的内容？"
    如果您需要更多产品、资源或技术支持，欢迎联系我们的团队：

    [**:material-archive-arrow-down: 知识库**](../../knowledge/tags.md){ .md-button .md-button--primary }
    [**:material-archive-arrow-down: 产品与解决方案**](https://www.chinasunyee.com){ .md-button }
    [**:material-email: 联系技术支持**](mailto:info@chinasunyee.com){ .md-button }
