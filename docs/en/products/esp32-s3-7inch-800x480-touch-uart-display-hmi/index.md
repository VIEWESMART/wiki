# 7" 800x480 ESP32-S3 Uart Smart Touch Display

<div class="grid cards" markdown>

-   **UEDX80480070E-WB-A**
    ---
    The **Mainstream AIoT** Smart Display powered by **ESP32-S3**.
    Featuring a 7-inch **800x480** TFT Display (RGB), Wi-Fi & BLE 5, and rich expansion interfaces.

    [:material-arrow-left: Back to Series](../esp32/){ .md-button }
    [:material-cart: Official Store](https://viewedisplay.com/product/esp32-7-inch-800x480-rgb-ips-tft-display-touch-screen-arduino-lvgl-uart/){ .md-button .md-button--primary }
    [:material-github: GitHub Repo](https://github.com/VIEWESMART/UEDX80480070ESP32-7inch-Touch-Display){ .md-button }

</div>

<div align="center"> 
  <img src="../../../assets/images/UEDX80480070E-WB-A/overview.png" width="90%" alt="7inch esp32 s3 touch display">
</div>

---

## 1. Introduction

The **UEDX80480070E-WB-A** is a high-performance HMI smart display module equipped with a 7-inch RGB screen (800x480). Powered by the **ESP32-S3-WROOM-1-N16R8** module, it integrates 2.4GHz Wi-Fi and Bluetooth 5 (LE) capabilities.

The board features a high-speed **RGB Interface** for the display, ensuring smooth UI performance . It also includes a Capacitive Touch Panel (GT911), rich GPIO expansion, and supports popular frameworks like **Arduino**, **ESP-IDF**, and **PlatformIO**.

### 1.1 Product Features
* **Processor**:
    * **ESP32-S3**: Xtensa® Dual-Core 32-bit LX7 MCU @ 240MHz.
    * Integrated 2.4 GHz Wi-Fi (802.11 b/g/n) & Bluetooth 5 (LE).
* **Memory**:
    * **16MB** Quad SPI Flash.
    * **8MB** Octal SPI PSRAM.
* **Display & Touch**:
    * **Screen**: 7.0-inch TFT LCD (800x480 Resolution).
    * **Interface**: 16-bit RGB Interface (High Refresh Rate).
    * **Driver IC**: EK9716BD3 + EK73002AB2.
    * **Touch**: Capacitive Multi-Touch (GT911) via I2C.
* **Peripherals**:
    * **Connectivity**: USB-C (UART/Program), RS485, CAN, RS232 (Optional/Expansion).
    * **Storage**: TF Card Slot (SDIO/SPI).
    <!-- * **Audio**: Onboard Speaker Connector & Buzzer. -->
    * **Expansion**: GPIO Header (UART, I2C, SPI, IOs).

### 1.2 Applications
* Industrial HMI Control Panels
* Smart Home Automation Centers
* Medical Devices & Instruments
* IoT Data Dashboards

---

## 2. Hardware Description

### 2.1 Module Overview
The detailed component layout is shown below:

![Board Layout](../../../assets/images/UEDX80480070E-WB-A/modules.png)

| No. | Component | Description |
| :--- | :--- | :--- |
| **①** | **ESP32-S3-N16R8** | Main SoC (16MB Flash / 8MB PSRAM). |
| **②** | **USB-C Port** | **Power (5V)** / Firmware Download / UART Debug (CH340C). |
| **③** | **Display Interface** | 40-Pin RGB Interface FPC Connector. |
| **④** | **Touch Interface** | 6-Pin Capacitive Touch Header (I2C). |
| **⑤** | **TF Card Slot** | For external storage (Images/Logs). |
| **⑥** | **UART/RS485** | Reserved pads/header for Industrial Serial communication. |
| **⑦** | **BOOT Button** | Press during power-on to enter Download Mode. |
| **⑧** | **RESET Button** | Hardware System Reset. |
| **⑨** | **Expansion Header** | GPIOs, 5V, 3.3V, GND for external sensors. |

### 2.2 GPIO Definition (Pinout)
The mapping for the Display and Touch interfaces:

<!-- ![Pin Definition](../../../assets/images/UEDX80480070E-WB-A/connection.png) -->

#### **Display (RGB Interface)**
| Pin Name | ESP32-S3 Pin | Function |
| :--- | :--- | :--- |
| **DE** | IO40 | Data Enable |
| **VSYNC** | IO41 | Vertical Sync |
| **HSYNC** | IO39 | Horizontal Sync |
| **PCLK** | IO42 | Pixel Clock |
| **R0 - R4** | IO45, 48, 47, 21, 14 | Red Data Lines |
| **G0 - G5** | IO5, 6, 7, 15, 16, 4 | Green Data Lines |
| **B0 - B4** | IO8, 3, 46, 9, 1 | Blue Data Lines |
| **BL** | IO2 | Backlight PWM |

#### **Touch (GT911)**
| Pin Name | ESP32-S3 Pin | Function |
| :--- | :--- | :--- |
| **SDA** | IO19 | I2C Data |
| **SCL** | IO20 | I2C Clock |
| **INT** | IO18 | Interrupt |
| **RST** | IO38 | Reset |

#### **Peripherals**
| Interface | ESP32-S3 Pin | Description |
| :--- | :--- | :--- |
| **UART0** | IO43 (TX), IO44 (RX) | USB-to-UART (Debug/Upload) |
| **SD Card** | IO10 (CS), IO11 (MOSI), IO12 (CLK), IO13 (MISO) | SPI/SDIO Mode |
| **RGB LED** | IO0 | WS2812B (Optional) |

### 2.3 Mechanical Dimensions
Physical size and mounting information:

![Dimensions](../../../assets/images/UEDX80480070E-WB-A/dimensions.png)

* **Outline Size**: 180.9mm x 105.45mm
* **Screen Size**: 7.0 Inch Diagonal

---

## 3. Software

We provide comprehensive support for **Arduino**, **PlatformIO**, and **ESP-IDF** frameworks, with pre-ported **LVGL** examples.

### 3.1 Software Examples
Examples are available in the [GitHub Repository](https://github.com/VIEWESMART/UEDX80480070ESP32-7inch-Touch-Display/tree/main/examples).

| Framework | Example Path | Description |
| :--- | :--- | :--- |
| **Arduino** | `examples/arduino/gui/lvgl_v8` | **LVGL Benchmark**: Demonstrates 800x480 UI rendering. It can also be directly opened in the Arduino IDE. |
| **esp-idf** | `examples/esp_idf/lvgl_port` | **lvgl port**: Example of porting and using lvgl in esp-idf |
| **esp-idf** | `examples/esp_idf/sd_card_spi` | **sd_card**: Examples of using an SD card on a device |
| **PlatformIO**| `examples/platformio/lvgl_v8_port` | **lvgl v8 port**: Usage example of lvgl v8. |

### 3.2 Getting Started

#### 3.2.1 Preparation
* **Hardware**: UEDX80480070E-WB-A Board, USB-C Cable.
* **Software**: VS Code (ESP-IDF v5.3+) or Arduino IDE (v2.0+) or VS Code (PlatformIO).
* **Library**: The following libraries are needed for Arduino IDE and PlatformIO

    |Libraries|version|Description|
    | :--- | :--- | :--- |
    |`ESP32_Display_Panel`| `1.0.3+` |by Espressif, This is necessary to drive the screen.|
    |`ESP32_IO_Expander`| `Arduino automatic selection` |The dependency library of `ESP32_Display_Panel` should be selected for installation together during the installation process.|
    |`esp-lib-utils`| `Arduino automatic selection` |The dependency library of `ESP32_Display_Panel` should be selected for installation together during the installation process.|
    |`lvgl`| `8.4.0` | A free and open-source embedded graphics library. |

#### 3.2.2  ESP-IDF Setup
1.  **Open platformio example**
    * go to GitHub to download the program. You can download the main branch by clicking on the "<> Code" with green text
    * Open the example using VS Code(ESP-IDF)
2.  **Compile and upload**:
    * Click `build` in the upper right corner to compile.
    * connect the microcontroller to the computer.If the compilation is correct.
    * Click `upload` in the upper right corner to download.

#### 3.2.3 Arduino Setup
1.  **Install ESP32 Board Package**:
    * Go to *Tools > Board > Boards Manager*.
    * Search `esp32` by Espressif and install version **3.0.0+**.
2.  **Install Libraries**:
    * Go to *Sketch > Include Library > Library Manager*.
    * Search `ESP32_Display_Panel` by Espressif and install version **1.0.3+**. You will be prompted whether to install its dependencies, please click **INSTALL ALL** to install all.
    * Install `lvgl` (v8.4.0 recommended).
3.  **Open example**:
    * Navigate to `File` > `Examples` > `ESP32_Display_Panel`
    * Select `Arduino` > `gui` > `lvgl_v8` > `simple_port`
4.  **Select Board**:
    * Target: `ESP32S3 Dev Module`.
    * Settings:
        * **Flash Size**: 16MB (128Mb)
        * **Partition Scheme**: 16M Flash (3MB APP/9.9MB FATFS)
        * **PSRAM**: **OPI PSRAM** (Crucial!)
5.  **config esp supported panel board**:
    * Open the `esp_panel_board_supported_conf.h` file in the example
    * Enable this file: change the `ESP_PANEL_BOARD_DEFAULT_USE_SUPPORTED` macro definition to `1`
    * ensure you uncomment: `#define BOARD_VIEWE_UEDX80480070E_WB_A`
6.  **Configure the example**:
    - [Optional] Edit the macro definitions in the `lvgl_v8_port.h` file
        - **If using `RGB/MIPI-DSI` interface**, change the `LVGL_PORT_AVOID_TEARING_MODE` macro definition to `1`/`2`/`3` to enable the avoid tearing function. After that, change the `LVGL_PORT_ROTATION_DEGREE` macro definition to the target rotation degree
        - **If using other interfaces**, please don't modify the `LVGL_PORT_AVOID_TEARING_MODE` and `LVGL_PORT_ROTATION_DEGREE` macro definitions
    - [Optional] Edit the macro definitions in the `lv_conf.h` file
        - **If using `SPI/QSPI` interface**, change the `LV_COLOR_16_SWAP` macro definition to `1`.
7.  **Select the correct port**:
    * Connect to the device.
    * Go to *Tools > Port*, Select the corresponding port.
8.  **Compile and upload**:
    * Click `√` in the upper right corner to compile.
    * connect the microcontroller to the computer.If the compilation is correct.
    * Click `→` in the upper right corner to download.


> [!TIP]
> **Configuration**: In `esp_panel_board_supported_conf.h`, ensure you uncomment:
> `#define BOARD_VIEWE_UEDX80480070E_WB_A`
> Do not enable both `ESP_PANEL_BOARD_DEFAULT_USE_SUPPORTED` and `ESP_PANEL_BOARD_DEFAULT_USE_CUSTOM`
> You cannot enable multiple esp supported panel boards at the same time.

#### 3.2.4 PlatformIO Setup
1.  **Open platformio example**
    * go to GitHub to download the program. You can download the main branch by clicking on the "<> Code" with green text
    * Open the example using VS Code(PlatformIO)
2.  **Configure PlatformIO**:
    * This example uses the `BOARD_ESPRESSIF_ESP32_S3_LCD_EV_BOARD_2_V1_5` board as default. Choose `BOARD_VIEWE_UEDX80480070E_WB_A` in the `[platformio]:default_envs` of the `platformio.ini` file.
3.  **Configure the example**:
    - [Optional] Edit the macro definitions in the `lvgl_v8_port.h` file
        - **If using `RGB/MIPI-DSI` interface**, change the `LVGL_PORT_AVOID_TEARING_MODE` macro definition to `1`/`2`/`3` to enable the avoid tearing function. After that, change the `LVGL_PORT_ROTATION_DEGREE` macro definition to the target rotation degree
        - **If using other interfaces**, please don't modify the `LVGL_PORT_AVOID_TEARING_MODE` and `LVGL_PORT_ROTATION_DEGREE` macro definitions
4.  **Compile and upload the project**
    - Click the `√`(Compile) button
    - Connect the board to your computer.If the compilation is correct.
    - Click the `→`(upload) button
---

## 4. Related Documents & Resources

### 📄 Documents
| Document Title | Type | Description |
| :--- | :--- | :--- |
| **[Product Specification](../../../assets/datasheet/UEDX80480070E-WB-A V2.0 SPEC.pdf)** | PDF | UEDX80480070E Datasheet |
| **[Schematic Diagram](../../../assets/schematic/UEDX80480070E-WB-A%20V1.1%20sch.png)** | PNG | Circuit Design & Connections |
| **[Display Datasheet](../../../assets/datasheet/display/ALL-UE070WV-RB40-A092A.pdf)** | PDF | Display Module Specification |
| **[Touch Driver](../../../assets/datasheet/touch/GT911_EN_Datasheet.pdf)** | PDF | Goodix GT911 Touch Controller Spec |

### 🛠️ Tools
* **[Flash Download Tool](../../../assets/software/flash_download_tool.zip)**: Utility for flashing firmware manually.
* **[Image Converter](https://lvgl.io/tools/imageconverter)**: Convert images for LVGL code.

> [!IMPORTANT]
> For more resources, please explore the [**Resource Center**](../../support/resource.md).

---

## :material-face-agent: Technical Support

<div class="grid cards" markdown>

-   [**:material-github: GitHub Issues**](https://github.com/VIEWESMART/UEDX80480070ESP32-7inch-Touch-Display/issues)
    ---
    Report bugs or request new features. Track development progress.

-   [**:material-email: Email Support**](mailto:smartrd1@viewedisplay.com)
    ---
    For direct technical support and business inquiries.

</div>