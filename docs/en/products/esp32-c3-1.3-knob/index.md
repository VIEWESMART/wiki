---
title: VIEWE ESP32 1.3 Inch Round IPS TFT Knob 
description: ESP32-C3 based 1.3-inch knob display with 240X240 resolution, IPS TFT screen, rotary encoder.
---

# ESP32 1.3 Inch Round IPS TFT Knob 

<div class="grid cards" markdown>

-   **UEDX24240013-MD50E**
    ---
    Powered by a robust ESP32 C3 microcontroller with built-in Wi-Fi and Bluetooth, it seamlessly integrates a vibrant 240X240 circular TFT touchscreen with a highly precise tactile rotary encoder. Natively supporting Arduino and LVGL, it enables developers to rapidly build smooth, multi-modal user interfaces. This turnkey solution is ideal for smart thermostats, industrial dashboards, high-end appliances and AIOT application.

    [:material-arrow-left: Back to Series](../esp32/){ .md-button }
    [:material-cart: Official Store](https://viewedisplay.com/product/esp32-1-28-inch-240x240-round-tft-knob-display-gc9a01-arduino-lvgl/){ .md-button .md-button--primary }
    [:material-github: GitHub Repo](https://github.com/VIEWESMART/UEDX24240013-MD50ESP32_1.3inch-Knob){ .md-button }

</div>

<div align="center">
    <img src="../../../assets/images/UEDX24240013-MD50E/1.3-inch tft Knob Display.png" alt="1.3-inch tft Knob Display" style="max-width: 90%; height: auto;">
</div>

## 📖 Introduction

The **UEDX24240013-MD50E** is a compact smart display module designed for knob‑style HMI applications. It combines a 1.3‑inch IPS display (240x240 pixels) with a rotary encoder and a hardware button. Powered by the **ESP32‑C3** (4 MB Flash), it provides Wi‑Fi and Bluetooth 5 (LE) connectivity, and supports development with **Arduino**, **ESP‑IDF** and **PlatformIO**.

## 🧩 Module Specifications

### 1. MCU

- **Chip:** ESP32-C3
- **FLASH:** 4M
- For more details, please visit [Espressif ESP32-C3 Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-c3_datasheet_en.pdf)

### 2. Screen

- **Size:** 1.3-inch IPS screen
- **Resolution:** 240x240px
- **Screen Type:** IPS
- **Driver Chip:** GC9A01
- **Compatibility Library:** ESP32_Display_Panel
- **Bus Communication Protocol:** 4 Wire SPI

### 3. Touch

- **Chip:** No touch

---

## Pin Overview

### IPS Screen Pin

| IPS Screen Pin | ESP32C3 Pin |
| :------------- | :---------- |
| SPI-CS         | IO10        |
| SPI-SCK        | IO1         |
| SPI-SDA        | IO0         |
| SPI-DC         | IO4         |
| LCD-TE         | IO5         |
| BACKLIGHT      | IO8         |

### Button Pin

| Button Pin | ESP32C3 Pin |
| :--------- | :---------- |
| BOOT       | IO9         |

### Encoder Pin

| Encoder Pin | ESP32C3 Pin |
| :---------- | :---------- |
| PHA         | IO7         |
| PHB         | IO6         |

### USB Pin

| USB Pin | ESP32C3 Pin |
| :------ | :---------- |
| USB-DN  | IO18        |
| USB-DP  | IO19        |

### UART Pin

| UART Pin   | ESP32C3 Pin |
| :--------- | :---------- |
| UART0 RXD  | IO20        |
| UART0 TXD  | IO21        |

---

## 🧩 Interface FPC PIN Defnition

| FPC Number | Adapter Pin | ESP32C3 Pin      |
| :--------- | :---------- | :--------------- |
| 1          | 5V          | 5V               |
| 2          | PB7         | GPIO3            |
| 3          | GND         | GND              |
| 4          | RX2         | NC               |
| 5          | TX2         | NC               |
| 6          | RX1         | UART0 RXD / IO20 |
| 7          | TX1         | UART0 TXD / IO21 |
| 8          | NC          | CHIP-EN          |
| 9          | SK & D+     | USB-DP / IO19    |
| 10         | SD & D-     | USB-DN / IO18    |

---

## 🚀 Quick Start

### Software Framework Configuration

| Support IDE     | Version           |
| :-------------- | :---------------- |
| ESP-IDF         | V5.1 / 5.2 / 5.3  |
| Arduino IDE     | esp32 >= v3.1.0   |
| PlatformIO IDE  | -                 |

### ESP-IDF Framework

[Novice Tutorial]()

- **Supported Versions:** v5.1 / 5.2 / 5.3
- Download the example code from the repository and compile/run it directly.
- **Repository Address:** [examples](examples/esp_idf)

### Arduino Framework

[Novice Tutorial](https://github.com/VIEWESMART/VIEWE-Tutorial/blob/main/Arduino%20Tutorial/Arduino%20Getting%20Started%20Tutorial.md)

#### 1. Install Arduino

Choose installation based on your system type: [Download Arduino](https://www.arduino.cc/en/software)  
Newcomers please refer to the [Beginner's Tutorial](https://github.com/VIEWESMART/VIEWE-Tutorial/blob/main/Arduino%20Tutorial/Arduino%20Getting%20Started%20Tutorial.md).

#### 2. Install ESP32 SDK

1. Open Arduino IDE
2. Go to `File` > `Preferences`
3. Add to `Additional boards manager URLs`:
   ```text
   https://espressif.github.io/arduino-esp32/package_esp32_index.json
   ```
4. Navigate to `Tools` > `Board` > `Boards Manager`
5. Search for `esp32` by `Espressif Systems`
6. Select `3.1.0` and above, click the `INSTALL` button

#### 3. Install Required Libraries

| ID | Library                                                                                   | Version                      |
| :-- | :---------------------------------------------------------------------------------------- | :--------------------------- |
| 1  | [ESP32_Display_Panel](https://github.com/esp-arduino-libs/ESP32_Display_Panel)            | Latest version recommended   |
| 2  | [ESP32_Button](https://github.com/esp-arduino-libs/ESP32_Button)                          | Latest version recommended   |
| 3  | [ESP32_Knob](https://github.com/esp-arduino-libs/ESP32_Knob)                              | Latest version recommended   |
| 4  | [lvgl-8.4.0](https://lvgl.io)                                                             | 8.4.0 (V9 not supported yet) |

**Online Installation:**

`ESP32_Display_Panel` and its dependencies are available in Arduino Library Manager:

1. In Arduino IDE, go to `Sketch` > `Include Library` > `Manage Libraries...`
2. Search for `ESP32_Display_Panel`, select `1.0.3` and above, click `Install`
3. When prompted to install dependencies, click `INSTALL ALL`
4. (Optional) Install `LVGL` library, recommended version `8.4.0`

**Manual Installation:**

Download the required version's `.zip` file from [GitHub](https://github.com/esp-arduino-libs/ESP32_Display_Panel) or [Arduino Library](https://www.arduinolibraries.info/libraries/esp32_display_panel), then in Arduino IDE navigate to `Sketch` > `Include Library` > `Add .ZIP Library...`, select the downloaded `.zip` file and click `Open`.

!!! note
    LVGL is only required for GUI examples.

#### 4. Select and Configure Board

Navigate to `Tools` > `Board` > `esp32` > `ESP32C3 Dev Module`

#### 5. Open Example

Navigate to `File` > `Examples` > `ESP32_Display_Panel` > `Arduino` > `gui` > `lvgl_v8` > `simple_port`

#### 6. Modify Code

Modify macro definitions in `esp_panel_board_supported_conf.h` to enable target board:

1. Enable file macro definition:
   ```c
   // Change from:
   #define ESP_PANEL_BOARD_DEFAULT_USE_SUPPORTED       (0)
   // To:
   #define ESP_PANEL_BOARD_DEFAULT_USE_SUPPORTED       (1)
   ```

2. Uncomment the corresponding board:
   ```c
   // Change from:
   // #define BOARD_VIEWE_UEDX24240013-MD50E
   // To:
   #define BOARD_VIEWE_UEDX24240013_MD50E
   ```

Example of modified `esp_panel_board_supported_conf.h`:

```c
/**
 * @brief Flag to enable supported board configuration (0/1)
 *
 * Set to `1` to enable supported board configuration, `0` to disable
 */
#define ESP_PANEL_BOARD_DEFAULT_USE_SUPPORTED       (1)

// #define BOARD_VIEWE_SMARTRING
#define BOARD_VIEWE_UEDX24240013_MD50E
// #define BOARD_VIEWE_UEDX24320024E_WB_A
// #define BOARD_VIEWE_UEDX24320028E_WB_A
// #define BOARD_VIEWE_UEDX24320035E_WB_A
// #define BOARD_VIEWE_UEDX32480035E_WB_A
// #define BOARD_VIEWE_UEDX46460015_MD50ET
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
```

!!! warning
    Do not enable both `ESP_PANEL_BOARD_DEFAULT_USE_SUPPORTED` and `ESP_PANEL_BOARD_DEFAULT_USE_CUSTOM`.  
    You cannot enable multiple boards simultaneously.

#### 7. Configure Tool Options (ESP32-C3)

| Setting                            | Value                |
| :--------------------------------- | :------------------- |
| Board                              | ESP32C3 Dev Module   |
| CPU Frequency                      | 160MHz (WiFi)        |
| Core Debug Level                   | None                 |
| USB CDC On Boot                    | Disabled             |
| Erase All Flash Before Sketch Upload | Disabled           |
| Flash Frequency                    | 80MHz                |
| Flash Mode                         | QIO                  |
| Flash Size                         | 4MB (32Mb)           |
| JTAG Adapter                       | Disabled             |
| Partition Scheme                   | Custom               |
| Upload Speed                       | 921600               |

#### 8. Compile and Upload

1. Select the correct port
2. Click **"√"** in the upper right corner to compile
3. If compilation succeeds, connect the microcontroller to the computer
4. Click **"→"** in the upper right corner to download

!!! note "LVGL Color Swap Settings"
    `SPI` and `QSPI` screens need to set the macro `LV_COLOR_16_SWAP` to `1` in `lv_conf.h`.  
    `RGB` screens should set it to `0`.

    ```c
    /**
     * @file lv_conf.h
     * Configuration file for v8.4.0
     */

    /* clang-format off */
    #if 1 /*Set it to "1" to enable content*/

    #ifndef LV_CONF_H
    #define LV_CONF_H

    #include 

    /*====================
       COLOR SETTINGS
     *====================*/

    /*Color depth: 1 (1 byte per pixel), 8 (RGB332), 16 (RGB565), 32 (ARGB8888)*/
    #define LV_COLOR_DEPTH 16

    /*Swap the 2 bytes of RGB565 color. Useful if the display has an 8-bit interface (e.g. SPI)*/
    #define LV_COLOR_16_SWAP 1
    ...
    ```

### Firmware Download

| Firmware  | Description | Picture |
| :-------- | :---------- | :------ |
| ESP-IDF   | Original    |         |

1. Open the project file `tools` and locate the ESP32 burning tool. Open it.
2. Select the correct burning chip and burning method, then click "OK".
3. Follow steps **1 → 2 → 3 → 4 → 5** to burn the program.
4. If burning fails, press and hold the **BOOT-0** button and retry.

Burn files are located in the project root directory under `[firmware](./firmware/)`. Refer to the firmware version description inside to choose the appropriate version.

---

## 📎 Resource & Datasheets

| Document | Link |
| :------- | :--- |
| Product Specification | [UEDX24240013-MD50E.PDF](../../../assets/datasheet/UEDX24240013-MD50E.pdf) |
| 2D Drawing(DWG) | [UEDX24240013-MD50E-2D.DWG](../../../assets/dimension/UEDX24240013-MD50E-2D.dwg) |
| ESP32-C3 (EN) | [Datasheet English](../../../assets/datasheet/chip/esp32-c3_datasheet_en.pdf) |
| ESP32-C3 (CN) | [Datasheet Chinese](../../../assets/datasheet/chip/esp32-c3_datasheet_cn.pdf) | 
| Schematic Diagram| [SCH-UEDX24240013-MD50E.pdf](../../../assets/schematic/SCH-UEDX24240013-MD50E.pdf) |   


## 🛠️ Tools

* **[Flash Download Tool](../../../assets/software/flash_download_tool.zip)** – Utility for manual firmware flashing.
* **[LVGL Image Converter](https://lvgl.io/tools/imageconverter)** – Convert images to C arrays for LVGL.

> [!IMPORTANT]
> For more resources, please explore the [**Resource Center**](../../support/resource.md).

## ❓ FAQ

??? question "After reading the above tutorials, I still don't know how to build a programming environment. What should I do?"
    If you still don't understand how to build an environment after reading the above tutorials, you can refer to the [VIEWE-FAQ]() document instructions to build it.

??? question "Why does Arduino IDE prompt me to update library files when I open it? Should I update them or not?"
    Choose **not** to update library files. Different versions of library files may not be mutually compatible, so it is not recommended to update library files.

??? question "Why is there no serial data output on the 'Uart' interface on my board? Is it defective and unusable?"
    The default project configuration uses the USB interface as Uart0 serial output for debugging purposes. The "Uart" interface is connected to Uart0, so it won't output any data without configuration.

    - **PlatformIO users:** Open `platformio.ini` and modify `-D ARDUINO_USB_CDC_ON_BOOT=true` to `-D ARDUINO_USB_CDC_ON_BOOT=false` under `build_flags = xxx`.
    - **Arduino users:** Open the `Tools` menu and select `USB CDC On Boot: Disabled` to enable the external "Uart" interface.

??? question "Why is my board continuously failing to download the program?"
    Please hold down the **BOOT** button and try downloading the program again.

---

!!! info "Can't find what you need?"    
    If you need more products, resources or support, please contact our team:  

    [**:material-archive-arrow-down: Resource Center**](../../support/resource.md){ .md-button .md-button--primary } 
    [**:material-magnify: More Products**](../esp32/index.md){ .md-button }
    [**:material-email: Contact Support**](mailto:support@viewedisplay.com){ .md-button }
