# FAQ for ESP32 with Arduino

## 📂 Library and Directory Settings

### Where is the directory for Arduino libraries?

You can find and modify the directory path for Arduino libraries by selecting `File` \> `Preferences` \> `Settings` \> `Sketchbook location` from the menu bar in the Arduino IDE.

### Where are the installation directory for arduino-esp32 and the SDK located?

The default installation path for **arduino-esp32** depends on your operating system:

\=== "Windows"
`C:\Users\<user name>\AppData\Local\Arduino15\packages\esp32`

\=== "Linux"
`~/.arduino15/packages/esp32`

\!\!\! info "SDK Location"
The SDK for **arduino-esp32 v3.x.x** version is located in the `tools/esp32-arduino-libs/idf-release_x` directory within the default installation path.

-----

## 📥 Installation Guide

### How to Install ESP32\_Display\_Panel in Arduino IDE?

You can choose one of the following methods to install the library:

\=== "Online Installation"
1\. Navigate to `Sketch` \> `Include Library` \> `Manage Libraries...` in the Arduino IDE.
2\. Search for `ESP32_Display_Panel`.
3\. Click the **Install** button.

\=== "Manual Installation"
1\. Download the required version of the `.zip` file from [ESP32\_Display\_Panel GitHub](https://github.com/esp-arduino-libs/ESP32_Display_Panel).
2\. Navigate to `Sketch` \> `Include Library` \> `Add .ZIP Library...` in the Arduino IDE.
3\. Select the downloaded `.zip` file and click **Open**.

\!\!\! tip "Official Guides"
You can also refer to the guides on library installation in the [Arduino IDE v1.x.x](https://docs.arduino.cc/software/ide-v1/tutorials/installing-libraries) or [Arduino IDE v2.x.x](https://docs.arduino.cc/software/ide-v2/tutorials/ide-v2-installing-a-library) documentation.

-----

## 🛠 Troubleshooting

### How to fix screen drift issue when driving RGB LCD with ESP32-S3?

When encountering screen drift issues, follow these steps to resolve them:

1.  **Refer to Documentation**: Understand the issue description in detail via [this document](https://docs.espressif.com/projects/esp-faq/en/latest/software-framework/peripherals/lcd.html#why-do-i-get-drift-overall-drift-of-the-display-when-esp32-s3-is-driving-an-rgb-lcd-screen).
2.  **Enable `Bounce Buffer + XIP on PSRAM`**:
      * **Step 1**: Download the "high\_perf" version of the SDK from [arduino-esp32-sdk](https://github.com/esp-arduino-libs/arduino-esp32-sdk) and replace it in the [installation directory](https://www.google.com/search?q=%23where-are-the-installation-directory-for-arduino-esp32-and-the-sdk-located).
      * **Step 2**: For supported development boards, `ESP_PANEL_LCD_RGB_BOUNCE_BUF_SIZE` is set to `(ESP_PANEL_LCD_WIDTH * 10)` by default. If issues persist, increase the size.
      * **Step 3**: For custom boards, confirm in `ESP_Panel_Board_Custom.h` if `ESP_PANEL_LCD_RGB_BOUNCE_BUF_SIZE` is non-zero.
      * **Step 4**: For independent drivers, manually set the size.
      * **Step 5**: For LVGL applications, assign the RGB initialization task and the `lv_timer_handler()` task to the **same core**.

#### Example Code for Bounce Buffer

\=== "Using ESP\_Panel Driver"
` cpp ESP_Panel *panel = new ESP_Panel(); panel->init(); // Start ESP_PanelBus_RGB *rgb_bus = static_cast<ESP_PanelBus_RGB *>(panel->getLcd()->getBus()); // Note: size * N (even) = width * height rgb_bus->configRgbBounceBufferSize((ESP_PANEL_LCD_WIDTH * 20)); // End panel->begin();  `

\=== "Using Independent Driver"
` cpp ESP_PanelBus_RGB *lcd_bus = new ESP_PanelBus_RGB(...); // Start // Note: size * N (even) = width * height lcd_bus->configRgbBounceBufferSize(EXAMPLE_LCD_WIDTH * 10); // End lcd_bus->begin();  `

-----

## 🚀 PlatformIO Support

### How to Use ESP32\_Display\_Panel on PlatformIO?

Refer to the [PlatformIO example](https://github.com/VIEWESMART/VIEWE-FAQ/blob/main/Arduino-FAQ/examples/PlatformIO). It is configured for **ESP32 Smart Display** and **ESP32 Dev Boards** by default. Modify the `boards/ESP-LCD.json` file as needed for your specific hardware.

-----

## 🎨 LVGL Configuration

### How to add an LVGL library and how to configure?

LVGL features and parameters are adjusted via the `lv_conf.h` file.

#### 1\. Configuration File Search Rules

  * **arduino-esp32 v3**: Searches in `Current project directory` \> `Arduino library directory`.
  * If no file is found, a compilation warning will trigger.
  * Ensure at least one directory contains `lv_conf.h`.

#### 2\. Configuration Steps

1.  **Get Template**: Navigate to the `lvgl` folder in your [Arduino library directory](https://www.google.com/search?q=%23where-is-the-directory-for-arduino-libraries).
2.  **Rename**: Copy `lv_conf_template.h` to your target directory and rename it to `lv_conf.h`.
3.  **Enable**: Open `lv_conf.h` and change the first `#if 0` to `#if 1`.

#### 3\. Common Configuration Items

| Setting | Recommended Value | Description |
| :--- | :--- | :--- |
| `LV_COLOR_DEPTH` | `16` | 16-bit color (RGB565). Set to `32` for ARGB8888. |
| `LV_COLOR_16_SWAP` | `0` or `1` | Set to `1` for SPI/QSPI LCDs (e.g., ESP32-C3-LCDkit). |
|`LV_COLOR_SCREEN_TRANSP`|`1`|LCD with alpha needs to set to 1|
| `LV_MEM_CUSTOM` | `1` | Use malloc/free for better performance. |
|`LV_MEMCPY_MEMSET_STD `|`1`|Use standard library functions|
|`V_FONT_MONTSERRAT_N`|`1`|Enable required built-in fonts (replace N with font size)|
| `LV_USE_PERF_MONITOR`| `1` | Display CPU usage and FPS. |
| `LV_USE_LOG` | `1` | Enable logging. |
| `LV_LOG_PRINTF `|`1`|Use printf for log output|
| `LV_ATTRIBUTE_FAST_MEM`| `IRAM_ATTR` | Improve performance using SRAM. |

#### 4\. Using LVGL Examples and Demos

1.  Copy the `demos` and `examples` folders from the lvgl library to your project's `src` folder.
2.  Please set the corresponding macros

```c
/*==================
* EXAMPLES
*==================*/

/*Enable the examples to be built with the library*/
#define LV_BUILD_EXAMPLES 1

/*===================
 * DEMO USAGE
 ====================*/

/*Show some widget. It might be required to increase `LV_MEM_SIZE` */
#define LV_USE_DEMO_WIDGETS 1
#if LV_USE_DEMO_WIDGETS
#define LV_DEMO_WIDGETS_SLIDESHOW 0
#endif

/*Demonstrate the usage of encoder and keyboard*/
#define LV_USE_DEMO_KEYPAD_AND_ENCODER 0

/*Benchmark your system*/
#define LV_USE_DEMO_BENCHMARK 0
#if LV_USE_DEMO_BENCHMARK
/*Use RGB565A8 images with 16 bit color depth instead of ARGB8565*/
#define LV_DEMO_BENCHMARK_RGB565A8 0
#endif

/*Stress test for LVGL*/
#define LV_USE_DEMO_STRESS 0

/*Music player demo*/
#define LV_USE_DEMO_MUSIC 0
#if LV_USE_DEMO_MUSIC
    #define LV_DEMO_MUSIC_SQUARE    0
    #define LV_DEMO_MUSIC_LANDSCAPE 0
    #define LV_DEMO_MUSIC_ROUND     0
    #define LV_DEMO_MUSIC_LARGE     0
    #define LV_DEMO_MUSIC_AUTO_PLAY 0
#endif
```