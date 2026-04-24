---
title: ESP32 1.5 Inch AMOLED Touch Knob Display
description: ESP32-S3 based 1.5-inch touch knob display with 466x466 resolution
---

# ESP32 1.5 Inch AMOLED Touch Knob Display

<div class="grid cards" markdown>

-   **ESP32-P4-Pi-VIEWE**
    ---
    development board is designed based on the VIEWE [ESP32-P4-Core](../esp32-p4-core/) module, which integrates **ESP32-P4** and **ESP32-C6** dual chips and supports Wi-Fi 6 and Bluetooth 5 wireless connections with **“Raspberry Pi” form factor**. 

    [:material-arrow-left: Back to Series](../embedded/index.md){ .md-button }
    [:material-cart: Official Store](https://viewedisplay.com/product/esp32-p4-pi-dev-board-wifi6/){ .md-button .md-button--primary }
    [:material-github: GitHub Repo](https://github.com/VIEWESMART/ESP32-P4-Pi){ .md-button }

</div>

<div align="center">
    <img src="image/1.5.jpg" alt="1.5-inch Touch Knob Display" style="max-width: 90%; height: auto;">
</div>


## Module

### 1. MCU

* **Chip**: ESP32-S3-R8
* **PSRAM**: 8M (Octal SPI)
* **FLASH**: 16M
* For more details, please visit [Espressif ESP32-S3 Datasheet](https://www.espressif.com.cn/sites/default/files/documentation/esp32-s3_datasheet_en.pdf)

### 2. Screen

* **Size**: 1.5-inch IPS screen
* **Resolution**: 466x466px
* **Screen type**: IPS
* **Driver chip**: CO5300AF-42
* **Compatibility library**: ESP32_Display_Panel
* **Bus communication protocol**: QSPI

### 3. Touch

* **Touch Chip**: CST820
* **Bus communication protocol**: I2C

## Pin Overview

### IPS Screen Pin Mapping

| IPS Screen Pin | ESP32S3 Pin |
|:--------------:|:-----------:|
| CS             | IO12        |
| PCLK           | IO10        |
| DATA0          | IO13        |
| DATA1          | IO11        |
| DATA2          | IO14        |
| DATA3          | IO9         |
| RST            | IO8         |
| BACKLIGHT      | IO17        |

### Touch Pin Mapping

| Touch Pin | ESP32S3 Pin |
|:---------:|:-----------:|
| SDA       | IO0         |
| SCL       | IO1         |
| RST       | IO3         |
| INT       | IO4         |

### Button Pin Mapping

| Button Pin | ESP32S3 Pin |
|:----------:|:-----------:|
| BOOT       | IO0         |

### Encoder Pin Mapping

| Encoder Pin | ESP32S3 Pin |
|:-----------:|:-----------:|
| PHA         | IO6         |
| PHB         | IO5         |

### USB/UART Pin Mapping

| USB/UART Pin | ESP32S3 Pin |
|:------------:|:-----------:|
| USB-DN       | IO19        |
| USB-DP       | IO20        |

## FPC PIN

| FPC Number | Adapter Pin      | ESP32S3 Pin       |
|:----------:|:----------------:|:-----------------:|
| 1          | 5V               | 5V                |
| 2          | PB7              | -                 |
| 3          | GND              | GND               |
| 4          | RX2              | GPIO40            |
| 5          | TX2              | GPIO39            |
| 6          | RX1              | UART0RXD/GPIO44   |
| 7          | TX1              | UART0TXD/GPIO43   |
| 8          | NC               | CHIP-EN           |
| 9          | SK & D+          | USB-DP/ GPIO20    |
| 10         | SD & D-          | USB-DN/ GPIO19    |

## Software

We provide comprehensive support for **Arduino**, **PlatformIO**, and **ESP-IDF** frameworks, with pre-ported **LVGL** examples.

### Software Examples

Examples are available in the [GitHub Repository](examples).

| Framework  | Example Path                | Description |
|:----------:|:---------------------------:|:-----------:|
| **Arduino**| `examples/arduino/gui/lvgl_v8` | **LVGL Benchmark**: Usage example of lvgl v8. It can also be directly opened in the Arduino IDE. |
| **ESP-IDF**| `examples/esp_idf`          | **LVGL port**: Example of porting and using LVGL in ESP-IDF |
| **PlatformIO**| `examples/platformio/lvgl_v8_port` | **LVGL v8 port**: Usage example of LVGL v8. |

### Getting Started

#### Preparation

* **Hardware**: BOARD_VIEWE_UEDX46460015_MD50ET Board, USB-C Cable
* **Software**: VS Code (ESP-IDF v5.3+) or Arduino IDE (v2.0+) or VS Code (PlatformIO)
* **Library**: The following libraries are needed for Arduino IDE and PlatformIO

| Libraries        | Version                | Description |
|:----------------:|:----------------------:|:-----------:|
| `ESP32_Display_Panel` | `1.0.3+`              | By Espressif, This is necessary to drive the screen |
| `ESP32_IO_Expander`   | `Arduino automatic selection` | The dependency library of `ESP32_Display_Panel` should be selected for installation together during the installation process |
| `esp-lib-utils`       | `Arduino automatic selection` | The dependency library of `ESP32_Display_Panel` should be selected for installation together during the installation process |
| `lvgl`              | `8.4.0`               | A free and open-source embedded graphics library |

#### ESP-IDF Setup

| Support IDE | Version |
|:-----------:|:-------:|
| `[ESP-IDF]` | `[V5.3/5.4/5.5]` |

1. **Open platformio example**
   - Go to GitHub to download the program. You can download the main branch by clicking on the "<> Code" with green text
   - Open the example using VS Code(ESP-IDF)

2. **Compile and upload**:
   - Click `build` in the upper right corner to compile
   - Connect the microcontroller to the computer. If the compilation is correct
   - Click `upload` in the upper right corner to download

#### Arduino Setup

1. **Install Arduino IDE**
   - Choose installation based on your system type
   - Newcomers please refer to the [beginner's tutorial](https://github.com/VIEWESMART/VIEWE-Tutorial/blob/main/Arduino%20Tutorial/Arduino%20Getting%20Started%20Tutorial.md)

2. **Install ESP32 Board Package**:
   - Open Arduino IDE
   - Go to `File` > `Preferences`
   - Add to `Additional boards manager URLs`:
     ```
     https://espressif.github.io/arduino-esp32/package_esp32_index.json
     ```
   - Go to `Tools` > `Board` > `Boards Manager`
   - Search `esp32` by Espressif and install version **3.0.0+**

3. **Install Libraries**:
   - Go to `Sketch` > `Include Library` > `Library Manager`
   - Search `ESP32_Display_Panel` by Espressif and install version **1.0.3+**. You will be prompted whether to install its dependencies, please click **INSTALL ALL** to install all
   - Install `lvgl` (v8.4.0 recommended)

4. **Open example**:
   - Navigate to `File` > `Examples` > `ESP32_Display_Panel`
   - Select `Arduino` > `gui` > `lvgl_v8` > `simple_port`

5. **Select Board**:
   - Target: `ESP32S3 Dev Module`
   - Settings:
     - **Flash Size**: 16MB (128Mb)
     - **Partition Scheme**: 16M Flash (3MB APP/9.9MB FATFS)
     - **PSRAM**: **OPI PSRAM** (Crucial!)

6. **Configure ESP supported panel board**:
   - Open the `esp_panel_board_supported_conf.h` file in the example
   - Enable this file: change the `ESP_PANEL_BOARD_DEFAULT_USE_SUPPORTED` macro definition to `1`
   - Ensure you uncomment: `#define BOARD_VIEWE_UEDX46460015_MD50ET`
     ```c
     ...
     /**
      * @brief Flag to enable supported board configuration (0/1)
      *
      * Set to `1` to enable supported board configuration, `0` to disable
      */
     #define ESP_PANEL_BOARD_DEFAULT_USE_SUPPORTED       (1)
     ...
     // #define BOARD_VIEWE_SMARTRING
     // #define BOARD_VIEWE_UEDX24240013_MD50E
     // #define BOARD_VIEWE_UEDX24320024E_WB_A
     // #define BOARD_VIEWE_UEDX24320028E_WB_A
     // #define BOARD_VIEWE_UEDX24320035E_WB_A
     // #define BOARD_VIEWE_UEDX32480035E_WB_A
     #define BOARD_VIEWE_UEDX46460015_MD50ET
     // #define BOARD_VIEWE_UEDX48270043E_WB_A
     // #define BOARD_VIEWE_UEDX48480021_MD80E_V2
     // #define BOARD_VIEWE_UEDX48480021_MD80E
     // #define BOARD_VIEWE_UEDX48480021_MD80ET
     // #define BOARD_VIEWE_UEDX48480028_MD80ET
     // #define BOARD_VIEWE_UEDX48480040E_WB_A
     // #define BOARD_VIEWE_UEDX80480043E_WB_A
     // #define BOARD_VIEWE_UEDX80480050E_AC_A
     // #define BOARD_VIEWE_UEDX80480050E_WB_A
     // #define BOARD_VIEWE_UEDX80480050E_WB_A_2
     // #define BOARD_VIEWE_UEDX80480070E_WB_A
     ...
     ```

7. **Configure the example**:
   - [Optional] Edit the macro definitions in the `lvgl_v8_port.h` file
     - **If using `RGB/MIPI-DSI` interface**, change the `LVGL_PORT_AVOID_TEARING_MODE` macro definition to `1`/`2`/`3` to enable the avoid tearing function. After that, change the `LVGL_PORT_ROTATION_DEGREE` macro definition to the target rotation degree
     - **If using other interfaces**, please don't modify the `LVGL_PORT_AVOID_TEARING_MODE` and `LVGL_PORT_ROTATION_DEGREE` macro definitions
   - [Optional] Edit the macro definitions in the `lv_conf.h` file
     - **If using `SPI/QSPI` interface**, change the `LV_COLOR_16_SWAP` macro definition to `1`

8. **Select the correct port**:
   - Connect to the device
   - Go to `Tools` > `Port`, Select the corresponding port

9. **Compile and upload**:
   - Click `√` in the upper right corner to compile
   - Connect the microcontroller to the computer. If the compilation is correct
   - Click `→` in the upper right corner to download

!!! tip "Configuration Tips"
    - In `esp_panel_board_supported_conf.h`, ensure you uncomment: `#define BOARD_VIEWE_UEDX46460015_MD50ET`
    - Do not enable both `ESP_PANEL_BOARD_DEFAULT_USE_SUPPORTED` and `ESP_PANEL_BOARD_DEFAULT_USE_CUSTOM`
    - You cannot enable multiple ESP supported panel boards at the same time

#### PlatformIO Setup

1. **Open platformio example**
   - Go to GitHub to download the program. You can download the main branch by clicking on the "<> Code" with green text
   - Open the example using VS Code(PlatformIO)

2. **Configure PlatformIO**:
   - This example uses the `BOARD_ESPRESSIF_ESP32_S3_LCD_EV_BOARD_2_V1_5` board as default. Choose `BOARD_VIEWE_UEDX46460015_MD50ET` in the `[platformio]:default_envs` of the `platformio.ini` file

3. **Configure the example**:
   - [Optional] Edit the macro definitions in the `lvgl_v8_port.h` file
     - **If using `RGB/MIPI-DSI` interface**, change the `LVGL_PORT_AVOID_TEARING_MODE` macro definition to `1`/`2`/`3` to enable the avoid tearing function. After that, change the `LVGL_PORT_ROTATION_DEGREE` macro definition to the target rotation degree
     - **If using other interfaces**, please don't modify the `LVGL_PORT_AVOID_TEARING_MODE` and `LVGL_PORT_ROTATION_DEGREE` macro definitions

4. **Compile and upload the project**
   - Click the `√` (Compile) button
   - Connect the board to your computer. If the compilation is correct
   - Click the `→` (upload) button

### Firmware Download

1. Open the project file "tools" and locate the ESP32 burning tool. Open it

2. Select the correct burning chip and burning method, then click "OK". As shown in the picture, follow steps 1->2->3->4->5 to burn the program. If the burning is not successful, press and hold the "BOOT-0" button and then download and burn again

3. Burn the file in the root directory of the project file "[firmware](./firmware/)" file. There is a description of the firmware file version inside, just choose the appropriate version to download

<div align="center">
    <img src="image/10.png" alt="Burning Tool Interface">
    <img src="image/11.png" alt="Burning Process">
</div>

## FAQ

### Q: After reading the above tutorials, I still don't know how to build a programming environment. What should I do?

**A:** If you still don't understand how to build an environment after reading the above tutorials, you can refer to the [VIEWE-FAQ]() document instructions to build it.

### Q: Why does Arduino IDE prompt me to update library files when I open it? Should I update them or not?

**A:** Choose not to update library files. Different versions of library files may not be mutually compatible, so it is not recommended to update library files.

### Q: Why is there no serial data output on the "Uart" interface on my board? Is it defective and unusable?

**A:** The default project configuration uses the USB interface as Uart0 serial output for debugging purposes. The "Uart" interface is connected to Uart0, so it won't output any data without configuration.

For PlatformIO users, please open the project file "platformio.ini" and modify the option under "build_flags = xxx" from "-D ARDUINO_USB_CDC_ON_BOOT=true" to "-D ARDUINO_USB_CDC_ON_BOOT=false" to enable external "Uart" interface.

For Arduino users, open the "Tools" menu and select "USB CDC On Boot: Disabled" to enable the external "Uart" interface.

### Q: Why is my board continuously failing to download the program?

**A:** Please hold down the "BOOT" button and try downloading the program again.

## Schematic

<div align="center">
    <img src="schematic/1.5%20MD50E%20SCH.V2.0_00.png" alt="Schematic Diagram" style="max-width: 100%; height: auto;">
</div>

## Information

- [Products Specification](information/UEDX48480021-MD80E%20V3.3%20SPEC.pdf)
- [Display Datasheet](information/UE021WV-RB40-L002B.pdf)
- [Button](information/6x6Silent%20switch.pdf)
- [Encoder](information/C219783_%E6%97%8B%E8%BD%AC%E7%BC%96%E7%A0%81%E5%99%A8_EC28A1520401_%E8%A7%84%E6%A0%BC%E4%B9%A6_WJ239718.PDF)

## Dependent Libraries

- [ESP32_Display_Panel > 0.2.1](https://github.com/esp-arduino-libs/ESP32_Display_Panel) (Please [download](./Libraries/ESP32_Display_Panel) the library first as the latest version has not been released yet)
- [ESP32_IO_Expander](https://github.com/esp-arduino-libs/ESP32_IO_Expander) (Please [download](./Libraries/ESP32_IO_Expander) the library first as the latest version has not been released yet)
- [ESP32_Button](https://github.com/esp-arduino-libs/ESP32_Button)
- [ESP32_Knob](https://github.com/esp-arduino-libs/ESP32_Knob)
- [lvgl-8.4.0](https://lvgl.io)


## 9. More Resource

!!! info "Can't find what you need?"    
    If you need more Support or Products or Resource, please contact our team: 

    [**:material-archive-arrow-down: Resource Center**](../../support/resource.md){ .md-button .md-button--primary } 
    [**:material-magnify: More Products**](../embedded/index.md){ .md-button  }
    [**:material-email: Contact Support**](mailto:support@viewedisplay.com){ .md-button }