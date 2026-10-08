---
title: VIEWE 1.5" 466x466 AMOLED ESP32-S3 Round Smart Display
description: A 70 mm round ESP32-S3 smart display dev board with a 1.5-inch 466x466 AMOLED panel, CO5300 QSPI driver, capacitive touch, I2S microphone and class-D audio, 6-axis IMU, SD3078 RTC and TF card slot.
---

# 1.5" 466x466 AMOLED ESP32-S3 Round Smart Display

<div class="grid cards" markdown>

-   **1.5" 466x466 AMOLED · ESP32-S3 Round Dev Board**
    ---
    A Ø70 mm circular development board built around the ESP32-S3-WROOM-1 (N16R8) and a 1.5-inch 466x466 AMOLED panel driven by a CO5300 controller over QSPI. Onboard: capacitive touch, I2S digital microphone, class-D audio with speaker connector, 6-axis IMU, SD3078 real-time clock, TF card slot and a rechargeable battery circuit.

    [:material-arrow-left: Back to Series](../esp32/){ .md-button }
    [:material-cart: Official Store](https://viewedisplay.com/product/esp32-s3-1-5-inch-amoled-touch-screen-dev-board-uart-smart-display/){ .md-button .md-button--primary }
    [:material-github: GitHub Repo](https://github.com/VIEWESMART/ESP32-S3-Round-Dev-Board){ .md-button }

</div>

<div align="center">
  <img src="../../../assets/images/ESP32S3RoundDevBoard/1.5 inch 466x466 round amoled esp32 s3 smart display.jpg" width="100%" alt="1.5 inch 466x466 round AMOLED ESP32-S3 smart display front and back">
</div>

---

## 1. Introduction

The ESP32-S3 Round Dev Board is a circular, 70 mm diameter development board that carries the ESP32-S3-WROOM-1 (N16R8) module on one side and a single round display on the other. The same PCB accepts three different round panels, and this page covers the **1.5-inch AMOLED** build: a 466x466 AMOLED panel driven by a CO5300 controller over a 4-bit QSPI bus, with capacitive touch on I2C.

The board is designed as an AI voice terminal first and a general ESP32-S3 development board second. It carries a digital MEMS microphone, an I2S DAC plus a class-D amplifier for an 8 Ω / 2 W speaker, a 6-axis IMU, an SD3078 real-time clock with a rechargeable backup-cell socket, a TF card slot and an RGB status LED. Power comes from USB Type-C or a battery, with automatic changeover and charging.

The repository ships standalone ESP-IDF bring-up projects for each panel size, and the 1.5-inch build maps to `examples/esp-idf/ESP32-S3-Round-Dev-Board/viewe1.5`.

### 1.1 Product Features

#### Processor & Wireless

- **Processor:** ESP32-S3-WROOM-1, marked **ESP32-S3-N16R8**. Xtensa® dual-core 32-bit LX7 up to 240 MHz.
- **Wireless:** 2.4 GHz Wi-Fi (802.11 b/g/n) and Bluetooth 5 (LE).

#### Memory

- **Flash:** 16 MB.
- **PSRAM:** 8 MB.
- **On-chip:** 520 KB SRAM, 448 KB ROM.

#### Display

| Parameter | Specification |
| :--- | :--- |
| Size | 1.5 inch (1.51 inch diagonal) |
| Resolution | 466 x 466 |
| Panel type | AMOLED, normally black |
| Interface | QSPI (4 data lines) |
| Driver IC | CO5300AF-42 |
| Touch IC | CST9217 |
| Touch interface | Capacitive, I2C |
| Brightness | 450 cd/m² (typ.) |
| Display color | 16.7 M (24-bit) |
| Pixel pitch | 0.0822 mm |
| Pixel density | 309 PPI |
| Active area | 38.3052 x 38.3052 mm |
| Module size | 44.3 (W) x 44.3 (H) x 2.405 (D) mm |
| Viewing direction | All o'clock |

#### Peripherals

- **Audio in:** onboard digital MEMS microphone on I2S.
- **Audio out:** I2S DAC plus class-D amplifier, MX1.25 2-pin speaker connector rated for an 8 Ω / 2 W speaker.
- **Motion:** QMI8658 6-axis inertial sensor (accelerometer + gyroscope) on I2C.
- **Timekeeping:** SD3078 real-time clock with a socket for a rechargeable backup cell.
- **Storage:** TF (micro SD) card slot.
- **Expansion:** USB_OTG interface, plus IO3, IO8, IO43 and IO44 broken out for SPI / I2C / I2S / UART.
- **Indication:** onboard RGB LED used for status signalling.
- **Buttons:** PWR (power), BOOT (download mode) and RST (hardware reset).

#### Other

- **Power supply:** DC 5 V through USB Type-C, or a battery with onboard charge and discharge management. USB takes priority when both are connected.
- **Operating current:** 1000 mA while charging at VCC = 5 V; 130 mA in non-charging operation. A 5 V / 1 A supply is recommended.
- **Board size:** Ø70 mm circular PCB.
- **Operating temperature:** -20 ~ 70 ℃
- **Storage temperature:** -30 ~ 80 ℃
- **Environmental:** RoHS 2.0 and halogen-free.
- **ESD:** ±4 kV contact, ±8 kV air.

### 1.2 Applications

A round, high-contrast AMOLED panel with a full audio front end and battery support suits products that sit on a desk, a wall or a wrist:

- AI voice assistants and desktop companion devices
- Smart speakers and network-radio style terminals with a visual face
- Wearable and ring-format concepts
- Smart home control dials, thermostats and scene controllers
- Portable, battery-powered instrument and sensor readouts
- Round gauge and dashboard UIs in industrial equipment

## 2. Hardware Description

### 2.1 Module Overview

The board is a single circular PCB with one panel mounted on the front. The numbered callouts below mark each functional block on the back of the board:

<p align="left">
  <img src="../../../assets/images/ESP32S3RoundDevBoard/module overview.jpg" alt="ESP32-S3 Round Dev Board module overview" width="80%">
</p>

| No. | Component | Description |
| :--- | :--- | :--- |
| ① | ESP32-S3-WROOM-1 | Main SoC module, 16 MB flash / 8 MB PSRAM. |
| ② | 1.5-inch Display Interface | QSPI FPC connector for the 1.5-inch AMOLED panel and its touch layer. |
| ③ | 1.75-inch Display Interface | Alternative QSPI connector; only one panel size is fitted at a time. |
| ④ | 1.85-inch Display Interface | Alternative QSPI connector; only one panel size is fitted at a time. |
| ⑤ | USB Type-C | 5 V power, firmware download and serial debug. |
| ⑥ | USER LED | Power indicator light. |
| ⑧ | BOOT Button | Hold while powering on or resetting to enter download mode. |
| ⑨ | RST Button | Hardware reset. |
| ⑩ | PWR Button | Long press to power the board on or off. |
| ⑪ | RTC Socket | Socket for a rechargeable RTC backup cell. Rechargeable cells only. |
| ⑫ | SMD Microphone | Digital MEMS microphone. |
| ⑬ | Speaker Interface | MX1.25 2-pin connector for an 8 Ω / 2 W speaker. |
| ⑭ | TF Card Slot | Micro SD card slot. |
| ⑮ | 6-Axis IMU | QMI8658 accelerometer and gyroscope for motion detection. |
| ⑯ | RTC | SD3078 real-time clock. |
| ⑰ | GPIO | Expansion pads for IO3, IO8, IO43 and IO44. |

!!! note "Numbering follows the specification"
    The callout numbers above match the numbering printed in the board specification. There is no callout ⑦ in that document, and the table above is listed in the same order so the diagram and the specification stay in sync.

### 2.2 GPIO Definition (Pinout)

The table below is the GPIO assignment summary from the board specification, colour-coded by function:

<p align="left">
  <img src="../../../assets/images/ESP32S3RoundDevBoard/gpio summary table.png" alt="ESP32-S3 Round Dev Board GPIO summary table" width="85%">
</p>

#### Display (QSPI)

All three panel options share the same QSPI bus on the board, so the pin assignment below is identical no matter which panel is fitted.

| Signal | ESP32-S3 Pin | Description |
| :--- | :--- | :--- |
| LCD_CS | IO12 | Chip select, active low. |
| LCD_CLK | IO48 | QSPI clock. |
| LCD_DA0 | IO13 | QSPI data line 0. |
| LCD_DA1 | IO47 | QSPI data line 1. |
| LCD_DA2 | IO21 | QSPI data line 2. |
| LCD_DA3 | IO14 | QSPI data line 3. |
| LCD_RST | IO11 | Panel reset. |
| LCDBLK | IO45 | Backlight and display power enable. |

The CO5300 is addressed in QSPI mode with four data lines. In the shipped example the controller window is set to 471 x 466 while the visible AMOLED aperture is 466 x 466, so the frame buffer is allocated at 471 x 466 and the panel is driven with 16 bits per pixel.

#### Touch

| Signal | ESP32-S3 Pin | Description |
| :--- | :--- | :--- |
| SDA | IO17 | I2C data line, shared with the IMU and the RTC. |
| SCL | IO18 | I2C clock line, shared with the IMU and the RTC. |
| TP_INT | IO9 | Touch interrupt output. |
| TP_RST | IO10 | Touch controller reset. |

#### Audio

| Function | Signal | ESP32-S3 Pin |
| :--- | :--- | :--- |
| Microphone | MICSCK | IO1 |
| Microphone | MICSD | IO2 |
| Microphone | MICWS | IO42 |
| Speaker (I2S) | DIN | IO4 |
| Speaker (I2S) | BCK | IO5 |
| Speaker (I2S) | LRCK | IO6 |
| Speaker (I2S) | CTRL | IO7 |

#### Sensors, Storage and Host Interfaces

| Function | Signal | ESP32-S3 Pin |
| :--- | :--- | :--- |
| IMU | Interrupt 1 | IO15 |
| IMU | Interrupt 2 | IO16 |
| RTC | INT | IO46 |
| I2C bus | SDA | IO17 |
| I2C bus | SCL | IO18 |
| TF card | CMD | IO38 |
| TF card | CLK | IO39 |
| TF card | DAT0 | IO40 |
| TF card | CD | IO41 |
| USB / UART | U0TXD | IO43 |
| USB / UART | U0RXD | IO44 |
| USB (native) | D- | IO19 |
| USB (native) | D+ | IO20 |
| RGB LED and BOOT | RGB&BOOT | IO0 |
| Expansion | Free IO | IO3, IO8 |

!!! warning "Shared and reserved pins"
    - The I2C bus on **IO17 / IO18** is shared by the touch controller, the 6-axis IMU and the RTC. Add new I2C devices on the same bus and check for address conflicts.
    - **IO0** is shared between the BOOT button and the RGB LED status line, which is why the specification groups them as **RGB&BOOT**.
    - **IO43 / IO44** are the ESP32-S3 UART0 pins. Both the USB interface and the expansion pads reach them, so a peripheral wired to IO43 / IO44 competes with the default serial console.
    - **IO3** and **IO8** are the two pins left free for user expansion. The 1.5-inch example reuses them as a rotary encoder input.
    - Only one display connector is populated at a time; the three footprints are alternatives, not a multi-panel setup.

### 2.3 Board Dimensions

<p align="left">
  <img src="../../../assets/images/ESP32S3RoundDevBoard/dimension drawing.png" alt="ESP32-S3 Round Dev Board dimension drawing" width="55%">
</p>

The PCB is a circle 70 mm in diameter. Panel module outlines differ per option: 44.3 x 44.3 x 2.405 mm for the 1.5-inch AMOLED, 45.93 x 46.35 mm for the 1.75-inch AMOLED and 48.08 x 49.95 x 2.12 mm for the 1.85-inch TFT.

## 3. Software

The repository ships standalone ESP-IDF projects, one per panel option. The 1.5-inch AMOLED build lives in `examples/esp-idf/ESP32-S3-Round-Dev-Board/viewe1.5` and bundles every driver it needs as a local component, so no external BSP download is required.

### 3.1 Software Examples

Examples are available in the [GitHub Repository](https://github.com/VIEWESMART/ESP32-S3-Round-Dev-Board/tree/main/examples/esp-idf/ESP32-S3-Round-Dev-Board).

| Framework | Example Path | Description |
| :--- | :--- | :--- |
| esp-idf | `examples/esp-idf/.../viewe1.5` | Bring-up for this board: CO5300 QSPI panel, CST816S-compatible touch over I2C, QMI8658 IMU, SD3078 RTC, NS4168 audio, SD card, RGB LED, INMP441 microphone and an LVGL demo UI. |
| esp-idf | `examples/esp-idf/.../viewe1.75` | Same firmware layout for the 1.75-inch AMOLED option (CO5300 plus CST9217 touch). |
| esp-idf | `examples/esp-idf/.../viewe1.8` | Same firmware layout for the 1.85-inch TFT option (ST77916). |
| esp-idf | `examples/esp-idf/.../viewe1.6` | Additional panel option (ST77903 QSPI plus CST3530 touch). |
| esp-idf | `examples/esp-idf/.../viewe2.1` | Additional panel option (ST7801N). |

Each project vendors these components under `components/`: `esp_lcd_co5300` (panel), `esp_lcd_touch` and `esp_lcd_touch_cst816s` (touch), `lvgl`, `qmi8658`, `sd3078`, `ns4168`, `inmp441`, `rgbled` and `sdcard`.

### 3.2 Getting Started

#### 3.2.1 Preparation

- **Hardware:** ESP32-S3 Round Dev Board with the 1.5-inch AMOLED fitted, a USB-C cable, and optionally an 8 Ω / 2 W speaker and a rechargeable RTC cell.
- **Software:** VS Code with the ESP-IDF extension and ESP-IDF v5.1 / 5.2 / 5.3, or the standalone `idf.py` toolchain.
- **Power:** Use a 5 V / 1 A supply. Peak current while charging is around 1000 mA.

#### 3.2.2 ESP-IDF Setup

1. **Open the example folder in VS Code** — `examples/esp-idf/ESP32-S3-Round-Dev-Board/viewe1.5`.
2. **Set the target** to `esp32s3`.
3. **Build, flash and monitor.** From the command line inside the example directory:

    ```bash
    idf.py set-target esp32s3
    idf.py build flash monitor
    ```

!!! tip "Bring-up order"
    Confirm the panel lights up and touch responds before adding application code. The I2C bus on IO17 / IO18 carries the touch controller, the IMU and the RTC, so an early scan of that bus tells you whether the panel flex is seated correctly.

If the board does not enter download mode automatically, hold **BOOT**, tap **RST**, release **BOOT**, then start the flash.

#### 3.2.3 Arduino Setup

The repository does not ship Arduino examples for this board, and the board is not yet in the Espressif `ESP32_Display_Panel` supported-board list, so there is no ready-made `BOARD_VIEWE_*` macro to select. Arduino is still usable — the panel is a standard QSPI CO5300 device — but you supply the pin map yourself:

1. **Install [Arduino IDE](https://www.arduino.cc/en/software)** and add the ESP32 board package:

    ```text
    https://espressif.github.io/arduino-esp32/package_esp32_index.json
    ```

2. **Select the board:** target `ESP32S3 Dev Module`, with Flash Size `16MB (128Mb)` and PSRAM `OPI PSRAM`. Getting the PSRAM mode wrong leads to a board that boots but never allocates a frame buffer.
3. **Install the libraries:** `ESP32_Display_Panel` and `lvgl` (v8.4.0 recommended).
4. **Configure the board:** in `esp_panel_board_supported_conf.h`, keep `ESP_PANEL_BOARD_DEFAULT_USE_SUPPORTED` at `0` and fill in `esp_panel_board_custom_conf.h` using the pin table in [2.2 GPIO Definition](#22-gpio-definition-pinout) — QSPI with a single CS line for the panel, and I2C on IO17 / IO18 for touch.
5. **Compile and upload** with the USB-C cable connected.

!!! warning "QSPI is not RGB"
    Do not enable the avoid-tearing modes that are meant for RGB panels, and do not set `LV_COLOR_16_SWAP` unless the panel colours come out inverted. This board talks to the panel over QSPI, which behaves differently from the RGB bus used on the larger square and rectangular modules.

#### 3.2.4 PlatformIO Setup

PlatformIO works the same way as the Arduino route: use a generic ESP32-S3 environment and provide the board definition yourself.

1. Create a `platformio.ini` with `board = esp32-s3-devkitc-1` and set `board_build.arduino.memory_type = qio_opi` so the octal PSRAM is used.
2. Add `-D BOARD_HAS_PSRAM` and `-D ARDUINO_USB_CDC_ON_BOOT=false` to `build_flags` so the serial console stays on UART0.
3. Add `ESP32_Display_Panel` and `lvgl` to `lib_deps`, then configure the custom board header as in the Arduino route.

## 4. Related Documents & Resources

| Document | Link |
| :--- | :--- |
| Product Specification (board) | [ESP32 S3 Round Dev Board SPEC V1.1](../../../assets/datasheet/ESP32%20S3%20Round%20Dev%20Board%20SPEC%20V1.1.pdf) |
| Schematic Diagram | [SCH-ESP32S3RoundDevBoard.png](../../../assets/schematic/SCH-ESP32S3RoundDevBoard.png) |
| AMOLED Panel Datasheet | [ALL-UE015WV-RB24-A021A V1.0](../../../assets/datasheet/display/ALL-UE015WV-RB24-A021A%20V1.0%20SPEC.pdf) |
| AMOLED Driver Datasheet | [CO5300](../../../assets/datasheet/display/CO5300.pdf) |
| ESP32-S3-WROOM-1 Datasheet (EN) | [esp32-s3-wroom-1_datasheet_en.pdf](../../../assets/datasheet/chip/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf) |
| ESP32-S3-WROOM-1 Datasheet (CN) | [esp32-s3-wroom-1_datasheet_cn.pdf](../../../assets/datasheet/chip/esp32-s3-wroom-1_wroom-1u_datasheet_cn.pdf) |
| 6-Axis IMU Datasheet | [QMI8658A.pdf](../../../assets/datasheet/peripheral/QMI8658A.pdf) |

## 5. Firmware Download

1. Open the `tools` folder of the repository and locate the ESP32 flash download tool (`flash_download_tool_3.9.5`). Extract and launch it.
2. Select the chip type `ESP32-S3` and the download mode, then click **OK**. Follow the numbered steps 1 → 2 → 3 → 4 → 5 shown below to burn the firmware. If the download fails, hold the **BOOT** button and try again.
3. Select the binary to burn. Prebuilt binaries, when published, are placed in the repository's `firmware` directory — check the version notes inside and choose the appropriate build.

If no prebuilt binary is available, build and flash from source instead — see [3.2 Getting Started](#32-getting-started).

<p align="center" width="100%">
  <img src="../../../assets/images/Espressif/esp32-s3-firmware-download-1.png" alt="Firmware Download Step 1">
  <img src="../../../assets/images/Espressif/esp32-s3-firmware-download-2.png" alt="Firmware Download Step 2">
</p>

## 6. FAQ

??? question "Which display driver and touch controller does this board use?"
    The 1.5-inch build pairs a 466x466 AMOLED panel with a `CO5300AF-42` display driver over QSPI, and capacitive touch handled by a `CST9217` controller on I2C at IO17 / IO18. The shipped ESP-IDF example vendors the `esp_lcd_co5300` display driver and a CST816S-compatible touch driver; both sit on the same I2C bus as the IMU and the RTC.

??? question "How does this panel compare with the other round options?"
    All three round panels share the same board, the same 466x466 or 360x360 QSPI pinout and a capacitive touch layer. This one is the smallest and dimmest at 44.3 x 44.3 mm and 450 cd/m², with a 38.3052 x 38.3052 mm active area. The 1.75-inch AMOLED is larger and roughly 1.5x brighter at 700 cd/m², and the 1.85-inch TFT is the largest at 45.68 x 45.68 mm but drops to 127 PPI against 309 PPI on both AMOLED panels.

??? question "After reading the tutorials, I still don't know how to build the programming environment. What should I do?"
    Refer to the [VIEWE FAQ](../../support/faq.md) document for detailed environment setup instructions.

??? question "Why does the Arduino IDE prompt me to update library files when I open it? Should I update them?"
    Choose **not** to update the library files. Different versions of library files may not be mutually compatible, so updating them is not recommended.

??? question "Why is there no serial data output on the UART pins? Is my board defective?"
    The default project configuration routes UART0 to the USB interface for debugging. IO43 and IO44 carry the same UART0 signals onto the expansion pads, so they stay silent unless you reconfigure the console. Set `ARDUINO_USB_CDC_ON_BOOT=false` in PlatformIO, or choose `USB CDC On Boot: Disabled` in the Arduino `Tools` menu.

??? question "Why does the board keep failing to download a program?"
    Hold the `BOOT` button while starting the download, or hold `BOOT`, tap `RST`, and then release `BOOT`. This forces the ESP32-S3 into its serial bootloader.

??? question "Can I fit a different round panel to the same board?"
    Yes. The PCB carries three separate QSPI display connectors — one each for the 1.5-inch AMOLED, the 1.75-inch AMOLED and the 1.85-inch TFT — but only one panel is mounted at a time. Each panel size has its own bring-up project under `examples/esp-idf/ESP32-S3-Round-Dev-Board/`, and the QSPI pin assignment is identical across all three, so switching panels means switching projects rather than rewiring.

??? question "The board draws around 1 A from USB. Is that normal?"
    That is the charging current for the battery, not the running current. The board is specified at roughly 1000 mA while charging at 5 V and about 130 mA when running without charging. A 5 V / 1 A adapter is the recommended supply.

!!! info "Can't find what you need?"
    If you need more Products or Resource or Support, please contact our team:

    [**:material-archive-arrow-down: Resource Center**](../../support/resource.md){ .md-button .md-button--primary }
    [**:material-magnify: More Products**](../esp32/index.md){ .md-button  }
    [**:material-email: Contact Support**](mailto:support@viewedisplay.com){ .md-button }
