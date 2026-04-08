---
title: MIPI DSI Displays
hide:
  - toc
---

# MIPI DSI Interface Displays

**Native DSI Interface. One Screen, Dual Ecosystems.**

VIEWE MIPI DSI displays are engineered for high-performance HMI.
With our unified interface design, a single display module is natively compatible with both **Raspberry Pi** and **ESP32-P4**, offering high bandwidth, low power consumption, and low EMI.

<div class="grid cards" markdown>

-   :material-link-variant: **Dual Support**
    ---
    **Raspberry Pi + ESP32-P4**.
    Seamlessly connects to RPi's DSI port and ESP32-P4's MIPI interface.

-   :material-cable-data: **1-Cable Solution**
    ---
    Say goodbye to messy wiring.
    A single FPC cable transmits **Video**, **Touch**, and **Power** simultaneously.

-   :material-speedometer: **High Speed**
    ---
    Supports high resolutions up to **1920x720** and high frame rates (60FPS+), far superior to SPI displays.

</div>

<br>

---

## :material-view-dashboard: Product Gallery

=== "🖥️ Standard (HD/FHD)"
    **Standard high-definition screens for HMI and Tablets.**

    <div class="grid cards" markdown>

    -   **7.0" Standard**
        ---
        **Res**: 1024x600
        **Note**: The most popular size for P4 & RPi.
        [:arrow_right: View Specs](#matrix)

    -   **10.1" WXGA**
        ---
        **Res**: 800x1280
        **Orientation**: Portrait (Rotatable)
        [:arrow_right: View Specs](#matrix)

    -   **5.0" HD Phone Screen**
        ---
        **Res**: 720x1280
        **Orientation**: Portrait (Rotatable)
        [:arrow_right: View Specs](#matrix)

    </div>

=== "🎨 Creative (Round & Square)"
    **Unique 1:1 ratio screens for Smart Knobs, 86-Boxes, and Thermostats.**

    <div class="grid cards" markdown>

    -   **4.0" Round**
        ---
        **Res**: 720x720
        **Shape**: Pure Circular
        **PPI**: High Pixel Density
        [:arrow_right: View Specs](#matrix)

    -   **4.0" Square**
        ---
        **Res**: 720x720
        **Shape**: 1:1 Square
        **Feature**: Symmetric Bezel
        [:arrow_right: View Specs](#matrix)

    </div>

=== "📏 Bar Type (Ultra-Wide)"
    **Ultrawide aspect ratio for Automotive Dashboards and Secondary Monitors.**

    <div class="grid cards" markdown>

    -   **12.3" Automotive Bar**
        ---
        **Res**: 720x1920
        **Size**: Large Cockpit Screen
        **App**: Digital Instrument Cluster
        [:arrow_right: View Specs](#matrix)

    -   **6.8" Strip Bar**
        ---
        **Res**: 480x1280
        **Size**: Compact Bar
        **App**: Smart Home Control / Rack Display
        [:arrow_right: View Specs](#matrix)

    </div>


<br>

---

## :material-table-search: Spec Matrix {: #matrix }

| Size | Resolution | Shape | Ratio | Touch | Compatibility |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **4.0"** | 720x720 | **Round** | 1:1 | Cap (I2C) | RPi / P4 |
| **4.0"** | 720x720 | **Square**| 1:1 | Cap (I2C) | RPi / P4 |
| **5.0"** | 720x1280 | Rect | 9:16 | Cap (I2C) | RPi / P4 |
| **6.8"** | 480x1280 | **Bar** | 3:8 | Cap (I2C) | RPi / P4 |
| **7.0"** | 1024x600 | Rect | 16:9 | Cap (I2C) | RPi / P4 |
| **10.1"**| 800x1280 | Rect | 10:16| Cap (I2C) | RPi / P4 |
| **12.3"**| 720x1920 | **Bar** | ~3:8 | Cap (I2C) | RPi / P4 |

> **Note**:
> * **Orientation**: 5.0", 10.1", and 12.3" are natively portrait (vertical). You can easily rotate them to landscape mode via software config in RPi or ESP-IDF.
> * **Touch Interface**: Touch signals are transmitted via I2C, integrated into the FPC cable.

<br>

## :material-developer-board: Driver & Setup

Getting started is easy with our ready-to-use drivers.

=== "Raspberry Pi"
    Add the overlay to your `/boot/config.txt` to enable the display and touch driver.
    ```ini
    dtoverlay=viewe-mipi-4inch
    # (Refer to specific wiki page for your model's overlay)
    ```

=== "ESP32-P4"
    We provide a component for **ESP-IDF** (`esp_lcd_dsi`).
    * **Example Code**: [View on GitHub](https://github.com/VIEWESMART)
    * **Library**: Includes initialization sequences for all 7 models.

<br>

## :material-download: Resources

[Download Datasheets](../support/resource.md){ .md-button .md-button--primary }
[Contact Support](https://viewedisplay.com/contacts/){ .md-button }