---
title: "PCB 类型与材料选择"
description: "面向硬件工程师的 PCB 类型与材料选型手册：按"层数 / 基板刚性 / 速率与频率 / 应用领域"四个维度对 PCB 分类，并详细拆解热性能（Tg / Td / CTE / 导热系数）、电气性能（Dk / Df / 损耗角正切）、机械性能（杨氏模量 / 弯曲强度）三大选材决策维度，配合典型工程参数与适用场景。"
date: 2026-09-01
categories:
  - 接口和电子
tags:
  - 工程应用
  - PCB
authors:
  - viewe_expert
keywords:
  - PCB
  - 工程应用
  - 类型与材料选择
og:type: article
og:image: ../assets/brand/viewe-cn-logo.png
twitter:card: summary_large_image
canonical: https://www.displaywiki.com/zh/knowledge/posts/pcb-types-materials
lastmod: 2026-09-02
cover: ../assets/brand/viewe-cn-logo.png
---


# PCB 类型与材料选择

!!! abstract "快速结论"
    PCB 可以从**层数 / 基板刚性 / 速率与频率 / 应用领域**四个维度分类：单 / 双 / 多层板、刚性 / 柔性 / 刚挠结合板、普通 / 高速 / 射频板、LED 金属基板 / 功率陶瓷基板等。选材核心看三类性能—热分解温度**热（Tg / Td / CTE / 导热系数）、电气（Dk / Df / 损耗角正切）、机械（杨氏模量 / 弯曲强度）**，三组参数必须与速率、功耗、热环境强相关才能反推工程取舍。

## 核心要点

- 按 **层数** PCB 可分为单面板、双面板、多层板。
- 按 **基板刚性** 可分为刚性板、柔性板、刚挠结合板。
- 按 **速率与频率** 可分为普通数字、高速数字（PCIe / DDR / USB 3.x / HDMI / MIPI）、射频微波（5G / 雷达 / WiGig）。
- 按 **应用** 可分为 LED 金属基板（铝基板、铜基板）、功率模块陶瓷基板、汽车级长寿命板等。
- 选材看三组特性：**热性能**（决定无铅回流与高温环境的可靠性）、**电气性能**（决定信号完整性、阻抗稳定性）、**机械性能**（决定振动 / 弯曲 / 跌落寿命）。

## 1. PCB 的分类维度

业界通常按下列四个维度分类 PCB，每个维度对应不同的工程取舍：

- **按层数**：单面、双面、多层。
- **按基板材料**：刚性（FR-4 / 高 Tg FR-4 / 高频 / 陶瓷）、柔性（PI / PET）、刚挠结合。
- **按频率 / 速率**：普通数字、高速数字、射频微波。
- **按应用**：消费类 LED 金属基板、功率模块陶瓷基板、车规级板、医疗板、航空航天板。

## 2. 按层数分类

### 2.1 单面板（Single-Sided PCB）

最简单的一类。蓝色 / 黄色 / 绿色分别是基板、导体铜层、阻焊层。单面板只有基板的一面有铜，是元件电气连接的唯一通道。

<figure markdown="span" class="displaywiki-figure">
  [![单面板的结构](pcb-types-materials-the-structure-of-the-single-sided-pcb.jpeg){ width="760" loading="lazy" }](pcb-types-materials-the-structure-of-the-single-sided-pcb.jpeg){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 2-1 单面板结构</figcaption>
</figure>

**优点**：成本最低，制造工艺简单。

**缺点**：导线不能交叉重叠，设计自由度极低。

**应用**：电子玩具、计算器、低成本遥控、简单电源等。常见结构如图 2-1 所示。

### 2.2 双面板（Double-Sided PCB）

基板两面均有铜层，元器件可在两面组装，通过通孔（PTH，Plated Through Hole）在两面之间导通。

<figure markdown="span" class="displaywiki-figure">
  [![双面板的结构](pcb-types-materials-the-structure-of-the-double-sided-pcb.jpeg){ width="760" loading="lazy" }](pcb-types-materials-the-structure-of-the-double-sided-pcb.jpeg){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 2-2 双面板结构</figcaption>
</figure>

<figure markdown="span" class="displaywiki-figure">
  [![双面板 PTH 镀通孔](pcb-types-materials-plated-through-holes-pth-on-the-double-sided-pcb.jpeg){ width="760" loading="lazy" }](pcb-types-materials-plated-through-holes-pth-on-the-double-sided-pcb.jpeg){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 2-3 双面板 PTH 镀通孔</figcaption>
</figure>

**优点**：布线可在两面分布，密度提升明显；过孔 + 表贴结合使元件布局更灵活。

**应用**：电源监测、放大器、工控、消费类电源、消费电子主控板。

### 2.3 多层板（Multi-Layer PCB）

由两层以上导电铜层组成，最外两层为单面，**内层全部为双面**。每个 2 层之间的介质是 Prepreg，可薄至 0.05 mm 甚至更低。

<figure markdown="span" class="displaywiki-figure">
  [![六层 PCB](pcb-types-materials-the-6-layer-pcb.jpeg){ width="760" loading="lazy" }](pcb-types-materials-the-6-layer-pcb.jpeg){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 2-4 六层 PCB</figcaption>
</figure>

全部层在高温高压下一次压合（**Lamination**）成一块板。**多层板** 适合高速、高密度、复杂互连场景：

- **手机 / 笔记本**：典型 6–10 层。
- **服务器 / 交换机**：10–20 层 + HDI。
- **核心路由 / AI 加速**：20+ 层 + 多阶 HDI。

不同层之间的互通用**过孔（PTH）、盲孔（Blind Via）、埋孔（Buried Via）** 三种 Via 完成（"管道 / 埋伏管 / 道"是早期机翻口径，工程师之间请统一用 Via）：见 [PCB 结构与制造流程](pcb-construction-process.md) 与 [PCB 设计、制造与互连方式选择](pcb-design-interconnections.md)。

<figure markdown="span" class="displaywiki-figure">
  [![Via 示意](pcb-types-materials-the-vias.jpeg){ width="760" loading="lazy" }](pcb-types-materials-the-vias.jpeg){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 2-5 过孔、盲孔与埋孔</figcaption>
</figure>

## 3. 按基板刚性分类

### 3.1 刚性 PCB（Rigid PCB）

基板材料是玻璃纤维等刚性材料，**成型后不可弯折**。刚性 PCB 可以是单 / 双 / 多层。

<figure markdown="span" class="displaywiki-figure">
  [![刚性 PCB](pcb-types-materials-the-rigid-pcb.jpeg){ width="760" loading="lazy" }](pcb-types-materials-the-rigid-pcb.jpeg){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 3-1 刚性 PCB</figcaption>
</figure>

**优点**：低电子噪声、抗振动、强度高、机械加工成熟。

**缺点**：一旦制成不可改动。

**应用**：笔记本、温度传感器、GPS、工业控制器、消费类主板。

### 3.2 柔性 PCB（Flexible PCB / FPC）

柔性 PCB 通常用**压延退火铜箔（Rolled-Annealed Copper, RA Copper）** 与 **聚酰亚胺（PI）** 或 **聚酯（PET）** 塑料薄膜组成，可弯折但不影响铜层上的电路。

<figure markdown="span" class="displaywiki-figure">
  [![柔性 PCB](pcb-types-materials-flexible-pcb.jpeg){ width="760" loading="lazy" }](pcb-types-materials-flexible-pcb.jpeg){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 3-2 柔性 PCB</figcaption>
</figure>

**优点**：省空间、降重量、适应不规则外形、可动态弯折。

**应用**：OLED / LCD 模组内部互连、手机摄像头模组、可穿戴设备、医疗探头、连接器补强板。

### 3.3 刚挠结合 PCB（Rigid-Flex PCB）

刚性板与柔性板通过层压组合连接；**刚性板之间的连接由柔性段完成**。这种板可在生产中预折成 3D 形状。

<figure markdown="span" class="displaywiki-figure">
  [![刚挠结合 PCB](pcb-types-materials-rigid-flex-pcb.jpeg){ width="760" loading="lazy" }](pcb-types-materials-rigid-flex-pcb.jpeg){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 3-3 刚挠结合 PCB</figcaption>
</figure>

**优点**：节省内部空间与连接器、提升连接可靠性、降低装配不良率。

**缺点**：工艺复杂、良率低、生产周期长、价格高。

**应用**：医疗、消费电子、航空航天、军工等结构紧凑且可靠性要求高的场景。

## 4. 按速率 / 频率分类

### 4.1 高频 PCB

专门面向 500 MHz – 2 GHz（甚至更高）的应用，要求信号传输速率快、损耗低、抗扰好。

<figure markdown="span" class="displaywiki-figure">
  [![高频 PCB](pcb-types-materials-high-frequency-pcb.jpeg){ width="760" loading="lazy" }](pcb-types-materials-high-frequency-pcb.jpeg){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 4-1 高频 PCB</figcaption>
</figure>

**高频基板必须满足**：

- **耐热**：能承受回流焊、波峰焊、热冲击测试。
- **耐化学**：承受镀液、蚀刻液、电镀药水。
- **抗冲击**：满足振动 / 跌落测试。
- **Dk 稳定**：相对介电常数在宽频率范围内保持稳定。
- **Df 低**：损耗角正切（tan δ）越小，信号损耗越低。
- **低吸水率**：吸水会导致 Dk / Df 漂移。

**应用**：防撞雷达（CAS）、卫星通信、无线电、5G 基站、移动设备射频前端。

### 4.2 高速数字 PCB

针对 PCIe、DDR、USB 3.x、HDMI、MIPI、SATA 等高速数字接口的 PCB。需要：

- **阻抗控制**（50 Ω / 90 Ω / 100 Ω）。
- **差分对长度匹配**（skew 控制）。
- **参考平面完整**（避免跨分割）。
- **低损耗材料**（如 Mid-loss / Low-loss 等级）。

### 4.3 普通数字 / 消费类 PCB

Dk 一般 4.2–4.5，Df 0.02 左右，FR-4 即可满足。

## 5. 按应用分类

### 5.1 金属基板（铝基板、铜基板）

**铝基板 / 铜基板**为 LED 照明、功率模组专用。基板底部贴铜或铝金属层承担高功率密度散热。

### 5.2 陶瓷基板（氧化铝、氮化铝、氧化铍）

高功率模块（IGBT、SiC、GaN）专用。氮化铝陶瓷基板热导率可达 170 W/(m·K)，远超 FR-4。陶瓷基板的电气绝缘与机械强度均远超普通基板，但成本高、不适合大批量消费类。

### 5.3 车规 PCB

符合 AEC-Q100 / Q104 / Q200 应力测试、长寿命、宽温、抗振动。基板多用高 Tg FR-4 或 PI，叠层需更高对称性、表面处理优先 ENIG。

## 6. PCB 材料的关键性能

设计 PCB 时**必须先定义板材**，主要看三类特性：**热、电气、机械**。

### 6.1 热性能

热性能决定 PCB 在极端温度下能否保持机械与电气稳定。

#### 6.1.1 玻璃化转变温度（Tg）

玻璃化转变温度 Tg 是聚合物从玻璃态向高弹态转变的温度范围。**在 Tg 与 Tm（熔化温度）之间**，基板处于"高弹态"；温度低于 Tg 时硬而脆，温度高于 Tg 时偏软。

<figure markdown="span" class="displaywiki-figure">
  [![基板的状态](pcb-types-materials-the-state-of-the-substrate.jpeg){ width="760" loading="lazy" }](pcb-types-materials-the-state-of-the-substrate.jpeg){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 6-1 基板的状态示意</figcaption>
</figure>

实务意义：无铅回流焊峰值温度 245–260 °C，要求板材 Tg > 150 °C（标准 FR-4）；多层 / 高密度 / 高过炉次数应选 Tg > 170 °C 的高 Tg FR-4。

#### 6.1.2 热分解温度（Td）

热分解温度 Td 是基板材料**热失重 5% 的温度**。一旦温度达到或超过 Td，材料发生不可逆分解。

实务要求：Td > 320 °C 的板材能稳定经过多次回流与返修。

#### 6.1.3 热膨胀系数（CTE）

热膨胀系数 CTE（单位 ppm/°C）描述材料随温度变化的尺寸膨胀。

- 基板 X / Y 方向 CTE 受玻璃纤维限制，通常较低（10–20 ppm/°C）。
- **基板 Z 方向 CTE 较高**（50–70 ppm/°C）：温度升高时 Z 向膨胀易破坏孔铜，需选低 Z-CTE 板材。
- 铜的 CTE 约 17 ppm/°C。基板与铜的 CTE 失配将引发应力、断裂、焊点开裂。

#### 6.1.4 热导率（k）

材料的热导率定义为单位厚度下，单位温差能传导的热功率。导热系数高的材料更利于散热：

```text
Q = k · A · ΔT / d
```

铜的 k 高达 386 W/(m·°C)，普通 FR-4 仅 0.3–0.6 W/(m·°C)。**金属基板 / 陶瓷基板**正是用高 k 材料把功率器件热量快速带走。

### 6.2 电气性能

#### 6.2.1 介电常数（Dk / εr）

介电常数 Dk 是材料介电与真空介电的比值。FR-4 的 Dk 通常在 4.2–4.5 之间。

**Dk 越低**：信号传播速度越快，但通常成本越高；Dk 在频率升高时往往下降。

#### 6.2.2 损耗角正切（Df / tan δ）

损耗角正切 Df 表征材料把电磁能量转换为热的损耗。

- 普通 FR-4：Df ≈ 0.02；
- 高频基板（Rogers RO4000 系列）：Df ≈ 0.0021；
- 超低损耗基板：Df < 0.0015。

高 Df 会让高速信号在介质中衰减明显，是 GHz 信号的"杀手"。

### 6.3 机械性能

#### 6.3.1 杨氏模量（Young's Modulus）

胡克定律适用范围内，应力与应变之比：

```text
E = σ / ε = (F / A) / [(L - L₀) / L₀]
```

E 越大材料越不易形变。多层板的"软硬匹配"会影响叠层翘曲与回流后的元件应力。

#### 6.3.2 弯曲强度（Flexural Strength）

弯曲强度又称横断裂力，是材料在三点 / 四点弯曲测试中断裂前的极限应力，单位 psi 或 N/mm²。

实务意义：**柔性 PCB 的弯曲寿命**与弯曲半径、弯曲角、动静态受力、材料厚度、铜层结构都相关。

## 7. 选材决策表

| 速率 / 频率 | 推荐材料 | Df | 适配场景 |
| --- | --- | --- | --- |
| 普通数字 ≤ 100 MHz | FR-4（标准 Tg） | ~ 0.02 | 玩具、家电、消费类主控 |
| 高速数字（PCIe / DDR / USB 3.x / HDMI / MIPI） | 高 Tg FR-4 / Mid-loss | 0.005–0.012 | 主板、网关、嵌入式 SoC |
| 5G / WiFi 6 射频 | 高频 PTFE / 改性树脂 | < 0.005 | 通信基站、Wi-Fi 前端 |
| 雷达 / 毫米波 | 超低损耗 PTFE（Df < 0.002） | < 0.002 | 汽车毫米波、卫星 |
| 大功率 LED | 铝基板 / 陶瓷基板 | 不敏感 | 路灯、车灯、投影光源 |
| 功率模块（IGBT / SiC / GaN） | 氮化铝 / 氮化硅陶瓷 | 不敏感 | 车载逆变器、服务器电源 |
| 长寿命 / 车规 | 高 Tg FR-4 + PI 增强 | 0.005–0.02 | ECU、ADAS、车载 TBOX |

## 8. FAQ

??? question "Q1：单面板和双面板何时选哪个？"
    单面板**只用于最简单电路**（玩具、计算器、遥控、DC 电源初级），因为不能交叉走线。稍复杂的应用（家电主控、电源板、工控板）几乎都需要双面板起跳。

??? question "Q2：高速 PCB 是否一定要选 PTFE？"
    不一定。**5 Gbps 以下**通常高 Tg FR-4 + 中损耗 / 低损耗等级就够；**5–10 Gbps** 选 Mid-loss；**10 Gbps 以上 / PCIe 4.0+ / DDR5** 才需要 PTFE（Rogers、Isola、Hitachi 等）路线。成本永远与速率强相关。

??? question "Q3：Tg 越高的板越好吗？"
    是工程取舍，**越高越耐热但越脆越贵**。标准 FR-4（Tg ~ 130 °C）够普通无铅回流；高 Tg FR-4（Tg ~ 150–170 °C）适合多层 / 多次回流 / 车规；超高 Tg（Tg > 200 °C）适合航天军工。

??? question "Q4：金属基板和陶瓷基板如何选？"
    **LED 照明、电源模块、低中功率**优先铝基板；**高功率密度电力电子（SiC / GaN）**优先氮化铝陶瓷；**散热要求极高 + 绝缘**考虑氮化硼（BeO，但有健康风险，与 SiC 一起慎选）。

??? question "Q5：柔性 PCB 是否可以完全替代刚性 PCB？"
    不行。FPC 成本高、焊接可靠性低、不能承载大电流与大尺寸元件、长期振动后铜皮易疲劳。**FPC 用于连接 / 走线 / 信号互连，刚性板用于元件承载**，刚挠结合板才是兼顾方案。
!!! warning "量产注意"
    在量产或恶劣工况（高低温、湿热、振动、ESD）下，注意该参数的 datasheet 曲线，超出范围会显著降低寿命。


??? question "Q6：高 Dk 和低 Dk 材料的应用差异？"
    低 Dk 让信号传播更快，常用于高速；高 Dk 让铜线做得更窄即可达到相同阻抗（参考 Rogers RO4003 是低 Dk，RO4350B 略高），适合微型化或天线。

## 相关阅读

- [PCB 结构与制造流程](pcb-construction-process.md)
- [PCB 设计、制造与互连方式选择](pcb-design-interconnections.md)
- [显示接口详解：MCU、RGB 并行、LVDS、MIPI、SPI、UART 等](display-interface-guide.md)

!!! tip "延伸阅读：相关主题"
    根据你的阅读主题，按相关度推荐以下文章：

    1. [PCB 结构与制造流程](../pcb-construction-process.md)
    2. [PCB 设计、制造与互连方式选择](../pcb-design-interconnections.md)
    3. [显示接口详解：MCU、RGB 并行、LVDS、MIPI、SPI、UART 等](../display-interface-guide.md)
!!! info "没有找到您需要的内容？"
    如果您需要更多产品、资源或技术支持，欢迎联系我们的团队：

    [**:material-archive-arrow-down: 知识库**](../../knowledge/tags.md){ .md-button .md-button--primary }
    [**:material-archive-arrow-down: 产品与解决方案**](https://www.chinasunyee.com){ .md-button }
    [**:material-email: 联系技术支持**](mailto:info@chinasunyee.com){ .md-button }
