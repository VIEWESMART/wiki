---
title: Resource Center
hide:
  - toc
---

# :material-cloud-download: Resource Center

Welcome to the VIEWE Technical Resource Hub. Here you can download datasheets, schematics, drivers, and 3D models for all our products.

<div class="grid cards" markdown>

-   :material-file-document-multiple: **Datasheets**
    ---
    PDF specifications for Display Modules, Driver ICs, and SoCs.
    [:arrow_down: Go to Section](#datasheets)

-   :material-github: **Software & SDK**
    ---
    Arduino Libraries, ESP-IDF Components, and Factory Firmware.
    [:arrow_down: Go to Section](#software-sdk)

-   :material-tools: **Tools & Drivers**
    ---
    Image Converters, USB-UART Drivers, and Flashing Tools.
    [:arrow_down: Go to Section](#development-tools)

</div>

<br>

---

## :material-file-pdf-box: Datasheets & 3D Models {: #datasheets }

Use the **Search Box** in the top right of the table to find your **Model SKU** (e.g., `UE070` or `P4`).

=== "📺 Display Modules"
    | Model SKU | Type | Resolution | Datasheet | 3D Step |
    | :--- | :--- | :--- | :--- | :--- |
    | **UEP4S070H1024V600C** | 7.0" P4 | 1024x600 | [:material-download: PDF](../../assets/datasheet/ESP32-P4-SmartDisplay_V1.1_SPEC.pdf) | [:material-cube: STEP](../assets/3d/7.0_p4.step) |
    | **UEDX80480070E-WB-A** | 7.0" S3 | 800x480 | [:material-download: PDF](../../assets/datasheet/UEDX80480070E-WB-A%20V2.0%20SPEC.pdf) | [:material-cube: STEP](../assets/3d/7.0_std.step) |
    | **UEDX80480050E-WB-A** | 5.0" S3 | 800x480 | [:material-download: PDF](../assets/ds/5.0_std.pdf) | [:material-cube: STEP](../assets/3d/5.0_std.step) |
    | **UEDX48480021-MD80E** | 2.1" Knob | 480x480 | [:material-download: PDF](../assets/ds/2.1_knob.pdf) | [:material-cube: STEP](../assets/3d/2.1_knob.step) |
    | **UEDX46460015-MD50E** | 1.5" AMOLED | 466x466 | [:material-download: PDF](../assets/ds/1.5_amoled.pdf) | [:material-cube: STEP](../assets/3d/1.5_amoled.step) |
    | **UEDX106000101-HMD** | 10.1" HDMI | 1024x600 | [:material-download: PDF](../assets/ds/10.1_hdmi.pdf) | [:material-cube: STEP](../assets/3d/10.1_hdmi.step) |

=== "🔌 Controller ICs"
    | Part Number | Function | Manufacturer | Datasheet |
    | :--- | :--- | :--- | :--- |
    | **ST7789V3** | LCD Controller | Sitronix | [:material-download: PDF](../assets/ds/ic/st7789v3.pdf) |
    | **GT911** | Touch Controller | Goodix | [:material-download: PDF](../../assets/datasheet/touch/GT911_EN_Datasheet.pdf) |
    | **ESP32-C6** | SoC | Espressif | [:material-link: Link](../../assets/datasheet/chip/esp32-c6-wroom-1_wroom-1u_datasheet_en.pdf) |
    | **ESP32-P4** | SoC | Espressif | [:material-link: Link](../../assets/datasheet/chip/esp32-p4_datasheet_en.pdf) |

<br>

---

## :material-github: Software & SDK {: #software-sdk }

We recommend using GitHub for the latest updates. Offline packages are also provided below.

### 📦 Arduino Libraries
For ESP32-S3 / C3 / P4 Smart Displays.

| Library Name | Version | Description | Download |
| :--- | :--- | :--- | :--- |
| **Arduino_GFX** | v1.4.9 | Core graphics library supporting all VIEWE displays. | [:material-download: ZIP](../assets/sw/Arduino_GFX.zip) |
| **ESP32_Display_Panel** | v0.1.0 | Official Espressif library optimized for P4/S3 RGB panels. | [:material-download: ZIP](../assets/sw/ESP32_Display_Panel.zip) |
| **VIEWE-S3-Demo** | v2.1 | Factory Firmware Source Code (LVGL included). | [:material-github: GitHub](https://github.com/VIEWESMART) |

### 🛠️ ESP-IDF Components
For professional C/C++ development.

* **esp_lcd_dsi**: MIPI DSI driver component for ESP32-P4.
* **esp_lcd_touch_gt911**: I2C Touch driver for GT911.
    * [:material-github: View on Espressif Registry](https://components.espressif.com/)

<br>

---

## :material-tools: Development Tools {: #development-tools }

Essential utilities for HMI development.

| Tool Name | Platform | Description | Download |
| :--- | :--- | :--- | :--- |
| **SquareLine Studio** | Win / Mac | Visual UI Editor for LVGL (Highly Recommended). | [:material-link: Website](https://squareline.io/) |
| **Image2LCD** | Windows | Tool to convert images into C arrays (RGB565). | [:material-download: ZIP](../assets/tools/Image2LCD.zip) |
| **PCtoLCD2002** | Windows | Font generation tool for microcontrollers. | [:material-download: ZIP](../assets/tools/PCtoLCD.zip) |
| **CH34x Driver** | Win / Mac | USB-UART Driver for flashing firmware. | [:material-download: ZIP](../assets/tools/CH34x_Install.zip) |

<br>

!!! info "Can't find what you need?"
    If you require legacy firmware, specific CAD drawings, or custom driver support, please contact our engineering team:
    
    [Contact Support](mailto:support@viewedisplay.com){ .md-button }