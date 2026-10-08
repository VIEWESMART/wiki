---
title: 优奕视界 2.1 英寸 480x480 ESP32-S3 触控旋钮智能屏
description: UEDX48480021-MD80ET 是一款 2.1 英寸 480x480 的 ESP32-S3 旋钮式智能触控显示模组，采用 ST7701S 3-Wire SPI-RGB 面板与 CST826 电容触摸，集成旋转编码器与硬件按键，支持 Wi-Fi 与蓝牙 5，并提供 Arduino / ESP-IDF / PlatformIO 完整支持。
---

# 2.1 英寸 480x480 ESP32-S3 触控旋钮智能屏

<div class="grid cards" markdown>

-   **UEDX48480021-MD80ET**
    ---
    由 **ESP32-S3** 驱动的旋钮式智能屏。将 480x480 圆形 TFT 触摸屏与高精度触感旋转编码器集成于一体，原生支持 Arduino 与 LVGL，可快速构建流畅的多模态交互界面，适合智能温控器、工业仪表盘、高端家电与 AIoT 应用。

    [:material-arrow-left: 返回系列列表](../esp32/){ .md-button }
    [:material-cart: 官方旗舰店](https://shop277726935.taobao.com/){ .md-button .md-button--primary }
    [:simple-gitee: Gitee 仓库](https://gitee.com/VIEWESMART/UEDX48480021-MD80ESP32-2.1inch-Touch-Knob-Display){ .md-button }

</div>

<div align="center">
  <img src="../../../assets/images/UEDX48480021-MD80ET/2.1 Touch Knob Display.jpg" width="100%" alt="2.1 英寸 480x480 ESP32-S3 触控旋钮智能屏">
</div>

---

## 1. 产品简介

**UEDX48480021-MD80ET** 是一款面向旋钮式 HMI 应用的紧凑型智能显示模组。它将 2.1 英寸 IPS 显示屏（480x480 像素）、电容触摸面板、旋转编码器与一个硬件按键集成于一体。模组以 **ESP32-S3-R8**（16 MB Flash、8 MB Octal PSRAM）为核心，提供 Wi-Fi 与蓝牙 5 (LE) 连接能力，并支持 **Arduino**、**ESP-IDF** 与 **PlatformIO** 三套框架开发。

### 1.1 产品特性

#### 处理器与无线

- **芯片**：ESP32-S3-R8，Xtensa® 双核 32 位 LX7，主频最高 240 MHz。
- **无线**：2.4 GHz Wi-Fi (802.11 b/g/n)、蓝牙 5 (LE) 及 BLE Mesh。
- **数据手册**：[Espressif ESP32-S3 数据手册](https://www.espressif.com.cn/sites/default/files/documentation/esp32-s3_datasheet_en.pdf)

#### 存储

- **PSRAM**：8 MB（Octal SPI）
- **Flash**：16 MB

#### 显示屏

| 参数 | 规格 |
| :--- | :--- |
| 尺寸 | 2.1 英寸 |
| 分辨率 | 480 x 480 |
| 面板类型 | IPS |
| 驱动 IC | ST7701S |
| 接口 | 3-Wire SPI + RGB（24-bit） |
| 兼容库 | ESP32_Display_Panel |

#### 触摸

| 参数 | 规格 |
| :--- | :--- |
| 触摸 IC | CST826 |
| 接口 | I2C (IIC) |

#### 外设

- **旋钮**：高精度触感旋转编码器（PHA / PHB 双相输出）。
- **按键**：BOOT（进入下载模式）与 RESET（系统复位）。
- **连接**：USB 口，用于 5 V 供电、固件下载与 UART 调试。

### 1.2 应用场景

- 智能温控器
- 工业 HMI 仪表盘
- 高端家电面板
- AIoT 多模态交互界面

## 2. 硬件说明

### 2.1 模块概览

模组将显示屏、电容触摸、旋转编码器与按键集成于一块圆形面板之上，外观如下图所示：

<p align="left">
  <img src="../../../assets/images/UEDX48480021-MD80ET/2.1 Touch Knob Display.jpg" alt="2.1 英寸 480x480 ESP32-S3 触控旋钮智能屏模块概览" width="80%">
</p>

| 项目 | 规格 |
| :--- | :--- |
| 主控 | ESP32-S3-R8（16 MB Flash / 8 MB PSRAM） |
| 显示驱动 IC | ST7701S |
| 显示接口 | 3-Wire SPI + RGB（24-bit） |
| 触摸 IC | CST826（I2C） |
| 旋转编码器 | PHA / PHB 双相输出 |
| 按键 | BOOT（IO0）、RESET（CHIP_EN） |

### 2.2 GPIO 定义（引脚图） { #22-gpio-definition-pinout }

#### 显示屏（3-Wire SPI + RGB）

面板先通过 3-wire SPI 总线完成初始化，随后由并行 RGB 总线送入像素数据。

| 屏幕引脚 | ESP32-S3 引脚 |
| :--- | :--- |
| DE | IO17 |
| VSYNC | IO3 |
| HSYNC | IO46 |
| PCLK | IO9 |
| DATA0 - DATA15 | IO10 - IO48 |
| SPI_CS | IO18 |
| SPI_SCK | IO13 |
| SPI_SDA | IO12 |
| RST | IO8 |
| BACKLIGHT | IO7 |

**RGB 数据引脚映射**

| 数据位 | 引脚 | 数据位 | 引脚 |
| :---: | :---: | :---: | :---: |
| D0 | IO10 | D8 | IO45 |
| D1 | IO11 | D9 | IO38 |
| D2 | IO12 | D10 | IO39 |
| D3 | IO13 | D11 | IO40 |
| D4 | IO14 | D12 | IO41 |
| D5 | IO21 | D13 | IO42 |
| D6 | IO47 | D14 | IO2 |
| D7 | IO48 | D15 | IO1 |

#### 触摸（CST826）

| 信号 | ESP32-S3 引脚 |
| :--- | :--- |
| SCL | IO15 |
| SDA | IO16 |

#### 按键

| 信号 | ESP32-S3 引脚 |
| :--- | :--- |
| BOOT | IO0 |
| RESET | CHIP_EN |

#### 旋转编码器

| 信号 | ESP32-S3 引脚 |
| :--- | :--- |
| PHA | IO6 |
| PHB | IO5 |

#### USB / UART

| 信号 | ESP32-S3 引脚 |
| :--- | :--- |
| USB-DN | IO19 |
| USB-DP | IO20 |
| UART TX | IO43 (U0TXD) |
| UART RX | IO44 (U0RXD) |

## 3. 软件开发

仓库提供 ESP-IDF 与 Arduino 两套可直接运行的示例，包含显示驱动与 SquareLine 界面移植工程。

### 3.1 软件示例

| 示例 | 支持的 IDE 与版本 | 说明 |
| :--- | :--- | :--- |
| [ESP-IDF](https://gitee.com/VIEWESMART/UEDX48480021-MD80ESP32-2.1inch-Touch-Knob-Display/tree/main/examples/ESP-IDF) | ESP-IDF V5.1 / 5.2 / 5.3 | ESP-IDF 驱动示例代码。 |
| [SquareLinePorting](https://gitee.com/VIEWESMART/UEDX48480021-MD80ESP32-2.1inch-Touch-Knob-Display/tree/main/examples/SquareLinePorting) | Arduino IDE (esp32_v2.0.14) | 面向 Arduino 的 SquareLine 界面移植示例。 |

**支持的框架与版本：**

| 支持的 IDE | 版本 |
| :--- | :--- |
| ESP-IDF | V5.1 / 5.2 / 5.3 |
| Arduino IDE | esp32 >= v3.0.7 |
| PlatformIO IDE | — |

### 3.2 快速入门 { #32-getting-started }

#### 3.2.1 准备工作

- **硬件**：UEDX48480021-MD80ET 开发板、USB 数据线。
- **软件**：VS Code（ESP-IDF v5.1+）、Arduino IDE，或 VS Code（PlatformIO）。
- **库文件**（Arduino IDE 与 PlatformIO）：

| 库文件 | 版本 | 说明 |
| :--- | :--- | :--- |
| ESP32_Display_Panel | 1.0.3+ | Espressif 出品。驱动面板与读取触摸 IC 所必需。 |
| lvgl | 8.4.0 | 免费开源的嵌入式图形库，仅 GUI 示例需要。 |

#### 3.2.2 ESP-IDF 环境配置

- **支持版本**：v5.1 / v5.2 / v5.3。
- **操作说明**：从仓库下载示例代码后直接编译运行。
- **示例目录**：[examples/esp_idf](https://gitee.com/VIEWESMART/UEDX48480021-MD80ESP32-2.1inch-Touch-Knob-Display/tree/main/examples/esp_idf)。

#### 3.2.3 Arduino 环境配置

!!! tip "新手教程"
    详细操作请参考[优奕视界常见问题](../../support/faq.md)中的环境搭建说明。

1. **安装 Arduino IDE**
   从 [Arduino 官网](https://www.arduino.cc/en/software) 按系统类型下载安装包。
2. **安装 ESP32 SDK**
    1. 打开 Arduino IDE → `文件` > `首选项`。
    2. 在 **附加开发板管理器网址** 中添加：
       ```text
       https://espressif.github.io/arduino-esp32/package_esp32_index.json
       ```
    3. 进入 `工具` > `开发板` > `开发板管理器`，搜索 Espressif Systems 的 `esp32`。
    4. 选择版本 **3.1.0** 或更高，点击 **INSTALL**。
3. **安装所需库文件**
    - **ESP32_Display_Panel**：进入 `项目` > `加载库` > `管理库...`，搜索 `ESP32_Display_Panel`，选择版本 **1.0.3+**，弹出依赖提示时点击「全部安装」。
    - **LVGL（可选）**：推荐版本 **8.4.0**，仅 GUI 示例需要。

    !!! note "手动安装"
        也可从 [Arduino Library](https://www.arduinolibraries.info/libraries/esp32_display_panel) 下载 `.zip` 文件，然后通过 `项目` > `加载库` > `添加 .ZIP 库...` 安装。

4. **配置开发板设置**
   进入 `工具` > `开发板` > `esp32` > `ESP32S3 Dev Module`。

   **工具选项：**

   | 设置 | 值 |
   | :--- | :--- |
   | 开发板 | ESP32S3 Dev Module |
   | Core Debug Level | None |
   | USB CDC On Boot | Disabled |
   | USB DFU On Boot | Disabled |
   | Flash Size | 16MB (128Mb) |
   | Partition Scheme | 16M Flash (3MB APP/9.9MB FATFS) |
   | PSRAM | OPI PSRAM |

5. **修改代码配置**
   打开示例：`文件` > `示例` > `ESP32_Display_Panel` > `Arduino` > `gui` > `lvgl_v8` > `simple_port`。

   修改 `esp_panel_board_supported_conf.h` 中的宏定义：

   ```text
   // 启用支持的板级配置
   #define ESP_PANEL_BOARD_DEFAULT_USE_SUPPORTED       (1)

   // 仅取消目标板宏定义的注释
   #define BOARD_VIEWE_UEDX48480021_MD80ET
   ```

   !!! warning "重要提示"
       不要同时启用 `ESP_PANEL_BOARD_DEFAULT_USE_SUPPORTED` 与 `ESP_PANEL_BOARD_DEFAULT_USE_CUSTOM`，也不能同时启用多个板级配置。

   !!! note "LVGL 颜色交换设置"
       - **SPI / QSPI 屏**：在 `lv_conf.h` 中将 `LV_COLOR_16_SWAP` 设为 `1`。
       - **RGB 屏**：在 `lv_conf.h` 中将 `LV_COLOR_16_SWAP` 设为 `0`。

6. **编译与上传**
    1. 选择正确的端口。
    2. 点击 **√** 编译。
    3. 连接开发板后点击 **→** 上传。

#### 3.2.4 PlatformIO 环境配置

1. 安装 [Visual Studio Code](https://code.visualstudio.com/Download)。
2. 安装 **PlatformIO IDE** 扩展。
3. 从 Gitee 仓库下载本工程（「克隆 / 下载」> 下载 ZIP）。
4. 在 VS Code 资源管理器（`Ctrl+Shift+E`）中点击 **打开文件夹**，选择下载好的工程目录。
5. 打开 `platformio.ini`，在 `[platformio]` 段中取消注释所需的示例（`default_envs = xxx`）。
6. 点击左下角 **√**（编译），再点击 **→**（上传）。

## 4. 相关文档与资源

| 文档 | 链接 |
| :--- | :--- |
| 产品规格书 | [UEDX48480021-MD80ET.pdf](../../../assets/datasheet/UEDX48480021-MD80ET.pdf) |
| 原理图 | [SCH-UEDX48480021-MD80ET.png](../../../assets/schematic/SCH-UEDX48480021-MD80ET.png) |
| ESP32-S3-WROOM-1 数据手册（英文） | [esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf](../../../assets/datasheet/chip/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf) |
| ESP32-S3-WROOM-1 数据手册（中文） | [esp32-s3-wroom-1_wroom-1u_datasheet_cn.pdf](../../../assets/datasheet/chip/esp32-s3-wroom-1_wroom-1u_datasheet_cn.pdf) |
| 烧录工具 | [flash_download_tool.zip](../../../assets/software/flash_download_tool.zip) |
| LVGL 图片转换工具 | [lvgl.io/tools/imageconverter](https://lvgl.io/tools/imageconverter) |

## 5. 固件下载

1. 打开工程 `tools` 目录下的烧录工具。
2. 选择正确的烧录芯片与烧录方式。
3. 按下图 **1 → 2 → 3 → 4 → 5** 的编号步骤，烧录 [`firmware`](https://gitee.com/VIEWESMART/UEDX48480021-MD80ESP32-2.1inch-Touch-Knob-Display/tree/main/firmware) 目录下的固件。
4. 若烧录失败，请按住 **BOOT-0** 键后重试。

<p align="center" width="100%">
  <img src="../../../assets/images/Espressif/esp32-s3-firmware-download-1.png" alt="固件下载步骤 1">
  <img src="../../../assets/images/Espressif/esp32-s3-firmware-download-2.png" alt="固件下载步骤 2">
</p>

## 6. 常见问题

??? question "看完教程还是不知道怎么搭建编程环境，怎么办？"
    请参考[优奕视界常见问题](../../support/faq.md)中的环境搭建说明。

??? question "为什么一打开 Arduino IDE 就提示库文件需要更新？要不要更新？"
    请选择**不**更新。不同版本的库文件之间可能不兼容，请坚持使用推荐版本。

??? question "为什么板上的「UART」排针没有串口输出？"
    默认配置把 USB 用作 UART0 用于调试。若要启用外部 UART 接口：

    - **PlatformIO**：打开 `platformio.ini`，将 `-D ARDUINO_USB_CDC_ON_BOOT=true` 改为 `-D ARDUINO_USB_CDC_ON_BOOT=false`。
    - **Arduino IDE**：进入 `工具` > `USB CDC On Boot` > 选择 **Disabled**。

??? question "为什么我的板子一直下载不成功？"
    请在点击上传 / 下载时按住 **BOOT** 键，连接建立后再松开，然后重试。

!!! info "没找到需要的内容？"
    如需更多产品、资料或技术支持，请联系我们的团队：

    [**:material-archive-arrow-down: 资源中心**](../../support/resource.md){ .md-button .md-button--primary }
    [**:material-magnify: 更多产品**](../esp32/index.md){ .md-button  }
    [**:material-email: 联系技术支持**](mailto:support@viewedisplay.com){ .md-button }
