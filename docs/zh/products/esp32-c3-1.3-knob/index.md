---
title: 优奕视界 1.3 英寸 240x240 ESP32-C3 旋钮屏
description: UEDX24240013-MD50E 是一款 1.3 英寸 240x240 的 ESP32-C3 旋钮显示屏，采用 GC9A01 SPI 面板与旋转编码器输入（不带触摸），支持 Wi-Fi 与蓝牙 5 (LE)，并提供 Arduino / ESP-IDF / PlatformIO 框架支持。
---

# 1.3 英寸 240x240 ESP32-C3 旋钮屏

<div class="grid cards" markdown>

-   **UEDX24240013-MD50E**
    ---
    基于 **ESP32-C3** 的旋钮式智能屏。集成 1.3 英寸 **240x240** 圆形 TFT 显示屏与高精度旋转编码器，内置 Wi-Fi 与蓝牙，原生支持 Arduino 与 LVGL，可快速构建流畅的多模态交互界面。适用于智能温控器、工业控制面板、高端家电与 AIoT 应用。

    [:material-arrow-left: 返回系列列表](../esp32/){ .md-button }
    [:material-cart: 官方旗舰店](https://shop277726935.taobao.com/){ .md-button .md-button--primary }
    [:simple-gitee: Gitee 仓库](https://gitee.com/VIEWESMART/UEDX24240013-MD50ESP32_1.3inch-Knob){ .md-button }

</div>

<div align="center">
    <img src="../../../assets/images/UEDX24240013-MD50E/1.3-inch tft Knob Display.png" alt="1.3 英寸旋钮屏" style="max-width: 90%; height: auto;">
</div>

---

## 1. 产品简介

**UEDX24240013-MD50E** 是一款面向旋钮式 HMI 应用的紧凑型智能显示模组，将 1.3 英寸 IPS 显示屏（240x240 像素）与旋转编码器、硬件按键集成在一起。它由 **ESP32-C3**（4 MB Flash）驱动，提供 Wi-Fi 与蓝牙 5 (LE) 连接能力，并支持 **Arduino**、**ESP-IDF** 与 **PlatformIO** 开发。

### 1.1 产品特性

#### 处理器与无线

- **处理器**：ESP32-C3，片内 4 MB Flash。
- **无线**：内置 2.4 GHz Wi-Fi 与蓝牙 5 (LE)。

#### 显示屏

| 参数 | 规格 |
| :--- | :--- |
| 尺寸 | 1.3 英寸 |
| 分辨率 | 240 x 240 |
| 面板类型 | IPS |
| 接口 | 4-Wire SPI |
| 驱动 IC | GC9A01 |
| 兼容库 | ESP32_Display_Panel |

#### 触摸

- **触摸**：无触摸。该型号采用旋钮交互，不带触摸屏。

#### 外设

- **旋钮输入**：旋转编码器（PHA / PHB 两相），提供精确的旋钮手感。
- **按键**：硬件按键，与 BOOT 共用。
- **连接**：USB（USB-DP / USB-DN）与 UART0，用于固件下载与串口调试。
- **扩展**：FPC 接口，引出 5 V、GND、UART0 与 USB 信号。

### 1.2 应用场景

- 智能温控器
- 工业控制面板
- 高端家电
- AIoT 应用

## 2. 硬件说明

### 2.1 模块概览

UEDX24240013-MD50E 将主控、显示屏与旋钮交互集成在一块紧凑的 PCB 上，主要功能区块如下：

| 元件 | 说明 |
| :--- | :--- |
| ESP32-C3 | 主控 MCU，片内 4 MB Flash。 |
| 1.3 英寸 IPS 屏 | 240x240 分辨率，GC9A01 驱动，4-Wire SPI 接口。 |
| 旋钮编码器 | 两相（PHA / PHB）旋转编码器，用于旋钮输入。 |
| 按键 | 硬件按键，与 BOOT（IO9）共用。 |
| USB / UART | USB-DP / USB-DN 与 UART0，用于固件下载与调试。 |
| FPC 接口 | 引出 5 V、GND、UART0 与 USB 信号。 |

### 2.2 GPIO 定义（引脚图） { #22-gpio-definition-pinout }

#### 显示屏（4-Wire SPI）

| 屏幕引脚 | ESP32-C3 引脚 |
| :--- | :--- |
| SPI-CS | IO10 |
| SPI-SCK | IO1 |
| SPI-SDA | IO0 |
| SPI-DC | IO4 |
| LCD-TE | IO5 |
| BACKLIGHT | IO8 |

#### 按键

| 按键引脚 | ESP32-C3 引脚 |
| :--- | :--- |
| BOOT | IO9 |

#### 旋钮编码器

| 编码器引脚 | ESP32-C3 引脚 |
| :--- | :--- |
| PHA | IO7 |
| PHB | IO6 |

#### USB

| USB 引脚 | ESP32-C3 引脚 |
| :--- | :--- |
| USB-DN | IO18 |
| USB-DP | IO19 |

#### UART

| UART 引脚 | ESP32-C3 引脚 |
| :--- | :--- |
| UART0 RXD | IO20 |
| UART0 TXD | IO21 |

#### FPC 接口定义

| FPC 编号 | 适配引脚 | ESP32-C3 引脚 |
| :--- | :--- | :--- |
| 1 | 5V | 5V |
| 2 | PB7 | GPIO3 |
| 3 | GND | GND |
| 4 | RX2 | NC |
| 5 | TX2 | NC |
| 6 | RX1 | UART0 RXD / IO20 |
| 7 | TX1 | UART0 TXD / IO21 |
| 8 | NC | CHIP-EN |
| 9 | SK & D+ | USB-DP / IO19 |
| 10 | SD & D- | USB-DN / IO18 |

## 3. 软件开发

仓库提供可直接运行的示例，包含已移植好的 LVGL 工程。

### 3.1 软件示例

所有示例代码均可在 [Gitee 仓库](https://gitee.com/VIEWESMART/UEDX24240013-MD50ESP32_1.3inch-Knob/tree/main/examples) 中找到。

| 开发环境 | 版本 |
| :--- | :--- |
| ESP-IDF | v5.1 / 5.2 / 5.3 |
| Arduino IDE | esp32 核心包 v3.1.0 及以上 |
| PlatformIO IDE | — |

### 3.2 快速入门 { #32-getting-started }

#### 3.2.1 准备工作

- **硬件**：UEDX24240013-MD50E 开发板、USB 数据线。
- **软件**：VS Code（ESP-IDF v5.1 / 5.2 / 5.3）或 Arduino IDE（esp32 核心包 v3.1.0 及以上）。
- **库文件**：Arduino IDE 需要安装以下库：

| 库文件 | 版本 | 说明 |
| :--- | :--- | :--- |
| ESP32_Display_Panel | 1.0.3+ | Espressif 出品。驱动屏幕所必需。 |
| ESP32_Button | 推荐最新版本 | 按键驱动库。 |
| ESP32_Knob | 推荐最新版本 | 旋钮编码器驱动库。 |
| lvgl | 8.4.0 | 免费开源的嵌入式图形库（暂不支持 v9）。 |

#### 3.2.2 ESP-IDF 环境配置

- **支持版本**：v5.1 / v5.2 / v5.3。
- 到 [Gitee 仓库](https://gitee.com/VIEWESMART/UEDX24240013-MD50ESP32_1.3inch-Knob/tree/main/examples) 下载示例代码，直接编译运行即可。

#### 3.2.3 Arduino 环境配置

1. **安装 [Arduino IDE](https://www.arduino.cc/en/software)**
   按系统类型选择安装包。新手可先参考[优奕视界常见问题](../../support/faq.md)中的环境搭建说明。
2. **安装 ESP32 开发板包**
    - 打开 Arduino IDE。
    - 进入 `文件` > `首选项`。
    - 在 `附加开发板管理器网址` 中添加：
      ```text
      https://espressif.github.io/arduino-esp32/package_esp32_index.json
      ```
    - 进入 `工具` > `开发板` > `开发板管理器`。
    - 搜索 Espressif Systems 的 `esp32`。
    - 选择 `3.1.0` 及以上版本，点击 `安装`。
3. **安装库文件**
    - **在线安装**：
        - 进入 `项目` > `加载库` > `管理库`。
        - 搜索 `ESP32_Display_Panel`，选择 `1.0.3` 及以上版本，点击 `安装`。
        - 弹出依赖提示时点击「全部安装」。
        - *[可选]* 安装 `LVGL` 库，推荐版本 `8.4.0`。
    - **手动安装**：
        - 从 [Arduino Library](https://www.arduinolibraries.info/libraries/esp32_display_panel) 下载所需版本的 `.zip` 文件。
        - 进入 `项目` > `加载库` > `添加 .ZIP 库...`，选择下载的 `.zip` 文件并点击「打开」。
4. **选择并配置开发板**
   进入 `工具` > `开发板` > `esp32` > `ESP32C3 Dev Module`。
5. **打开示例**
   进入 `文件` > `示例` > `ESP32_Display_Panel` > `Arduino` > `gui` > `lvgl_v8` > `simple_port`。
6. **修改代码**
   在 `esp_panel_board_supported_conf.h` 中修改宏定义以启用目标开发板：先将文件级宏 `ESP_PANEL_BOARD_DEFAULT_USE_SUPPORTED` 由 `0` 改为 `1`，再取消 `#define BOARD_VIEWE_UEDX24240013_MD50E` 的注释（注意开发板宏使用下划线，而非连字符）。修改后的文件示例如下：

   ```c
   /**
    * @brief Flag to enable supported board configuration (0/1)
    *
    * Set to `1` to enable supported board configuration, `0` to disable
    */
   #define ESP_PANEL_BOARD_DEFAULT_USE_SUPPORTED       (1)

   // #define BOARD_VIEWE_SMARTRING
   #define BOARD_VIEWE_UEDX24240013_MD50E
   // #define BOARD_VIEWE_UEDX24320024E_WB_A
   // #define BOARD_VIEWE_UEDX24320028E_WB_A
   // #define BOARD_VIEWE_UEDX24320035E_WB_A
   // #define BOARD_VIEWE_UEDX32480035E_WB_A
   // #define BOARD_VIEWE_UEDX46460015_MD50ET
   // #define BOARD_VIEWE_UEDX48270043E_WB_A
   // #define BOARD_VIEWE_UEDX48480021_MD80E_V2
   // #define BOARD_VIEWE_UEDX48480021_MD80E
   // #define BOARD_VIEWE_UEDX48480021_MD80ET
   // #define BOARD_VIEWE_UEDX48480028_MD80ET
   // #define BOARD_VIEWE_UEDX48480040E_WB_A
   // #define BOARD_VIEWE_UEDX80480043E_WB_A
   // #define BOARD_VIEWE_UEDX80480050E_AC_A
   // #define BOARD_VIEWE_UEDX80480050E_WB_A
   // #define BOARD_VIEWE_UEDX80480050E_WB_A_2
   // #define BOARD_VIEWE_UEDX80480070E_WB_A
   ```
7. **配置工具选项（ESP32-C3）**

| 设置项 | 取值 |
| :--- | :--- |
| Board | ESP32C3 Dev Module |
| CPU Frequency | 160MHz (WiFi) |
| Core Debug Level | None |
| USB CDC On Boot | Disabled |
| Erase All Flash Before Sketch Upload | Disabled |
| Flash Frequency | 80MHz |
| Flash Mode | QIO |
| Flash Size | 4MB (32Mb) |
| JTAG Adapter | Disabled |
| Partition Scheme | Custom |
| Upload Speed | 921600 |

8. **编译与上传**
    1. 选择正确的端口。
    2. 点击右上角 **「√」** 编译。
    3. 编译无误后，将开发板连接到电脑。
    4. 点击右上角 **「→」** 下载。

!!! warning "配置提示"
    不要同时启用 `ESP_PANEL_BOARD_DEFAULT_USE_SUPPORTED` 与 `ESP_PANEL_BOARD_DEFAULT_USE_CUSTOM`，也不能同时启用多个开发板定义。

!!! note "LVGL 颜色交换设置"
    `SPI` 与 `QSPI` 屏幕需要在 `lv_conf.h` 中将宏 `LV_COLOR_16_SWAP` 设为 `1`，`RGB` 屏幕则应设为 `0`。

    ```c
    /*Color depth: 1 (1 byte per pixel), 8 (RGB332), 16 (RGB565), 32 (ARGB8888)*/
    #define LV_COLOR_DEPTH 16

    /*Swap the 2 bytes of RGB565 color. Useful if the display has an 8-bit interface (e.g. SPI)*/
    #define LV_COLOR_16_SWAP 1
    ```

## 4. 相关文档与资源

| 文档 | 链接 |
| :--- | :--- |
| 产品规格书 | [UEDX24240013-MD50E.pdf](../../../assets/datasheet/UEDX24240013-MD50E.pdf) |
| 2D 图纸 (DWG) | [UEDX24240013-MD50E-2D.dwg](../../../assets/dimension/UEDX24240013-MD50E-2D.dwg) |
| 原理图 | [SCH-UEDX24240013-MD50E.pdf](../../../assets/schematic/SCH-UEDX24240013-MD50E.pdf) |
| ESP32-C3 数据手册（英文） | [esp32-c3_datasheet_en.pdf](../../../assets/datasheet/chip/esp32-c3_datasheet_en.pdf) |
| ESP32-C3 数据手册（中文） | [esp32-c3_datasheet_cn.pdf](../../../assets/datasheet/chip/esp32-c3_datasheet_cn.pdf) |

**工具**

| 工具 | 说明 |
| :--- | :--- |
| [Flash Download Tool](../../../assets/software/flash_download_tool.zip) | 手动烧录固件工具。 |
| [LVGL Image Converter](https://lvgl.io/tools/imageconverter) | 将图片转换为 LVGL 的 C 数组。 |

更多资源请访问[**资源中心**](../../support/resource.md)。

## 5. 固件下载

| 固件 | 说明 |
| :--- | :--- |
| ESP-IDF | 原始版本 |

1. 打开工程的 `tools` 目录，找到 ESP32 烧录工具并运行。
2. 选择正确的烧录芯片与烧录方式，点击 **OK**。
3. 按 1 → 2 → 3 → 4 → 5 的编号步骤烧录程序。
4. 若烧录失败，请按住 **BOOT** 按键后重试。

烧录文件位于工程根目录的 `firmware` 目录下，请参考其中的固件版本说明选择合适的版本。

## 6. 常见问题

??? question "看完上述教程还是不知道怎么搭建编程环境，怎么办？"
    请参考[优奕视界常见问题](../../support/faq.md)中的环境搭建说明。

??? question "为什么一打开 Arduino IDE 就提示库文件需要更新？要不要更新？"
    请选择**不**更新库文件。不同版本的库文件之间可能不兼容，不建议更新。

??? question "为什么板上的 UART 接口没有串口数据输出？是板子坏了吗？"
    默认工程配置把 USB 接口用作 UART0 串口输出用于调试。板上 UART 接口接的是同一组 UART0 引脚，未重新配置时不会有任何数据输出。

    - **PlatformIO 用户**：打开 `platformio.ini`，将 `build_flags` 下的 `-D ARDUINO_USB_CDC_ON_BOOT=true` 改为 `-D ARDUINO_USB_CDC_ON_BOOT=false`。
    - **Arduino 用户**：打开 `工具` 菜单，将 `USB CDC On Boot` 设为 `Disabled`。

??? question "为什么我的板子一直下载不成功？"
    请按住 **BOOT** 按键后重新下载程序。

!!! info "没找到需要的内容？"
    如需更多产品、资料或技术支持，请联系我们的团队：

    [**:material-archive-arrow-down: 资源中心**](../../support/resource.md){ .md-button .md-button--primary }
    [**:material-magnify: 更多产品**](../esp32/index.md){ .md-button  }
    [**:material-email: 联系技术支持**](mailto:info@chinasunyee.com){ .md-button }
