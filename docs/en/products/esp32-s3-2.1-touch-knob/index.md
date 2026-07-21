---
title: VIEWE ESP32 2.1 Inch 480x480 Touch Knob TFT Display
description: ESP32-S3 based 2.1-inch touch knob display with 480x480 resolution, IPS TFT screen, capactive touch, rotary encoder.
---

# ESP32 2.1 Inch 480x480 TFT Touch Knob 

<div class="grid cards" markdown>

-   **UEDX48480021-MD80ET**
    ---
    Powered by a robust ESP32 S3 microcontroller with built-in Wi-Fi and Bluetooth, it seamlessly integrates a vibrant 480x480 circular TFT touchscreen with a highly precise tactile rotary encoder. Natively supporting Arduino and LVGL, it enables developers to rapidly build smooth, multi-modal user interfaces. This turnkey solution is ideal for smart thermostats, industrial dashboards, high-end appliances and AIOT application.

    [:material-arrow-left: Back to Series](../esp32/){ .md-button }
    [:material-cart: Official Store](https://viewedisplay.com/product/esp32-2-1-inch-480x480-round-tft-knob-touch-display-rotary-encoder-arduino-lvgl/){ .md-button .md-button--primary }
    [:material-github: GitHub Repo](https://github.com/VIEWESMART/UEDX48480021-MD80ESP32-2.1inch-Touch-Knob-Display){ .md-button }

</div>

<div align="center">
    <img src="../../../assets/images/UEDX48480021-MD80ET/Main.png" alt="2.1-inch Touch Knob Display" style="max-width: 90%; height: auto;">
</div>


---

## 📖 Introduction

The **UEDX48480021-MD80ET** is a compact smart display module designed for knob‑style HMI applications. It combines a 2.1‑inch IPS display (480×480 pixels) with a capacitive touch panel, a rotary encoder and a hardware button. Powered by the **ESP32‑S3‑R8** (16 MB Flash, 8 MB Octal PSRAM), it provides Wi‑Fi and Bluetooth 5 (LE) connectivity, and supports development with **Arduino**, **ESP‑IDF** and **PlatformIO**.

## 🧩 Module Specifications

### 1. MCU
- **Chip:** ESP32-S3-R8
- **PSRAM:** 8M (Octal SPI)
- **FLASH:** 16M
- **Datasheet:** [Espressif ESP32-S3 Datasheet](https://www.espressif.com.cn/sites/default/files/documentation/esp32-s3_datasheet_en.pdf)

### 2. Screen
- **Size:** 2.1-inch IPS screen
- **Resolution:** 480x480px
- **Driver Chip:** ST7701S
- **Compatibility Library:** ESP32_Display_Panel
- **Bus Protocol:** 3 Wire SPI-RGB 24bits

### 3. Touch
- **Touch Chip:** CST826
- **Bus Protocol:** IIC

## 🔌 Pin Overview

### IPS Screen & ESP32S3

| IPS Screen Pin | ESP32S3 Pin |
| :------------- | :---------- |
| DE             | IO17        |
| VSYNC          | IO3         |
| HSYNC          | IO46        |
| PCLK           | IO9         |
| DATA0 - DATA15 | IO10-IO48*  |
| SPI_CS         | IO18        |
| SPI_SCK        | IO13        |
| SPI_SDA        | IO12        |
| RST            | IO8         |
| BACKLIGHT      | IO7         |

> *Note: Data pins mapping: D0(IO10), D1(IO11), D2(IO12), D3(IO13), D4(IO14), D5(IO21), D6(IO47), D7(IO48), D8(IO45), D9(IO38), D10(IO39), D11(IO40), D12(IO41), D13(IO42), D14(IO2), D15(IO1)*

### Other Peripherals

| Component | Pin Name | ESP32S3 Pin |
| :-------- | :------- | :---------- |
| **Touch** | SCL      | IO15        |
|           | SDA      | IO16        |
| **Button**| BOOT     | IO0         |
|           | RESET    | CHIP_EN     |
| **Encoder**| PHA     | IO6         |
|           | PHB      | IO5         |
| **USB/UART**| USB-DN | IO19        |
|           | USB-DP   | IO20        |
|           | UART RX  | IO43        |
|           | UART TX  | IO44        |

## 🚀 Quick Start

### Examples Support

| Example                | Support IDE And Version   | Description                          |
| :--------------------- | :------------------------ | :----------------------------------- |
| [ESP-IDF](./examples/ESP-IDF)           | ESP-IDF V5.1 / 5.2 / 5.3  | IDF driver example code              |
| [SquareLinePorting](./examples/SquareLinePorting) | Arduino IDE (esp32_v2.0.14) | SquareLine porting example for Arduino |

### Software Framework Configuration

| Support IDE   | Version          |
| :------------ | :--------------- |
| ESP-IDF       | V5.1 / 5.2 / 5.3 |
| Arduino IDE   | esp32 >= v3.0.7  |
| PlatformIO IDE| -                |

### ESP-IDF Framework
- **Supported Versions:** v5.1 / 5.2 / 5.3
- **Instructions:** Download the example code from the repository and compile/run it directly.
- **Repository Address:** [examples/esp_idf](examples/esp_idf)

### Arduino Framework
[Novice Tutorial](https://github.com/VIEWESMART/VIEWE-Tutorial/blob/main/Arduino%20Tutorial/Arduino%20Getting%20Started%20Tutorial.md)

#### 1. Install Arduino IDE
Download from [Arduino Official Website](https://www.arduino.cc/en/software) based on your system type.

#### 2. Install ESP32 SDK
1. Open Arduino IDE → `File` > `Preferences`
2. Add to **Additional boards manager URLs**:
   ```text
   https://espressif.github.io/arduino-esp32/package_esp32_index.json
   ```
3. Navigate to `Tools` > `Board` > `Boards Manager`, search for `esp32` by Espressif Systems.
4. Select version **3.1.0** or above and click **INSTALL**.

#### 3. Install Required Libraries
- **ESP32_Display_Panel:** Go to `Sketch` > `Include Library` > `Manage Libraries...`, search for `ESP32_Display_Panel`, select version **1.0.3+** and click **Install All** when prompted for dependencies.
- **LVGL (Optional):** Recommended version **8.4.0**. Only required for GUI examples.

!!! note "Manual Installation"
    You can download the `.zip` file from [Github](https://github.com/esp-arduino-libs/ESP32_Display_Panel) or [Arduino Library](https://www.arduinolibraries.info/libraries/esp32_display_panel), then use `Sketch` > `Include Library` > `Add .ZIP Library...`.

#### 4. Configure Board Settings
Navigate to `Tools` > `Board` > `esp32` > `ESP32S3 Dev Module`.

**Tool Options:**

| Setting           | Value                             |
| :---------------- | :-------------------------------- |
| Board             | ESP32S3 Dev Module                |
| Core Debug Level  | None                              |
| USB CDC On Boot   | Disabled                          |
| USB DFU On Boot   | Disabled                          |
| Flash Size        | 16MB (128Mb)                      |
| Partition Scheme  | 16M Flash (3MB APP/9.9MB FATFS)   |
| PSRAM             | OPI PSRAM                         |

#### 5. Modify Code Configuration
Open example: `File` > `Examples` > `ESP32_Display_Panel` > `Arduino` > `gui` > `lvgl_v8` > `simple_port`.

Modify macros in `esp_panel_board_supported_conf.h`:

```c
// Enable supported board configuration
#define ESP_PANEL_BOARD_DEFAULT_USE_SUPPORTED       (1)

// Uncomment the target board
#define BOARD_VIEWE_UEDX48480021_MD80ET
```

!!! warning "Important"
    Do not enable both `ESP_PANEL_BOARD_DEFAULT_USE_SUPPORTED` and `ESP_PANEL_BOARD_DEFAULT_USE_CUSTOM` simultaneously. You cannot enable multiple boards at the same time.

!!! note "LVGL Color Swap Settings"
    - **SPI/QSPI screens:** Set `LV_COLOR_16_SWAP` to `1` in `lv_conf.h`
    - **RGB screens:** Set `LV_COLOR_16_SWAP` to `0` in `lv_conf.h`

#### 6. Compile & Upload
1. Select the correct port.
2. Click **√** to compile.
3. Connect the microcontroller and click **→** to upload.

### PlatformIO Framework

1. Install [Visual Studio Code](https://code.visualstudio.com/Download).
2. Install the **PlatformIO IDE** extension.
3. Download this repository via GitHub (`<> Code` > Download ZIP).
4. In VS Code Explorer (`Ctrl+Shift+E`), click **Open Folder** and select the downloaded project folder.
5. Open `platformio.ini`, uncomment the desired example under `[platformio]` section (`default_envs = xxx`).
6. Click **√** (bottom left) to compile, then **→** to upload.

### Firmware Download

1. Open the burning tool located in the `tools` directory.
2. Select the correct chip and burning method.
3. Follow steps 1→2→3→4→5 as shown below to burn the firmware from the `[firmware](./firmware/)` directory.
4. If burning fails, hold the **BOOT-0** button and retry.

<p align="center" width="100%">
  <img src="image/10.png" alt="Burning Step 1" style="max-width:45%; display:inline-block;">
  <img src="image/11.png" alt="Burning Step 2" style="max-width:45%; display:inline-block;">
</p>

## ❓ FAQ

??? question "After reading the tutorials, I still don't know how to build the programming environment?"
    Refer to the [VIEWE-FAQ](../../support/faq.md) document for detailed environment setup instructions.

??? question "Why does Arduino IDE prompt me to update library files? Should I update?"
    **Do not update.** Different versions of library files may not be mutually compatible. Stick to the recommended versions.

??? question "Why is there no serial data output on the 'Uart' interface?"
    The default configuration uses USB as UART0 for debugging. To enable the external UART interface:
    
    - **PlatformIO:** In `platformio.ini`, change `-D ARDUINO_USB_CDC_ON_BOOT=true` to `-D ARDUINO_USB_CDC_ON_BOOT=false`
    - **Arduino IDE:** Go to `Tools` > `USB CDC On Boot` > Select **Disabled**

??? question "Why does the board continuously fail to download the program?"
    Hold down the **BOOT** button while clicking the upload/download button, then release after the connection is established.

## 📐 Schematic

<p align="center" width="100%">
  <img src="Schematic/MD80ET-V1.0%20SCH_00.png" alt="Schematic">
</p>

## 📎 Information & Datasheets

| Document | Link |
| :------- | :--- |
| Product Specification | [UEDX48480021-MD80ET V1.1 SPEC](information/UEDX48480021-MD80ET%20V1.1%20SPEC.pdf) |
| Display Datasheet | [ALL-UE021WV-RB40-A009A V1.0 SPEC](information/ALL-UE021WV-RB40-A009A%20V1.0%20SPEC.pdf) |
| Button Datasheet | [6x6 Silent Switch](information/6x6Silent%20switch.pdf) |
| Encoder Datasheet | [EC28A1520401 Specification](information/C219783_%E6%97%8B%E8%BD%AC%E7%BC%96%E7%A0%81%E5%99%A8_EC28A1520401_%E8%A7%84%E6%A0%BC%E4%B9%A6_WJ239718.PDF) |
| ESP32-S3-WROOM-1 (EN) | [Datasheet English](information/esp32-s3-wroom-1_wroom-1u_datasheet_cn.pdf) |
| ESP32-S3-WROOM-1 (CN) | [Datasheet Chinese](information/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf) |


## 🛠️ Tools

* **[Flash Download Tool](../../../assets/software/flash_download_tool.zip)** – Utility for manual firmware flashing.
* **[LVGL Image Converter](https://lvgl.io/tools/imageconverter)** – Convert images to C arrays for LVGL.

> [!IMPORTANT]
> For more resources, please explore the [**Resource Center**](../../support/resource.md).

!!! info "Can't find what you need?"    
    If you need more products, resources or support, please contact our team:  

    [**:material-archive-arrow-down: Resource Center**](../../support/resource.md){ .md-button .md-button--primary } 
    [**:material-magnify: More Products**](../esp32/index.md){ .md-button }
    [**:material-email: Contact Support**](mailto:support@viewedisplay.com){ .md-button }