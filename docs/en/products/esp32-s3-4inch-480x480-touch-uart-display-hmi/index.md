---
title: VIEWE 4" 480x480 ESP32-S3 Smart Touch Display
description: UEDX48480040E-WB-A is a 4-inch 480x480 ESP32-S3 smart touch display module with a GC9503V RGB panel, FT6336U capacitive touch, Wi-Fi and BLE 5, and Arduino / ESP-IDF / PlatformIO support.
---

# 4" 480x480 ESP32-S3 Smart Touch Display


<div class="grid cards" markdown>

-   **UEDX48480040E-WB-A**
    ---
    The Mainstream AIoT Smart Display powered by ESP32-S3. Featuring a 4-inch 480x480 IPS TFT Display with Capacitive Touch Screen, Wi-Fi & BLE 5, and rich expansion interfaces.

    [:material-arrow-left: Back to Series](../esp32/){ .md-button }
    [:material-cart: Official Store](https://viewedisplay.com/product/esp32-4-inch-tft-display-touch-screen-arduino-lvgl/){ .md-button .md-button--primary }
    [:material-github: GitHub Repo](https://github.com/VIEWESMART/UEDX48480040ESP32-4inch-Touch-Display){ .md-button }

</div>

<div align="center">
  <img src="../../../assets/images/UEDX48480040E-WB-A/4 inch 480x480 esp32 tft touch display.jpg" width="100%" alt="4 inch 480x480 esp32 tft touch display">
</div>

---

## 1. Introduction

The UEDX48480040E-WB-A is a square-format HMI smart display module built around the ESP32-S3-WROOM-1 (N16R8) module and a 4-inch 480x480 IPS TFT panel. The panel is driven by a GC9503V controller over a 3-wire SPI + RGB interface, and the capacitive touch panel is read through an FT6336U controller on I2C.

Everything fits on a single square PCB: a 2x21 2.54 mm expansion header for external peripherals, two USB Type-C ports for power, download and serial debug, a TF card slot, an addressable RGB LED, and BOOT / RESET buttons. Out of the box the board supports Arduino, ESP-IDF and PlatformIO, with LVGL examples already ported for each framework.

### 1.1 Product Features

#### Processor & Wireless

- **Processor:** ESP32-S3-WROOM-1 (marked ESP32-S3-N16R8). Xtensa® dual-core 32-bit LX7 MCU up to 240 MHz.
- **Wireless:** 2.4 GHz Wi-Fi (802.11 b/g/n), Bluetooth 5 (LE) and BLE Mesh.

#### Memory

- **Flash:** 16 MB.
- **PSRAM:** 8 MB (Octal SPI).

#### Display

| Parameter | Specification |
| :--- | :--- |
| Size | 4.0 inch |
| Resolution | 480 x 480 |
| Panel type | IPS TFT, RGB vertical stripe |
| Interface | 3-wire SPI + RGB (16-bit data bus) |
| Driver IC | GC9503V |
| Touch IC | FT6336U (FT5x06-compatible driver) |
| Touch interface | Capacitive, I2C |
| Brightness | 350 cd/m² (typ.) |
| Display color | 262K |
| Pixel density | 169 PPI |
| Viewing direction | All o'clock |
| Display mode | Normally black |
| Backlight | White LED |
| Active area | 72.46 (W) x 71.78 (H) mm |
| Module size | 84 (W) x 84 (H) x 3.22 (D) mm |

#### Peripherals

- **Connectivity:** 2 x USB Type-C (USB download / program and UART), onboard CH340C USB-to-serial bridge.
- **Expansion:** 2x21 2.54 mm header breaking out GPIO, UART, 3.3 V, 5 V and GND.
- **Storage:** TF card slot (SPI interface).
- **Indication:** Onboard WS2812B addressable RGB LED.
- **Buttons:** BOOT (for download mode) and RESET.

#### Other

- **Power supply:** DC 5 V (4.0 - 5.5 V), 260 mA maximum with the backlight on. A 5 V / 1 A supply is recommended.
- **Operating temperature:** -20 ~ 70 ℃
- **Storage temperature:** -30 ~ 80 ℃
- **Operating humidity:** 10% ~ 90% RH (at 25 ℃)

### 1.2 Applications

With a square 480x480 panel and Wi-Fi / BLE connectivity, the UEDX48480040E-WB-A suits applications that need a balanced, rotatable UI surface:

- Smart home control panels and room thermostats
- Industrial HMI and machine status displays
- Smart appliance front panels
- IoT data dashboards and gateways
- Medical devices and laboratory instruments
- Knob-free, touch-first user interfaces

## 2. Hardware Description

### 2.1 Module Overview

The board is a single 94 x 94 mm PCB. The numbered callouts below mark each functional block on the back of the board:

<p align="left">
  <img src="../../../assets/images/UEDX48480040E-WB-A/module overview.jpg" alt="Module Overview" width="80%">
</p>

| No. | Component | Description |
| :--- | :--- | :--- |
| ① | 2x21 Expansion Header (J1) | 2.54 mm pitch header breaking out GPIO, UART, 3.3 V, 5 V and GND. |
| ② | Display Interface (J2) | 40-pin FPC connector for the RGB panel and the capacitive touch panel. |
| ③ | USB Type-C (USB) | 5 V power and firmware download / serial debug through the CH340C. |
| ④ | USB Type-C (UART) | 5 V power and external serial communication. |
| ⑤ | BOOT / RESET Buttons | BOOT enters download mode; RESET performs a hardware reset. |
| ⑥ | RGB LED | WS2812B addressable LED, single-wire control. |
| ⑦ | CH340C | USB-to-serial bridge used for download and debug. |
| ⑧ | TF Card Slot | Micro SD slot on the SPI bus. |
| ⑨ | ESP32-S3-WROOM-1 | Main SoC module, 16 MB flash / 8 MB PSRAM. |

### 2.2 GPIO Definition (Pinout)

#### Display (3-Wire SPI + RGB)

The panel is initialised over a 3-wire SPI bus, then fed pixel data over a parallel RGB bus.

**Initialisation bus (3-wire SPI)**

| Signal | ESP32-S3 Pin | Description |
| :--- | :--- | :--- |
| SPI SDA | IO47 | Serial data for the initial RGB interface configuration. |
| SPI SCK | IO48 | Serial interface clock. |
| SPI CS | IO39 | Chip select input, active low. |

**RGB data bus**

| Red | Pin | Green | Pin | Blue | Pin |
| :---: | :---: | :---: | :---: | :---: | :---: |
| R0 | IO4 | G0 | IO10 | B0 | IO15 |
| R1 | IO3 | G1 | IO9 | B1 | IO14 |
| R2 | IO2 | G2 | IO8 | B2 | IO13 |
| R3 | IO1 | G3 | IO7 | B3 | IO12 |
| R4 | IO0 | G4 | IO6 | B4 | IO11 |
|  |  | G5 | IO5 |  |  |

**Timing and control**

| Signal | ESP32-S3 Pin | Description |
| :--- | :--- | :--- |
| PCLK | IO21 | Pixel clock input, negative polarity. |
| DE | IO18 | Data input enable, active high. |
| VSYNC | IO17 | Vertical sync signal, negative polarity. |
| HSYNC | IO16 | Horizontal sync signal, negative polarity. |
| BACKLIGHT | IO38 | Backlight enable (LCD-BL-EN). |

#### Touch (FT6336U)

| Signal | ESP32-S3 Pin | Description |
| :--- | :--- | :--- |
| SDA | IO40 | I2C data line for the touch controller. |
| SCL | IO41 | I2C clock line for the touch controller. |
| TP INT | — | Interrupt signal, not connected on this board. |
| TP RST | — | Reset signal, not connected on this board. |

The touch controller answers at I2C address `0x38`. The `01_i2c_scan` example uses that address as its pass criterion.

#### Peripherals

| Function | Signal | ESP32-S3 Pin |
| :--- | :--- | :--- |
| Button | BOOT | IO0 |
| Button | RESET | CHIP-EN |
| TF card | CS | IO47 |
| TF card | CLK | IO45 |
| TF card | MOSI | IO42 |
| TF card | MISO | IO46 |
| UART header | TX | IO43 (U0TXD) |
| UART header | RX | IO44 (U0RXD) |
| RGB LED | WS2812B data | IO42 |
| USB (CH340C) | D- | IO19 |
| USB (CH340C) | D+ | IO20 |

!!! warning "Shared pins"
    Because the panel uses a parallel RGB bus, most GPIOs are occupied once the display interface is in use.

    - **IO42** is shared between the TF card MOSI line and the WS2812B RGB LED data line.
    - **IO47** carries the panel's 3-wire SPI data and is also used as the TF card chip select.
    - **IO45** and **IO46** are dedicated to the TF card and are free for other purposes when no card is used.
    - GPIO35, GPIO36 and GPIO37 are not used and are not routed out.

    Use the 2x21 expansion header for any additional peripherals.

## 3. Software

The repository ships ready-to-run examples for Arduino, ESP-IDF and PlatformIO, including LVGL ports and a hardware bring-up sequence.

### 3.1 Software Examples

Examples are available in the [GitHub Repository](https://github.com/VIEWESMART/UEDX48480040ESP32-4inch-Touch-Display/tree/main/examples).

| Framework | Example Path | Description |
| :--- | :--- | :--- |
| esp-idf | `examples/esp_idf/01_i2c_scan` | Scan the touch I2C bus. Passes when the log shows a green PASS with `0x38` in the list. |
| esp-idf | `examples/esp_idf/02_wifi` | Scan nearby Wi-Fi networks, optionally joining one. |
| esp-idf | `examples/esp_idf/03_lvgl_port` | LVGL port plus the official demos. Passes when the UI is visible and the badge turns green on tap. |
| esp-idf | `examples/esp_idf/04_sd` | Mount the TF card and list the `/sdcard` directory. |
| esp-idf | `examples/esp_idf/05_album` | Phone-style launcher with a photo album application. |
| esp-idf | `examples/esp_idf/06_brookesia_iphone` | Full phone UI built on Brookesia, with screen and touch test apps. |
| Arduino | `examples/arduino/board/board_static_config` | Board bring-up using a statically configured board definition. |
| Arduino | `examples/arduino/board/board_dynamic_config` | Board bring-up using a runtime board configuration. |
| Arduino | `examples/arduino/drivers/lcd/lcd_3wire_spi_rgb` | Drive the panel over the 3-wire SPI + RGB bus and display colour bars. |
| Arduino | `examples/arduino/drivers/touch/touch_i2c` | Read the FT6336U touch controller over I2C. |
| Arduino | `examples/arduino/gui/lvgl_v8/simple_port` | Minimal LVGL v8 port; also available from the ESP32_Display_Panel library. |
| Arduino | `examples/arduino/gui/lvgl_v8/simple_rotation` | LVGL v8 port with screen rotation. |
| Arduino | `examples/arduino/gui/lvgl_v8/squareline_port` | LVGL v8 port driven by a SquareLine Studio UI project. |
| Arduino | `examples/arduino/gui/lvgl_v8/squareline_wifi_clock` | SquareLine weather clock UI with Wi-Fi connectivity. |
| PlatformIO | `examples/platformio/lvgl_v8_port` | LVGL v8 port for PlatformIO, with avoid-tearing and rotation support. |

### 3.2 Getting Started

#### 3.2.1 Preparation

- **Hardware:** UEDX48480040E-WB-A board, USB-C cable, 5 V / 1 A power supply.
- **Software:** VS Code with ESP-IDF v5.1 / 5.2 / 5.3, or Arduino IDE with the ESP32 core v3.0.7 or newer, or VS Code with PlatformIO.
- **Library:** The following libraries are needed for the Arduino IDE and PlatformIO:

| Libraries | version | Description |
| :--- | :--- | :--- |
| ESP32_Display_Panel | 1.0.0+ | by Espressif. Required to drive the RGB panel and read the touch controller. |
| ESP32_IO_Expander | Arduino automatic selection | Dependency of ESP32_Display_Panel, installed together when prompted. |
| esp-lib-utils | Arduino automatic selection | Dependency of ESP32_Display_Panel, installed together when prompted. |
| lvgl | 8.4.0 | A free and open-source embedded graphics library. |

#### 3.2.2 ESP-IDF Setup

Every folder under `examples/esp_idf/` is a standalone ESP-IDF project. The first build fetches the board support package `viewesmart/bsp_uedx48480040e_wb_a` from the ESP Component Registry, so no manual component wiring is required.

Bring the hardware up in order — `01 → 02 → 03 → 04` — then run `05` and `06`.

1. **Open the example folder in VS Code** (for example `examples/esp_idf/01_i2c_scan`).
2. **Set the target** to `esp32s3`.
3. **Compile, flash and monitor** using the VS Code buttons, or from the command line inside the example directory:

    ```bash
    idf.py set-target esp32s3
    idf.py build flash monitor
    ```

!!! tip "Bring-up order"
    Run `01_i2c_scan` first and confirm the touch controller shows up at I2C address `0x38` before moving on. If the display stays blank or touch does not respond, the fault is almost always in the bring-up sequence rather than in the application code.

#### 3.2.3 Arduino Setup

1. **Install [Arduino IDE](https://www.arduino.cc/en/software)**
   Choose the installation matching your system. Newcomers can follow the [beginner's tutorial](../../support/tutorials.md).
2. **Install the ESP32 board package:**
    - Open Arduino IDE.
    - Go to `File` > `Preferences`.
    - Add to `Additional boards manager URLs`:
      ```text
      https://espressif.github.io/arduino-esp32/package_esp32_index.json
      ```
    - Go to `Tools` > `Board` > `Boards Manager`.
    - Search `esp32` by Espressif and install version 3.0.7 or newer.
3. **Install the libraries:**
    - Go to `Sketch` > `Include Library` > `Manage Libraries`.
    - Search `ESP32_Display_Panel` by Espressif and install version 1.0.0 or newer. When prompted about dependencies, click INSTALL ALL.
    - Install `lvgl` (v8.4.0 recommended).
4. **Open an example:**
    - From this repository: `examples/arduino/gui/lvgl_v8/simple_port`.
    - Or from the library: `File` > `Examples` > `ESP32_Display_Panel` > `Arduino` > `gui` > `lvgl_v8` > `simple_port`.
5. **Select the board:**
    - Target: `ESP32S3 Dev Module`.
    - Settings:
        - Core Debug Level: None
        - USB CDC On Boot: Disabled
        - USB DFU On Boot: Disabled
        - Flash Size: 16MB (128Mb)
        - Partition Scheme: 16M Flash (3MB APP/9.9MB FATFS)
        - PSRAM: OPI PSRAM (Crucial!)
6. **Enable the board configuration:**
   Open `esp_panel_board_supported_conf.h` in the example. Set the supported-board flag to `1` and uncomment the macro for this board:

   ```c
   /**
    * @brief Flag to enable supported board configuration (0/1)
    *
    * Set to `1` to enable supported board configuration, `0` to disable
    */
   #define ESP_PANEL_BOARD_DEFAULT_USE_SUPPORTED       (1)

   // #define BOARD_VIEWE_UEDX32480035E_WB_A
   // #define BOARD_VIEWE_UEDX48270043E_WB_A
    #define BOARD_VIEWE_UEDX48480040E_WB_A
   // #define BOARD_VIEWE_UEDX80480043E_WB_A
   // #define BOARD_VIEWE_UEDX80480050E_WB_A
   ```
7. **Configure the example:**
    - *[Optional]* Edit the macro definitions in `lvgl_v8_port.h`:
        - This board uses an `RGB` interface, so you can set `LVGL_PORT_AVOID_TEARING_MODE` to `1` / `2` / `3` to enable the avoid tearing function, and then set `LVGL_PORT_ROTATION_DEGREE` to the rotation you need.
    - *[Optional]* Edit the macro definitions in `lv_conf.h`:
        - Do **not** set `LV_COLOR_16_SWAP` to `1` here. That option only applies to `SPI` / `QSPI` panels, not to the RGB bus used on this board.
8. **Select the correct port:**
    - Connect the board with the USB-C cable.
    - Go to `Tools` > `Port` and select the corresponding port.
9. **Compile and upload:**
    - Click `√` in the upper left corner to compile.
    - If the compilation is correct, connect the board and click `→` to download.

!!! tip "Configuration Note"
    In `esp_panel_board_supported_conf.h`, ensure you uncomment `#define BOARD_VIEWE_UEDX48480040E_WB_A`.

    Do not enable both `ESP_PANEL_BOARD_DEFAULT_USE_SUPPORTED` and `ESP_PANEL_BOARD_DEFAULT_USE_CUSTOM`.
    You cannot enable multiple esp supported panel boards at the same time.

#### 3.2.4 PlatformIO Setup

1. **Open the example**
   Open `examples/platformio/lvgl_v8_port` in VS Code with the PlatformIO extension installed.
2. **Choose the board**
   The `[platformio]:default_envs` entry in `platformio.ini` selects which environment is built, and the matching board description file must exist in the `boards/` directory.
   The example ships board files for several Espressif dev boards and for `BOARD_VIEWE_UEDX80480070E_WB_A`. To build for this board, add a board file for `BOARD_VIEWE_UEDX48480040E_WB_A` (copy an ESP32-S3 RGB board file and update the pin definitions), or select `BOARD_CUSTOM` and fill in `src/esp_panel_board_custom_conf.h`.
3. **Configure the example**
    - *[Optional]* Edit the macro definitions in `lvgl_v8_port.h`:
        - Set `LVGL_PORT_AVOID_TEARING_MODE` to `1` / `2` / `3` to enable the avoid tearing function for the `RGB` interface, then set `LVGL_PORT_ROTATION_DEGREE` to the rotation you need.
4. **Compile and upload the project**
    - Click the `√` (Compile) button.
    - Connect the board to your computer. If the compilation is correct, click the `→` (upload) button.

## 4. Related Documents & Resources

| Document | Link |
| :--- | :--- |
| Product Specification | [UEDX48480040E-WB-A V3.2 SPEC.pdf](../../../assets/datasheet/UEDX48480040E-WB-A.pdf) |
| Schematic Diagram | [SCH-UEDX48480040E-WB-A.png](../../../assets/schematic/SCH-UEDX48480040E-WB-A.png) |
| Display Panel Datasheet | [UE040WV-RH40-A044C V1.3](https://github.com/VIEWESMART/UEDX48480040ESP32-4inch-Touch-Display/blob/main/information/UE040WV-RH40-A044C%20V1.3.pdf) |
| Touch Controller Datasheet | [FT6336U V1.1](https://github.com/VIEWESMART/UEDX48480040ESP32-4inch-Touch-Display/blob/main/information/FT6336U-DataSheet-V1.1.pdf) |
| ESP32-S3-WROOM-1 Datasheet (CN) | [esp32-s3-wroom-1_datasheet_cn.pdf](../../../assets/datasheet/chip/esp32-s3-wroom-1_wroom-1u_datasheet_cn.pdf) |
| ESP32-S3-WROOM-1 Datasheet (EN) | [esp32-s3-wroom-1_datasheet_en.pdf](../../../assets/datasheet/chip/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf) |

## 5. Firmware Download

1. Open the `tools` folder of the repository and locate the ESP32 flash download tool (`flash_download_tool_3.9.5`). Extract and launch it.
2. Select the chip type `ESP32-S3` and the download mode, then click **OK**. Follow the numbered steps 1 → 2 → 3 → 4 → 5 shown below to burn the firmware. If the download fails, hold the **BOOT** button and try again.
3. Select the binary to burn. Prebuilt binaries, when published, are placed in the repository's `firmware` directory — check the version notes inside and choose the appropriate build.

If no prebuilt binary is available for your target, build and flash from source instead — see [3.2 Getting Started](#32-getting-started).

<p align="center" width="100%">
  <img src="../../../assets/images/Espressif/esp32-s3-firmware-download-1.png" alt="Firmware Download Step 1">
  <img src="../../../assets/images/Espressif/esp32-s3-firmware-download-2.png" alt="Firmware Download Step 2">
</p>

## 6. FAQ

??? question "After reading the tutorials, I still don't know how to build the programming environment. What should I do?"
    Refer to the [VIEWE FAQ](../../support/faq.md) document for detailed environment setup instructions.

??? question "Why does the Arduino IDE prompt me to update library files when I open it? Should I update them?"
    Choose **not** to update the library files. Different versions of library files may not be mutually compatible, so updating them is not recommended.

??? question "Why is there no serial data output on the UART header on my board? Is it defective and unusable?"
    The default project configuration uses the USB interface as UART0 serial output for debugging. The UART header is wired to the same UART0 pins, so it will not output any data without reconfiguration.

    - **PlatformIO users:** open `platformio.ini` and change the option under `build_flags` from `-D ARDUINO_USB_CDC_ON_BOOT=true` to `-D ARDUINO_USB_CDC_ON_BOOT=false`.
    - **Arduino users:** open the `Tools` menu and select `USB CDC On Boot: Disabled`.

??? question "Why does my board keep failing to download the program?"
    Please hold down the `BOOT` button while starting the download, then release it once the connection is established, and try again.

??? question "Which display driver IC and touch controller does this board use?"
    The 480x480 panel is driven by a `GC9503V` controller over a 3-wire SPI + RGB bus. Capacitive touch is handled by an `FT6336U` controller on I2C, driven with the FT5x06-compatible driver; it answers at I2C address `0x38`.

!!! info "Can't find what you need?"
    If you need more Products or Resource or Support, please contact our team:

    [**:material-archive-arrow-down: Resource Center**](../../support/resource.md){ .md-button .md-button--primary }
    [**:material-magnify: More Products**](../esp32/index.md){ .md-button  }
    [**:material-email: Contact Support**](mailto:support@viewedisplay.com){ .md-button }
