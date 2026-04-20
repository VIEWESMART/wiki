# LVGL Configuration and SquareLine Project Porting

!!! success "Officially Supported by Espressif Arduino"
    [VIEWE ESP32 Smart Display Dev Board](https://viewedisplay.com/iot_aiot-smart-display/): Officially Supported by [Espressif ESP32 Arduino](https://github.com/esp-arduino-libs/ESP32_Display_Panel/blob/master/docs/board/board_viewe.md).      
    One-click core & driver installation, no pin configuration needed, ready to develop in Arduino IDE.  

## Configuring LVGL

The functionality and parameters of LVGL can be configured by editing the `lv_conf.h` file, where users can modify macro definitions to update the behavior or default parameters of the driver. Here are some features for configuring LVGL:

1. When using arduino-esp32 v3.x.x version, LVGL will search for the configuration file in the following order: `current project directory` > `Arduino library directory`. If the configuration file is not found, a compilation error indicating the absence of the configuration file will be prompted. Therefore, users need to ensure that at least one directory contains the `lv_conf.h` file.

2. If multiple projects need to use the same configuration, users can place the configuration file in the [Arduino library directory](./FAQ.md#where-is-the-directory-for-arduino-libraries), so that all projects can share the same configuration.

Below are detailed steps for sharing the same LVGL configuration:

1. Navigate to the [Arduino library directory](./FAQ.md#where-is-the-directory-for-arduino-libraries).

2. Enter the `lvgl` folder, copy the `lv_conf_template.h` file, and place the copy at the same level as the `lvgl` folder. Then, rename the copied file to `lv_conf.h`.

3. Finally, the layout of the Arduino library folder should look like this:

   ```
   Arduino
       |-libraries
           |-lv_conf.h
           |-lvgl
           |-other_lib_1
           |-other_lib_2
   ```

4. Open the `lv_conf.h` file, and change the first `#if 0` to `#if 1` to enable the contents of the file.

5. Set other configurations according to requirements. Here are some examples of common configuration options for LVGL v8:

   ```c
   #define LV_COLOR_DEPTH          16  // Typically use 16-bit color depth (RGB565),
                                       // but can also set it to `32` to support 24-bit color depth (RGB888)
   #define LV_COLOR_16_SWAP        0   // If using SPI/QSPI LCD (e.g., ESP32-C3-LCDkit), set this to `1`
   #define LV_COLOR_SCREEN_TRANSP  1
   #define LV_MEM_CUSTOM           1
   #define LV_MEMCPY_MEMSET_STD    1
   #define LV_TICK_CUSTOM          1
   #define LV_ATTRIBUTE_FAST_MEM   IRAM_ATTR
                                      // Get higher performance but use more SRAM
   #define LV_FONT_MONTSERRAT_N    1  // Enable all internal fonts needed (`N` should be replaced with font size)
   ```

6. For more information, please refer to the [LVGL official documentation](https://docs.lvgl.io/8.3/get-started/platforms/arduino.html).

## Porting SquareLine Project

SquareLine Studio (v1.3.x) allows for the rapid design of beautiful UIs through visual editing. If you want to use UI source files exported from SquareLine in the Arduino IDE, you can follow these steps for porting:

1. First, create a new project in SquareLine Studio. Go to `Create` -> `Arduino`, select `Arduino with TFT-eSPI` as the project template, then configure the LCD properties for the target development board in the `PROJECT SETTINGS` section, such as `Resolution` and `Color depth`. Finally, click the `Create` button to create the project.

2. For existing projects, you can also click on `File` -> `Project Settings` in the navigation bar to enter the project settings. Then, in the `BOARD PROPERTIES` section, configure `Board Group` as `Arduino` and `Board` as `Arduino with TFT-eSPI`. Additionally, configure the LCD properties for the target development board in the `DISPLAY PROPERTIES` section. Finally, click the `Save` button to save the project settings.

3. Once the UI design is complete and the export path is configured, click on `Export` -> `Create Template Project` and `Export UI Files` buttons in the menu bar to export the project and UI source files. The layout of the project directory will be as follows:

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

4. Copy the `lv_conf.h`, `lvgl`, and `ui` folders from the `libraries` folder in the project directory to the Arduino library directory. If you need to use a locally installed `lvgl`, skip copying `lvgl` and `lv_conf.h`, then refer to the steps in the [LVGL Configuration](#configuring-lvgl) section to configure LVGL. The layout of the Arduino library folder will be as follows:

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



!!! info "Can't find what you need?"
    If you need more support, please watch the video or contact us:
    
    [ :simple-youtube: Video Tutorial](../../tutorials.md/#video-lvgl-gui){ .md-button }
    [Contact Support](mailto:support@viewedisplay.com){ .md-button }