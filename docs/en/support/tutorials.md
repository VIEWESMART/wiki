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
        How to install the **Arduino IDE**  and configure IDE for VIEWE products.      
        [:arrow_right: Start Here](./tutorial/Arduino/How_To_Configure_Arduino.md)

    -   :material-monitor-screenshot: **Run Arduino**
        ---
        Fully tutorial includes environment, configuration and examples for Arduino .     
        [:arrow_right: Arduino Tutorial](./tutorial/Arduino/How-to-Use-Arduino.md)

    -   :material-layers: **Porting LVGL**
        ---
        How to run the powerful **LVGL** graphics engine on VIEWE displays with Arduino.    
        [:arrow_right: LVGL Guide](./tutorial/Arduino/LVGL-Configuration-and-SquareLine-Project-Porting.md)

    </div>

=== "⚫ ESP-IDF (Professional)"
    **For Production & High Performance.**
    The official Espressif IoT Development Framework. Ideal for complex projects requiring multitasking (FreeRTOS) and deep hardware control.

    <div class="grid cards" markdown>

    -   :material-console: **Environment Setup**
        ---
        Setting up VS Code, ESP-IDF extension, and compiling your first project.     
        [:arrow_right: Get Started](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/get-started/index.html)

    -   :material-chip: **Driver Integration**
        ---
        How to use the `esp_lcd` component to drive RGB/MIPI/SPI screens directly.    
        [:arrow_right: Drive Display](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-reference/peripherals/lcd/index.html#)

    </div>

=== "🎨 LVGL GUI"
    **Seamlessly UI Design.**
    Lightweight and powerful embedded graphics library.  Design your interface visually and export code for ESP32 and more.

    <div class="grid cards" markdown>

    -   :material-brush: **GUI LVGL Basics**
        ---
        Creating screens, adding widgets (Buttons, Labels, Charts) and events.     
        [:arrow_right: Design Guide](https://docs.lvgl.io/master/index.html)

    -   :material-export: **UI Editor**
        ---
        How to design cool and seamlessly UI by UI Editor fastly (SquareLine/LVGL Pro) with [VIEWE](https://viewedisplay.com/) modules?    
        [:arrow_right: Squareline](https://docs.squareline.io/docs/tutorials/example)
        [:arrow_right: LVGL Pro](https://docs.lvgl.io/master/xml/index.html)

    </div>

<br>

---

## :material-lightbulb-on: Topic Guides

Explore specific features and peripherals of your Smart Display.

<div class="grid cards" markdown>

-   :material-wifi: **Wireless (ESP-NOW)**     
    Realize wireless communication between two displays using the ESP-NOW protocol.    
    [:arrow_right: View Tutorial](#video-wirless-espnow)

-   :material-sd: **SD Card Filesystem**    
    How to mount the onboard SD card, read images, and log data.     
    [:arrow_right: View Tutorial](#video-sdcard-use)

-   :material-knob: **Smart Knob Control**     
    Driving the rotary encoder and handling knob press/turn events.    
    [:arrow_right: View Tutorial](#video-drive-knob)

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
    
    <div class="video-wrapper"> <a id="video-lvgl-gui"></a>
        <iframe src="https://www.youtube.com/embed/do9dNKBkUSQ?si=eDvDOIyog_5rClBn" allowfullscreen></iframe>
    </div>
    
    Design professional interfaces using SquareLine Studio.

-   **3. How to Drive ESP32-S3 Display with GFX Library?**
    ---
    
    <div class="video-wrapper">
        <iframe src="https://www.youtube.com/embed/KR_eoGvRKqM?si=YHH5o-dd4ASKV4nI" allowfullscreen></iframe>
    </div>
    
    Deep dive into the official Espressif IoT Development Framework.

-   **4. How to Drive ESP32 Smart Rotary Knob Display?** <a id="video-drive-knob"></a>
    ---
    
    <div class="video-wrapper">
        <iframe src="https://www.youtube.com/embed/_3Hx9lhOMsg?si=v9AH-pB7BP6Rt6pN" allowfullscreen></iframe>
    </div>
    
    How to handle rotary encoder events and motor feedback.

-   **5. How to Realize wireless communication between two displays using the ESP-NOW protocol** <a id="video-wirless-espnow"></a>
    ---
    
    <div class="video-wrapper">
        <iframe src="https://www.youtube.com/embed/1siwBBuNR2A?si=qyAfiO0QCx5MM04M"  allowfullscreen></iframe>
    </div>
    
    Wifi and Bluetooth commnication by ESP-NOW.    

-   **5. How to use SD card with esp32** <a id="video-sdcard-use"></a>
    ---
    
    <div class="video-wrapper">
        <iframe src="https://www.youtube.com/embed/Dk0MKfdLvGM?si=d12qvDywSE-odCBY" allowfullscreen></iframe>
    </div>
    
    How to mount the onboard SD card, read images, and log data    
    

</div>

<!-- ## :material-lifebuoy: Learn More

[ :material-github: More Vedio](https://youtube.com/playlist?list=PLM2TqiCfQM467LPRFVgJkHRajdR-wuVb8&si=fVDSm13eE9w-JkoH){ .md-button }
[ :material-file-download: Offical Tutorial](https://viewedisplay.com/category/tutorial/){ .md-button }
[ :material-email: Contact Support](mailto:support@viewedisplay.com){ .md-button }    -->

