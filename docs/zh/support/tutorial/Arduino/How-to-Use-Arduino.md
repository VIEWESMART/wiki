---
title: Arduino 使用教程
description: 优奕视界 ESP32 智能屏 Arduino 教程，涵盖依赖版本、arduino-esp32 与库的安装、开发板配置、触摸与 LVGL 示例，以及 PlatformIO 用法。
---

# Arduino 使用教程

!!! success "获得 Espressif Arduino 官方支持"
    [优奕视界 ESP32 系列](https://www.chinasunyee.com/)：已获得 [Espressif ESP32 Arduino](https://github.com/esp-arduino-libs/ESP32_Display_Panel/blob/master/docs/board/board_viewe.md) 官方支持。      
    一键安装核心与驱动，无需配置引脚，即可在 Arduino IDE 中开始开发。  

## 依赖与版本

| **依赖** | **版本** |
| -------------- | ----------- |
| [arduino-esp32](https://github.com/espressif/arduino-esp32) | >= v3.0.0-alpha3 |
| [ESP32_IO_Expander](https://github.com/esp-arduino-libs/ESP32_IO_Expander) | >= 0.1.0 && < 0.2.0 |
| [ESP32_Display_Panel](https://github.com/esp-arduino-libs/ESP32_Display_Panel)| > 0.2.1 |

## 安装 arduino-esp32
关于在 Arduino IDE 中安装 esp32，请参阅 [Arduino IDE 安装与配置指南](./How_To_Configure_Arduino.md#step-1-download-install)。

## 安装库

关于安装 ESP32_Display_Panel 库，请参阅 [如何在 Arduino IDE 中安装 ESP32_Display_Panel](../../FAQ-Arduino-ESP32.md#how-to-install-esp32_display_panel-in-arduino-ide)。

<!-- ## 工具选项配置
关于 `tools` 选项的配置，请参阅 [Arduino IDE 中的推荐配置](./Board_Instructions.md#recommended-configurations-in-the-arduino-ide)。 -->


## 配置说明

以下是如何配置 ESP32_Display_Panel 的详细说明，主要包括 [配置驱动](#configuring-drivers)、[使用受支持的开发板](#using-supported-development-boards) 和 [使用自定义开发板](#using-custom-development-boards)。这些都是可选操作，并通过指定的头文件进行配置。用户可以根据自身需求选择使用，其特性如下：

1. ESP32_Display_Panel 查找配置文件的路径顺序为：`当前项目目录` > `Arduino 库目录` > `ESP32_Display_Panel 目录`。
2. ESP32_Display_Panel 中的所有示例默认都包含其所需的配置文件，用户可以直接修改其中的宏定义。
3. 对于没有配置文件的工程，用户可以从 ESP32_Display_Panel 的根目录或示例中将其复制到自己的项目中。
4. 如果多个工程需要使用相同的配置，用户可以将配置文件放入 [Arduino 库目录](../../FAQ-Arduino-ESP32.md#where-is-the-directory-for-arduino-libraries)，这样所有工程都能共享同一份配置。

!!! warning

    * 同一目录下可以同时包含 `ESP_Panel_Board_Supported.h` 和 `ESP_Panel_Board_Custom.h` 配置文件，但不能同时启用，也就是说 `ESP_PANEL_USE_SUPPORTED_BOARD` 和 `ESP_PANEL_USE_CUSTOM_BOARD` 只能有一个被设为 `1`。
    * 如果上述两个配置文件都未启用，用户将无法使用 `ESP_Panel` 驱动，只能使用其他独立的设备驱动，例如 `ESP_PanelBus`、`ESP_PanelLcd` 等。
    * 由于这些文件内的配置可能发生变化，例如新增、删除或重命名，为保证程序的兼容性，库会独立管理这些文件的版本，并在编译时检查用户当前使用的配置文件是否与库兼容。详细的版本信息与检查规则可在文件末尾查看。


### 配置驱动 { #configuring-drivers }

ESP32_Display_Panel 会根据 `ESP_Panel_Conf.h` 文件来配置驱动功能与参数。用户可以通过修改该文件中的宏定义来更新驱动的行为或默认参数。例如，要启用调试日志输出，以下是一段修改后的 `ESP_Panel_Conf.h` 文件片段：

```c
...
/* 设为 1 以打印调试日志信息 */
#define ESP_PANEL_ENABLE_LOG                (1)         // 0/1
...
```

### 使用受支持的开发板 { #using-supported-development-boards }

ESP32_Display_Panel 会根据 `ESP_Panel_Board_Supported.h` 文件，将 `ESP_Panel` 配置为目标开发板的驱动。用户可以通过修改该文件中的宏定义来选择受支持的开发板。例如，要使用 *ESP32-S3-BOX-3* 开发板，请按以下步骤操作：

1. 将 `ESP_Panel_Board_Supported.h` 文件中的 `ESP_PANEL_USE_SUPPORTED_BOARD` 宏定义设为 `1`。
2. 取消注释目标开发板型号对应的宏定义。

以下是一段修改后的 `ESP_Panel_Board_Supported.h` 文件片段：

```c
...
/* 使用受支持的开发板时设为 1 */
#define ESP_PANEL_USE_SUPPORTED_BOARD       (1)         // 0/1

#if ESP_PANEL_USE_SUPPORTED_BOARD
...
// #define BOARD_UEDX24320028E_WB_A_2_4
// #define BOARD_UEDX24320028E_WB_A_2_8 
#define BOARD_UEDX24320028E_WB_A_3_5_240_320
// #define BOARD_UEDX24320028E_WB_A_3_5_320_480
...
#endif /* ESP_PANEL_USE_SUPPORTED_BOARD */
```

### 使用自定义开发板 { #using-custom-development-boards }

ESP32_Display_Panel 会根据 `ESP_Panel_Board_Custom.h` 文件，将 `ESP_Panel` 配置为自定义开发板的驱动。用户需要根据自定义开发板的实际参数修改该文件。例如，要使用一块 *480x480 RGB ST7701 LCD + I2C GT911 Touch* 的自定义开发板，请按以下步骤操作：

1. 将 `ESP_Panel_Board_Custom.h` 文件中的 `ESP_PANEL_USE_CUSTOM_BOARD` 宏定义设为 `1`。
2. 设置 LCD 相关的宏定义：   
   a. 将 `ESP_PANEL_USE_LCD` 设为 `1`。  
   b. 将 `ESP_PANEL_LCD_WIDTH` 和 `ESP_PANEL_LCD_HEIGHT` 设为 `480`。   
   c. 将 `ESP_PANEL_LCD_BUS_TYPE` 设为 `ESP_PANEL_BUS_TYPE_RGB`。    
   d. 在 `ESP_PANEL_LCD_BUS_TYPE == ESP_PANEL_BUS_TYPE_RGB` 下方设置 LCD 信号引脚及其他参数。    
   e. 根据屏幕厂商提供的初始化命令参数，取消注释并修改 `ESP_PANEL_LCD_VENDOR_INIT_CMD` 宏定义。   
   f. 按需修改其他 LCD 配置。     
3. 设置 Touch 相关的宏定义：
   a. 将 `ESP_PANEL_USE_TOUCH` 设为 `1`。    
   b. 在 `ESP_PANEL_TOUCH_BUS_TYPE == ESP_PANEL_BUS_TYPE_I2C` 下方设置 Touch 信号引脚及其他参数。    
   c. 按需修改其他 Touch 配置。     
4. 按需启用其他驱动宏定义，例如 `ESP_PANEL_USE_BACKLIGHT`、`ESP_PANEL_USE_EXPANDER` 等。    

以下是一段修改后的 `ESP_Panel_Board_Custom.h` 文件片段：

```c
...
/* 使用自定义开发板时设为 1 */
#define ESP_PANEL_USE_CUSTOM_BOARD  (1)         // 0/1

/* 使用 LCD 面板时设为 1 */
#define ESP_PANEL_USE_LCD           (1)     // 0/1

#if ESP_PANEL_USE_LCD
/**
 * LCD 控制器名称
 */
#define ESP_PANEL_LCD_NAME          ST7701

/* LCD 分辨率（像素） */
#define ESP_PANEL_LCD_WIDTH         (480)
#define ESP_PANEL_LCD_HEIGHT        (480)
...
/**
 * LCD 总线类型。
 */
#define ESP_PANEL_LCD_BUS_TYPE      (ESP_PANEL_BUS_TYPE_RGB)
/**
 * LCD 总线参数。
 *
 * 更多详情请参阅 https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-reference/peripherals/lcd.html 以及
 * https://docs.espressif.com/projects/esp-iot-solution/en/latest/display/lcd/index.html。
 *
 */
#if ESP_PANEL_LCD_BUS_TYPE == ESP_PANEL_BUS_TYPE_RGB
...
#endif /* ESP_PANEL_LCD_BUS_TYPE */
...
/**
 * LCD 厂商初始化命令。
 *
 * 不同厂商的初始化序列可能不同，应向 LCD 供应商索取初始化序列代码。请取消注释并修改以下宏定义，
 * 否则 LCD 驱动将使用默认的初始化序列代码。
 *
 * 序列代码有两种格式：
 *   1. 原始数据：{command, (uint8_t []){ data0, data1, ... }, data_size, delay_ms}
 *   2. 格式化宏：ESP_PANEL_LCD_CMD_WITH_8BIT_PARAM(delay_ms, command, { data0, data1, ... }) 以及
 *                ESP_PANEL_LCD_CMD_WITH_NONE_PARAM(delay_ms, command)
 */
#define ESP_PANEL_LCD_VENDOR_INIT_CMD() \
    { \
        ESP_PANEL_LCD_CMD_WITH_8BIT_PARAM(0, 0xFF, {0x77, 0x01, 0x00, 0x00, 0x10}), \
        ESP_PANEL_LCD_CMD_WITH_8BIT_PARAM(0, 0xC0, {0x3B, 0x00}), \
        ESP_PANEL_LCD_CMD_WITH_8BIT_PARAM(0, 0xC1, {0x0D, 0x02}), \
        ESP_PANEL_LCD_CMD_WITH_8BIT_PARAM(0, 0xC2, {0x31, 0x05}), \
        ESP_PANEL_LCD_CMD_WITH_8BIT_PARAM(0, 0xCD, {0x00}), \
        ...
        ESP_PANEL_LCD_CMD_WITH_NONE_PARAM(120, 0x11), \
    }
...
#endif /* ESP_PANEL_USE_LCD */

/* 使用触摸面板时设为 1 */
#define ESP_PANEL_USE_TOUCH         (1)         // 0/1
#if ESP_PANEL_USE_TOUCH
/**
 * 触摸控制器名称
 */
#define ESP_PANEL_TOUCH_NAME        GT911
...
/**
 * 触摸面板总线类型
 */
#define ESP_PANEL_TOUCH_BUS_TYPE    (ESP_PANEL_BUS_TYPE_I2C)
/* 触摸面板总线参数 */
#if ESP_PANEL_TOUCH_BUS_TYPE == ESP_PANEL_BUS_TYPE_I2C
...
#endif /* ESP_PANEL_TOUCH_BUS_TYPE */
...
#endif /* ESP_PANEL_USE_TOUCH */
...
#define ESP_PANEL_USE_BACKLIGHT     (1)         // 0/1
#if ESP_PANEL_USE_BACKLIGHT
...
#endif /* ESP_PANEL_USE_BACKLIGHT */
...
#endif /* ESP_PANEL_USE_CUSTOM_BOARD */
```

## 使用示例

你可以在 Arduino IDE 中通过 `文件` > `示例` > `ESP32_Display_Panel` 访问这些示例。如果找不到 `ESP32_Display_Panel` 选项，请检查库是否已正确安装，并确认已选择一块 ESP 开发板。

!!! note

    在我们的 GitHub 上可以找到实用的使用示例，涵盖 Arduino 与 ESP-IDF 两种框架、GUI 应用以及各类外设驱动。

### 触摸

以下示例演示了如何使用独立驱动来开发不同接口和型号的触摸屏，并通过打印触摸点坐标进行测试：

* [I2C](https://github.com/esp-arduino-libs/ESP32_Display_Panel/tree/master/examples/arduino/drivers/touch/touch_i2c)
* [SPI](https://github.com/esp-arduino-libs/ESP32_Display_Panel/tree/master/examples/arduino/drivers/touch/touch_spi)

<!-- ### 面板

以下示例演示了如何使用 `ESP_Panel` 驱动来开发内置或自定义开发板：

* [Panel Test](../examples/Panel/PanelTest/)：该示例通过显示彩条并打印触摸点坐标进行测试。 -->

### LVGL v8

关于配置 LVGL（v8.3.x），请参阅 [LVGL 配置](./LVGL-Configuration-and-SquareLine-Project-Porting.md#configuring-lvgl) 获取更详细的信息。

* [Porting](https://github.com/esp-arduino-libs/ESP32_Display_Panel/tree/master/examples/arduino/gui/lvgl_v8/simple_port/)：该示例演示了如何移植 LVGL（v8.3.x）。对于 RGB LCD，它还可以启用防撕裂功能。
* [Rotation](https://github.com/esp-arduino-libs/ESP32_Display_Panel/tree/master/examples/arduino/gui/lvgl_v8/simple_rotation/)：该示例演示了如何使用 LVGL 旋转显示画面。

!!! warning

    目前防撕裂特性仅支持 RGB LCD，且要求 LVGL 版本 >= v8.3.9。如果你使用的是其他类型的 LCD，或 LVGL 版本不满足要求，请不要启用该特性。

### SquareLine

- [Porting](https://github.com/esp-arduino-libs/ESP32_Display_Panel/tree/master/examples/arduino/gui/lvgl_v8/squareline_port/)：该示例演示了如何移植 SquareLine 工程。
- [WiFiClock](https://github.com/esp-arduino-libs/ESP32_Display_Panel/tree/master/examples/arduino/gui/lvgl_v8/squareline_wifi_clock/)：该示例实现了一个简单的 Wi-Fi 时钟，并可以显示天气信息。

## PlatformIO

- [PlatformIO](https://github.com/esp-arduino-libs/ESP32_Display_Panel/tree/master/examples/platformio/lvgl_v8_port/)：该示例演示了如何在 PlatformIO 中使用 ESP32_Display_Panel。默认情况下，它适用于 **ESP32-S3-LCD-EV-Board** 和 **ESP32-S3-LCD-EV-Board-2** 开发板。用户需要根据实际情况修改 [boards/BOARD_CUSTOM.json](https://github.com/esp-arduino-libs/ESP32_Display_Panel/blob/master/examples/platformio/lvgl_v8_port/boards/BOARD_CUSTOM.json) 文件。


!!! info "没找到需要的内容？"
    如需更多使用示例，请观看视频或联系我们：
    
    [ :simple-youtube: 视频教程](https://youtube.com/playlist?list=PLM2TqiCfQM467LPRFVgJkHRajdR-wuVb8&si=fVDSm13eE9w-JkoH){ .md-button }
    [联系技术支持](mailto:support@chinasunyee.com){ .md-button }
