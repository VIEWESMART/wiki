---
title: "显示接口详解：MCU、RGB 并行、LVDS、MIPI、SPI、UART 等"
description: "一篇面向嵌入式工程师的显示接口选型指南，逐项拆解 MCU 8080/6800、并行 RGB 并行、LVDS、MIPI DSI、eDP、SPI、I2C、UART、USB、HDMI、RS232、CAN、RS485 等接口的总线特征、带宽、典型应用与选型取舍，附带接口横向对比表。"
date: 2026-09-01
categories:
  - 接口和电子
tags:
  - 接口协议
  - MIPI DSI
  - LVDS
  - 工程应用
authors:
  - viewe_expert
keywords:
  - LVDS
  - MCU
  - MIPI
  - MIPI DSI
  - RGB
  - SPI
  - UART
  - 工程应用
  - 并行
  - 接口协议
og:type: article
og:image: ../assets/brand/viewe-cn-logo.png
twitter:card: summary_large_image
canonical: https://www.displaywiki.com/zh/knowledge/posts/display-interface-guide
lastmod: 2026-09-02
cover: ../assets/brand/viewe-cn-logo.png
---


# 显示接口详解：MCU、RGB 并行、LVDS、MIPI、SPI、UART 等

!!! abstract "快速结论"
    显示接口的选型与分辨率、传输距离、抗干扰、连接器成本、芯片资源强相关。本文按"并行 / 串行 / 通讯总线"三类逐项拆解主流接口，并给出一张横向对比表，帮助工程师用一张图完成初版选型。

## 核心要点

- **并行接口**适合中小尺寸 TFT：MCU 8080/6800 用于低分辨率小屏，并行 RGB 并行 用于 3.5"–8" 中等分辨率。
- **高速串行接口**适合高分辨率大屏：LVDS 与 MIPI DSI 已成主流，eDP 正在笔记本与一体机快速渗透。
- **低速串行与总线接口**用于参数与触摸：I2C、SPI、UART、USB、HDMI、RS232、CAN、RS485 各自定位不同，需结合场景搭配。
- **选型不是找最强，而是找最匹配**：分辨率、传输距离、抗干扰、芯片资源、连接器成本共同决定接口选择。

## 1. 并行接口

并行接口在小尺寸 TFT 上仍是主力方案，理由是布线简单、对 MCU 资源要求低、协议成熟。

### 1.1 MCU 8080/6800

<figure markdown="span" class="displaywiki-figure">
  [![1-1 MCU 并行 8080/6800](display-interface-guide-1-1-mcu-interface-8080-6800.jpeg){ width="760" loading="lazy" }](display-interface-guide-1-1-mcu-interface-8080-6800.jpeg){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 1-1 MCU 并行 8080/6800</figcaption>
</figure>

MCU 接口由 8080 与 6800 两种时序组成，其中 8080 更为主流。数据线常见 4/8/9/16 位宽度（8 位最常用），控制信号包括 CS（片选）、RS（数据 / 寄存器选择）、RD（读使能）、WR（写使能）。

显示器根据控制总线信号直接接收总线原始数据，通信带宽取决于驱动 IC 的运行速度。以 QVGA 320 × 240 为例，数据使能 信号有效时所需通信带宽约为：

```text
320 × 240 / 8-bit（数据宽度）× 60 fps ≈ 576 kHz
```

**优点**：协议简单、控制逻辑清晰。

**缺点**：需要外部帧缓存（GRAM）；速度受限，难以驱动大尺寸高分辨率屏。

**应用**：单色字符、图形、小尺寸 TFT（< 3.5"）。

<figure markdown="span" class="displaywiki-figure">
  [![MCU/并行接口](display-interface-guide-mcu-parallel-interface.png){ width="760" loading="lazy" }](display-interface-guide-mcu-parallel-interface.png){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 1-2 MCU 并行接口示意</figcaption>
</figure>

### 1.2 并行 RGB 并行 16/18/24 位

RGB 并行 接口按并行方式把像素数据送入显示驱动 IC，常见位宽为 16、18、24 位。信号集合包括：

- **R/G/B 数据线**（6 / 16 / 18 / 24 位，分别对应 RGB666、RGB565、RGB666、RGB888）
- **VSYNC**：垂直同步信号
- **HSYNC**：水平同步信号
- **数据使能**：数据使能（Data Enable）
- **PCLK**：像素时钟

<figure markdown="span" class="displaywiki-figure">
  [![RGB 并行 并行](display-interface-guide-rgb-interface.png){ width="760" loading="lazy" }](display-interface-guide-rgb-interface.png){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 1-3 RGB 并行 接口结构示意</figcaption>
</figure>

以 WVGA 800 × 480 @ 60 fps 为例：

```text
800 × 480 × 60 fps ≈ 23.04 MHz（像素时钟）
```

**优点**：R/G/B 数据直接写入 LCD，无需 GRAM，刷新速率高，协议简单。

**缺点**：控制信号多于 MCU 并行，布线更密；走线长度与阻抗匹配要小心。

**应用**：中等尺寸 TFT（3.5"–8"）。

<figure markdown="span" class="displaywiki-figure">
  [![24 位和 18 位 RGB 并行 接口的例子](display-interface-guide-examples-of-24-bit-and-18-bit-rgb-interface.png){ width="760" loading="lazy" }](display-interface-guide-examples-of-24-bit-and-18-bit-rgb-interface.png){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 1-4 24 位与 18 位 RGB 并行 接口对比</figcaption>
</figure>

### 1.3 串行 RGB 并行 6/8 位

为减少 RGB 并行 接口的信号线数量，可将多比特数据按周期拆分串行传输：

<figure markdown="span" class="displaywiki-figure">
  [![2.3 串行 RGB 并行 6/8 位](display-interface-guide-2-3-serial-rgb-6-8-bits.jpeg){ width="760" loading="lazy" }](display-interface-guide-2-3-serial-rgb-6-8-bits.jpeg){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 1-5 串行 RGB 并行 6/8 位结构</figcaption>
</figure>

以 QVGA 320 × 240 + 16 位色深 + 30 fps 为例：

```text
320 × 240 × 3（三通道）× 30 fps ≈ 6.912 MHz（DCLK）
```

串行 RGB 并行 在保留 RGB 并行 接口优势的同时，把引脚数压到 8 条以内，是中等尺寸 TFT 在低成本 MCU 上常用的折衷。

## 2. 高速串行接口

分辨率越过 800 × 480 之后，并行接口的引脚数与 EMI 问题开始显现；高速串行接口正是为此而设计。

### 2.1 SPI（Serial Peripheral Interface）

SPI 是主从结构，典型拓扑是 1 个主机 + 1 个或多个从机。共 4 根信号线：

- **SCLK**：同步时钟，由主机驱动。
- **MOSI**：主出从入，主机向从机发送数据。
- **MISO**：主入从出，从机向主机回送数据。
- **CS**：片选，每个从机独占。

<figure markdown="span" class="displaywiki-figure">
  [![SPI 方案示例](display-interface-guide-示例.jpeg){ width="760" loading="lazy" }](display-interface-guide-示例.jpeg){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 2-1 SPI 方案示例</figcaption>
</figure>

显示器场景下，SPI 适合传输配置命令与小尺寸低分辨率图像。以 QVGA 320 × 240 + 16 位色深 + 30 fps 为例：

```text
320 × 240 × 16 bit × 30 fps ≈ 36.864 MHz
```

### 2.2 I2C（Inter-Integrated Circuit）

与 SPI 的点对点不同，I2C 是总线型接口，允许 1 个或多个主机搭配多个从机：

> 图 2-2 I2C 方案示意：SDA 串行数据线 + SCL 串行时钟线，主机通过 7-bit / 10-bit 地址帧发起传输，从机 ACK 应答。

> 图 2-3 I2C 链路示例：多个主机 + 多个从机挂在同一总线上，通过仲裁与冲突检测保证逻辑不冲突。

I2C 常见速度档位：

| 模式 | 位速率 |
| --- | --- |
| 标准模式 | 100 kbit/s |
| 快速模式 | 400 kbit/s |
| 快速模式 + | 1 Mbit/s |
| 高速模式 | 3.2 Mbit/s |

I2C 主要用于寄存器配置与触摸上报，很少承担图像传输。

### 2.3 LVDS（Low-Voltage Differential Signaling）

LVDS 是 1994 年推出的电气层标准，而非完整协议。它定义了一种"低电压差分信号"在低成本双绞线上的高带宽传输特性，因此被多个上层协议复用。平板显示领域经常把"平板显示链路"统称为 FPD-Link，部分厂商早期直接用 LVDS 指代整套协议。

<figure markdown="span" class="displaywiki-figure">
  [![2.4 LVDS 低电压差分信号](display-interface-guide-2-4-lvds-low-voltage-differential-signal-it-should-name-fpd-link-for-t.jpeg){ width="760" loading="lazy" }](display-interface-guide-2-4-lvds-low-voltage-differential-signal-it-should-name-fpd-link-for-t.jpeg){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 2-4 LVDS 低电压差分信号</figcaption>
</figure>

<figure markdown="span" class="displaywiki-figure">
  [![LVDS 信号示例](display-interface-guide-features-2.jpeg){ width="760" loading="lazy" }](display-interface-guide-features-2.jpeg){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 2-5 LVDS 信号电平</figcaption>
</figure>

**特点**：差分走线抗电磁干扰、低功耗、可在廉价双绞线上跑到 GHz 级。

**应用**：大尺寸面板（> 7"）、工业控制显示、车载仪表。

<figure markdown="span" class="displaywiki-figure">
  [![LVDS 接口示例](display-interface-guide-example-of-lvds-interface.png){ width="760" loading="lazy" }](display-interface-guide-example-of-lvds-interface.png){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 2-6 LVDS 接口示例</figcaption>
</figure>

### 2.4 MIPI DSI / CSI（MIPI Alliance）

MIPI 联盟面向移动设备降低显示控制器成本，定义了 DSI（显示）与 CSI（摄像头）两套串行总线协议。DSI 在物理层基于 D-PHY，单 lane 速率随版本演进（D-PHY 2.0 单 lane 可达 4.5 Gbit/s），由 1 条时钟 lane + 1 至多条数据 lane 组成。

<figure markdown="span" class="displaywiki-figure">
  [![DSI 显示视图](display-interface-guide-显示器视频.jpeg){ width="760" loading="lazy" }](display-interface-guide-显示器视频.jpeg){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 2-7 DSI 显示视图</figcaption>
</figure>

<figure markdown="span" class="displaywiki-figure">
  [![DSI 系统视图](display-interface-guide-系统视图dsi.jpeg){ width="760" loading="lazy" }](display-interface-guide-系统视图dsi.jpeg){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 2-8 DSI 系统视图</figcaption>
</figure>

总线上的图像数据与 H/V blanking 区间信号交织；显示端无需大帧缓冲，但需持续刷新（30 或 60 fps），否则图像立即丢失。像素数据只走 HS 高速模式，命令则在 LP 低功耗模式 + blanking 区间内传输。

<figure markdown="span" class="displaywiki-figure">
  [![MIPI 接口示例](display-interface-guide-an-example-of-mipi-interface.png){ width="760" loading="lazy" }](display-interface-guide-an-example-of-mipi-interface.png){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 2-9 MIPI 接口示例</figcaption>
</figure>

**特点**：高速、低引脚数、低 EMI；MIPI DSI 已成为智能手机与多数 TFT 模组的默认接口。

### 2.5 eDP（Embedded DisplayPort）

DisplayPort 由 PC 与芯片厂商联盟开发，VESA 标准化。eDP 是面向笔记本、一体机、平板等内置显示器的嵌入式版本，目标是取代 VGA、DVI、FPD-Link（LVDS），并通过主动 / 被动适配器兼容 HDMI 与 DVI。它不仅传输视频，也可携带音频、USB 与其它形式数据。

<figure markdown="span" class="displaywiki-figure">
  [![eDP 接口](display-interface-guide-edp-interface.png){ width="760" loading="lazy" }](display-interface-guide-edp-interface.png){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 2-10 eDP 接口</figcaption>
</figure>

<figure markdown="span" class="displaywiki-figure">
  [![eDP 接口](display-interface-guide-edp-interface-2.png){ width="760" loading="lazy" }](display-interface-guide-edp-interface-2.png){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 2-11 eDP 接口示图</figcaption>
</figure>

**特点**：高带宽、支持高分辨率与高色深；主要用于笔记本与一体机大屏。

## 3. 通讯与外围总线

下面这些接口更像"通用通讯总线"，它们经常用于触摸上报、屏参配置、上位机调试、整机制造测试。

### 3.1 UART 接口

UART（Universal Asynchronous Receiver / Transmitter）实现串行通信，本质是"并行 / 串行"之间的桥梁。UART 一端是 8 条数据线 + 少量控制引脚的总线，另一端是 RX、TX 两条串行线。

<figure markdown="span" class="displaywiki-figure">
  [![UART 接口](display-interface-guide-urat-interface.png){ width="760" loading="lazy" }](display-interface-guide-urat-interface.png){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 3-1 UART 接口</figcaption>
</figure>

优奕视界 的"串口屏"即基于 UART，配合简单指令集即可下发 UI 与控件渲染，被广泛用于工业 HMI 改造与原型验证。

### 3.2 USB 接口

USB（Universal Serial Bus）用于连接 PC 与外围设备（摄像头、鼠标、键盘、打印机、扫描仪、外置存储等），已经历 USB 1.x、USB 2.0、USB 3.x 与 USB 4 多代。电容触摸屏也常通过 USB 桥接 HID 协议上报触摸数据。

<figure markdown="span" class="displaywiki-figure">
  [![USB 接口](display-interface-guide-usb-interface.png){ width="760" loading="lazy" }](display-interface-guide-usb-interface.png){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 3-2 USB 接口</figcaption>
</figure>

### 3.3 HDMI 接口

HDMI（High-Definition Multimedia Interface）是面向"未压缩视频 + 数字音频"的专有接口，把兼容 HDMI 的源设备（如显示控制器）连接到显示器、投影机、数字电视或数字音频设备，是模拟视频标准之后的数字替代。

<figure markdown="span" class="displaywiki-figure">
  [![HDMI 接口](display-interface-guide-hdmi-interface.png){ width="760" loading="lazy" }](display-interface-guide-hdmi-interface.png){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 3-3 HDMI 接口</figcaption>
</figure>

随着彩色 TFT LCD 普及，HDMI 在显示行业的渗透迅速，但实际嵌入式场景仍以 RGB 并行 / LVDS / MIPI 为主，HDMI 多用于外接显示器或视频传输。

### 3.4 RS232 接口

RS232 是经典的串行通信标准，用于连接计算机与外设，支持点对点串行数据交换。常见连接定义：

- **GND**：信号地
- **VCC**：+5 V（部分场景用 ±12 V 电平）

<figure markdown="span" class="displaywiki-figure">
  [![RS232 接口](display-interface-guide-rs232-interface.png){ width="760" loading="lazy" }](display-interface-guide-rs232-interface.png){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 3-4 RS232 接口</figcaption>
</figure>

相比 RS-422、RS-485 与以太网，RS-232 速率较低、传输距离短、电平摆幅大、连接器笨重、不支持多点。在 PC 上，USB 已替代大部分 RS-232 外设功能；新机型几乎不再原生带 RS-232，需通过 USB-to-RS232 转换器或扩展卡连接。但凭借简洁可靠，RS-232 仍在工业机器、网络设备与科学仪器中保有位置。

### 3.5 CAN 总线

CAN（Controller Area Network）由 Bosch 推出的车载总线标准，目标是让 ECU 互相通信而无需中心主机：

<figure markdown="span" class="displaywiki-figure">
  [![CAN 总线系统拓扑](display-interface-guide-can-bus-system-topology.jpeg){ width="760" loading="lazy" }](display-interface-guide-can-bus-system-topology.jpeg){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 3-5 CAN 总线系统拓扑</figcaption>
</figure>

CAN 在 OSI 模型中只覆盖物理层与数据链路层，物理层差分线特征阻抗通常为 120 Ω。逻辑信号：

- 显性（Dominant，逻辑 0）：CAN_H 拉高、CAN_L 拉低，差分约 2 V
- 隐性（Recessive，逻辑 1）：总线不被驱动

<figure markdown="span" class="displaywiki-figure">
  [![WL0F00039000QGAAASB00 实测 CAN_H / CAN_L](display-interface-guide-realistic-measurement-on-wl0f00039000qgaaasb00-can-h-can-l.jpeg){ width="760" loading="lazy" }](display-interface-guide-realistic-measurement-on-wl0f00039000qgaaasb00-can-h-can-l.jpeg){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 3-6 WL0F00039000QGAAASB00 实测 CAN_H / CAN_L</figcaption>
</figure>

CAN 是基于消息 ID 的广播机制，ID 既是内容标识也是优先级仲裁依据。同节点同时发送时，ID 越小优先级越高；位仲裁用"线与"逻辑，赢得仲裁的节点继续发送，输家自动重发，无需中心调度。

### 3.6 CAN 历史速览

- **1986**：CAN 在 SAE 国际汽车工程师协会（底特律）会议上正式发布。
- **1987**：Intel 与 Philips 推出首批 CAN 控制器芯片；1991 年奔驰 W140 成为首款搭载 CAN 多线系统的量产车。
- **1991**：Bosch 发布 CAN 2.0 规范，分 A（11 位 ID，标准格式）与 B（29 位 ID，扩展格式）两部分。
- **1993**：ISO 发布 CAN 国际标准 ISO 11898；后续拆分为 ISO 11898-1（数据链路层）、ISO 11898-2（高速物理层）、ISO 11898-3（低速容错物理层）。
- **2001 / 2004**：欧盟 EOBD 标准分别在汽油车与柴油车生效，要求车辆支持车载诊断总线；美国 2008 年起强制要求所有销售车辆必须支持 CAN。
- **2012**：Bosch 发布 CAN FD 1.0，允许仲裁后切换到更高比特率并传输更长数据，且与 CAN 2.0 网络兼容。

### 3.7 CAN 帧结构与硬件特性

每帧含 11 位（CAN 2.0A）或 29 位（CAN 2.0B）ID、最高 8 字节数据、CRC、ACK 字段。每个节点同时监听自己的发送：若发现总线电平与自己发出的不一致，说明发生仲裁或冲突。

<figure markdown="span" class="displaywiki-figure">
  [![CAN 总线帧数据](display-interface-guide-can-bus-traffic-data-looks.jpeg){ width="760" loading="lazy" }](display-interface-guide-can-bus-traffic-data-looks.jpeg){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 3-7 CAN 总线帧数据</figcaption>
</figure>

<figure markdown="span" class="displaywiki-figure">
  [![有效载荷数据序列](display-interface-guide-data-sequences-in-payload.jpeg){ width="760" loading="lazy" }](display-interface-guide-data-sequences-in-payload.jpeg){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 3-8 有效载荷数据序列</figcaption>
</figure>

硬件上所有节点共用一对差分线，终端匹配 120 Ω。每个节点都可以同时收发。

<figure markdown="span" class="displaywiki-figure">
  [![CAN 固件特性](display-interface-guide-firmware-features.jpeg){ width="760" loading="lazy" }](display-interface-guide-firmware-features.jpeg){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 3-9 CAN 固件特性</figcaption>
</figure>

### 3.8 CAN 的五大优势与应用场景

1. **低成本**：多个 ECU 通过单条 CAN 总线交互，布线轻量、连接器简化。
2. **集中诊断**：CAN 总线为 OBD-II 等中央错误诊断与配置提供天然通路。
3. **强抗扰**：差分物理层对子系统故障与 EMC 都有较好的鲁棒性。
4. **优先级确定**：基于 ID 的位仲裁确保高优先级消息不被中断。
5. **扩展灵活**：每个 ECU 可接收所有广播消息并按相关性处理，便于增加节点。

常见应用：汽车（仪表、ABS、OBD-II）、轨道交通与航空航海、移动机械（堆 / 叉车 / 建筑 / 农业机械）、工业自动化、医疗与实验室自动化。

**限制**：在 CANopen 中，11 位 ID 拆为 4 位功能码 + 7 位节点 ID，单总线最多 127 个唯一地址；J1939 中设备地址上限 253；速度与传输距离互为约束（距离越远速率越低）。

### 3.9 RS485 与 Modbus

RS485 / Modbus 是工业界常见的低成本接口组合。差分对 RS485_A / RS485_B 即可通信，编程时多数操作系统把它视作"串口"，各平台都有对应开发库。Modbus 协议简单直观，常被作为示例。

<figure markdown="span" class="displaywiki-figure">
  [![Modbus 协议](display-interface-guide-rs232-interface.png){ width="760" loading="lazy" }](display-interface-guide-rs232-interface.png){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 3-10 Modbus / RS485 物理链</figcaption>
</figure>

**Modbus 协议要点**：

- **数据格式定义**：Modbus 实际上是"数据格式"而非物理接口，定义主从架构下的通信内容；它可在 RS232、RS422、RS485、TCP 等多种物理层上承载。
- **概念模型**：Modbus 把数据访问视为"寄存器"读写。每个设备定义自己的寄存器映射与地址供外部寻址；写寄存器即下发数据，读寄存器即回读数据。每个寄存器位宽 16 bit。
- **功能码**：不同的读写方式用功能码区分，常见如 03（读保持寄存器）、06（写单个寄存器）、16（写多个寄存器）等。

<figure markdown="span" class="displaywiki-figure">
  [![表 3-1 Modbus 功能码](display-interface-guide-table-5-1-modbus-function-codes.jpeg){ width="760" loading="lazy" }](display-interface-guide-table-5-1-modbus-function-codes.jpeg){ .displaywiki-image-link title="查看原图" }
  <figcaption>图 3-11 Modbus 功能码速查表</figcaption>
</figure>

- **CRC**：消息末尾两个字节是 CRC（Cyclic Redundancy Check，循环冗余校验），本质是查表 + 位运算得到的 16 位校验码；只要按现成库调用即可。
- **寄存器分类**：
    - **设备信息**（版本号、设备名称等）：用 04 读输入寄存器，只在固件升级时变化，连接后读一次即可。
    - **对象属性**（控件类型、位置、颜色等）：用 03 读、16 写，影响 UI 显示；设计阶段确定，运行期不常变。
    - **对象值**（数值、开关、百分比等）：操作中频繁变更，每个对象一个 16 位值，用 06 写单个寄存器。

## 4. 接口横向对比

下列表是常见显示接口的横向对比，侧重"工程取舍"而非性能极限。实际项目应结合分辨率、距离、抗扰要求、芯片资源与连接器成本综合判断。

| 显示接口 | 分辨率范围 | 速率 | 引脚数 | 抗扰 | 功耗 | 传输距离 | 成本 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MCU 8080/6800 | 中等偏低 | 低 | 多 | 中 | 低 | 短 | 低 |
| 并行 RGB 并行 16/18/24 | 中等 | 高 | 多 | 较差 | 高 | 短 | 低 |
| SPI | 小 | 低 | 少（4） | 中 | 低 | 短 | 低 |
| I2C | 小 | 低 | 少（2） | 中 | 低 | 短 | 低 |
| 串行 RGB 并行 6/8 位 | 中等 | 中 | 少 | 较差 | 中 | 短 | 低 |
| LVDS | 大 | 高 | 中 | 好 | 低 | 长 | 中 |
| MIPI DSI | 大 | 高 | 少 | 好 | 低 | 短 | 中 |
| eDP | 大 | 高 | 少 | 好 | 低 | 长 | 中 |
| UART | 小 | 低 | 少（2） | 中 | 低 | 短 | 低 |
| USB | 中 | 高 | 中 | 中 | 中 | 短 | 中 |
| HDMI | 大 | 高 | 中 | 好 | 中 | 短 | 中 |
| RS232 | 小 | 低 | 多（≥ 3） | 中 | 中 | 短 | 低 |
| CAN | 中 | 中 | 少（2） | 好 | 低 | 中 | 低 |
| RS485 / Modbus | 中 | 中 | 少（2） | 好 | 低 | 长 | 低 |

## 5. 选型流程

1. **先定分辨率与尺寸**：3.5" 以下优先 MCU / SPI / I2C；3.5"–8" 走并行 RGB 并行；8" 以上考虑 LVDS / MIPI DSI / eDP。
2. **再看传输距离与抗扰**：差分接口（LVDS / MIPI / eDP / CAN / RS485）在长距离与电磁噪声环境下明显占优。
3. **评估芯片资源**：MCU 资源有限时可优先选 MCU 8080；带 GPU / DSP / 视频专用 IP 时优先 LVDS / MIPI / eDP。
4. **考虑生态与开发成本**：UART / RS485 / Modbus 在工业协议栈成熟，I2C / SPI 在屏参与触摸最常见。
5. **整车与产线测试**：CAN 总线、RS485 在产线诊断与上位机通讯中是首选。

## 6. FAQ

??? question "Q1：分辨率 1024 × 600 及以上的 7"–10" 屏应优先选哪种接口？"
    首选 **MIPI DSI**（4 lane）或 **LVDS**；笔记本、一体机场景可直接上 **eDP**。三者都是差分串行，配 8" 以上方案都能稳定传输。

??? question "Q2：SPI 屏与 MCU 8080 屏如何选？"
    两者定位不同：**SPI** 适合低分辨率小尺寸（< 2"）或触摸上报，引脚极省；**MCU 8080** 是单色字符 / 图形 / 3.5" 以下小 TFT 的事实标准。需不需要更新画面、刷新速率高不高、用不用 GRAM，是核心判断点。

??? question "Q3：为什么 MIPI 在手机上这么普及？"
    MIPI DSI 把并行 RGB 并行 用 4–8 条差分 lane 替换后，引脚数大幅减少、EMI 大幅下降，且 D-PHY 物理层速率足够覆盖手机面板的高分辨率；这正是手机追求"轻薄 + 高 PPI + 长续航"的折衷结果。

??? question "Q4：UART 串口屏主要用在什么场景？"
    用于**工业 HMI 改造与快速原型**：上位机通过串口下发 UI 与控件命令，屏端 MCU 解析后渲染，省去在外置 MCU 上移植 GUI 库的成本。优奕视界 串口屏即基于此。

??? question "Q5：CAN 总线 ID 长度 11 位和 29 位怎么选？"
    11 位（CAN 2.0A）节点少时足够，是主流。29 位（CAN 2.0B / CAN FD）支持更复杂网络，是车载多域控制器趋势。两者在同一总线上通过帧格式区分，可以混跑。

??? question "Q6：Modbus 寄存器读写经常用哪些功能码？"
    - 03 读保持寄存器
    - 06 写单个寄存器
    - 16（0x10）写多个寄存器
    - 04 读输入寄存器

??? question "Q7：eDP 和 MIPI DSI 都能跑 4K，到底差在哪？"
    **eDP** 主要服务笔记本 / 一体机 / 嵌入式主板，链路较长、带 Aux 通道、强调长距与固定连接。**MIPI DSI** 服务手机 / 平板 / 小尺寸强推屏，更短距、引脚更省、热设计更敏感。

## 相关阅读

- [PCB 结构与制造流程](pcb-construction-process.md)
- [PCB 类型与材料选择](pcb-types-materials.md)
- [PCB 设计、制造与互连方式选择](pcb-design-interconnections.md)
- [MIPI 接口基础](mipi-interface-basics.md)
- [LCD 面板时序参数详解](lcd-panel-timing-parameters.md)

!!! tip "延伸阅读：相关主题"
    根据你的阅读主题，按相关度推荐以下文章：

    1. [LCD 屏参详解：把点屏参数讲成能看见的样子](../lcd-panel-timing-parameters.md)
    2. [MIPI 接口详解：DSI、CSI-2 与 D-PHY 图解](../mipi-interface-basics.md)
    3. [PCB 设计、制造与互连方式选择](../pcb-design-interconnections.md)
## 参考数据来源

本文涉及的标准、规格、应用笔记与官方资料：

- [I2C 总线规范（UM10204, NXP）](https://www.nxp.com/docs/en/user-guide/UM10204.pdf)
- [MIPI DSI-2 规范](https://www.mipi.org/specifications/dsi-2)
- [TIA/EIA-644 LVDS 标准](https://standards.globalspec.com/std/1419681/TIA-EIA-644)


!!! info "没有找到您需要的内容？"
    如果您需要更多产品、资源或技术支持，欢迎联系我们的团队：

    [**:material-archive-arrow-down: 知识库**](../../knowledge/tags.md){ .md-button .md-button--primary }
    [**:material-archive-arrow-down: 产品与解决方案**](https://www.chinasunyee.com){ .md-button }
    [**:material-email: 联系技术支持**](mailto:info@chinasunyee.com){ .md-button }
