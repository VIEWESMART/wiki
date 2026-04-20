
# Arduino Tutrorial

!!! success "Officially Supported by Espressif Arduino"
    [VIEWE ESP32 Series](https://viewedisplay.com/iot_aiot-smart-display/): Officially Supported by [Espressif ESP32 Arduino](https://github.com/esp-arduino-libs/ESP32_Display_Panel/blob/master/docs/board/board_viewe.md).      
    One-click core & driver installation, no pin configuration needed, ready to develop in Arduino IDE.  

## Dependencies and Versions

| **Dependency** | **Version** |
| -------------- | ----------- |
| [arduino-esp32](https://github.com/espressif/arduino-esp32) | >= v3.0.0-alpha3 |
| [ESP32_IO_Expander](https://github.com/esp-arduino-libs/ESP32_IO_Expander) | >= 0.1.0 && < 0.2.0 |
| [ESP32_Display_Panel](https://github.com/esp-arduino-libs/ESP32_Display_Panel)| > 0.2.1 |

## Installing arduino-esp32
For installation of the esp32 in the Arduino IDE, refer to [How_To_Configure_Arduino](./How_To_Configure_Arduino.md/#-1-download--install).

## Installing the Library

For installation of the ESP32_Display_Panel library, refer to [How to Install ESP32_Display_Panel in Arduino IDE](../../FAQ-Arduino-ESP32.md/#how-to-install-esp32_display_panel-in-arduino-ide).

## Configuration of tools options
For configuration of `tools` options, refer to [recommended configurations in the Arduino IDE](./Board_Instructions.md#recommended-configurations-in-the-arduino-ide).


## Configuration Instructions

Below are detailed instructions on how to configure ESP32_Display_Panel, mainly including [Configuring Drivers](#configuring-drivers), [Using Supported Development Boards](#using-supported-development-boards), and [Using Custom Development Boards](#using-custom-development-boards). These are all optional operations and are configured through specified header files. Users can choose to use them according to their needs, with the following characteristics:

1. The path sequence for ESP32_Display_Panel to search for configuration files is: `Current Project Directory` > `Arduino Library Directory` > `ESP32_Display_Panel Directory`.
2. All examples in ESP32_Display_Panel include their required configuration files by default, which users can directly modify macro definitions.
3. For projects without configuration files, users can copy them from the root directory or examples of ESP32_Display_Panel to their own projects.
4. If multiple projects need to use the same configuration, users can place the configuration files in the [Arduino Library Directory](../../FAQ-Arduino-ESP32.md/#where-is-the-directory-for-arduino-libraries), so that all projects can share the same configuration.

!!! warning

    * The same directory can simultaneously contain both `ESP_Panel_Board_Supported.h` and `ESP_Panel_Board_Custom.h` configuration files, but they cannot be enabled at the same time, meaning `ESP_PANEL_USE_SUPPORTED_BOARD` and `ESP_PANEL_USE_CUSTOM_BOARD` can only have one set to `1`.
    * If neither of the above two configuration files is enabled, users cannot use the `ESP_Panel` driver and can only use other standalone device drivers, such as `ESP_PanelBus`, `ESP_PanelLcd`, etc.
    * Since the configurations within these files might change, such as adding, deleting, or renaming, to ensure the compatibility of the program, the library manages the versions of these files independently and checks whether the configuration files currently used by the user are compatible with the library during compilation. Detailed version information and checking rules can be found at the end of the file.


### Configuring Drivers

ESP32_Display_Panel configures driver functionality and parameters based on the `ESP_Panel_Conf.h` file. Users can update the behavior or default parameters of the driver by modifying macro definitions in this file. For example, to enable debug log output, here is a snippet of the modified `ESP_Panel_Conf.h` file:

```c
...
/* Set to 1 if print log message for debug */
#define ESP_PANEL_ENABLE_LOG                (1)         // 0/1
...
```

### Using Supported Development Boards

ESP32_Display_Panel configures `ESP_Panel` as the driver for the target development board based on the `ESP_Panel_Board_Supported.h` file. Users can select supported development boards by modifying macro definitions in this file. For example, to use the *ESP32-S3-BOX-3* development board, follow these steps:

1. Set the `ESP_PANEL_USE_SUPPORTED_BOARD` macro definition in the `ESP_Panel_Board_Supported.h` file to `1`.
2. Uncomment the corresponding macro definition for the target development board model.

Here is a snippet of the modified `ESP_Panel_Board_Supported.h` file:

```c
...
/* Set to 1 if using a supported board */
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

### Using Custom Development Boards

ESP32_Display_Panel configures `ESP_Panel` as the driver for custom development boards based on the `ESP_Panel_Board_Custom.h` file. Users need to modify this file according to the actual parameters of the custom development board. For example, to use a custom development board with a *480x480 RGB ST7701 LCD + I2C GT911 Touch*, follow these steps:

1. Set the `ESP_PANEL_USE_CUSTOM_BOARD` macro definition in the `ESP_Panel_Board_Custom.h` file to `1`.
2. Set the LCD-related macro definitions:   
   a. Set `ESP_PANEL_USE_LCD` to `1`.  
   b. Set `ESP_PANEL_LCD_WIDTH` and `ESP_PANEL_LCD_HEIGHT` to `480`.   
   c. Set `ESP_PANEL_LCD_BUS_TYPE` to `ESP_PANEL_BUS_TYPE_RGB`.    
   d. Set LCD signal pins and other parameters below `ESP_PANEL_LCD_BUS_TYPE == ESP_PANEL_BUS_TYPE_RGB`.    
   e. Uncomment and modify the `ESP_PANEL_LCD_VENDOR_INIT_CMD` macro definition according to the initialization command parameters provided by the screen vendor.   
   f. Modify other LCD configurations as needed.     
3. Set the Touch-related macro definitions:
   a. Set `ESP_PANEL_USE_TOUCH` to `1`.    
   b. Set Touch signal pins and other parameters below `ESP_PANEL_TOUCH_BUS_TYPE == ESP_PANEL_BUS_TYPE_I2C`.    
   c. Modify other Touch configurations as needed.     
4. Enable other driver macro definitions as needed, such as `ESP_PANEL_USE_BACKLIGHT`, `ESP_PANEL_USE_EXPANDER`, etc.    

Here is a snippet of the modified `ESP_Panel_Board_Custom.h` file:

```c
...
/* Set to 1 if using a custom board */
#define ESP_PANEL_USE_CUSTOM_BOARD  (1)         // 0/1

/* Set to 1 when using an LCD panel */
#define ESP_PANEL_USE_LCD           (1)     // 0/1

#if ESP_PANEL_USE_LCD
/**
 * LCD Controller Name
 */
#define ESP_PANEL_LCD_NAME          ST7701

/* LCD resolution in pixels */
#define ESP_PANEL_LCD_WIDTH         (480)
#define ESP_PANEL_LCD_HEIGHT        (480)
...
/**
 * LCD Bus Type.
 */
#define ESP_PANEL_LCD_BUS_TYPE      (ESP_PANEL_BUS_TYPE_RGB)
/**
 * LCD Bus Parameters.
 *
 * Please refer to https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-reference/peripherals/lcd.html and
 * https://docs.espressif.com/projects/esp-iot-solution/en/latest/display/lcd/index.html for more details.
 *
 */
#if ESP_PANEL_LCD_BUS_TYPE == ESP_PANEL_BUS_TYPE_RGB
...
#endif /* ESP_PANEL_LCD_BUS_TYPE */
...
/**
 * LCD Vendor Initialization Commands.
 *
 * Vendor specific initialization can be different between manufacturers, should consult the LCD supplier for
 * initialization sequence code. Please uncomment and change the following macro definitions. Otherwise, the LCD driver
 * will use the default initialization sequence code.
 *
 * There are two formats for the sequence code:
 *   1. Raw data: {command, (uint8_t []){ data0, data1, ... }, data_size, delay_ms}
 *   2. Formatter: ESP_PANEL_LCD_CMD_WITH_8BIT_PARAM(delay_ms, command, { data0, data1, ... }) and
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

/* Set to 1 when using a touch panel */
#define ESP_PANEL_USE_TOUCH         (1)         // 0/1
#if ESP_PANEL_USE_TOUCH
/**
 * Touch controller name
 */
#define ESP_PANEL_TOUCH_NAME        GT911
...
/**
 * Touch panel bus type
 */
#define ESP_PANEL_TOUCH_BUS_TYPE    (ESP_PANEL_BUS_TYPE_I2C)
/* Touch panel bus parameters */
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

## Usage Examples

You can access them in the Arduino IDE by navigating to `File` > `Examples` > `ESP32_Display_Panel`. If you cannot find the `ESP32_Display_Panel` option, please check if the library has been installed correctly and ensure that an ESP development board is selected.

!!! note

    Find practical usage examples on our GitHub, covering both Arduino and ESP-IDF frameworks, GUI applications and various peripheral drivers.

### Touch

The following example demonstrates how to develop touch screens of different interfaces and models using standalone drivers and test them by printing touch point coordinates:

* [I2C](https://github.com/VIEWESMART)
* [SPI](https://github.com/VIEWESMART)

### Panel

The following example demonstrates how to develop built-in or custom development boards using the `ESP_Panel` driver:

* [Panel Test](../examples/Panel/PanelTest/): This example tests by displaying color bars and printing touch point coordinates.

### LVGL v8

For configuring LVGL (v8.3.x), please refer to [here](#configuring-lvgl) for more detailed information.

* [Porting](../examples/LVGL/v8/Porting/): This example demonstrates how to port LVGL (v8.3.x). And for RGB LCD, it can enable the avoid tearing function.
* [Rotation](../examples/LVGL/v8/Rotation/): This example demonstrates how to use LVGL to rotate the display.

!!! warning

    Currently, the anti-tearing feature is only supported for RGB LCD and requires LVGL version >= v8.3.9. If you are using a different type of LCD or an LVGL version that does not meet the requirements, please do not enable this feature.

### SquareLine

To port the SquareLine project (v1.3.x), please refer to [here](#porting-squareline-project) for more detailed information.

- [Porting](../examples/SquareLine/v8/Porting/): This example demonstrates how to port the SquareLine project.
- [WiFiClock](../examples/SquareLine/v8/WiFiClock/): This example implements a simple Wi-Fi clock and can display weather information.

## PlatformIO

- [PlatformIO](../examples/PlatformIO/): This example demonstrates how to use ESP32_Display_Panel in PlatformIO. By default, it is suitable for the **ESP32-S3-LCD-EV-Board** and **ESP32-S3-LCD-EV-Board-2** development boards. Users need to modify the [boards/ESP-LCD.json](../examples/PlatformIO/boards/ESP-LCD.json) file according to the actual situation.


!!! info "Can't find what you need?"
    If you need more usage examples, please watch video or contact us:
    
    [ :simple-youtube: Video Tutorial](https://youtube.com/playlist?list=PLM2TqiCfQM467LPRFVgJkHRajdR-wuVb8&si=fVDSm13eE9w-JkoH){ .md-button }
    [Contact Support](mailto:support@viewedisplay.com){ .md-button }
