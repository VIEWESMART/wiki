---
title: 优奕视界 1.85 英寸 360x360 TFT 圆形 ESP32-S3 智能屏
description: 一款直径 70 mm 的圆形 ESP32-S3 智能屏开发板，搭载 1.85 英寸 360x360 a-Si TFT 面板，ST77916 QSPI 驱动，电容触摸、I2S 麦克风与 D 类功放、六轴 IMU、SD3078 RTC 及 TF 卡槽。
---

# 1.85 英寸 360x360 TFT 圆形 ESP32-S3 智能屏

<div class="grid cards" markdown>

-   **1.85 英寸 360x360 TFT · ESP32-S3 圆形开发板**
    ---
    圆形系列中的 TFT 版本：一块直径 Ø70 mm 的圆形开发板，以 **ESP32-S3-WROOM-1 (N16R8)** 与 1.85 英寸 360x360 a-Si TFT 面板为核心，面板由 **ST77916** 驱动 IC 通过 QSPI 驱动。另有电容触摸、I2S 数字麦克风、带扬声器接口的 D 类功放、六轴 IMU、SD3078 实时时钟及 TF 卡槽。

    [:material-arrow-left: 返回系列列表](../esp32/){ .md-button }
    [:material-cart: 官方旗舰店](https://shop277726935.taobao.com/){ .md-button .md-button--primary }
    [:simple-gitee: Gitee 仓库](https://gitee.com/VIEWESMART/ESP32-S3-Round-Dev-Board){ .md-button }

</div>

<div align="center">
  <img src="../../../assets/images/ESP32S3RoundDevBoard/1.85 inch 360x360 round tft esp32 s3 smart display.jpg" width="100%" alt="1.85 英寸 360x360 圆形 TFT ESP32-S3 智能屏正反面">
</div>

---

## 1. 产品简介

ESP32-S3 圆形开发板是一块直径 70 mm 的圆形开发板，一面搭载 ESP32-S3-WROOM-1 (N16R8) 模组，另一面安装一块圆形显示屏。同一块 PCB 可装配三种不同的圆形面板，本页介绍 **1.85 英寸 TFT** 版本：一块 360x360 a-Si TFT 面板，由 ST77916 驱动 IC 通过 4-bit QSPI 总线驱动，电容触摸走 I2C。

这是三种圆形面板中最大的一块，显示区达 45.68 x 45.68 mm，也是唯一采用透射式 TFT 而非自发光 AMOLED 的一款。127 PPI 的像素肉眼可辨，明显大于两款 AMOLED 方案，因此很适合仪表式界面、大字号读数，以及那些「完整圆形图表比高像素密度更有用」的成本敏感型产品。典型亮度为 400 cd/m²。

板上保留了完整外设：数字 MEMS 麦克风、I2S DAC 加 D 类功放（可驱动 8 Ω / 2 W 扬声器）、六轴 IMU、带可充电纽扣电池座的 SD3078 实时时钟、TF 卡槽与 RGB 状态灯。供电来自 USB Type-C 或电池，支持自动切换与充电。

仓库为每种面板尺寸都提供了独立的 ESP-IDF 上电自检工程，1.85 英寸版本对应 `examples/esp-idf/ESP32-S3-Round-Dev-Board/viewe1.8`。

### 1.1 产品特性

#### 处理器与无线

- **处理器**：ESP32-S3-WROOM-1，丝印 **ESP32-S3-N16R8**。Xtensa® 双核 32 位 LX7，主频最高 240 MHz。
- **无线**：2.4 GHz Wi-Fi (802.11 b/g/n) 与蓝牙 5 (LE)。

#### 存储

- **Flash**：16 MB。
- **PSRAM**：8 MB。
- **片上**：520 KB SRAM、448 KB ROM。

#### 显示屏

| 参数    | 规格                                  |
| :---- | :---------------------------------- |
| 尺寸    | 1.85 英寸                             |
| 分辨率   | 360 x 360                           |
| 面板类型  | a-Si TFT，normally black             |
| 接口    | QSPI（4 条数据线）                        |
| 驱动 IC | ST77916                             |
| 触摸 IC | CST816S                             |
| 触摸接口  | 电容式，I2C                             |
| 亮度    | 400 cd/m²（典型值）                      |
| 显示色彩  | 262 K（24-bit）                       |
| 像素间距  | 0.2 mm                              |
| 像素密度  | 127 PPI                             |
| 显示区   | 45.68 (H) x 45.68 (V) mm            |
| 模组外形  | 48.08 (H) x 49.95 (V) x 2.12 (T) mm |
| 可视角度  | 全视角                                 |

#### 外设

- **音频输入**：板载 I2S 数字 MEMS 麦克风。
- **音频输出**：I2S DAC 加 D 类功放，MX1.25 2-pin 扬声器连接器，适配 8 Ω / 2 W 扬声器。
- **运动传感**：I2C 上的 QMI8658 六轴惯性传感器（加速度计 + 陀螺仪）。
- **计时**：SD3078 实时时钟，带可充电备用电池座。
- **存储**：TF（Micro SD）卡槽。
- **扩展**：USB_OTG 接口，并引出 IO3、IO8、IO43、IO44 用于 SPI / I2C / I2S / UART。
- **指示**：板载 RGB 灯珠，用于状态指示。
- **按键**：PWR（电源）、BOOT（下载模式）、RST（硬件复位）。

#### 其他

- **供电**：通过 USB Type-C 输入 DC 5 V，或使用电池（板载充放电管理）。两者同时接入时 USB 优先。
- **工作电流**：VCC = 5 V 充电时 1100 mA；非充电运行 210 mA。建议使用 5 V / 1 A 电源。
- **板型尺寸**：Ø70 mm 圆形 PCB。
- **工作温度**：-20 ~ 70 ℃
- **储存温度**：-30 ~ 80 ℃
- **环保**：RoHS 2.0，无卤素。
- **静电防护**：接触放电 ±4 kV，空气放电 ±8 kV。

### 1.2 应用场景

大尺寸高亮圆形 TFT 配合音频前端、电池支持与运动传感，适合需要「清晰圆形读数」而非「照片级画面」的产品：

- 圆形表盘、仪表与仪器刻度盘
- AI 语音助手与桌面陪伴设备
- 智能家居控制旋钮、温控器与场景控制器
- 水泵、阀门与环境监测的工业 HMI
- 可穿戴与吊坠形态的概念产品
- 便携、电池供电的传感器读数设备

## 2. 硬件说明

### 2.1 模块概览

整块板为单块圆形 PCB，正面安装一块面板。下图编号标出板背面的各个功能区块：

<p align="left">
  <img src="../../../assets/images/ESP32S3RoundDevBoard/module overview.jpg" alt="ESP32-S3 圆形开发板模块概览" width="80%">
</p>

| 编号 | 元件               | 说明                                 |
| :- | :--------------- | :--------------------------------- |
| ①  | ESP32-S3-WROOM-1 | 主控模组，16 MB Flash / 8 MB PSRAM。     |
| ②  | 1.5 英寸显示接口       | QSPI FPC 连接器；备用面板尺寸。               |
| ③  | 1.75 英寸显示接口      | QSPI FPC 连接器；备用面板尺寸。               |
| ④  | 1.85 英寸显示接口      | 本版本所用的 QSPI FPC 连接器。               |
| ⑤  | USB Type-C       | 5 V 供电、固件下载与串口调试。                  |
| ⑥  | USER LED         | 电源指示灯。                             |
| ⑧  | BOOT 按键          | 上电或复位时按住可进入下载模式。                   |
| ⑨  | RST 按键           | 硬件复位。                              |
| ⑩  | PWR 按键           | 长按开 / 关机。                          |
| ⑪  | RTC 电池座          | 可充电 RTC 备用电池座。仅限可充电电池。             |
| ⑫  | 贴片麦克风            | 数字 MEMS 麦克风。                       |
| ⑬  | 扬声器接口            | MX1.25 2-pin 连接器，适配 8 Ω / 2 W 扬声器。 |
| ⑭  | TF 卡槽            | Micro SD 卡槽。                       |
| ⑮  | 六轴 IMU           | QMI8658 加速度计与陀螺仪，用于运动检测。           |
| ⑯  | RTC              | SD3078 实时时钟。                       |
| ⑰  | GPIO             | IO3、IO8、IO43、IO44 的扩展焊盘。           |

!!! note "编号与规格书一致"
    上表编号与产品规格书中印刷的编号完全一致。规格书中没有 ⑦ 号标注，本表也按相同顺序排列，以保证图示与规格书同步。

### 2.2 GPIO 定义（引脚图） { #22-gpio-definition-pinout }

下表为产品规格书中的 GPIO 分配汇总，按功能着色标出：

<p align="left">
  <img src="../../../assets/images/ESP32S3RoundDevBoard/gpio summary table.png" alt="ESP32-S3 圆形开发板 GPIO 汇总表" width="85%">
</p>

#### 显示屏（QSPI）

三种面板共用板上同一组 QSPI 总线，因此下表引脚分配与装配哪种面板无关。

| 信号      | ESP32-S3 引脚 | 说明          |
| :------ | :---------- | :---------- |
| LCD_CS  | IO12        | 片选，低电平有效。   |
| LCD_CLK | IO48        | QSPI 时钟。    |
| LCD_DA0 | IO13        | QSPI 数据线 0。 |
| LCD_DA1 | IO47        | QSPI 数据线 1。 |
| LCD_DA2 | IO21        | QSPI 数据线 2。 |
| LCD_DA3 | IO14        | QSPI 数据线 3。 |
| LCD_RST | IO11        | 面板复位。       |
| LCDBLK  | IO45        | 背光与显示电源使能。  |

ST77916 以 4 条数据线的 QSPI 模式寻址，随附示例以 360 x 360、每像素 16 bit 驱动。

#### 触摸

| 信号     | ESP32-S3 引脚 | 说明                    |
| :----- | :---------- | :-------------------- |
| SDA    | IO17        | I2C 数据线，与 IMU、RTC 共用。 |
| SCL    | IO18        | I2C 时钟线，与 IMU、RTC 共用。 |
| TP_INT | IO9         | 触摸中断输出。               |
| TP_RST | IO10        | 触摸 IC 复位。             |

#### 音频

| 功能        | 信号     | ESP32-S3 引脚 |
| :-------- | :----- | :---------- |
| 麦克风       | MICSCK | IO1         |
| 麦克风       | MICSD  | IO2         |
| 麦克风       | MICWS  | IO42        |
| 扬声器 (I2S) | DIN    | IO4         |
| 扬声器 (I2S) | BCK    | IO5         |
| 扬声器 (I2S) | LRCK   | IO6         |
| 扬声器 (I2S) | CTRL   | IO7         |

#### 传感器、存储与主机接口

| 功能          | 信号        | ESP32-S3 引脚 |
| :---------- | :-------- | :---------- |
| IMU         | 中断 1      | IO15        |
| IMU         | 中断 2      | IO16        |
| RTC         | INT       | IO46        |
| I2C 总线      | SDA       | IO17        |
| I2C 总线      | SCL       | IO18        |
| TF 卡        | CMD       | IO38        |
| TF 卡        | CLK       | IO39        |
| TF 卡        | DAT0      | IO40        |
| TF 卡        | CD        | IO41        |
| USB / UART  | U0TXD     | IO43        |
| USB / UART  | U0RXD     | IO44        |
| USB（原生）     | D-        | IO19        |
| USB（原生）     | D+        | IO20        |
| RGB 灯与 BOOT | RGB&BOOT | IO0         |
| 扩展          | 空闲 IO     | IO3、IO8     |

!!! warning "共用与预留引脚"
    - **IO17 / IO18** 上的 I2C 总线由触摸 IC、六轴 IMU 与 RTC 共用。新增同类 I2C 器件时请挂在同一总线上并检查地址冲突。
    - **IO0** 由 BOOT 按键与 RGB 灯状态线共用，规格书中将其合并标注为 **RGB&BOOT**。
    - **IO43 / IO44** 是 ESP32-S3 的 UART0 引脚。USB 接口与扩展焊盘都接到这两根线上，因此外接到 IO43 / IO44 的外设会与默认串口控制台冲突。
    - **IO3** 与 **IO8** 是留给用户扩展的两根引脚。
    - 1.85 英寸示例还把可选的旋转编码器映射到 **IO5 / IO6**。GPIO 汇总表将这两根引脚分配给 I2S 扬声器（BCK / LRCK），因此不要同时启用编码器与音频输出。
    - 同一时间只装配一个显示连接器，三处焊盘是互斥方案，不是多屏同时使用。

### 2.3 机械尺寸

<p align="left">
  <img src="../../../assets/images/ESP32S3RoundDevBoard/dimension drawing.png" alt="ESP32-S3 圆形开发板尺寸图" width="55%">
</p>

PCB 为直径 70 mm 的圆形。1.85 英寸 TFT 模组为 48.08 x 49.95 x 2.12 mm，有效显示区 45.68 x 45.68 mm，是三种方案中最宽的一款，略微超出板边。作为对比，1.5 英寸 AMOLED 模组为 44.3 x 44.3 x 2.405 mm，1.75 英寸 AMOLED 模组为 45.93 x 46.35 mm。

## 3. 软件开发

仓库为每种面板方案提供独立的 ESP-IDF 工程。1.85 英寸 TFT 版本位于 `examples/esp-idf/ESP32-S3-Round-Dev-Board/viewe1.8`，ST77916 面板驱动以本地组件形式随工程提供，无需下载外部 BSP。

### 3.1 软件示例

所有示例代码均可在 [Gitee 仓库](https://gitee.com/VIEWESMART/ESP32-S3-Round-Dev-Board/tree/main/examples/esp-idf/ESP32-S3-Round-Dev-Board) 中找到。

| 框架      | 示例路径                             | 说明                                                          |
| :------ | :------------------------------- | :---------------------------------------------------------- |
| esp-idf | `examples/esp-idf/.../viewe1.8`  | 本板上电自检：ST77916 QSPI 面板、QMI8658 IMU、SD3078 RTC 及 LVGL 演示 UI。 |
| esp-idf | `examples/esp-idf/.../viewe1.5`  | 1.5 英寸 AMOLED 方案的同构固件（CO5300 + 兼容 CST816S 的触摸）。             |
| esp-idf | `examples/esp-idf/.../viewe1.75` | 1.75 英寸 AMOLED 方案的同构固件（CO5300 + CST9217 触摸）。                |
| esp-idf | `examples/esp-idf/.../viewe1.6`  | 附加面板方案（ST77903 QSPI + CST3530 触摸）。                          |
| esp-idf | `examples/esp-idf/.../viewe2.1`  | 附加面板方案（ST7801N）。                                            |

1.85 英寸工程在 `components/` 下内置这些组件：`esp_lcd_st77916`（面板）、`lvgl`、`qmi8658`（IMU）、`sd3078`（RTC）。

!!! note "本工程未内置触摸驱动"
    触摸 IC 挂在 IO17 / IO18 的共用 I2C 总线上，地址脚已固定接好，因此接入它只需把触摸组件放进来即可。1.5 英寸工程内置的 `esp_lcd_touch_cst816s` 组件与本面板规格书中标注的 CST816S 触摸 IC 相匹配，可直接拷贝过来；接线为 SDA IO17、SCL IO18、RST IO10、INT IO9。

### 3.2 快速入门 { #32-getting-started }

#### 3.2.1 准备工作

- **硬件**：装配 1.85 英寸 TFT 的 ESP32-S3 圆形开发板、USB-C 数据线，可选配 8 Ω / 2 W 扬声器与可充电 RTC 电池。
- **软件**：安装 ESP-IDF 插件的 VS Code 与 ESP-IDF v5.1 / 5.2 / 5.3，或独立的 `idf.py` 工具链。
- **供电**：使用 5 V / 1 A 电源。充电时峰值电流约 1100 mA；本面板运行时的耗电明显高于 AMOLED 方案——约 210 mA 对比 130 mA。

#### 3.2.2 ESP-IDF 环境配置

1. **在 VS Code 中打开示例目录** —— `examples/esp-idf/ESP32-S3-Round-Dev-Board/viewe1.8`。
2. **设置目标芯片**为 `esp32s3`。
3. **编译、烧录与监视**。在示例目录下使用命令行：
   ```bash
   idf.py set-target esp32s3
   idf.py build flash monitor
   ```

!!! tip "自检顺序"
    在编写应用代码之前，先确认面板点亮。若背光已亮而画面仍为空白，请先检查 QSPI 数据线与面板复位，再去怀疑驱动。

    若开发板没有自动进入下载模式，请按住 **BOOT**，点按 **RST**，松开 **BOOT**，再开始烧录。

#### 3.2.3 Arduino 环境配置

仓库未提供本板的 Arduino 示例，本板也尚未进入 Espressif `ESP32_Display_Panel` 的支持板列表，因此没有现成的 `BOARD_VIEWE_*` 宏可选。Arduino 仍然可用——面板是标准的 QSPI ST77916 器件——但需要自行提供引脚映射：

1. **安装 [Arduino IDE](https://www.arduino.cc/en/software)** 并添加 ESP32 开发板包：
   ```text
   https://espressif.github.io/arduino-esp32/package_esp32_index.json
   ```
2. **选择开发板**：目标 `ESP32S3 Dev Module`，Flash Size 设为 `16MB (128Mb)`，PSRAM 设为 `OPI PSRAM`。PSRAM 模式设错会导致板子能启动但始终无法分配帧缓冲。
3. **安装库文件**：`ESP32_Display_Panel` 与 `lvgl`（推荐 v8.4.0）。
4. **配置板级参数**：在 `esp_panel_board_supported_conf.h` 中将 `ESP_PANEL_BOARD_DEFAULT_USE_SUPPORTED` 保持为 `0`，并按 [2.2 GPIO 定义](#22-gpio-definition-pinout) 的引脚表填写 `esp_panel_board_custom_conf.h` —— 面板使用单 CS 线的 QSPI，触摸使用 IO17 / IO18 上的 I2C。
5. **编译并上传**，保持 USB-C 线连接。

!!! warning "QSPI 不是 RGB"
    不要开启那些面向 RGB 面板的防撕裂模式，也不要设置 `LV_COLOR_16_SWAP`（除非面板颜色出现反色）。本板通过 QSPI 与面板通信，行为与更大的方形、矩形模组所用的 RGB 总线不同。

#### 3.2.4 PlatformIO 环境配置

PlatformIO 与 Arduino 路线思路相同：使用通用的 ESP32-S3 环境，并自行提供板级定义。

1. 创建 `platformio.ini`，设置 `board = esp32-s3-devkitc-1`，并设置 `board_build.arduino.memory_type = qio_opi` 以启用 Octal PSRAM。
2. 在 `build_flags` 中加入 `-D BOARD_HAS_PSRAM` 与 `-D ARDUINO_USB_CDC_ON_BOOT=false`，让串口控制台保留在 UART0 上。
3. 在 `lib_deps` 中加入 `ESP32_Display_Panel` 与 `lvgl`，再按 Arduino 路线配置自定义板级头文件。

## 4. 相关文档与资源

| 文档                        | 链接                                                                                                                 |
| :------------------------ | :----------------------------------------------------------------------------------------------------------------- |
| 产品规格书（开发板）                | [ESP32 S3 Round Dev Board SPEC V1.1](../../../assets/datasheet/ESP32%20S3%20Round%20Dev%20Board%20SPEC%20V1.1.pdf) |
| 原理图                       | [SCH-ESP32S3RoundDevBoard.png](../../../assets/schematic/SCH-ESP32S3RoundDevBoard.png)                             |
| TFT 屏规格书                  | [ALL-UEOL018VG-RA31-A001A V1.0](../../../assets/datasheet/display/ALL-UEOL018VG-RA31-A001A%20V1.0%20SPEC.pdf)      |
| ESP32-S3-WROOM-1 数据手册（英文） | [esp32-s3-wroom-1_datasheet_en.pdf](../../../assets/datasheet/chip/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf)   |
| ESP32-S3-WROOM-1 数据手册（中文） | [esp32-s3-wroom-1_datasheet_cn.pdf](../../../assets/datasheet/chip/esp32-s3-wroom-1_wroom-1u_datasheet_cn.pdf)   |
| 六轴 IMU 手册                 | [QMI8658A.pdf](../../../assets/datasheet/peripheral/QMI8658A.pdf)                                                  |

## 5. 固件下载


1. 打开仓库的 `tools` 目录，找到 ESP32 烧录工具（`flash_download_tool_3.9.5`），解压并运行。
2. 芯片类型选择 `ESP32-S3` 与对应下载模式，点击 **OK**。按下图 1 → 2 → 3 → 4 → 5 的编号步骤烧录固件。若下载失败，请按住 **BOOT** 键重试。
3. 选择待烧录的 bin 文件。预编译固件（若已发布）放在仓库的 `firmware` 目录下，请查看其中的版本说明并选择合适版本。

若没有预编译固件，请改为从源码编译烧录，参见 [3.2 快速入门](#32-getting-started)。

<p align="center" width="100%">
  <img src="../../../assets/images/Espressif/esp32-s3-firmware-download-1.png" alt="固件下载步骤 1">
  <img src="../../../assets/images/Espressif/esp32-s3-firmware-download-2.png" alt="固件下载步骤 2">
</p>

## 6. 常见问题

??? question "这块板用的是哪颗显示驱动和触摸 IC？"
    1.85 英寸版本为 360x360 a-Si TFT 面板搭配 QSPI 的 `ST77916` 显示驱动，电容触摸由 IO17 / IO18 上 I2C 的 `CST816S` 处理。随附 ESP-IDF 示例内置了 `esp_lcd_st77916` 面板驱动；触摸驱动未随该工程提供，可从 1.5 英寸工程移植过来。

??? question "这块面板和两款 AMOLED 方案相比如何？"
    它是三者中有效区最大的一块，45.68 x 45.68 mm，但像素密度最低，127 PPI，而两款 AMOLED 均为 309 PPI。典型亮度 400 cd/m²。运行电流也更高——约 210 mA，而 AMOLED 方案约 130 mA。

??? question "看完教程还是不知道怎么搭建编程环境，怎么办？"
    请参考[优奕视界常见问题](../../support/faq.md)中的环境搭建说明。

??? question "为什么一打开 Arduino IDE 就提示库文件需要更新？要不要更新？"
    请选择**不**更新库文件。不同版本的库文件之间可能不兼容，不建议更新。

??? question "为什么 UART 引脚没有串口输出？是板子坏了吗？"
    默认工程配置把 UART0 路由到 USB 接口用于调试。IO43 与 IO44 把同一组 UART0 信号引到扩展焊盘上，未重新配置控制台之前不会有输出。在 PlatformIO 中设置 `ARDUINO_USB_CDC_ON_BOOT=false`，或在 Arduino 的 `工具` 菜单中选择 `USB CDC On Boot: Disabled`。

??? question "为什么板子一直下载失败？"
    在开始下载时按住 `BOOT` 键，或者按住 `BOOT`、点按 `RST`、再松开 `BOOT`。这样可强制 ESP32-S3 进入串口 bootloader。

??? question "同一块板能换装其他圆形面板吗？"
    可以。PCB 上有三处独立的 QSPI 显示连接器，分别对应 1.5 英寸 AMOLED、1.75 英寸 AMOLED 与 1.85 英寸 TFT，但同一时间只能装一种面板。每种面板尺寸在 `examples/esp-idf/ESP32-S3-Round-Dev-Board/` 下都有独立的上电自检工程，三者的 QSPI 引脚分配完全相同，因此换面板只需换工程，不必改接线。

??? question "板子从 USB 取电约 1 A，正常吗？"
    那是电池的充电电流，不是运行电流。规格书给出 5 V 充电时约 1100 mA，非充电运行时约 210 mA。推荐使用 5 V / 1 A 适配器。

!!! info "没找到需要的内容？"
    如需更多产品、资料或技术支持，请联系我们的团队：

    [**:material-archive-arrow-down: 资源中心**](../../support/resource.md){ .md-button .md-button--primary }
    [**:material-magnify: 更多产品**](../esp32/index.md){ .md-button  }
    [**:material-email: 联系技术支持**](mailto:info@chinasunyee.com){ .md-button }
