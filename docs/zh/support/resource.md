---
title: 资源中心
description: 优奕视界技术资源中心，提供 ESP32 智能屏、旋钮屏、HDMI 显示屏的规格书、驱动芯片手册、Arduino 库、ESP-IDF 组件与开发工具下载。
hide:
  - toc
---

# :material-cloud-download: 资源中心

欢迎来到优奕视界技术资源中心。在这里可以下载所有产品的规格书、原理图、驱动与工具。

<div class="grid cards" markdown>

-   :material-file-document-multiple: **规格书**
    ---
    显示模组、驱动 IC 与 SoC 的 PDF 规格文档。
    [:arrow_down: 前往下载](#datasheets)

-   :material-package-variant-closed: **软件与 SDK**
    ---
    Arduino 库、ESP-IDF 组件与出厂固件。
    [:arrow_down: 前往下载](#software-sdk)

-   :material-tools: **工具与驱动**
    ---
    取模工具、USB-UART 驱动与烧录工具。
    [:arrow_down: 前往下载](#development-tools)

</div>

<br>

---

## :material-file-pdf-box: 规格书与 3D 模型 {: #datasheets }

使用表格右上角的**搜索框**按**型号 SKU** 查找（例如 `UE070` 或 `P4`）。

### 优奕视界产品

=== "📱 ESP32 智能屏"
    | 型号 SKU | 类型 | 分辨率 | 规格书 |
    | :--- | :--- | :--- | :--- |
    | [**UEP4S070H1024V600C**](../products/esp32-p4-wifi6-7inch-1024x600-touch-uart-display-hmi/index.md) | 7.0 英寸 ESP32-P4 智能屏 | 1024x600 | [:material-download: PDF](../../assets/datasheet/UEP4S070H1024V600C-WBA.pdf) |
    | [**UEDX80480070E-WB-A**](../products/esp32-s3-7inch-800x480-touch-uart-display-hmi/index.md) | 7.0 英寸 ESP32-S3 智能屏 | 800x480 | [:material-download: PDF](../../assets/datasheet/UEDX80480070E-WB-A.pdf) |
    | **UEDX80480050E-WB-A** | 5.0 英寸 ESP32-S3 智能屏 | 800x480 | [:material-download: PDF](../../assets/datasheet/UEDX80480050E-WB-A.pdf) |
    | **UEDX80480043E-WB-A** | 4.3 英寸 ESP32-S3 智能屏 | 800x480 | [:material-download: PDF](../../assets/datasheet/UEDX80480043E-WB-A.pdf) |
    | **UEDX48270043E-WB-A** | 4.3 英寸 ESP32-S3 智能屏 | 480x272 | [:material-download: PDF](../../assets/datasheet/UEDX48270043E-WB-A.pdf) |
    | **UEDX48480040E-WB-A** | 4.0 英寸 ESP32-S3 智能屏 | 480x480 | [:material-download: PDF](../../assets/datasheet/UEDX48480040E-WB-A.pdf) |
    | **UEDX32480035E-WB-A** | 3.5 英寸 ESP32-S3 智能屏 | 320x480 | [:material-download: PDF](../../assets/datasheet/UEDX32480035E-WB-A.pdf) |
    | **UEDX24320028E-WB-A** | 2.8 英寸 ESP32-S3 智能屏 | 240x320 | [:material-download: PDF](../../assets/datasheet/UEDX24320028E-WB-A.pdf) |
    | **UEDX24320024E-WB-A** | 2.4 英寸 ESP32-S3 智能屏 | 240x320 | [:material-download: PDF](../../assets/datasheet/UEDX24320024E-WB-A.pdf) |
    | **UEDX17320019E-WB-A** | 1.9 英寸 ESP32-S3 智能屏 | 170x320 | [:material-download: PDF](../../assets/datasheet/UEDX17320019E-WB-A.pdf) |

=== "🔘 ESP32 旋钮屏"
    | 型号 SKU | 类型 | 分辨率 | 规格书 |
    | :--- | :--- | :--- | :--- |
    | **UEDX48480021-MD80E** | 2.1 英寸 ESP32 触控旋钮屏 | 480x480 | [:material-download: PDF](../../assets/datasheet/UEDX48480021-MD80ET.pdf) |
    | **UEDX46460015-MD50E** | 1.5 英寸 ESP32 AMOLED 触控旋钮屏 | 466x466 | [:material-download: PDF](../../assets/datasheet/UEDX46460015-MD50ET.pdf) |
    | **UEDX24240013-MD50E** | 1.3 英寸 ESP32 旋钮屏 | 240x240 | [:material-download: PDF](../../assets/datasheet/UEDX24240013-MD50E.pdf) |

=== "📺 HDMI 显示屏"
    | 型号 SKU | 类型 | 分辨率 | 规格书 |
    | :--- | :--- | :--- | :--- |
    | **UEDX106000101-HMD** | 10.1 英寸 HDMI 显示屏 | 1024x600 | 请联系我们获取 |

!!! tip "关于 3D 模型"
    3D STEP 文件仍在最终确认中，暂不提供下载。如需 3D 模型或 CAD 图纸，请联系我们的工程团队。

### 🛠️ 关键器件

=== "🔌 SoC"
    | 型号 | 类别 | 厂商 | 资料 |
    | :--- | :--- | :--- | :--- |
    | **ESP32-C6** | SoC 规格书 | 乐鑫 | [:material-download: PDF](../../assets/datasheet/chip/esp32-c6-wroom-1_wroom-1u_datasheet_cn.pdf) |
    | **ESP32-P4** | SoC 规格书 | 乐鑫 | [:material-download: PDF](../../assets/datasheet/chip/esp32-p4_datasheet_cn.pdf) |
    | **ESP32-P4** | 技术参考手册 | 乐鑫 | [:material-download: PDF](../../assets/datasheet/chip/Esp32-p4_technical_reference_manual_cn.pdf) |

=== "📺 显示驱动 IC"
    | 型号 | 厂商 | 分辨率 | 手册 |
    | :--- | :--- | :--- | :--- |
    | **ST7789** | Sitronix | 240x320 | [:material-download: PDF](../../assets/datasheet/display/ST7789V3.pdf) |
    | **ST7701** | Sitronix | 480x800 | [:material-download: PDF](../../assets/datasheet/display/ST7701S.pdf) |
    | **ST7703** | Sitronix | 720x1280 | [:material-download: PDF](../../assets/datasheet/display/ST7703.pdf) |

=== "🖱️ 触摸 IC"
    | 型号 | 接口 | 厂商 | 手册 |
    | :--- | :--- | :--- | :--- |
    | **GT911** | I2C | Goodix | [:material-download: PDF](../../assets/datasheet/touch/GT911_CN_Datasheet.pdf) |
    | **FT6336** | I2C | FocalTech | [:material-download: PDF](../../assets/datasheet/touch/FT6336.pdf) |

<br>

---

## :material-package-variant-closed: 软件与 SDK {: #software-sdk }

建议通过 Git 仓库获取最新版本，下方同时提供离线下载包。

### 📦 Arduino 库
适用于 ESP32-S3 / C3 / P4 系列智能屏。

| 库名称 | 版本 | 说明 | 下载 |
| :--- | :--- | :--- | :--- |
| **Arduino_GFX** | v1.4.9 | 支持全部优奕视界显示屏的核心图形库（第三方）。 | [:material-link: LINK](https://github.com/moononournation/Arduino_GFX) |
| **ESP32_Display_Panel** | v0.1.0 | 乐鑫官方库，针对 P4 / S3 RGB 屏优化。 | [:material-link: LINK](https://github.com/esp-arduino-libs/ESP32_Display_Panel) |
| **VIEWE-S3-Demo** | v2.1 | 出厂固件源码（含 LVGL）。 | [:simple-gitee: Gitee](https://gitee.com/VIEWESMART) |

### 🛠️ ESP-IDF 组件
面向专业 C/C++ 开发。

* **esp_lcd_dsi**：ESP32-P4 的 MIPI DSI 驱动组件。
* **esp_lcd_touch_gt911**：GT911 的 I2C 触摸驱动。
    * [:material-link: 在乐鑫组件注册表查看](https://components.espressif.com/)

<br>

---

## :material-tools: 开发工具 {: #development-tools }

HMI 开发常用工具。

| 工具名称 | 平台 | 说明 | 下载 |
| :--- | :--- | :--- | :--- |
| **显示时序与配置生成器** | Web | 计算 RGB / MIPI-DSI 时序，并生成 RTOS、Linux、Android 配置模板。 | [:material-open-in-new: 打开工具](./display-timing-generator/) |
| **SquareLine Studio** | Win / Mac | LVGL 可视化 UI 编辑器（推荐）。 | [:material-link: 官网](https://squareline.io/) |
| **LVGL Pro** | Win / Mac | LVGL 官方 UI 编辑器（强烈推荐）。 | [:material-link: 官网](https://pro.lvgl.io/) |
| **Image Converter** | Win / Mac | LVGL 线上图片转 C 数组工具。 | [:material-link: 官网](https://lvgl.io/tools/imageconverter) |
| **Image2LCD** | Windows | 将图片转换为 C 数组的工具。 | [:material-download: ZIP](../../assets/software/Image2Lcd.zip) |
| **PCtoLCD2002** | Windows | 面向单片机的字模生成工具。 | [:material-download: ZIP](../../assets/software/PCtoLCD2002.zip) |
| **CH34x 驱动** | Win / Mac | 用于烧录固件的 USB-UART 驱动。 | [:material-download: RAR](../../assets/software/USB-SERIAL%20CH340.rar) |
| **Sscom 工具** | Windows | 经典轻量的串口调试助手。 | [:material-download: ZIP](../../assets/software/Sscom5.13.1.zip) |
| **Flash Download Tool** | Windows | 手动烧录固件的官方工具。 | [:material-download: ZIP](../../assets/software/flash_download_tool.zip) |

<br>

!!! info "没找到需要的内容？"
    如果你需要历史版本固件、特定 CAD 图纸或自定义驱动支持，请联系我们的工程团队：

    [联系技术支持](mailto:support@chinasunyee.com){ .md-button }
