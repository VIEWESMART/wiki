---
title: LVGL 配置与 SquareLine 工程移植
description: 在优奕视界 ESP32 智能屏上配置 LVGL，并将 SquareLine Studio 导出的工程移植到 Arduino 项目的完整步骤。
---

# LVGL 配置与 SquareLine 工程移植

!!! success "获得 Espressif Arduino 官方支持"
    [优奕视界 ESP32 智能屏开发板](https://www.chinasunyee.com/)：已获得 [Espressif ESP32 Arduino](https://github.com/esp-arduino-libs/ESP32_Display_Panel/blob/master/docs/board/board_viewe.md) 官方支持。      
    一键安装核心与驱动，无需配置引脚，即可在 Arduino IDE 中开始开发。  

## 配置 LVGL { #configuring-lvgl }

LVGL 的功能与参数可以通过编辑 `lv_conf.h` 文件进行配置，用户可以在该文件中修改宏定义，以更新驱动的行为或默认参数。以下是配置 LVGL 的一些要点：

1. 使用 arduino-esp32 v3.x.x 版本时，LVGL 会按以下顺序查找配置文件：`当前项目目录` > `Arduino 库目录`。如果找不到配置文件，编译时会报错并提示缺少配置文件。因此，用户需要确保至少有一个目录包含 `lv_conf.h` 文件。

2. 如果多个工程需要使用相同的配置，用户可以将配置文件放入 [Arduino 库目录](../../FAQ-Arduino-ESP32.md#where-is-the-directory-for-arduino-libraries)，这样所有工程都能共享同一份配置。

以下是共享同一份 LVGL 配置的详细步骤：

1. 进入 [Arduino 库目录](../../FAQ-Arduino-ESP32.md#where-is-the-directory-for-arduino-libraries)。

2. 进入 `lvgl` 文件夹，复制 `lv_conf_template.h` 文件，并将副本放到与 `lvgl` 文件夹同一层级的位置。然后，将复制出的文件重命名为 `lv_conf.h`。

3. 最终，Arduino 库文件夹的结构应如下所示：

   ```
   Arduino
       |-libraries
           |-lv_conf.h
           |-lvgl
           |-other_lib_1
           |-other_lib_2
   ```

4. 打开 `lv_conf.h` 文件，将第一处 `#if 0` 改为 `#if 1`，以启用该文件的内容。

5. 根据需求设置其他配置项。以下是 LVGL v8 一些常见配置选项的示例：

   ```c
   #define LV_COLOR_DEPTH          16  // 通常使用 16 位色深（RGB565），
                                       // 但也可以设为 `32` 以支持 24 位色深（RGB888）
   #define LV_COLOR_16_SWAP        0   // 如果使用 SPI/QSPI LCD（例如 ESP32-C3-LCDkit），请将其设为 `1`
   #define LV_COLOR_SCREEN_TRANSP  1
   #define LV_MEM_CUSTOM           1
   #define LV_MEMCPY_MEMSET_STD    1
   #define LV_TICK_CUSTOM          1
   #define LV_ATTRIBUTE_FAST_MEM   IRAM_ATTR
                                      // 获得更高性能，但会占用更多 SRAM
   #define LV_FONT_MONTSERRAT_N    1  // 启用所需的所有内置字体（`N` 应替换为字号）
   ```

6. 更多信息，请参阅 [LVGL 官方文档](https://docs.lvgl.io/8.3/get-started/platforms/arduino.html)。

## 移植 SquareLine 工程

SquareLine Studio（v1.3.x）可以通过可视化编辑快速设计出精美的 UI。如果你想在 Arduino IDE 中使用从 SquareLine 导出的 UI 源文件，可以按以下步骤进行移植：

1. 首先，在 SquareLine Studio 中新建一个工程。进入 `Create` -> `Arduino`，选择 `Arduino with TFT-eSPI` 作为工程模板，然后在 `PROJECT SETTINGS` 区域为目标开发板配置 LCD 属性，例如 `Resolution` 和 `Color depth`。最后，点击 `Create` 按钮创建工程。

2. 对于已有工程，你也可以点击导航栏中的 `File` -> `Project Settings` 进入工程设置。然后，在 `BOARD PROPERTIES` 区域将 `Board Group` 配置为 `Arduino`、将 `Board` 配置为 `Arduino with TFT-eSPI`。此外，在 `DISPLAY PROPERTIES` 区域为目标开发板配置 LCD 属性。最后，点击 `Save` 按钮保存工程设置。

3. 完成 UI 设计并配置好导出路径后，点击菜单栏中的 `Export` -> `Create Template Project` 和 `Export UI Files` 按钮，导出工程和 UI 源文件。工程目录的结构将如下所示：

    ```
    Project
        |-libraries
            |-lv_conf.h
            |-lvgl
            |-readme.txt
            |-TFT_eSPI
            |-ui
        |-README.md
        |-ui
    ```

4. 将工程目录中 `libraries` 文件夹内的 `lv_conf.h`、`lvgl` 和 `ui` 文件夹复制到 Arduino 库目录。如果你需要使用本地已安装的 `lvgl`，则跳过复制 `lvgl` 和 `lv_conf.h`，然后参考 [LVGL 配置](#configuring-lvgl) 一节中的步骤来配置 LVGL。Arduino 库文件夹的结构将如下所示：

    ```
    Arduino
        |-libraries
            |-ESP32_Display_Panel
            |-ESP_Panel_Conf.h (optional)
            |-lv_conf.h (optional)
            |-lvgl
            |-ui
            |-other_lib_1
            |-other_lib_2
    ```



!!! info "没找到需要的内容？"
    如需更多支持，请观看视频或联系我们：
    
    [ :simple-youtube: 视频教程](../../tutorials.md#video-lvgl-gui){ .md-button }
    [联系技术支持](mailto:support@chinasunyee.com){ .md-button }
