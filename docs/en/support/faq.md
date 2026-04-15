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

-   :material-code-braces: __Software Development FAQ__
    ---
    FAQ for Arduino, ESP-IDF, PlatformIO and LVGL framework.
    [:octicons-arrow-right-24: View FAQ](#software-development)

-   :material-chip: __Hardware & Wiring FAQ__
    ---
    Display types, pinouts, power requirements, and touch.
    [:octicons-arrow-right-24: View FAQ](#hardware-wiring)

-   :material-cart-check: __Orders & Customization FAQ__
    ---
    Bulk ordering, custom PCB/Screen, and warranty.
    [:octicons-arrow-right-24: View Policy](#orders-customization)

</div>

---

## 🔥 Top Frequently Asked Questions

These are the most common issues reported by users. Click to expand solutions.

??? question "1. Which library should I use: LVGL or Arduino_GFX?"
    * **Arduino_GFX**: Best for simple drawing (circles, lines, text) and raw driver performance.
    * **LVGL**: The industry standard for complex UIs (Buttons, Charts, Animations). We recommend **LVGL** for professional products.

??? question "2. Do you support MicroPython or CircuitPython?"
    Yes, our hardware is fully compatible. While our official tutorials focus on **C++**, the community provides drivers for ST7701/ST7789 screens.

??? bug "3. The screen is black but the backlight is on."
    1.  **Check PSRAM**: For RGB screens, PSRAM must be enabled (`Tools` -> `PSRAM` -> `OPI PSRAM`).
    2.  **Check Library**: Use [Arduino_GFX](https://github.com/moononournation/Arduino_GFX) for best compatibility.
    3.  **Check Resolution**: Ensure code matches hardware (e.g., 800x480).

??? bug "4. The touch function is not working or mirrored."
    1.  **I2C Address**: GT911 usually uses `0x5D` or `0x14`.
    2.  **Cable**: Ensure the 6-pin FPC is inserted fully (contacts facing down).
    3.  **Mirrored**: Use `touch.setRotation()` or swap coordinates in LVGL `indev_drv`.

??? failure "5. Compilation Error: `esp_lcd_panel_io.h` not found."
    Update your **ESP32 Board Package** in Arduino IDE to version **2.0.14** or **3.0.x**.

??? info "6. HDMI 'No Signal' on Raspberry Pi."
    Force HDMI resolution in `config.txt`. [See HDMI Guide](../products/hdmi/index.md#configuration-guide).

??? tip "7. How to export UI from SquareLine Studio?"
    Select **Arduino** protocol -> Export UI files -> Copy to project `libraries` -> Call `ui_init()`.

---



## 💻 Software Development {: #software-development}

Choose your preferred development framework. Each section below leads to a comprehensive setup and optimization guide.

### 📦 Development Frameworks

<div class="grid cards" markdown>

-   :simple-arduino: __Arduino__
    ---
    Perfect for rapid prototyping.

    [:octicons-link-external-16: **Arduino FAQ**](FAQ-Arduino-ESP32.md)

-   :simple-espressif: __ESP-IDF__
    ---
    Professional native environment.

    [:octicons-link-external-16: **ESP-IDF FAQ**](../software/esp-idf/index.md)

-   :simple-platformio: __PlatformIO__
    ---
    Modern IDE for team collaboration.
 
    [:octicons-link-external-16: **PlatformIO FAQ**](../software/platformio/index.md)

</div>






## 🛠️ Hardware & Wiring {: #hardware-wiring}

Detailed hardware specs and wiring diagrams are located in our sub-pages.

| Topic | Quick Summary | Full Link |
| :--- | :--- | :--- |
| **Panel Types** | IPS (178° View) vs TN (Budget) | [:octicons-arrow-right-24: Compare](../knowledge/posts/ips-vs-tn.md) |
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
    - [Alibaba Store](https://viewelcd.en.alibaba.com/)
    - [AliExpress Store](https://www.aliexpress.com/store/1103785142)

-   __Custom Services__
    - PCB Redesign (RS485/CAN)
    - High-brightness (1000 nits+)
    - Custom Touch Lens (MOQ > 500)
    - [More about customization](https://viewedisplay.com/customization/)
    - [Contact Sales](mailto:sales@viewedisplay.com)

</div>

---

## :material-lifebuoy: Support Center

[ :material-github: Submit GitHub Issue](https://github.com/VIEWESMART/VIEWE-FAQ/issues){ .md-button }
[ :material-email: Contact Support](mailto:support@viewedisplay.com){ .md-button }
[ :material-file-download: Download Center](../support/resource.md){ .md-button }