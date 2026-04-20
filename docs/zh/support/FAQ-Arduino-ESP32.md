# ESP32 与 Arduino 常见问题解答 (FAQ)

## 📂 库与目录设置

### Arduino 库目录在哪里？

您可以通过 Arduino IDE 菜单栏选择 **文件 (File)** > **首选项 (Preferences)** > **设置 (Settings)** > **项目文件夹位置 (Sketchbook location)** 来查找和修改 Arduino 库的目录路径。

### arduino-esp32 及其 SDK 的安装目录在哪里？

**arduino-esp32** 的默认安装路径取决于您的操作系统：

=== "Windows"
    `C:\Users\<用户名>\AppData\Local\Arduino15\packages\esp32`

=== "Linux"
    `~/.arduino15/packages/esp32`

!!! info "SDK 位置"
    对于 **arduino-esp32 v3.x.x** 版本，SDK 位于默认安装路径下的 `tools/esp32-arduino-libs/idf-release_x` 目录中。

---

## 📥 安装指南

### 如何在 Arduino IDE 中安装 ESP32_Display_Panel？

您可以选择以下方法之一安装该库：

=== "在线安装"
    1. 在 Arduino IDE 中导航至 **项目 (Sketch)** > **包含库 (Include Library)** > **管理库... (Manage Libraries...)**。
    2. 搜索 `ESP32_Display_Panel`。
    3. 点击 **安装 (Install)** 按钮。

=== "手动安装"
    1. 从 [ESP32_Display_Panel GitHub](https://github.com/esp-arduino-libs/ESP32_Display_Panel) 下载所需版本的 `.zip` 文件。
    2. 在 Arduino IDE 中导航至 **项目 (Sketch)** > **包含库 (Include Library)** > **添加 .ZIP 库... (Add .ZIP Library...)**。
    3. 选择下载的 `.zip` 文件并点击 **打开 (Open)**。

!!! tip "官方指南"
    您也可以参考 [Arduino IDE v1.x.x](https://docs.arduino.cc/software/ide-v1/tutorials/installing-libraries) 或 [Arduino IDE v2.x.x](https://docs.arduino.cc/software/ide-v2/tutorials/ide-v2-installing-a-library) 文档中的库安装指南。

---

## 🛠 故障排除

### 如何解决使用 ESP32-S3 驱动 RGB LCD 时的屏幕漂移问题？

当遇到屏幕漂移问题时，请按照以下步骤解决：

1.  **参考文档**：通过[此文档](https://docs.espressif.com/projects/esp-faq/en/latest/software-framework/peripherals/lcd.html#why-do-i-get-drift-overall-drift-of-the-display-when-esp32-s3-is-driving-an-rgb-lcd-screen)详细了解问题描述。
2.  **启用 `Bounce Buffer + XIP on PSRAM` 特性**：
    * **步骤 1**：从 [arduino-esp32-sdk](https://github.com/esp-arduino-libs/arduino-esp32-sdk) 下载 "high_perf" 版本的 SDK，并替换[安装目录](https://www.google.com/search?q=%23where-are-the-installation-directory-for-arduino-esp32-and-the-sdk-located)中的原文件。
    * **步骤 2**：对于受支持的开发板，默认已将 `ESP_PANEL_LCD_RGB_BOUNCE_BUF_SIZE` 设置为 `(ESP_PANEL_LCD_WIDTH * 10)`。如果问题依旧，请增大该数值。
    * **步骤 3**：对于自定义开发板，请确认 `ESP_Panel_Board_Custom.h` 文件中 `ESP_PANEL_LCD_RGB_BOUNCE_BUF_SIZE` 是否设置为非零值。
    * **步骤 4**：如果使用独立驱动，请手动设置该缓冲区大小。
    * **步骤 5**：对于 LVGL 应用，请将初始化 RGB 外设的任务和运行 `lv_timer_handler()` 的任务分配给 **同一个 CPU 核心**。

#### Bounce Buffer 示例代码

=== "使用 ESP_Panel 驱动"
    ```cpp
    ESP_Panel *panel = new ESP_Panel();
    panel->init();
    // 开始
    ESP_PanelBus_RGB *rgb_bus = static_cast<ESP_PanelBus_RGB *>(panel->getLcd()->getBus());
    // 注意：size * N (N 为偶数) = 宽度 * 高度
    rgb_bus->configRgbBounceBufferSize((ESP_PANEL_LCD_WIDTH * 20));
    // 结束
    panel->begin();
    ```

=== "使用独立驱动"
    ```cpp
    ESP_PanelBus_RGB *lcd_bus = new ESP_PanelBus_RGB(...);
    // 开始
    // 注意：size * N (N 为偶数) = 宽度 * 高度
    lcd_bus->configRgbBounceBufferSize(EXAMPLE_LCD_WIDTH * 10);
    // 结束
    lcd_bus->begin();
    ```

---

## 🚀 PlatformIO 支持

### 如何在 PlatformIO 上使用 ESP32_Display_Panel？

请参考 [PlatformIO 示例](https://github.com/VIEWESMART/VIEWE-FAQ/blob/main/Arduino-FAQ/examples/PlatformIO)。该示例默认配置适用于 **ESP32 智能显示屏** 和 **ESP32 开发板**。请根据您的具体硬件修改 `boards/ESP-LCD.json` 文件。

---

## 🎨 LVGL 配置

### 如何添加 LVGL 库以及如何配置？

LVGL 的功能和参数是通过 `lv_conf.h` 文件进行调整的。

#### 1. 配置文件搜索规则

* **arduino-esp32 v3**：搜索顺序为 `当前项目目录` > `Arduino 库目录`。
* 如果未找到文件，将触发编译警告。
* 请确保至少有一个目录包含 `lv_conf.h`。

#### 2. 配置步骤

1.  **获取模板**：导航至 [Arduino 库目录](https://www.google.com/search?q=%23where-is-the-directory-for-arduino-libraries) 中的 `lvgl` 文件夹。
2.  **重命名**：将 `lv_conf_template.h` 复制到您的目标目录，并重命名为 `lv_conf.h`。
3.  **启用**：打开 `lv_conf.h`，将第一行 `#if 0` 改为 `#if 1`。

#### 3. 常用配置项

| 设置项 | 推荐值 | 说明 |
| :--- | :--- | :--- |
| `LV_COLOR_DEPTH` | `16` | 16 位颜色 (RGB565)。若支持 ARGB8888 请设为 `32`。 |
| `LV_COLOR_16_SWAP` | `0` 或 `1` | SPI/QSPI LCD（如 ESP32-C3-LCDkit）需设为 `1`。 |
| `LV_COLOR_SCREEN_TRANSP` | `1` | 具有 alpha 通道的 LCD 需设为 1。 |
| `LV_MEM_CUSTOM` | `1` | 使用 malloc/free 以获得更好性能。 |
| `LV_MEMCPY_MEMSET_STD` | `1` | 使用标准库函数。 |
| `V_FONT_MONTSERRAT_N` | `1` | 启用内置字体（将 N 替换为字号）。 |
| `LV_USE_PERF_MONITOR` | `1` | 显示 CPU 占用率和 FPS。 |
| `LV_USE_LOG` | `1` | 启用日志功能。 |
| `LV_LOG_PRINTF` | `1` | 使用 printf 输出日志。 |
| `LV_ATTRIBUTE_FAST_MEM` | `IRAM_ATTR` | 使用 SRAM 以提升性能。 |

#### 4. 使用 LVGL 示例与演示 (Demos)

1.  将 lvgl 库中的 `demos` 和 `examples` 文件夹复制到项目中的 `src` 文件夹下。
2.  请设置对应的宏开关：

```c
/*==================
* 示例 (EXAMPLES)
*==================*/

/* 允许将示例与库一起编译 */
#define LV_BUILD_EXAMPLES 1

/*===================
 * 演示使用 (DEMO USAGE)
 ====================*/

/* 显示部分组件。可能需要增大 `LV_MEM_SIZE` */
#define LV_USE_DEMO_WIDGETS 1
#if LV_USE_DEMO_WIDGETS
#define LV_DEMO_WIDGETS_SLIDESHOW 0
#endif

/* 演示编码器和键盘的使用 */
#define LV_USE_DEMO_KEYPAD_AND_ENCODER 0

/* 系统基准测试 */
#define LV_USE_DEMO_BENCHMARK 0
#if LV_USE_DEMO_BENCHMARK
/* 使用 16 位色深的 RGB565A8 图像代替 ARGB8565 */
#define LV_DEMO_BENCHMARK_RGB565A8 0
#endif

/* LVGL 压力测试 */
#define LV_USE_DEMO_STRESS 0

/* 音乐播放器演示 */
#define LV_USE_DEMO_MUSIC 0
#if LV_USE_DEMO_MUSIC
    #define LV_DEMO_MUSIC_SQUARE    0
    #define LV_DEMO_MUSIC_LANDSCAPE 0
    #define LV_DEMO_MUSIC_ROUND     0
    #define LV_DEMO_MUSIC_LARGE     0
    #define LV_DEMO_MUSIC_AUTO_PLAY 0
#endif
```