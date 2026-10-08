---
title: 优奕视界 4 英寸 480x480 ESP32-S3 触控智能屏
description: UEDX48480040E-WB-A 是一款 4 英寸 480x480 的 ESP32-S3 智能触控显示模组，采用 GC9503V RGB 面板与 FT6336U 电容触摸，支持 Wi-Fi 与蓝牙 5，并提供 Arduino / ESP-IDF / PlatformIO 完整支持。
---

# 4 英寸 480x480 ESP32-S3 触控智能屏

<div class="grid cards" markdown>

-   **UEDX48480040E-WB-A**
    ---
    基于 **ESP32-S3** 的主流 AIoT 智能屏。配备 4 英寸 **480x480** IPS TFT 显示屏与电容触摸屏，支持 Wi-Fi / 蓝牙 5 (LE)，并拥有丰富的扩展接口。

    [:material-arrow-left: 返回系列列表](../esp32/){ .md-button }
    [:material-cart: 官方旗舰店](https://shop277726935.taobao.com/){ .md-button .md-button--primary }
    [:simple-gitee: Gitee 仓库](https://gitee.com/VIEWESMART/UEDX48480040ESP32-4inch-Touch-Display){ .md-button }

</div>

<div align="center">
  <img src="../../../assets/images/UEDX48480040E-WB-A/4 inch 480x480 esp32 tft touch display.jpg" width="100%" alt="4 英寸 480x480 ESP32-S3 触控智能屏正反面">
</div>

---

## 1. 产品简介

**UEDX48480040E-WB-A** 是一款方形 HMI 智能显示模组，以 **ESP32-S3-WROOM-1 (N16R8)** 模组与 4 英寸 **480x480** IPS TFT 面板为核心。面板由 **GC9503V** 驱动 IC 通过 3-wire SPI + RGB 接口驱动，电容触摸面板则通过 I2C 由 **FT6336U** 触摸 IC 读取。

所有器件集成在一块方形 PCB 上：一路 2x21 2.54 mm 扩展排针用于外接外设，两个 USB Type-C 口分别用于供电、下载与串口调试，另有 TF 卡槽、可编程 RGB 灯珠以及 BOOT / RESET 按键。开箱即支持 Arduino、ESP-IDF 与 PlatformIO，三套框架均已移植好 LVGL 示例。

### 1.1 产品特性

#### 处理器与无线

- **处理器**：ESP32-S3-WROOM-1（丝印 ESP32-S3-N16R8）。Xtensa® 双核 32 位 LX7 MCU，主频最高 240 MHz。
- **无线**：2.4 GHz Wi-Fi (802.11 b/g/n)、蓝牙 5 (LE) 及 BLE Mesh。

#### 存储

- **Flash**：16 MB。
- **PSRAM**：8 MB（Octal SPI）。

#### 显示屏

| 参数 | 规格 |
| :--- | :--- |
| 尺寸 | 4.0 英寸 |
| 分辨率 | 480 x 480 |
| 面板类型 | IPS TFT，RGB 垂直条状排列 |
| 接口 | 3-wire SPI + RGB（16-bit 数据总线） |
| 驱动 IC | GC9503V |
| 触摸 IC | FT6336U（兼容 FT5x06 驱动） |
| 触摸接口 | 电容式，I2C |
| 亮度 | 350 cd/m²（典型值） |
| 显示色彩 | 262K |
| 像素密度 | 169 PPI |
| 可视角度 | 全视角 |
| 显示模式 | Normally black |
| 背光 | 白光 LED |
| 有效显示区 | 72.46 (W) x 71.78 (H) mm |
| 模组尺寸 | 84 (W) x 84 (H) x 3.22 (D) mm |

#### 外设

- **连接**：2 路 USB Type-C（一路用于固件下载 / 烧录，一路用于 UART），板载 CH340C USB 转串口桥。
- **扩展**：2x21 2.54 mm 排针，引出 GPIO、UART、3.3 V、5 V 与 GND。
- **存储**：TF 卡槽（SPI 接口）。
- **指示**：板载 WS2812B 可编程 RGB 灯珠。
- **按键**：BOOT（进入下载模式）与 RESET。

#### 其他

- **供电**：DC 5 V（4.0 - 5.5 V），背光点亮时最大 260 mA。建议使用 5 V / 1 A 电源。
- **工作温度**：-20 ~ 70 ℃
- **储存温度**：-30 ~ 80 ℃
- **工作湿度**：10% ~ 90% RH（25 ℃）

### 1.2 应用场景

方形 480x480 面板配合 Wi-Fi / 蓝牙连接能力，UEDX48480040E-WB-A 适合需要一块比例均衡、可旋转 UI 载体的场景：

- 智能家居中控面板与房间温控器
- 工业 HMI 与设备状态显示
- 智能家电前面板
- IoT 数据看板与网关
- 医疗设备与实验室仪器
- 触摸优先、无需旋钮的交互界面

## 2. 硬件说明

### 2.1 模块概览

整块板为单块 94 x 94 mm PCB。下图编号标出板背面的各个功能区块：

<p align="left">
  <img src="../../../assets/images/UEDX48480040E-WB-A/module overview.jpg" alt="模块概览" width="80%">
</p>

| 编号 | 元件 | 说明 |
| :--- | :--- | :--- |
| ① | 2x21 扩展排针 (J1) | 2.54 mm 间距排针，引出 GPIO、UART、3.3 V、5 V 与 GND。 |
| ② | 显示接口 (J2) | 40-pin FPC 连接器，连接 RGB 面板与电容触摸面板。 |
| ③ | USB Type-C (USB) | 5 V 供电，并通过 CH340C 完成固件下载 / 串口调试。 |
| ④ | USB Type-C (UART) | 5 V 供电与外部串口通信。 |
| ⑤ | BOOT / RESET 按键 | BOOT 进入下载模式；RESET 执行硬件复位。 |
| ⑥ | RGB 灯珠 | WS2812B 可编程灯珠，单线控制。 |
| ⑦ | CH340C | 用于下载与调试的 USB 转串口桥。 |
| ⑧ | TF 卡槽 | 挂载在 SPI 总线上的 Micro SD 卡槽。 |
| ⑨ | ESP32-S3-WROOM-1 | 主控模组，16 MB Flash / 8 MB PSRAM。 |

### 2.2 GPIO 定义（引脚图） { #22-gpio-definition-pinout }

#### 显示屏（3-Wire SPI + RGB）

面板先通过 3-wire SPI 总线完成初始化，随后由并行 RGB 总线送入像素数据。

**初始化总线（3-wire SPI）**

| 信号 | ESP32-S3 引脚 | 说明 |
| :--- | :--- | :--- |
| SPI SDA | IO47 | 串行数据，用于配置 RGB 接口参数。 |
| SPI SCK | IO48 | 串行接口时钟。 |
| SPI CS | IO39 | 片选输入，低电平有效。 |

**RGB 数据总线**

| Red | Pin | Green | Pin | Blue | Pin |
| :---: | :---: | :---: | :---: | :---: | :---: |
| R0 | IO4 | G0 | IO10 | B0 | IO15 |
| R1 | IO3 | G1 | IO9 | B1 | IO14 |
| R2 | IO2 | G2 | IO8 | B2 | IO13 |
| R3 | IO1 | G3 | IO7 | B3 | IO12 |
| R4 | IO0 | G4 | IO6 | B4 | IO11 |
|  |  | G5 | IO5 |  |  |

**时序与控制**

| 信号 | ESP32-S3 引脚 | 说明 |
| :--- | :--- | :--- |
| PCLK | IO21 | 像素时钟输入，负极性。 |
| DE | IO18 | 数据输入使能，高电平有效。 |
| VSYNC | IO17 | 垂直同步信号，负极性。 |
| HSYNC | IO16 | 水平同步信号，负极性。 |
| BACKLIGHT | IO38 | 背光使能 (LCD-BL-EN)。 |

#### 触摸（FT6336U）

| 信号 | ESP32-S3 引脚 | 说明 |
| :--- | :--- | :--- |
| SDA | IO40 | 触摸 IC 的 I2C 数据线。 |
| SCL | IO41 | 触摸 IC 的 I2C 时钟线。 |
| TP INT | — | 中断信号，本板未连接。 |
| TP RST | — | 复位信号，本板未连接。 |

触摸 IC 的 I2C 地址为 `0x38`，`01_i2c_scan` 示例即以该地址作为通过判据。

#### 外设

| 功能 | 信号 | ESP32-S3 引脚 |
| :--- | :--- | :--- |
| 按键 | BOOT | IO0 |
| 按键 | RESET | CHIP-EN |
| TF 卡 | CS | IO47 |
| TF 卡 | CLK | IO45 |
| TF 卡 | MOSI | IO42 |
| TF 卡 | MISO | IO46 |
| UART 排针 | TX | IO43 (U0TXD) |
| UART 排针 | RX | IO44 (U0RXD) |
| RGB 灯珠 | WS2812B 数据 | IO42 |
| USB (CH340C) | D- | IO19 |
| USB (CH340C) | D+ | IO20 |

!!! warning "引脚复用说明"
    由于面板使用并行 RGB 总线，显示接口启用后大部分 GPIO 已被占用。

    - **IO42** 由 TF 卡 MOSI 与 WS2812B RGB 灯珠数据线共用。
    - **IO47** 承载面板的 3-wire SPI 数据，同时也用作 TF 卡片选。
    - **IO45** 与 **IO46** 专用于 TF 卡，不插卡时可挪作他用。
    - GPIO35、GPIO36、GPIO37 未使用，也未引出。

    其他外设请使用 2x21 扩展排针。

## 3. 软件开发

仓库提供 Arduino、ESP-IDF 与 PlatformIO 三套可直接运行的示例，包含 LVGL 移植与硬件上电自检流程。

### 3.1 软件示例

所有示例代码均可在 [Gitee 仓库](https://gitee.com/VIEWESMART/UEDX48480040ESP32-4inch-Touch-Display/tree/main/examples) 中找到。

| 框架 | 示例路径 | 说明 |
| :--- | :--- | :--- |
| esp-idf | `examples/esp_idf/01_i2c_scan` | 扫描触摸 I2C 总线。日志中出现绿色 PASS 且列表含 `0x38` 即通过。 |
| esp-idf | `examples/esp_idf/02_wifi` | 扫描周边 Wi-Fi 网络，可选择加入其中一个。 |
| esp-idf | `examples/esp_idf/03_lvgl_port` | LVGL 移植及官方 Demo。UI 显示正常、点击后徽标变绿即通过。 |
| esp-idf | `examples/esp_idf/04_sd` | 挂载 TF 卡并列出 `/sdcard` 目录。 |
| esp-idf | `examples/esp_idf/05_album` | 手机风格启动器，含相册应用。 |
| esp-idf | `examples/esp_idf/06_brookesia_iphone` | 基于 Brookesia 的完整手机 UI，含屏幕与触摸测试应用。 |
| Arduino | `examples/arduino/board/board_static_config` | 使用静态板级定义完成上电自检。 |
| Arduino | `examples/arduino/board/board_dynamic_config` | 使用运行时板级配置完成上电自检。 |
| Arduino | `examples/arduino/drivers/lcd/lcd_3wire_spi_rgb` | 通过 3-wire SPI + RGB 总线驱动面板并显示彩条。 |
| Arduino | `examples/arduino/drivers/touch/touch_i2c` | 通过 I2C 读取 FT6336U 触摸 IC。 |
| Arduino | `examples/arduino/gui/lvgl_v8/simple_port` | 最小化 LVGL v8 移植；也可从 ESP32_Display_Panel 库中获取。 |
| Arduino | `examples/arduino/gui/lvgl_v8/simple_rotation` | 带屏幕旋转的 LVGL v8 移植。 |
| Arduino | `examples/arduino/gui/lvgl_v8/squareline_port` | 由 SquareLine Studio UI 工程驱动的 LVGL v8 移植。 |
| Arduino | `examples/arduino/gui/lvgl_v8/squareline_wifi_clock` | SquareLine 天气时钟 UI，带 Wi-Fi 联网。 |
| PlatformIO | `examples/platformio/lvgl_v8_port` | 面向 PlatformIO 的 LVGL v8 移植，支持防撕裂与旋转。 |

### 3.2 快速入门 { #32-getting-started }

#### 3.2.1 准备工作

- **硬件**：UEDX48480040E-WB-A 开发板、USB-C 数据线、5 V / 1 A 电源。
- **软件**：安装了 ESP-IDF v5.1 / 5.2 / 5.3 的 VS Code，或 ESP32 核心包 v3.0.7 及以上的 Arduino IDE，或安装了 PlatformIO 的 VS Code。
- **库文件**：Arduino IDE 与 PlatformIO 需要安装以下库：

| 库文件 | 版本 | 说明 |
| :--- | :--- | :--- |
| ESP32_Display_Panel | 1.0.0+ | Espressif 出品。驱动 RGB 面板与读取触摸 IC 所必需。 |
| ESP32_IO_Expander | Arduino 自动选择 | ESP32_Display_Panel 的依赖库，按提示一并安装。 |
| esp-lib-utils | Arduino 自动选择 | ESP32_Display_Panel 的依赖库，按提示一并安装。 |
| lvgl | 8.4.0 | 免费开源的嵌入式图形库。 |

#### 3.2.2 ESP-IDF 环境配置

`examples/esp_idf/` 下的每个目录都是独立的 ESP-IDF 工程。首次编译会从 ESP Component Registry 拉取板级支持包 `viewesmart/bsp_uedx48480040e_wb_a`，无需手工挂载组件。

建议按 `01 → 02 → 03 → 04` 的顺序完成硬件自检，再运行 `05` 与 `06`。

1. **在 VS Code 中打开示例目录**（例如 `examples/esp_idf/01_i2c_scan`）。
2. **设置目标芯片**为 `esp32s3`。
3. **编译、烧录与监视**：可使用 VS Code 的按钮，或在示例目录下使用命令行：

    ```bash
    idf.py set-target esp32s3
    idf.py build flash monitor
    ```

!!! tip "自检顺序"
    先跑 `01_i2c_scan`，确认触摸 IC 出现在 I2C 地址 `0x38` 之后再继续。若屏幕无显示或触摸无响应，问题几乎总是出在上电自检流程，而非应用代码。

#### 3.2.3 Arduino 环境配置

1. **安装 [Arduino IDE](https://www.arduino.cc/en/software)**
   选择与系统匹配的安装包。新手可先参考[优奕视界常见问题](../../support/faq.md)中的环境搭建说明。
2. **安装 ESP32 开发板包**：
    - 打开 Arduino IDE。
    - 进入 `文件` > `首选项`。
    - 在 `附加开发板管理器网址` 中添加：
      ```text
      https://espressif.github.io/arduino-esp32/package_esp32_index.json
      ```
    - 进入 `工具` > `开发板` > `开发板管理器`。
    - 搜索 Espressif 的 `esp32`，安装 3.0.7 或更高版本。
3. **安装库文件**：
    - 进入 `项目` > `加载库` > `管理库`。
    - 搜索 Espressif 的 `ESP32_Display_Panel`，安装 1.0.0 或更高版本。弹出依赖提示时点击「全部安装」。
    - 安装 `lvgl`（推荐 v8.4.0）。
4. **打开示例**：
    - 本仓库：`examples/arduino/gui/lvgl_v8/simple_port`。
    - 或从库中打开：`文件` > `示例` > `ESP32_Display_Panel` > `Arduino` > `gui` > `lvgl_v8` > `simple_port`。
5. **选择开发板**：
    - 目标板：`ESP32S3 Dev Module`。
    - 设置：
        - Core Debug Level: None
        - USB CDC On Boot: Disabled
        - USB DFU On Boot: Disabled
        - Flash Size: 16MB (128Mb)
        - Partition Scheme: 16M Flash (3MB APP/9.9MB FATFS)
        - PSRAM: OPI PSRAM（至关重要！）
6. **启用板级配置**：
   打开示例中的 `esp_panel_board_supported_conf.h`，将 supported board 开关置为 `1`，并取消本板宏定义的注释：

   ```c
   /**
    * @brief Flag to enable supported board configuration (0/1)
    *
    * Set to `1` to enable supported board configuration, `0` to disable
    */
   #define ESP_PANEL_BOARD_DEFAULT_USE_SUPPORTED       (1)

   // #define BOARD_VIEWE_UEDX32480035E_WB_A
   // #define BOARD_VIEWE_UEDX48270043E_WB_A
    #define BOARD_VIEWE_UEDX48480040E_WB_A
   // #define BOARD_VIEWE_UEDX80480043E_WB_A
   // #define BOARD_VIEWE_UEDX80480050E_WB_A
   ```
7. **配置示例**：
    - *[可选]* 修改 `lvgl_v8_port.h` 中的宏定义：
        - 本板使用 `RGB` 接口，可将 `LVGL_PORT_AVOID_TEARING_MODE` 设为 `1` / `2` / `3` 开启防撕裂功能，再按需要设置 `LVGL_PORT_ROTATION_DEGREE` 旋转角度。
    - *[可选]* 修改 `lv_conf.h` 中的宏定义：
        - **不要**将 `LV_COLOR_16_SWAP` 设为 `1`。该选项只对 `SPI` / `QSPI` 面板有效，不适用于本板所用的 RGB 总线。
8. **选择正确的端口**：
    - 用 USB-C 线连接开发板。
    - 进入 `工具` > `端口`，选择对应端口。
9. **编译与上传**：
    - 点击左上角 `√` 编译。
    - 编译无误后连接开发板，点击 `→` 下载。

!!! tip "配置提示"
    在 `esp_panel_board_supported_conf.h` 中，请确保已取消 `#define BOARD_VIEWE_UEDX48480040E_WB_A` 的注释。

    不要同时启用 `ESP_PANEL_BOARD_DEFAULT_USE_SUPPORTED` 与 `ESP_PANEL_BOARD_DEFAULT_USE_CUSTOM`。
    也不能同时启用多个 Espressif 支持的板级配置。

#### 3.2.4 PlatformIO 环境配置

1. **打开示例**
   在装有 PlatformIO 插件的 VS Code 中打开 `examples/platformio/lvgl_v8_port`。
2. **选择开发板**
   `platformio.ini` 中的 `[platformio]:default_envs` 决定编译哪个环境，且 `boards/` 目录下必须存在对应的板级描述文件。
   该示例已内置若干 Espressif 开发板以及 `BOARD_VIEWE_UEDX80480070E_WB_A` 的描述文件。若需为本板编译，请新增 `BOARD_VIEWE_UEDX48480040E_WB_A` 的板级文件（复制一份 ESP32-S3 RGB 板级文件并更新引脚定义），或选择 `BOARD_CUSTOM` 并填写 `src/esp_panel_board_custom_conf.h`。
3. **配置示例**
    - *[可选]* 修改 `lvgl_v8_port.h` 中的宏定义：
        - 将 `LVGL_PORT_AVOID_TEARING_MODE` 设为 `1` / `2` / `3`，为 `RGB` 接口开启防撕裂功能，再按需要设置 `LVGL_PORT_ROTATION_DEGREE` 旋转角度。
4. **编译并上传工程**
    - 点击 `√`（编译）按钮。
    - 将开发板连接到电脑。编译无误后点击 `→`（上传）按钮。

## 4. 相关文档与资源

| 文档 | 链接 |
| :--- | :--- |
| 产品规格书 | [UEDX48480040E-WB-A V3.2 SPEC.pdf](../../../assets/datasheet/UEDX48480040E-WB-A.pdf) |
| 原理图 | [SCH-UEDX48480040E-WB-A.png](../../../assets/schematic/SCH-UEDX48480040E-WB-A.png) |
| 显示屏规格书 | [UE040WV-RH40-A044C V1.3](https://gitee.com/VIEWESMART/UEDX48480040ESP32-4inch-Touch-Display/blob/main/information/UE040WV-RH40-A044C%20V1.3.pdf) |
| 触摸驱动手册 | [FT6336U V1.1](https://gitee.com/VIEWESMART/UEDX48480040ESP32-4inch-Touch-Display/blob/main/information/FT6336U-DataSheet-V1.1.pdf) |
| ESP32-S3-WROOM-1 数据手册（中文） | [esp32-s3-wroom-1_datasheet_cn.pdf](../../../assets/datasheet/chip/esp32-s3-wroom-1_wroom-1u_datasheet_cn.pdf) |
| ESP32-S3-WROOM-1 数据手册（英文） | [esp32-s3-wroom-1_datasheet_en.pdf](../../../assets/datasheet/chip/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf) |

## 5. 固件下载

1. 打开仓库的 `tools` 目录，找到 ESP32 烧录工具（`flash_download_tool_3.9.5`），解压并运行。
2. 芯片类型选择 `ESP32-S3` 与对应下载模式，点击 **OK**。按下图 1 → 2 → 3 → 4 → 5 的编号步骤烧录固件。若下载失败，请按住 **BOOT** 键重试。
3. 选择待烧录的 bin 文件。预编译固件（若已发布）放在仓库的 `firmware` 目录下，请查看其中的版本说明并选择合适版本。

若没有对应目标的预编译固件，请改为从源码编译烧录，参见 [3.2 快速入门](#32-getting-started)。

<p align="center" width="100%">
  <img src="../../../assets/images/Espressif/esp32-s3-firmware-download-1.png" alt="固件下载步骤 1">
  <img src="../../../assets/images/Espressif/esp32-s3-firmware-download-2.png" alt="固件下载步骤 2">
</p>

## 6. 常见问题

??? question "看完教程还是不知道怎么搭建编程环境，怎么办？"
    请参考[优奕视界常见问题](../../support/faq.md)中的环境搭建说明。

??? question "为什么一打开 Arduino IDE 就提示库文件需要更新？要不要更新？"
    请选择**不**更新库文件。不同版本的库文件之间可能不兼容，不建议更新。

??? question "为什么板上的 UART 排针没有串口输出？是板子坏了吗？"
    默认工程配置把 USB 接口用作 UART0 串口输出用于调试。UART 排针接的是同一组 UART0 引脚，未重新配置时不会有任何输出。

    - **PlatformIO 用户**：打开 `platformio.ini`，将 `build_flags` 下的 `-D ARDUINO_USB_CDC_ON_BOOT=true` 改为 `-D ARDUINO_USB_CDC_ON_BOOT=false`。
    - **Arduino 用户**：打开 `工具` 菜单，将 `USB CDC On Boot` 设为 `Disabled`。

??? question "为什么我的板子一直下载不成功？"
    请在开始下载时按住 `BOOT` 键，连接建立后再松开，然后重试。

??? question "这块板用的是哪颗显示驱动 IC 和触摸 IC？"
    480x480 面板由 `GC9503V` 驱动 IC 通过 3-wire SPI + RGB 总线驱动。电容触摸由 I2C 上的 `FT6336U` 处理，使用兼容 FT5x06 的驱动，其 I2C 地址为 `0x38`。

!!! info "没找到需要的内容？"
    如需更多产品、资料或技术支持，请联系我们的团队：

    [**:material-archive-arrow-down: 资源中心**](../../support/resource.md){ .md-button .md-button--primary }
    [**:material-magnify: 更多产品**](../esp32/index.md){ .md-button  }
    [**:material-email: 联系技术支持**](mailto:info@chinasunyee.com){ .md-button }
