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

[ :simple-youtube: More Video](https://youtube.com/playlist?list=PLM2TqiCfQM467LPRFVgJkHRajdR-wuVb8&si=fVDSm13eE9w-JkoH){ .md-button }
[ :material-earth: VIEWE Tutorial](https://viewedisplay.com/category/tutorial/){ .md-button }

**Watch step-by-step guides directly from our engineers.**

<div class="grid cards" markdown>

-   **1. How to drive touch and display with ESP32-S3 board in Arduino IDE?**
    ---
    
    <div class="video-wrapper">
        <iframe src="https://www.youtube.com/embed/SD2pItGLeGk?si=iFAXDXYXmvnt8Zxz"  allowfullscreen></iframe>
    </div>
-   **2.  How to use LVGL to Build a Smart Display GUI with Arduino IDE?**
    ---
    
    <div class="video-wrapper">
        <iframe src="https://www.youtube.com/embed/do9dNKBkUSQ?si=eDvDOIyog_5rClBn" allowfullscreen></iframe>
    </div>
    
    Design professional interfaces using SquareLine Studio.

-   **3. How to Drive ESP32-S3 Display with GFX Library?**
    ---
    
    <div class="video-wrapper">
        <iframe src="https://www.youtube.com/embed/KR_eoGvRKqM?si=YHH5o-dd4ASKV4nI" allowfullscreen></iframe>
    </div>
    
    Deep dive into the official Espressif IoT Development Framework.

-   **4. How to Drive ESP32 Smart Rotary Knob Display?**
    ---
    
    <div class="video-wrapper">
        <iframe src="https://www.youtube.com/embed/_3Hx9lhOMsg?si=v9AH-pB7BP6Rt6pN" allowfullscreen></iframe>
    </div>
    
    How to handle rotary encoder events and motor feedback.
  

</div>

<!-- ## :material-lifebuoy: Learn More

[ :material-github: More Vedio](https://youtube.com/playlist?list=PLM2TqiCfQM467LPRFVgJkHRajdR-wuVb8&si=fVDSm13eE9w-JkoH){ .md-button }
[ :material-file-download: Offical Tutorial](https://viewedisplay.com/category/tutorial/){ .md-button }
[ :material-email: Contact Support](mailto:support@viewedisplay.com){ .md-button }    -->
