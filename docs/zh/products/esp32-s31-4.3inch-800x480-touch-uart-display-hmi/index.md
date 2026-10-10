---
title: 优奕视界 4.3 英寸 800x480 ESP32-S31 WiFi6 触控智能屏
description: UES31S043H800V480C-U 是一款 4.3 英寸 800x480 的 ESP32-S31 WiFi6 电容触控智能显示模组，集成 RS485、CAN、USB 2.0 高速 OTG 与立体声音频。
---

# 4.3 英寸 800x480 ESP32-S31 WiFi6 触控智能屏


<div class="grid cards" markdown>

-   **UES31S043H800V480C-U**
    ---
    基于 **ESP32-S31**（双核 RISC-V @ 320 MHz）的**下一代旗舰** ESP32 智能显示模组。
    配备 4.3 英寸 **800x480** IPS 显示屏、**Wi-Fi 6** + 蓝牙 5.4 + 802.15.4、**USB 2.0 高速 OTG**、立体声音频，以及工业级 **RS485 / CAN** 接口。

    [:material-arrow-left: 返回系列列表](../esp32/){ .md-button }
    [:material-cart: 官方旗舰店](https://shop277726935.taobao.com/){ .md-button .md-button--primary }
    [:simple-gitee: Gitee 仓库](https://gitee.com/VIEWESMART/PLCM-UES31S043H800V480C-U){ .md-button }

</div>

<div align="center">
  <img src="../../../assets/images/UES31S043H800V480C-U/4.3 Inch 800x480 ESP32-S31  Smart Display.webp" width="80%" alt="4.3 英寸 800x480 ESP32-S31 WiFi6 触控智能屏">
</div>

---

## 1. 产品简介

**UES31S043H800V480C-U** 是一款由优奕视界设计的高性能智能显示模组。它基于乐鑫 **ESP32-S31-WROOM-3** 模组与一块 4.3 英寸 RGB 电容触控屏（800x480）构建。其 LCD 与触控器件与 UEDX80480043E-WB-B 同料（同为 ST7262 驱动 IC 与 GT911 电容触摸）。主板围绕 ESP32-S31 全新设计：双核 32 位 RISC-V MCU，主频最高 320 MHz，集成 Wi-Fi 6、蓝牙 5.4 LE 及蓝牙经典、USB 2.0 高速 OTG、立体声音频、SDIO 3.0 存储，以及 RS485 / CAN 工业接口。

!!! warning "ESP32-S31 属于预览版芯片"
    ESP-IDF 编译必须使用 `--preview` 选项，例如 `idf.py --preview set-target esp32s31`。带版本号的稳定版不包含 `esp32s31`。模组参数以乐鑫 **ESP32-S31-WROOM-3** 数据手册（预发布版）为准。

### 1.1 产品特性

* **处理器**：
    * **ESP32-S31**：RISC-V 32 位双核处理器，主频最高 **320 MHz**，另含 ULP-RISC-V 协处理器。
    * **无线**：2.4 GHz **Wi-Fi 6**（IEEE 802.11 b/g/n/ax，HT20/40，最高 150 Mbps）、**蓝牙 5.4 LE**（含 LE Audio）、**蓝牙经典**（BR/EDR）以及 **IEEE 802.15.4**（Zigbee / Thread）。
    * **天线**：模组板载 PCB 天线。
    * **安全**：Secure Boot、Flash / PSRAM 加密、密码学加速引擎与 TEE。
* **存储**：
    * **片内**：320 KB ROM、512 KB SRAM、32 KB 低功耗 SRAM。
    * **模组**：**16 MB Quad SPI Flash + 16 MB Octal SPI PSRAM**（ESP32-S31-WROOM-3-N16R16V），可并行访问。
* **显示**：
    * **面板**：4.3 英寸 IPS，**800x480**，RGB 竖条纹。
    * **接口**：40-pin RGB 24-bit。
    * **驱动 IC**：**ST7262E43-G4**。**触摸 IC**：**GT911**（电容式）。
    * **亮度**：400 cd/m²（典型值）。
    * **已验证时序**：PCLK 18 MHz，负极性；HSYNC 1/40/20；VSYNC 1/10/5。
* **外设**：
    * **USB Type-C**：5 V 供电、固件下载与串口调试（CH340C 桥接到 UART0）。
    * **USB Type-A**：专用 **USB 2.0 高速 OTG PHY**（USB_DP / USB_DM，非 GPIO）。Host 5 V 经 TPS2051C 输出（约 500 mA）。
    * **存储**：板载 MicroSD 卡槽，**4-bit SDMMC / SDIO 3.0**。
    * **音频**：**ES8389** 立体声编解码器、双 **NS4150B** 扬声器功放、双模拟麦克风、左/右扬声器接口。
    * **工业**：6-pin 端子提供 **RS485**（SIT3088E，硬件自动换向）与 **CAN**（SIT1050T + 片内 TWAI）。
    * **扩展**：**2x10 pin 2.54 mm 排针（H1）**，引出 UART0 / UART1、I2C、RS485 / CAN GPIO 与 3.3 V / 5 V / GND。
    * **其他**：四路 ADC 按键、RESET / BOOT 按键、WS2812B RGB 灯珠，以及 3 kHz 无源蜂鸣器（默认不贴片）。
* **其他**：
    * **工作温度**：-20 ~ 70 ℃（受 LCD 限制）。
    * **储存温度**：-30 ~ 80 ℃。
    * **MCU 模组额定温度**：-40 ~ 85 ℃。

### 1.2 应用场景

凭借丰富的连接能力与强劲的处理性能，UES31S043H800V480C-U 是以下领域 IoT 设备的理想选择：

* 智能家居控制面板
* 工业自动化 HMI
* 智能家电
* 消费类电子
* 无线数据记录仪
* 触控交互界面
* 教育学习平台

### 1.3 产品命名规则

| 字段 | 代码 | 含义 |
| :--- | :--- | :--- |
| **形态** | PLCM | PCB + LCM（显示模组） |
| **品牌 / 系列** | UE | 优奕视界智能显示模组 |
| **主控** | S31 | ESP32-S31-WROOM-3 |
| **尺寸** | S043 | 4.3 英寸 |
| **分辨率** | H800V480 | 800x480 |
| **触摸** | C | 电容式（GT911） |
| **总线** | U | UART / RS485 / I2C / CAN / USB 2.0 高速 OTG |

---

## 2. 硬件说明

### 2.1 接口说明

本模组通过 UART、RS485 与 CAN 总线与主控单元高效通信，并支持 USB 2.0 高速 OTG 功能，满足多样化的数据交互需求。电容触摸屏采用 GT911 方案，带来顺滑灵敏的触控体验。4.3 英寸屏幕具备 800x480 高清分辨率，显示内容清晰细腻。配合 ESP32-S31-WROOM-3，在高性能处理与低功耗运行之间取得平衡。

<div align="center">
  <img src="../../../assets/images/UES31S043H800V480C-U/Interface_Layout_en.jpg" width="90%" alt="接口布局">
</div>

| 序号 | 接口 | 说明 |
| :---: | :--- | :--- |
| 1 | **主控模组** | ESP32-S31-WROOM-3。双核 RISC-V，主频最高 320 MHz，16 MB Flash + 16 MB PSRAM，PCB 天线。 |
| 2 | **显示接口** | 40-pin RGB 输出。面板本身支持 24-bit；本板实际连接为 **RGB666**（R2-R7 / G2-G7 / B2-B7）。详见「显示屏接口」表。 |
| 3 | **SD 卡槽** | 4-bit SDMMC。CLK = GPIO24，CMD = GPIO25，D0-D3 = GPIO20-23，SD_CTRL = GPIO60（低电平有效）。示例程序以 `SDMMC_FREQ_HIGHSPEED` 挂载 FAT。初始化主机前须先将 GPIO60 拉低。 |
| 4 | **触摸接口** | I2C（SDA = GPIO0，SCL = GPIO1，400 kHz）连接 GT911，与 ES8389 共用。INT 为 GPIO38，RST 见于 6-pin FPC。规格书说明已验证示例未使用 INT 与 RST。 |
| 5 | **USB Type-C** | 5 V 直流输入、程序烧录与串口调试，经 CH340C（UART0）。按住 BOOT（GPIO61），再点按 RESET。 |
| 6 | **USB Type-A** | USB 2.0 高速 OTG PHY（USB_DP / USB_DM）。Host 5 V 经 TPS2051C 输出。VBUS-EN 由硬件上拉。Type-A 默认作为 USB Host 输出 5 V。当同一端口用作连接 PC 的 Device 时，请避免两端同时向 VBUS 倒灌。 |
| 7 | **UART 辅助排针（4-pin，2.5 mm）** | GND / RX / TX / VCC，用于外接串口适配器。 |
| 8 | **RGB 灯珠（WS2812B）** | 一颗 XL-5050RGBC-WS2812B，DIN = GPIO37，由 5 V 经电平转换网络供电。 |
| 9 | **Boot 按键** | BOOT（GPIO61，SW2），用于进入固件下载模式。H1 上同样引出。 |
| 10 | **Reset 按键** | RESET（CHIP-EN，SW1）。 |
| 11 | **外部 GPIO 排针 H1** | 2x10 pin，2.54 mm。详见 H1 引脚表。 |
| 12 | **工业端子 CN3（CAN / RS485）** | CAN_H、CAN_L、VCC、GND、485_B、485_A。请以 PCB 丝印为准。 |
| 13 | **音频** | 左/右扬声器（CN2 / CN1），2-pin 1.25 mm；板载麦克风 MIC1 / MIC2，经 ES8389 与 NS4150B。 |
| 14 | **ADC 按键** | SW3-SW6，接 GPIO42。 |
| 15 | **蜂鸣器** | BEEP_EN = GPIO46，高电平开启，3 kHz 无源型。 |
| 16 | **DCIN / 5V_SEL** | 外部 5 V 输入与 5 V 来源选择跳线。 |

### 2.2 GPIO 定义

<div align="center">
  <img src="../../../assets/images/UES31S043H800V480C-U/GPIO_Definition.png" width="80%" alt="GPIO 定义">
</div>

!!! note "空闲引脚"
    图中**绿色标注的 GPIO**（GPIO55-57）为空闲 IO，未被任何功能占用。

| GPIO 编号 | 当前用途 | 功能说明 |
| :--- | :--- | :--- |
| **CHIP-EN** | 复位 | RESET 按键（SW1） |
| **GPIO0** | I2C SDA | GT911 + ES8389。复位时被上拉（正常启动）。不是 BOOT 按键；H1 上同样引出 |
| **GPIO1** | I2C SCL | GT911 + ES8389；H1 上同样引出 |
| **GPIO2-7** | LCD-R2-R7 | LCD 红色数据，高 6 位 |
| **GPIO8-13** | LCD-G2-G7 | LCD 绿色数据，高 6 位 |
| **GPIO14-19** | LCD-B2-B7 | LCD 蓝色数据，高 6 位 |
| **GPIO20-23** | SD-D0-D3 | SDMMC 4-bit 数据 |
| **GPIO24** | SD-CLK | SDMMC 时钟 |
| **GPIO25** | SD-CMD | SDMMC 命令 |
| **USB_DP / USB_DM** | USB 2.0 HS PHY | 模组专用引脚。请勿配置为 GPIO |
| **GPIO33** | UART1 TX | 已验证为 UART1 TX；同时是 USB Serial / JTAG 焊盘 |
| **GPIO34** | UART1 RX | 已验证为 UART1 RX |
| **GPIO35** | RS485 TX | SIT3088E DI；由 S8050 自动驱动 DE/~RE；H1 上同样引出 |
| **GPIO36** | RS485 RX | SIT3088E RO；H1 上同样引出 |
| **GPIO37** | WS2812 DIN | 板载 XL-5050RGBC-WS2812B |
| **GPIO39** | LCD-BL-EN | 背光使能，高电平有效 |
| **GPIO40** | LCD-PCLK | 像素时钟，18 MHz，负极性 |
| **GPIO42** | ADC KEY | SW3-SW6 电阻分压，ADC1，可用范围约 0-2 V |
| **GPIO43** | LCD-DE | 数据使能 |
| **GPIO44** | LCD-HS | 水平同步（GPIO 编号，非 USB_DM） |
| **GPIO45** | LCD-VS | 垂直同步（GPIO 编号，非 USB_DP） |
| **GPIO46** | BEEP-EN | 蜂鸣器，高电平开启；建议使用 3 kHz PWM |
| **GPIO47** | PA-EN | NS4150B 功放使能，高电平有效 |
| **GPIO48** | I2S MCLK | 原理图上有此引脚；固件示例留空 NC（编解码器 `no_mclk`） |
| **GPIO49** | I2S BCK | ES8389 位时钟 |
| **GPIO50** | I2S WS | ES8389 字选择 / LRCK |
| **GPIO51** | I2S DOUT | MCU → ES8389 DAC |
| **GPIO52** | I2S DIN | ES8389 ADC → MCU |
| **GPIO53** | CAN TX | SIT1050T TXD |
| **GPIO54** | CAN RX | SIT1050T RXD |
| **GPIO55-57** | H1 GPIO | 引出至 H1 |
| **TX0 (IO58) / RX0 (IO59)** | UART0 | CH340C 下载 / 日志；H1 上同样引出 |
| **GPIO60** | SD-CTRL | SD 3.3 V 电源开关，低电平有效 |
| **GPIO61** | BOOT | BOOT 按键（SW2）；H1 上同样引出 |

### 2.3 显示屏接口（40-pin）

| 引脚号 | 符号 | I/O | 说明 |
| :---: | :--- | :---: | :--- |
| 1 | LEDK | P | 背光负极电源 |
| 2 | LEDA | P | 背光正极电源 |
| 3 | GND | P | 电源地 |
| 4 | VDD | P | 逻辑电源，3.3 V |
| 5-12 | R0-R7 | I | 红色数据。本板使用 R2-R7（GPIO2-7）。R0/R1 = NC |
| 13-20 | G0-G7 | I | 绿色数据。本板使用 G2-G7（GPIO8-13）。G0/G1 = NC |
| 21-28 | B0-B7 | I | 蓝色数据。本板使用 B2-B7（GPIO14-19）。B0/B1 = NC |
| 29 | GND | P | 电源地 |
| 30 | CLK | I | 像素时钟，负极性（GPIO40） |
| 31 | DISP | I | 待机模式。通常上拉为高 |
| 32 | HSYNC | I | 水平同步，负极性（GPIO44） |
| 33 | VSYNC | I | 垂直同步，负极性（GPIO45） |
| 34 | DEN | I | 数据使能。DE 为高时允许访问显示（GPIO43） |
| 35 | NC | I | 空脚 |
| 36 | GND | P | 电源地 |
| 37-40 | XR / YD / XL / YU | - | 空脚 |

### 2.4 触摸接口（6-pin）

| 引脚号 | 符号 | I/O | 说明 |
| :---: | :--- | :---: | :--- |
| 1 | RST | P | FPC 上的触摸复位；未使用 |
| 2 | 3.3V | P | 3.3 V 逻辑电源 |
| 3 | GND | P | 电源地 |
| 4 | INT | I | FPC 上的触摸中断；TP INT = GPIO38 |
| 5 | SDA | I | SDA = GPIO0，与 ES8389 共用 |
| 6 | SCL | P | SCL = GPIO1，400 kHz，与 ES8389 共用 |

### 2.5 显示屏规格

| 项目 | 规格 | 单位 | 备注 |
| :--- | :--- | :--- | :--- |
| **像素驱动元件** | IPS TFT | - | - |
| **屏幕尺寸** | 4.3 | 英寸 | 对角线 |
| **分辨率** | 800 (W) x 3 (RGB) x 480 (H) | Dots | - |
| **接口** | RGB 24 bits | - | 40 PIN |
| **模组功耗** | 1.04 | W | 典型值 |
| **有效显示区域** | 95.04 (W) x 53.86 (H) | mm | - |
| **像素间距（W x H）** | 0.1188 (W) x 0.1122 (H) | mm | - |
| **模组尺寸（W x H x D）** | 105.52 (W) x 67.17 (H) x 2.8 (D) | mm | 公差：±0.2 |
| **亮度** | 400 | cd/m² | 典型值 |
| **可视方向** | All O'clock | - | - |
| **显示色彩** | 16.2M Colors | 24 bits | - |

### 2.6 LCD RGB 时序（已验证）

| 参数 | 取值 |
| :--- | :--- |
| **PCLK** | 18 MHz，`pclk_active_neg=true` |
| **水平分辨率** | 800 |
| **垂直分辨率** | 480 |
| **HSYNC 脉宽 / 后肩 / 前肩** | 1 / 40 / 20 |
| **VSYNC 脉宽 / 后肩 / 前肩** | 1 / 10 / 5 |
| **帧缓冲** | RGB888 置于 PSRAM，单缓冲 |

### 2.7 音频接口

音频编解码器为 Everest **ES8389**（I2C 7 位地址 `0x20`）。使用 **I2S0** 全双工模式。48 kHz / 16-bit / 立体声的播放与录音均已验证。无需 MCLK（编解码器配置为 `no_mclk`）。双 **NS4150B** D 类功放驱动左、右扬声器。`PA_EN` = GPIO47。MIC1 与 MIC2 为板载模拟麦克风。

| 信号 | GPIO / 器件 | 说明 |
| :--- | :--- | :--- |
| **I2C SDA / SCL** | GPIO0 / GPIO1 | 与 GT911 共用，400 kHz |
| **I2S BCK** | GPIO49 | 位时钟 |
| **I2S WS** | GPIO50 | 字选择 / LRCK |
| **I2S DOUT** | GPIO51 | DAC 播放 |
| **I2S DIN** | GPIO52 | ADC 录音 |
| **I2S MCLK** | 固件中为 NC | 原理图上为可选 |
| **PA_EN** | GPIO47 | 高电平 = 功放开启 |
| **扬声器** | CN1 / CN2 | NS4150B 差分输出，典型 4 Ω / 3 W 级 |

### 2.8 H1 排针（2 x 10，2.54 mm）

| 序号 | 左列 | 序号 | 右列 |
| :---: | :--- | :---: | :--- |
| 1 | 3V3 | 2 | 5V |
| 3 | 3V3 | 4 | 5V |
| 5 | GND | 6 | GND |
| 7 | GPIO0 (SDA) | 8 | TX1 (GPIO33) |
| 9 | GPIO1 (SCL) | 10 | RX1 (GPIO34) |
| 11 | GPIO35 (485_TX) | 12 | GPIO36 (485_RX) |
| 13 | GPIO53 (CAN_TX) | 14 | GPIO54 (CAN_RX) |
| 15 | GPIO55 | 16 | GPIO56 |
| 17 | GPIO57 | 18 | TX0 |
| 19 | GPIO61 (BOOT) | 20 | RX0 |

!!! warning "复用引脚"
    H1 上的 GPIO35/36 与 GPIO53/54 与板载 RS485、CAN 收发器并联。请勿同时驱动排针与端子。GPIO0/1 已带 I2C 上拉。

### 2.9 USB 2.0 接口

ESP32-S31 在专用 USB_DP / USB_DM 引脚（芯片封装第 44 / 45 脚）上集成了 **USB 2.0 高速 OTG PHY**。这两个引脚不是 GPIO，无需任何 GPIO Matrix 配置。板载提供两个物理接口：

| 端口 | 桥接 / PHY | 角色 | 说明 |
| :--- | :--- | :--- | :--- |
| **Type-C** | CH340C → UART0 | 下载 / 日志 / 5 V 输入 | 按住 BOOT（GPIO61），再点按 RESET |
| **Type-A** | USB 2.0 HS PHY | OTG Host 或 Device | TPS2051C 提供 5 V；VBUS-EN 硬拉高 |

**已验证的应用：**
1. **TinyUSB HID 鼠标** —— 将触摸面板映射为鼠标，在 Windows 与 Linux 上免驱（标准 HID 类）。
2. **USB 扩展显示** —— 需主机侧 IDD / 厂商驱动，JPEG 解码后输出到 RGB 屏。

Type-A 默认作为 USB Host 输出 5 V。当同一端口用作连接 PC 的 Device 时，请避免两端同时向 VBUS 倒灌。

### 2.10 UART / RS485 / CAN

| 接口 | 控制器 | MCU 引脚 | 对外 | 已验证配置 |
| :--- | :--- | :--- | :--- | :--- |
| **UART0** | CH340C | TX0 / RX0 | Type-C / H1 | 下载与监视 |
| **UART1** | GPIO Matrix | TX = 33，RX = 34 | H1 TX1 / RX1 | 115200 8N1 |
| **RS485** | SIT3088E + UART | TX = 35，RX = 36 | CN3 485_A / 485_B / GND | 115200 8N1，自动 DE |
| **CAN** | SIT1050T + TWAI | TX = 53，RX = 54 | CN3 CAN_H / CAN_L / GND | 500 kbit/s，经典 CAN |

**CN3 端子**（请以 PCB 丝印为准）：

| 丝印 | 功能 |
| :--- | :--- |
| **CAN_H** | CAN 高 |
| **CAN_L** | CAN 低 |
| **VCC** | 5 V —— 用作供电前请先确认跳线与负载 |
| **GND** | 公共地 |
| **485_B** | RS485 B |
| **485_A** | RS485 A |

**RS485**：`DE/~RE` 由 485_TX 经 S8050 自动换向。软件上按普通 UART 使用即可；**切勿配置 RTS**。板载已含 120 Ω 终端电阻与 A 上拉 / B 下拉。

**CAN**：板载 120 Ω 终端电阻；CAN_GND 经 0 Ω 连接系统地。

!!! danger "请勿将 USB-TTL 适配器接到 A/B 或 CAN_H/L"

### 2.11 存储、按键、指示灯

**Micro SD**：SDMMC 4-bit —— CLK = GPIO24，CMD = GPIO25，D0-D3 = GPIO20-23，SD_CTRL = GPIO60（低电平有效）。示例程序以 `SDMMC_FREQ_HIGHSPEED` 挂载 FAT。**初始化主机前须先将 GPIO60 拉低。**

**ADC 按键**（在实机上实测）：

| 按键 | 典型电压 | 软件判定区间 | 备注 |
| :--- | :--- | :--- | :--- |
| **空闲** | ≈3.3 V（上拉） | 饱和 / 空闲 | S31 ADC 0 dB 约 0-2 V；空闲时饱和 |
| **SW3** | ≈0.38 V | 100-600 mV | GPIO42 |
| **SW4** | ≈0.82 V | 600-1080 mV | GPIO42 |
| **SW5** | ≈1.34 V | 1080-1605 mV | GPIO42 |
| **SW6** | ≈1.87 V | 1605-2200 mV | GPIO42 |

无法同时检测两个按键（由分压电路本身决定）。部分图纸上的丝印顺序与实测电压不一致，请以本表为准。

**RGB 灯珠**：一颗 WS2812B，DIN = GPIO37。**蜂鸣器**：3 kHz 无源蜂鸣器，BEEP-EN = GPIO46，默认不贴片。

### 2.12 电压与电流

| 项目 | 条件 | 最小 | 典型 | 最大 | 单位 |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **电源电压** | DC | - | 5.0 | - | V |
| **工作电流** | VCC = +5 V，背光最大电流 | 80 | 320 | 500 | mA |
| **工作电流** | VCC = +5 V，背光关闭 | - | 100 | - | mA |

**推荐供电：5 V 1 A 直流。**

### 2.13 可靠性测试

| 项目 | 条件 | 最小 | 典型 | 最大 | 单位 |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **工作温度** | 5 V 电压下 60% RH | -20 | 25 | 70 | ℃ |
| **储存温度** | --- | -30 | 25 | 85 | ℃ |
| **工作湿度** | 25 ℃ | 10% | 60% | 90% | RH |
| **ESD** | --- | 接触：±4KV / 空气：±8KV | | | KV |

### 2.14 结构尺寸图

<div align="center">
  <img src="../../../assets/images/UES31S043H800V480C-U/4.3 Inch 800x480 ESP32-S31  Smart Display outline demension.webp" width="70%" alt="模组外形尺寸">
</div>

!!! note "结构说明"
    * 显示类型：4.3 英寸 800x480 TFT LCD，透射式常黑。
    * 可视方向：All O'clock。LCM 驱动 IC：ST7262E43-G4。
    * TP 类型：G+G。盖板材质：AGC。盖板表面硬度：3H，视窗透过率 ≥ 85%。
    * 背光 LED：27 颗白光 LED，If = 40 mA，Vf = 16 V（典型值）。
    * 有效显示区域：95.04 x 53.86 mm。LCM 外形：105.52 ± 0.2 x 67.2 ± 0.2 mm。
    * 未标注公差：±0.2 mm。符合 RoHS 2.0。

---

## 3. 功能框图

ESP32-S31 在单颗模组上集成了显示（RGB）、触摸（I2C）、音频（I2S）、存储（SDIO 3.0）、工业（UART / RS485 / CAN）与 USB 2.0 高速 OTG 各子系统。

<div align="center">
  <img src="../../../assets/images/UES31S043H800V480C-U/Functional_Block_Diagram.png" width="90%" alt="功能框图">
</div>

!!! note "共用射频前端"
    ESP32-S31 内置 2.4 GHz 射频，支持 Wi-Fi 6、蓝牙 5.4（LE）、蓝牙经典与 802.15.4。由于共用同一射频前端，**Wi-Fi 与蓝牙无法同时收发**，射频会按需在协议间切换。USB 2.0 高速为独立 PHY，不占用该前端。

---

## 4. 软件开发

我们提供一套完整的基于 **ESP-IDF** 的示例代码。所有工程均使用板级支持包 **`viewesmart/bsp_ues31s043h800v480c_u`**。

!!! warning "ESP32-S31 必须使用 ESP-IDF master"
    ESP32-S31 只能使用 **ESP-IDF master**。5.4、5.5 等稳定版不包含该芯片。请先安装乐鑫 **EIM**，再安装 **master** 分支。针对该 target 的所有 `idf.py` 命令都需要加 `--preview` 选项。

### 4.1 快速上手

#### 4.1.1 准备工作

* **硬件**：UES31S043H800V480C-U 开发板、USB-C 数据线。
* **软件**：**ESP-IDF master**（必需），且需具备 `esp32s31` target。

#### 4.1.2 编译与烧录步骤

1.  **克隆仓库**
    ```bash
    git clone https://github.com/VIEWESMART/PLCM-UES31S043H800V480C-U.git
    ```

2.  **检查工具链**
    ```bash
    idf.py --version
    idf.py --preview --list-targets
    ```
    `idf.py --version` 输出的路径中必须包含 `master`。target 列表中必须包含 `esp32s31`。

3.  **打开某个示例目录**
    每个带编号的目录都是独立工程。不要在 `examples/` 或 `examples/esp-idf` 目录下编译。
    例如：`examples/esp-idf/01_display_touch`。

4.  **编译、烧录与监视**
    连接 USB Type-C，选择 **USB-SERIAL CH340** 端口（下文的 `COMx`）。在该示例目录下执行：
    ```bash
    idf.py --preview set-target esp32s31
    idf.py --preview -p COMx flash monitor
    ```

!!! tip "烧录成功的标志"
    当日志出现 **100%**、**Hash of data verified**、**Hard resetting via RTS pin...**，随后打印 `Project name:` 及该目录名时，表示烧录成功。按 `Ctrl+]` 退出监视器。

### 4.2 软件示例

[`examples/esp-idf`](https://github.com/VIEWESMART/PLCM-UES31S043H800V480C-U/tree/main/examples/esp-idf) 目录下共有 **18 个可直接运行的示例**。

| # | 示例名称 | 说明 | 关键技术 / 特性 |
| :-: | :--- | :--- | :--- |
| **01** | [**display_touch**](https://github.com/VIEWESMART/PLCM-UES31S043H800V480C-U/tree/main/examples/esp-idf/01_display_touch) | **LCD / 触摸** | LCD、GT911、背光。 |
| **02** | [**audio_speaker**](https://github.com/VIEWESMART/PLCM-UES31S043H800V480C-U/tree/main/examples/esp-idf/02_audio_speaker) | **扬声器** | ES8389 扬声器播放。 |
| **03** | [**audio_mic**](https://github.com/VIEWESMART/PLCM-UES31S043H800V480C-U/tree/main/examples/esp-idf/03_audio_mic) | **麦克风** | 麦克风录音到 SD 卡。 |
| **04** | [**sdcard**](https://github.com/VIEWESMART/PLCM-UES31S043H800V480C-U/tree/main/examples/esp-idf/04_sdcard) | **SD 卡** | TF / SDMMC 4-bit，挂载 FAT。 |
| **05** | [**adc_buttons**](https://github.com/VIEWESMART/PLCM-UES31S043H800V480C-U/tree/main/examples/esp-idf/05_adc_buttons) | **ADC 按键** | GPIO42 上的 SW3-SW6 电阻分压。 |
| **06** | [**uart1**](https://github.com/VIEWESMART/PLCM-UES31S043H800V480C-U/tree/main/examples/esp-idf/06_uart1) | **UART1** | UART1 GPIO33/34 回环。 |
| **07** | [**rs485**](https://github.com/VIEWESMART/PLCM-UES31S043H800V480C-U/tree/main/examples/esp-idf/07_rs485) | **RS485** | RS485 GPIO35/36，自动换向。 |
| **08** | [**can**](https://github.com/VIEWESMART/PLCM-UES31S043H800V480C-U/tree/main/examples/esp-idf/08_can) | **CAN 总线** | CAN GPIO53/54，500 kbit/s 经典 CAN。 |
| **09** | [**wifi_sta**](https://github.com/VIEWESMART/PLCM-UES31S043H800V480C-U/tree/main/examples/esp-idf/09_wifi_sta) | **Wi-Fi 6** | Wi-Fi 6 Station 模式。 |
| **10** | [**ble_gatt**](https://github.com/VIEWESMART/PLCM-UES31S043H800V480C-U/tree/main/examples/esp-idf/10_ble_gatt) | **BLE HID** | BLE HID 遥控器（`S31-BSP-HID`）。 |
| **11** | [**bt_spp**](https://github.com/VIEWESMART/PLCM-UES31S043H800V480C-U/tree/main/examples/esp-idf/11_bt_spp) | **BLE UART** | BLE UART 回显（`S31-BSP-UART`）。 |
| **12** | [**usb_hid**](https://github.com/VIEWESMART/PLCM-UES31S043H800V480C-U/tree/main/examples/esp-idf/12_usb_hid) | **USB HID** | 由触摸生成 USB HID 鼠标。 |
| **13** | [**led_buzzer**](https://github.com/VIEWESMART/PLCM-UES31S043H800V480C-U/tree/main/examples/esp-idf/13_led_buzzer) | **LED / 蜂鸣器** | WS2812 + 蜂鸣器。 |
| **14** | [**avi_player**](https://github.com/VIEWESMART/PLCM-UES31S043H800V480C-U/tree/main/examples/esp-idf/14_avi_player) | **AVI 播放器** | SD AVI + JPEG + 扬声器。 |
| **15** | [**mp4_player**](https://github.com/VIEWESMART/PLCM-UES31S043H800V480C-U/tree/main/examples/esp-idf/15_mp4_player) | **MP4 播放器** | SD MP4 / MJPEG + AAC + 扬声器。 |
| **16** | [**sd_music**](https://github.com/VIEWESMART/PLCM-UES31S043H800V480C-U/tree/main/examples/esp-idf/16_sd_music) | **音乐播放器** | SD MP3 + LVGL 播放器。 |
| **17** | [**bt_audio**](https://github.com/VIEWESMART/PLCM-UES31S043H800V480C-U/tree/main/examples/esp-idf/17_bt_audio) | **蓝牙音频** | 经典 A2DP / HFP + LVGL（`S31-BT-AUDIO`）。 |
| **18** | [**lvgl**](https://github.com/VIEWESMART/PLCM-UES31S043H800V480C-U/tree/main/examples/esp-idf/18_lvgl) | **出厂 UI** | LVGL 控件 + 触摸。 |

!!! note "示例专属配置"
    * 烧录 **`09_wifi_sta`** 前，请先修改 `main/main.c` 中的 `EXAMPLE_WIFI_SSID` 与 `EXAMPLE_WIFI_PASSWORD`，改为自己的 2.4 GHz 接入点。
    * **`17_bt_audio`** 需要在执行 `idf.py` 前设置 `$env:SDKCONFIG_DEFAULTS = "sdkconfig.defaults;sdkconfig.defaults.esp32s31.classic"`，且不得使用 `idf.py bmgr`。编译 BLE 示例前请清除该变量。
    * **BLE（示例 10、11）与蓝牙经典（示例 17）不可编译进同一固件。**

!!! tip "Arduino 支持"
    Arduino IDE 相关的示例程序仍在适配中，敬请期待。

---

## 5. 相关文档与资料

### 📄 产品文档
| 文档 | 链接 |
| :--- | :--- |
| 智能显示规格书 V1.0 | [UES31S043H800V480C-U.pdf](../../../assets/datasheet/UES31S043H800V480C-U.pdf) |
| 原理图 | [SCH_UES31S043H800V480C-U.pdf](../../../assets/schematic/SCH_UES31S043H800V480C-U.pdf) |
| 屏规格书（UE043WV-RB40-A070A） | [UE043WV-RB40-A070A_V1.0.pdf](../../../assets/datasheet/display/UE043WV-RB40-A070A_V1.0.pdf) |

### 🧠 芯片数据手册
| 芯片 | 文档 | 语言 |
| :--- | :--- | :--- |
| **ESP32-S31-WROOM-3** | [数据手册](../../../assets/datasheet/chip/esp32-s31-wroom-3_wroom-3u_datasheet_en.pdf) | 英文 |
| **ESP32-S31-WROOM-3** | [数据手册](../../../assets/datasheet/chip/esp32-s31-wroom-3_wroom-3u_datasheet_cn.pdf) | 中文 |

### 🔧 外设数据手册
| 器件 | 文档 |
| :--- | :--- |
| **ST7262**（LCD 驱动） | [数据手册](../../../assets/datasheet/display/ST7262.pdf) |
| **GT911**（触摸 IC） | [数据手册（英文）](../../../assets/datasheet/touch/GT911_EN_Datasheet.pdf) / [数据手册（中文）](../../../assets/datasheet/touch/GT911_CN_Datasheet.pdf) |
| **NS4150B**（扬声器功放） | [数据手册](../../../assets/datasheet/peripheral/NS4150B.pdf) |
| **TPS2051C**（USB 电源开关） | [数据手册](../../../assets/datasheet/peripheral/TPS2051CDBVR.pdf) |
| **CH340C**（USB 转串口） | [数据手册](../../../assets/datasheet/peripheral/CH340C.pdf) |
| **WS2812B**（RGB 灯珠） | [数据手册](../../../assets/datasheet/peripheral/XL-5050RGBC-WS2812B%20RGB%20LED.PDF) |

---

## 6. 常见问题

??? question "为什么 idf.py 提示 target esp32s31 未知？"
    ESP32-S31 属于**预览版芯片**。带版本号的稳定版（5.4、5.5）不包含它。请安装 **ESP-IDF master**，并给每条命令都加上 `--preview`，例如 `idf.py --preview set-target esp32s31`。

??? question "如何进入下载模式？"
    按住 **BOOT** 按键（GPIO61）并点按 **RESET**，然后松开 BOOT。连接 USB Type-C 端口，选择 USB-SERIAL CH340 端口。

??? question "RS485 需要配置 RTS 吗？"
    不需要。`DE/~RE` 由 485_TX 经 S8050 自动换向。软件上按普通 UART 使用即可，**切勿配置 RTS**。

??? question "H1 排针与 CN3 端子可以同时使用吗？"
    不可以。H1 上的 GPIO35/36 与 GPIO53/54 与板载 RS485、CAN 收发器并联。请勿同时驱动排针与端子。

??? question "音频编解码器为什么不用 MCLK？"
    GPIO48（I2S MCLK）在原理图上有引出，但固件示例将其留空 NC，并把 ES8389 配置为 `no_mclk`。48 kHz / 16-bit / 立体声的播放与录音均已验证。

??? question "Wi-Fi 和蓝牙可以同时运行吗？"
    两者共用同一 2.4 GHz 射频前端，因此 Wi-Fi 与蓝牙无法同时收发，射频会按需在协议间切换。另外注意，BLE（示例 10、11）与蓝牙经典（示例 17）不可编译进同一固件。

??? question "外接 UART 排针没有日志，端口坏了吗？"
    没有坏。下载与默认日志走 **UART0**，经 Type-C 的 CH340C 桥接（TX0 / RX0，IO58 / IO59）。H1 上的 UART1 为 GPIO33（TX）与 GPIO34（RX），115200 8N1。请勿将 USB-TTL 适配器接到 RS485 A/B 或 CAN_H/L。

??? question "为什么丝印上印的 ADC 按键电压与实测不一致？"
    部分图纸上的丝印顺序与实测电压不一致。请以 2.11 节的实测表为准：SW3 ≈0.38 V、SW4 ≈0.82 V、SW5 ≈1.34 V、SW6 ≈1.87 V。

---

## 相关阅读

<div class="grid cards" markdown>

-   [**:material-view-module: ESP32 智能显示系列**](../esp32/index.md)
    ---
    浏览完整的 ESP32 显示产品家族，从 1.28 英寸旋钮屏到 11 英寸高清大屏。

-   [**:material-chip: ESP32-P4 显示接口与能力边界**](../../knowledge/posts/esp32-p4-display.md)
    ---
    ESP32 显示平台在接口选型与分辨率上限上分别处在什么位置。

-   [**:material-file-document: RGB LCD 时序参数详解**](../../knowledge/posts/lcd-panel-timing-parameters.md)
    ---
    HBP / HFP / VBP / VFP 如何共同决定一套可用的 RGB 面板配置。

</div>

!!! info "没找到需要的内容？"
    如需更多产品、资料或技术支持，请联系我们的团队：

    [**:material-archive-arrow-down: 资源中心**](../../support/resource.md){ .md-button .md-button--primary }
    [**:material-magnify: 更多产品**](../esp32/index.md){ .md-button  }
    [**:material-email: 联系技术支持**](mailto:support@chinasunyee.com){ .md-button }
