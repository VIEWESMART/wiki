---
title: 教程中心
description: 优奕视界开发者教程中心，覆盖 Arduino IDE、ESP-IDF、PlatformIO 与 LVGL，从环境搭建到复杂 HMI 项目的完整分步指南。
hide:
  - toc
---

# :material-school: 教程中心

**从「Hello World」到复杂的 HMI 项目。**

欢迎来到优奕视界开发者中心。无论你是使用 **Arduino** 的爱好者，还是使用 **ESP-IDF** 的专业工程师，这里都有为你准备的分步指南。

## :material-tools: 选择开发框架

=== "🟢 Arduino IDE（推荐）"
    **最适合初学者与快速原型验证。**
    Arduino IDE 是上手最快的方式。我们提供完整的库，涵盖显示屏、触摸与 LVGL 驱动。

    <div class="grid cards" markdown>

    -   :material-play-circle: **环境准备**
        ---
        如何安装 **Arduino IDE** 并为优奕视界产品完成配置。
        [:arrow_right: 从这里开始](./tutorial/Arduino/How_To_Configure_Arduino.md)

    -   :material-monitor-screenshot: **跑通 Arduino**
        ---
        完整教程，涵盖 Arduino 的环境、配置与示例。
        [:arrow_right: Arduino 教程](./tutorial/Arduino/How-to-Use-Arduino.md)

    -   :material-layers: **移植 LVGL**
        ---
        如何在优奕视界显示屏上用 Arduino 运行强大的 **LVGL** 图形引擎。
        [:arrow_right: LVGL 指南](./tutorial/Arduino/LVGL-Configuration-and-SquareLine-Project-Porting.md)

    </div>

=== "⚫ ESP-IDF（专业）"
    **面向量产与高性能场景。**
    乐鑫官方的物联网开发框架，适合需要多任务（FreeRTOS）与深度硬件控制的复杂项目。

    <div class="grid cards" markdown>

    -   :material-console: **环境搭建**
        ---
        配置 VS Code、ESP-IDF 插件，并编译第一个工程。
        [:arrow_right: 立即开始](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/get-started/index.html)

    -   :material-chip: **驱动集成**
        ---
        如何使用 `esp_lcd` 组件直接驱动 RGB / MIPI / SPI 屏幕。
        [:arrow_right: 驱动显示屏](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-reference/peripherals/lcd/index.html#)

    </div>

=== "🎨 LVGL GUI"
    **无缝的界面设计体验。**
    轻量而强大的嵌入式图形库。可视化设计界面，并导出可在 ESP32 等平台运行的代码。

    <div class="grid cards" markdown>

    -   :material-brush: **LVGL 图形基础**
        ---
        创建屏幕、添加控件（按钮、标签、图表）与事件处理。
        [:arrow_right: 设计指南](https://docs.lvgl.io/master/index.html)

    -   :material-export: **UI 编辑器**
        ---
        如何借助 UI 编辑器（SquareLine / LVGL Pro）为[优奕视界](https://www.chinasunyee.com/)模组快速设计出色界面。
        [:arrow_right: SquareLine](https://docs.squareline.io/docs/tutorials/example)
        [:arrow_right: LVGL Pro](https://docs.lvgl.io/master/xml/index.html)

    </div>

<br>

---

## :material-lightbulb-on: 专题指南

了解智能屏的具体功能与外设。

<div class="grid cards" markdown>

-   :material-wifi: **无线通信（ESP-NOW）**
    使用 ESP-NOW 协议实现两块显示屏之间的无线通信。
    [:arrow_right: 查看教程](#video-wirless-espnow)

-   :material-sd: **SD 卡文件系统**
    如何挂载板载 SD 卡、读取图片并记录数据。
    [:arrow_right: 查看教程](#video-sdcard-use)

-   :material-knob: **智能旋钮控制**
    驱动旋转编码器，并处理旋钮的按压与旋转事件。
    [:arrow_right: 查看教程](#video-drive-knob)

</div>

<br>

---

## :material-video: 视频教程

[ :simple-youtube: 更多视频](https://youtube.com/playlist?list=PLM2TqiCfQM467LPRFVgJkHRajdR-wuVb8&si=fVDSm13eE9w-JkoH){ .md-button }
[ :simple-bilibili: B 站视频](https://space.bilibili.com/1545248509){ .md-button }
[ :material-earth: 优奕视界官网](https://www.chinasunyee.com/){ .md-button }

**以下视频由优奕视界工程师录制，讲解语言为英文。**

<div class="grid cards" markdown>

-   **1. 如何在 Arduino IDE 中用 ESP32-S3 开发板驱动触摸与显示？**
    ---
    
    <div class="video-wrapper">
        <iframe src="https://www.youtube.com/embed/SD2pItGLeGk?si=iFAXDXYXmvnt8Zxz"  allowfullscreen></iframe>
    </div>
-   **2. 如何用 Arduino IDE 与 LVGL 打造智能屏 GUI？**
    ---
    
    <div class="video-wrapper"> <a id="video-lvgl-gui"></a>
        <iframe src="https://www.youtube.com/embed/do9dNKBkUSQ?si=eDvDOIyog_5rClBn" allowfullscreen></iframe>
    </div>
    
    使用 SquareLine Studio 设计专业界面。

-   **3. 如何用 GFX 库驱动 ESP32-S3 显示屏？**
    ---
    
    <div class="video-wrapper">
        <iframe src="https://www.youtube.com/embed/KR_eoGvRKqM?si=YHH5o-dd4ASKV4nI" allowfullscreen></iframe>
    </div>
    
    深入讲解乐鑫官方物联网开发框架。

-   **4. 如何驱动 ESP32 智能旋钮屏？** <a id="video-drive-knob"></a>
    ---
    
    <div class="video-wrapper">
        <iframe src="https://www.youtube.com/embed/_3Hx9lhOMsg?si=v9AH-pB7BP6Rt6pN" allowfullscreen></iframe>
    </div>
    
    如何处理旋转编码器事件与电机反馈。

-   **5. 如何用 ESP-NOW 协议实现两块显示屏之间的无线通信** <a id="video-wirless-espnow"></a>
    ---
    
    <div class="video-wrapper">
        <iframe src="https://www.youtube.com/embed/1siwBBuNR2A?si=qyAfiO0QCx5MM04M"  allowfullscreen></iframe>
    </div>
    
    通过 ESP-NOW 实现 Wi-Fi 与蓝牙通信。

-   **5. 如何在 ESP32 上使用 SD 卡** <a id="video-sdcard-use"></a>
    ---
    
    <div class="video-wrapper">
        <iframe src="https://www.youtube.com/embed/Dk0MKfdLvGM?si=d12qvDywSE-odCBY" allowfullscreen></iframe>
    </div>
    
    如何挂载板载 SD 卡、读取图片并记录数据。
    

</div>
