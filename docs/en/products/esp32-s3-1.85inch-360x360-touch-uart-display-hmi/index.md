---
title: VIEWE 1.85" 360x360 TFT ESP32-S3 Round Smart Display
description: A 70 mm round ESP32-S3 smart display dev board with a 1.85-inch 360x360 a-Si TFT panel, ST77916 QSPI driver, capacitive touch, I2S microphone and class-D audio, 6-axis IMU, SD3078 RTC and TF card slot.
---

# 1.85" 360x360 TFT ESP32-S3 Round Smart Display

<div class="grid cards" markdown>

-   **1.85" 360x360 TFT · ESP32-S3 Round Dev Board**
    ---
    The TFT option in the round series: a Ø70 mm circular development board built around the ESP32-S3-WROOM-1 (N16R8) with a 1.85-inch 360x360 a-Si TFT panel driven by an ST77916 controller over QSPI, plus capacitive touch, I2S digital microphone, class-D audio with speaker connector, 6-axis IMU, SD3078 real-time clock and a TF card slot.

    [:material-arrow-left: Back to Series](../esp32/){ .md-button }
    [:material-cart: Official Store](https://viewedisplay.com/product/esp32-s3-1-85-inch-tft-touch-screen-uart-smart-display-dev-board/){ .md-button .md-button--primary }
    [:material-github: GitHub Repo](https://github.com/VIEWESMART/ESP32-S3-Round-Dev-Board){ .md-button }

</div>

<div align="center">
  <img src="../../../assets/images/ESP32S3RoundDevBoard/1.85 inch 360x360 round tft esp32 s3 smart display.jpg" width="100%" alt="1.85 inch 360x360 round TFT ESP32-S3 smart display front and back">
</div>

---

## 1. Introduction

The ESP32-S3 Round Dev Board is a circular, 70 mm diameter development board that carries the ESP32-S3-WROOM-1 (N16R8) module on one side and a single round display on the other. The same PCB accepts three different round panels, and this page covers the **1.85-inch TFT** build: a 360x360 a-Si TFT panel driven by an ST77916 controller over a 4-bit QSPI bus, with capacitive touch on I2C.

This is the largest of the three round panels, with a 45.68 x 45.68 mm display area, and the only one that uses a transmissive TFT rather than an emissive AMOLED. At 127 PPI the pixels are visibly larger than on the two AMOLED options, which makes it a good fit for gauge-style interfaces, large-type readouts and cost-sensitive products where a full circular graph is more useful than a high pixel density. Typical brightness is 400 cd/m².

The board keeps the full peripheral set: digital MEMS microphone, I2S DAC and class-D amplifier for an 8 Ω / 2 W speaker, 6-axis IMU, SD3078 real-time clock with a rechargeable backup-cell socket, TF card slot and an RGB status LED. Power comes from USB Type-C or a battery, with automatic changeover and charging.

The repository ships standalone ESP-IDF bring-up projects for each panel size, and the 1.85-inch build maps to `examples/esp-idf/ESP32-S3-Round-Dev-Board/viewe1.8`.

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
| Size | 1.85 inch |
| Resolution | 360 x 360 |
| Panel type | a-Si TFT, normally black |
| Interface | QSPI (4 data lines) |
| Driver IC | ST77916 |
| Touch IC | CST816S |
| Touch interface | Capacitive, I2C |
| Brightness | 400 cd/m² (typ.) |
| Display color | 262 K (24-bit) |
| Pixel pitch | 0.2 mm |
| Pixel density | 127 PPI |
| Display area | 45.68 (H) x 45.68 (V) mm |
| Module outline | 48.08 (H) x 49.95 (V) x 2.12 (T) mm |
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
- **Operating current:** 1100 mA while charging at VCC = 5 V; 210 mA in non-charging operation. A 5 V / 1 A supply is recommended.
- **Board size:** Ø70 mm circular PCB.
- **Operating temperature:** -20 ~ 70 ℃
- **Storage temperature:** -30 ~ 80 ℃
- **Environmental:** RoHS 2.0 and halogen-free.
- **ESD:** ±4 kV contact, ±8 kV air.

### 1.2 Applications

A large, bright circular TFT with an audio front end, battery support and motion sensing suits products that need a legible round readout rather than a photographic image:

- Round gauges, meters and instrument dials
- AI voice assistants and desktop companion devices
- Smart home control dials, thermostats and scene controllers
- Industrial HMI for pumps, valves and environmental monitors
- Wearable and pendant-format concepts
- Portable, battery-powered sensor readouts

## 2. Hardware Description

### 2.1 Module Overview

The board is a single circular PCB with one panel mounted on the front. The numbered callouts below mark each functional block on the back of the board:

<p align="left">
  <img src="../../../assets/images/ESP32S3RoundDevBoard/module overview.jpg" alt="ESP32-S3 Round Dev Board module overview" width="80%">
</p>

| No. | Component | Description |
| :--- | :--- | :--- |
| ① | ESP32-S3-WROOM-1 | Main SoC module, 16 MB flash / 8 MB PSRAM. |
| ② | 1.5-inch Display Interface | QSPI FPC connector; alternative panel size. |
| ③ | 1.75-inch Display Interface | QSPI FPC connector; alternative panel size. |
| ④ | 1.85-inch Display Interface | QSPI FPC connector for this build. |
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

The ST77916 is addressed in QSPI mode with four data lines, and the shipped example drives it at 360 x 360 with 16 bits per pixel.

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
    - **IO3** and **IO8** are the two pins left free for user expansion.
    - The 1.85-inch example also maps an optional rotary encoder to **IO5 / IO6**. The GPIO summary table assigns those same pins to the I2S speaker (BCK / LRCK), so do not enable the encoder and the audio output at the same time.
    - Only one display connector is populated at a time; the three footprints are alternatives, not a multi-panel setup.

### 2.3 Board Dimensions

<p align="left">
  <img src="../../../assets/images/ESP32S3RoundDevBoard/dimension drawing.png" alt="ESP32-S3 Round Dev Board dimension drawing" width="55%">
</p>

The PCB is a circle 70 mm in diameter. The 1.85-inch TFT module measures 48.08 x 49.95 x 2.12 mm and its active area is 45.68 x 45.68 mm, so it is the widest of the three options and overhangs the board outline slightly. For comparison, the 1.5-inch AMOLED module is 44.3 x 44.3 x 2.405 mm and the 1.75-inch AMOLED module is 45.93 x 46.35 mm.

## 3. Software

The repository ships standalone ESP-IDF projects, one per panel option. The 1.85-inch TFT build lives in `examples/esp-idf/ESP32-S3-Round-Dev-Board/viewe1.8` and bundles the ST77916 panel driver as a local component, so no external BSP download is required.

### 3.1 Software Examples

Examples are available in the [GitHub Repository](https://github.com/VIEWESMART/ESP32-S3-Round-Dev-Board/tree/main/examples/esp-idf/ESP32-S3-Round-Dev-Board).

| Framework | Example Path | Description |
| :--- | :--- | :--- |
| esp-idf | `examples/esp-idf/.../viewe1.8` | Bring-up for this board: ST77916 QSPI panel, QMI8658 IMU, SD3078 RTC and an LVGL demo UI. |
| esp-idf | `examples/esp-idf/.../viewe1.5` | Same firmware layout for the 1.5-inch AMOLED option (CO5300 plus CST816S-compatible touch). |
| esp-idf | `examples/esp-idf/.../viewe1.75` | Same firmware layout for the 1.75-inch AMOLED option (CO5300 plus CST9217 touch). |
| esp-idf | `examples/esp-idf/.../viewe1.6` | Additional panel option (ST77903 QSPI plus CST3530 touch). |
| esp-idf | `examples/esp-idf/.../viewe2.1` | Additional panel option (ST7801N). |

The 1.85-inch project vendors these components under `components/`: `esp_lcd_st77916` (panel), `lvgl`, `qmi8658` (IMU), `sd3078` (RTC).

!!! note "Touch driver is not bundled in this project"
    The touch controller sits on the shared I2C bus at IO17 / IO18 with address pins already wired, so adding it is a matter of dropping in the touch component. The `esp_lcd_touch_cst816s` component vendored in the 1.5-inch project matches the CST816S controller specified for this panel and can be copied across; wire it to SDA IO17, SCL IO18, RST IO10 and INT IO9.

### 3.2 Getting Started

#### 3.2.1 Preparation

- **Hardware:** ESP32-S3 Round Dev Board with the 1.85-inch TFT fitted, a USB-C cable, and optionally an 8 Ω / 2 W speaker and a rechargeable RTC cell.
- **Software:** VS Code with the ESP-IDF extension and ESP-IDF v5.1 / 5.2 / 5.3, or the standalone `idf.py` toolchain.
- **Power:** Use a 5 V / 1 A supply. Peak current while charging is around 1100 mA, and this panel draws noticeably more than the AMOLED options when running — about 210 mA against 130 mA.

#### 3.2.2 ESP-IDF Setup

1. **Open the example folder in VS Code** — `examples/esp-idf/ESP32-S3-Round-Dev-Board/viewe1.8`.
2. **Set the target** to `esp32s3`.
3. **Build, flash and monitor.** From the command line inside the example directory:

    ```bash
    idf.py set-target esp32s3
    idf.py build flash monitor
    ```

!!! tip "Bring-up order"
    Confirm the panel lights up before adding application code. If the backlight comes on but the image stays blank, check the QSPI data lines and the panel reset before suspecting the driver.

If the board does not enter download mode automatically, hold **BOOT**, tap **RST**, release **BOOT**, then start the flash.

#### 3.2.3 Arduino Setup

The repository does not ship Arduino examples for this board, and the board is not yet in the Espressif `ESP32_Display_Panel` supported-board list, so there is no ready-made `BOARD_VIEWE_*` macro to select. Arduino is still usable — the panel is a standard QSPI ST77916 device — but you supply the pin map yourself:

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
| TFT Panel Datasheet | [ALL-UEOL018VG-RA31-A001A V1.0](../../../assets/datasheet/display/ALL-UEOL018VG-RA31-A001A%20V1.0%20SPEC.pdf) |
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
    The 1.85-inch build pairs a 360x360 a-Si TFT panel with an `ST77916` display driver over QSPI, and capacitive touch handled by a `CST816S` controller on I2C at IO17 / IO18. The shipped ESP-IDF example vendors the `esp_lcd_st77916` panel driver; the touch driver is not bundled with this particular project and can be carried over from the 1.5-inch project.

??? question "How does this panel compare with the two AMOLED options?"
    It is the largest of the three at 45.68 x 45.68 mm active area, but the lowest in pixel density at 127 PPI, against 309 PPI on both AMOLED panels. Typical brightness is 400 cd/m². It also costs more current to run — roughly 210 mA against 130 mA for the AMOLED builds.

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
    That is the charging current for the battery, not the running current. The board is specified at roughly 1100 mA while charging at 5 V and about 210 mA when running without charging. A 5 V / 1 A adapter is the recommended supply.

!!! info "Can't find what you need?"
    If you need more Products or Resource or Support, please contact our team:

    [**:material-archive-arrow-down: Resource Center**](../../support/resource.md){ .md-button .md-button--primary }
    [**:material-magnify: More Products**](../esp32/index.md){ .md-button  }
    [**:material-email: Contact Support**](mailto:support@viewedisplay.com){ .md-button }
