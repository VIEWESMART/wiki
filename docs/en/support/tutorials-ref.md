---
title: FAQ & Troubleshooting
hide:
  - toc
---

# :material-frequently-asked-questions: FAQ & Troubleshooting

Find quick answers to common questions about Hardware, Software, and Ordering.

!!! tip "Quick Search"
    Use the **Search Bar (Ctrl+F)** at the top to find specific errors, or check our [GitHub Issues](https://github.com/VIEWESMART/VIEWE-FAQ/issues).

---

## 🚀 Quick Navigation

<div class="grid cards" borderless markdown>

-   :material-code-braces: __Software Development__
    ---
    Framework guides for Arduino, ESP-IDF, and PlatformIO.
    [:octicons-arrow-right-24: View Guides](#software-development)

-   :material-chip: __Hardware & Wiring__
    ---
    Display types, pinouts, power requirements, and touch.
    [:octicons-arrow-right-24: View Details](#hardware-wiring)

-   :material-cart-check: __Orders & Customization__
    ---
    Bulk ordering, custom PCB/Screen, and warranty.
    [:octicons-arrow-right-24: View Policy](#orders-customization)

</div>

---

## 💻 Software Development {: #software-development}

Choose your preferred development framework. Each section below leads to a comprehensive setup and optimization guide.

### 📦 Development Frameworks

<div class="grid cards" markdown>

-   :simple-arduino: __Arduino__
    ---
    Perfect for rapid prototyping.
    - `ESP32_Display_Panel` library
    - **Bounce Buffer** optimization
    - Simple LVGL porting
    [:octicons-link-external-16: **Arduino Guide**](../software/arduino/index.md)

-   :simple-espressif: __ESP-IDF__
    ---
    Professional native environment.
    - High-performance SDK integration
    - Advanced multi-core tasking
    - Precision RGB control
    [:octicons-link-external-16: **ESP-IDF Guide**](../software/esp-idf/index.md)

-   :simple-platformio: __PlatformIO__
    ---
    Modern IDE for team collaboration.
    - Automated dependency management
    - Custom board JSON configs
    - VS Code integration
    [:octicons-link-external-16: **PlatformIO Guide**](../software/platformio/index.md)

</div>

### ❓ Framework FAQs

??? question "Which library should I use: LVGL or Arduino_GFX?"
    * **Arduino_GFX**: Best for simple drawing (circles, lines, text) and raw driver performance.
    * **LVGL**: The industry standard for complex UIs (Buttons, Charts, Animations). We recommend **LVGL** for professional products.

??? question "Do you support MicroPython or CircuitPython?"
    Yes, our hardware is fully compatible. While our official tutorials focus on **C++**, the community provides drivers for ST7701/ST7789 screens.

---

## 🔥 Top 5 Critical Issues

These are the most common issues reported by users. Click to expand solutions.

??? bug "1. The screen is black but the backlight is on."
    1.  **Check PSRAM**: For RGB screens, PSRAM must be enabled (`Tools` -> `PSRAM` -> `OPI PSRAM`).
    2.  **Check Library**: Use [Arduino_GFX](https://github.com/moononournation/Arduino_GFX) for best compatibility.
    3.  **Check Resolution**: Ensure code matches hardware (e.g., 800x480).

??? bug "2. The touch function is not working or mirrored."
    1.  **I2C Address**: GT911 usually uses `0x5D` or `0x14`.
    2.  **Cable**: Ensure the 6-pin FPC is inserted fully (contacts facing down).
    3.  **Mirrored**: Use `touch.setRotation()` or swap coordinates in LVGL `indev_drv`.

??? failure "3. Compilation Error: `esp_lcd_panel_io.h` not found."
    Update your **ESP32 Board Package** in Arduino IDE to version **2.0.14** or **3.0.x**.

??? info "4. HDMI 'No Signal' on Raspberry Pi."
    Force HDMI resolution in `config.txt`. [See HDMI Guide](../products/hdmi/index.md#configuration-guide).

??? tip "5. How to export UI from SquareLine Studio?"
    Select **Arduino** protocol -> Export UI files -> Copy to project `libraries` -> Call `ui_init()`.

---


## 🛠️ Hardware & Wiring {: #hardware-wiring}

Detailed hardware specs and wiring diagrams are located in our sub-pages.

| Topic | Quick Summary | Full Link |
| :--- | :--- | :--- |
| **Panel Types** | IPS (178° View) vs TN (Budget) | [:octicons-arrow-right-24: Compare](../hardware/panels.md) |
| **Power Supply** | **5.0V Required**. 3.3V is for Logic ONLY. | [:octicons-arrow-right-24: Power](../hardware/power.md) |
| **Interfaces** | RGB (40P/50P), SPI, I2C, HDMI, SDMMC | [:octicons-arrow-right-24: Pinouts](../hardware/wiring.md) |

### ⚡ Quick Tips
* **Flicker?** Check if USB current is `< 500mA`. Try a 5V/2A adapter.
* **Logic Level?** Logic pins are **3.3V**. Connecting 5V directly to ESP32 IOs will damage it.

---

## 💼 Orders & Customization {: #orders-customization}

<div class="grid cards" markdown>

-   __How to Order__
    - [VIEWE Official Website](https://viewedisplay.com/)
    - [Alibaba Store](https://viewesmart.en.alibaba.com/)
    - [AliExpress Store](https://www.aliexpress.com/)

-   __Custom Services__
    - PCB Redesign (RS485/CAN)
    - High-brightness (1000 nits+)
    - Custom Touch Lens (MOQ > 500)
    - [Contact Sales](mailto:sales@viewedisplay.com)

</div>

---

## :material-lifebuoy: Support Center

[ :material-github: Submit GitHub Issue](https://github.com/VIEWESMART/VIEWE-FAQ/issues){ .md-button }
[ :material-email: Contact Support](mailto:support@viewedisplay.com){ .md-button }
[ :material-file-download: Download Center](../support/resource.md){ .md-button }