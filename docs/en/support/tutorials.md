---
title: Tutorial Center
hide:
  - toc        # 👈 关键修改：隐藏右侧目录栏，让页面变宽！
---

# :material-school: Tutorial Center

**From "Hello World" to Complex HMI Projects.**

Welcome to the VIEWE Developer Hub. Whether you are a hobbyist using **Arduino** or a professional engineer using **ESP-IDF**, we have step-by-step guides for you.

## :material-tools: Choose Your Framework

=== "🟢 Arduino IDE (Recommended)"
    **Best for Beginners & Rapid Prototyping.**
    Arduino IDE is the easiest way to get started. We provide a comprehensive library that includes drivers for Display, Touch, and LVGL.

    <div class="grid cards" markdown>

    -   :material-play-circle: **Getting Started**
        ---
        How to install the `Arduino_GFX` library and setup the board environment.
        [:arrow_right: Start Here](arduino/getting-started.md)

    -   :material-monitor-screenshot: **Draw Graphics (GFX)**
        ---
        Learn to draw basic shapes, text, and images using the lightweight GFX library.
        [:arrow_right: GFX Tutorial](arduino/gfx-guide.md)

    -   :material-layers: **Porting LVGL**
        ---
        How to run the powerful **LVGL** graphics engine on VIEWE displays with Arduino.
        [:arrow_right: LVGL Guide](arduino/lvgl-porting.md)

    </div>

=== "⚫ ESP-IDF (Professional)"
    **For Production & High Performance.**
    The official Espressif IoT Development Framework. Ideal for complex projects requiring multitasking (FreeRTOS) and deep hardware control.

    <div class="grid cards" markdown>

    -   :material-console: **Environment Setup**
        ---
        Setting up VS Code, ESP-IDF extension, and compiling your first "Hello World".
        [:arrow_right: Setup Guide](idf/setup.md)

    -   :material-chip: **Driver Integration**
        ---
        How to use the `esp_lcd` component to drive RGB/MIPI/SPI screens directly.
        [:arrow_right: Driver Guide](idf/driver-guide.md)

    </div>

=== "🎨 SquareLine Studio (UI Tool)"
    **No-Code UI Design.**
    Drag-and-drop UI editor for LVGL. Design your interface visually and export code for ESP32.

    <div class="grid cards" markdown>

    -   :material-brush: **UI Design Basics**
        ---
        Creating screens, adding widgets (Buttons, Labels, Charts) and events.
        [:arrow_right: Design Guide](squareline/basics.md)

    -   :material-export: **Export to ESP32**
        ---
        How to generate code from SquareLine and flash it to VIEWE modules.
        [:arrow_right: Export Guide](squareline/export.md)

    </div>

<br>

---

## :material-lightbulb-on: Topic Guides

Explore specific features and peripherals of your Smart Display.

<div class="grid cards" markdown>

-   :material-wifi: **Wireless (ESP-NOW)**
    ---
    Realize wireless communication between two displays using the ESP-NOW protocol.
    [:arrow_right: View Tutorial](topics/esp-now.md)

-   :material-sd: **SD Card Filesystem**
    ---
    How to mount the onboard SD card, read images, and log data.
    [:arrow_right: View Tutorial](topics/sd-card.md)

-   :material-knob: **Smart Knob Control**
    ---
    Driving the rotary encoder and handling knob press/turn events.
    [:arrow_right: View Tutorial](topics/smart-knob.md)

</div>

<br>

---

## :material-video: Video Tutorials

Watch step-by-step guides directly from our engineers.

<div class="grid cards" markdown>

-   **1. Getting Started with ESP32-S3**
    ---
    
    <div class="video-wrapper">
        <iframe src="https://www.youtube.com/embed/dQw4w9WgXcQ" allowfullscreen></iframe>
    </div>
    
    How to setup Arduino IDE and install GFX library.

-   **2. LVGL UI Design Guide**
    ---
    
    <div class="video-wrapper">
        <iframe src="https://www.youtube.com/embed/VIDEO_ID_2" allowfullscreen></iframe>
    </div>
    
    Design professional interfaces using SquareLine Studio.

-   **3. ESP-IDF Development**
    ---
    
    <div class="video-wrapper">
        <iframe src="https://www.youtube.com/embed/VIDEO_ID_3" allowfullscreen></iframe>
    </div>
    
    Deep dive into the official Espressif IoT Development Framework.

-   **4. Smart Knob & Encoder**
    ---
    
    <div class="video-wrapper">
        <iframe src="https://www.youtube.com/embed/VIDEO_ID_4" allowfullscreen></iframe>
    </div>
    
    How to handle rotary encoder events and motor feedback.

</div>