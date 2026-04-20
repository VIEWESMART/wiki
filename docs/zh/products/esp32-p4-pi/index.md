# ESP32-P4-Pi 开发套件


<div class="grid cards" markdown>

-   **ESP32-P4-Pi**
    ---
    基于 **VIEWE ESP32-P4-Core** 的**旗舰**开发板和智能屏，
    配备 7 英寸 **1024x600** DSI 显示屏，支持 Wi-Fi 6、H.264 硬件编码及丰富的工业接口。

    [:material-arrow-left: 返回系列列表](../esp32/){ .md-button }
    [:material-cart: 官方商城](https://viewedisplay.com/product/7-inch-1024x600-esp32-p4-wifi6-touch-smart-hmi-uart-display/){ .md-button .md-button--primary }
    [:material-github: GitHub 仓库](https://github.com/VIEWESMART/ESP32-P4-Pi/tree/main){ .md-button }

</div>

<div align="center"> 
  <img src="../../../assets/images/ESP32-P4-Pi/ESP32-p4-pi.png" width="45%" alt="正面视图">
  
</div>

---

## 1. 产品简介

**ESP32-P4-Pi-VIEWE** 开发板基于 **VIEWE ESP32-P4-Core** 模块设计，该模块集成了 ESP32-P4 和 ESP32-C6 芯片，支持 Wi-Fi 6 和蓝牙 5 无线连接。
开发板提供了多种人机界面（HMI）接口，包括 MIPI-CSI（集成图像信号处理器 ISP）、MIPI-DSI、SPI、I2S、I2C、LED PWM、MCPWM、RMT、ADC、UART 和 TWAI；支持 USB OTG 2.0 H5，预留 RJ45 以太网接口（可扩展 POE 以太网供电功能），并配备 40 针 GPIO 扩展接口。

### 1.1 产品特性
* **处理器**:
    * **VIEWE ESP32-P4-Core**: 该模组由ESP32-P4芯片提供RISC-V 双核高性能核心 @ 400MHz + 低功耗核心 @ 40MHz，搭配ESP32-C6芯片提供Wi-Fi 6 / BLE 5.0 协处理器 (通过 SDIO 连接)。
* **存储**:
    * 32MB PSRAM (合封)，16MB NOR Flash。
* **多媒体**:
    * **显示**: 7 英寸 IPS (1024x600)，MIPI-DSI (2-Lane) 15pin接口。
    * **摄像头**: MIPI-CSI 接口 (支持 1080P @ 30fps 输入)。
    * **视频**: 硬件 H.264 编码 / JPEG 解码。
    * **分离式音频方案**: ES7210 专做 4 路麦克风 ADC（采集），ES8311 单声道 CODEC（播放 + 辅助采集），配合 I2S/I2C 与主控通信，支持回声消除 AEC、远场语音唤醒。
* **外设接口**:
    * **连接**: USB 2.0 OTG (Type-A)，UART\USB (Type-C)。
    * **存储**: microSD 卡槽 (SDIO 3.0 高速模式)。
    * **扩展**: 2x20 Pin 排针 (引出 GPIO, I2C, SPI, UART)。
    * **其他**: WS2812B RGB 灯珠，板载 USB 转 UART 调试桥，以太网（RJ45），双麦克风，扬声器端子，RTC 电池端子。

### 1.2 应用场景
* 智能家居中控屏
* 工业 HMI 与自动化控制
* 边缘 AI 视觉与多媒体播放器

---

## 2. 硬件说明

### 2.1 模块概览
详细的板载元件布局如下图所示：

![板载布局](../../../assets/images/ESP32-P4-Pi/Module_definition.png)

| 编号 | 元件 | 说明 |
| :--- | :--- | :--- |
| **①** | **ESP32-P4-Core** | 主控芯片模组，内置ESP32-C6提供WIFI 6/蓝牙5(合封 16MB Flash，32MB PSRAM)。 |
| **②** | **RGB灯珠** | WS2812B 可编程灯珠。 |
| **③** | **以太网端口芯片** | 100Mbps 以太网相关芯片。 |
| **④** | **ES8311** | 音频编解码芯片。 |
| **⑤** | **麦克风1** | 数字麦克风。 |
| **⑥** | **扬声器接口** | MX1.25 2P连接器，支持8Ω2W扬声器。 |
| **⑦** | **Type-A接口** | USB OTG 2.0高速接口。 |
| **⑧** | **RJ45以太网端口** | 100Mbps 网口。 |
| **⑨** | **PoE模块接口** | 支持外接PoE模块连接，使用PoE供电。 |
| **⑩** | **DSI显示接口** | MIPI-2通道 15PIN接口。 |
| **⑪** | **麦克风2** | 数字麦克风。 |
| **⑫** | **按键** | boot按键上电时按住可进入下载模式，reset按键重启设备。 |
| **⑬** | **Type-C 接口** | 供电、程序烧录。 |
| **⑭** | **Type-C UART 接口** | 供电、程序烧录、调试。 |
| **⑮** | **CH340C** | USB 转 UART 芯片。 |
| **⑯** | **ES7210** | 音频采集芯片。 |
| **⑰** | **TF 卡槽** | ESP32-P4 引脚扩展排针。 |
| **⑱** | **ESP32-C6 UART 接口** | ESP32-C6 引脚扩展排针。 |
| **⑲** | **电源指示灯** | 5V 电源指示。 |
| **⑳** | **CSI摄像头接口** | MIPI 2 通道 CSI 接口。 |
| **㉑** | **6 轴姿态传感器** | QMI8658A（3 轴加速度计 + 3 轴陀螺仪）。 |
| **㉒** | **ESP32-C6 贴片天线** | SDIO 接口扩展 Wi-Fi 6 / 蓝牙 5。 |
| **㉓** | **40PIN 排针** | GPIO 扩展接口。 |


### 2.2 GPIO 定义 (引脚图)
2x20 排针的完整引脚映射如下：

![引脚定义](../../../assets/images/ESP32-P4-Pi/pin_definition.png)

### 2.3 GPIO 功能详情
P4 和 C6 GPIO 的详细功能列表：

![引脚介绍](../../../assets/images/ESP32-P4-Pi/p4-pi-pin.png)


### 2.4 机械尺寸
物理尺寸及安装孔位：

![尺寸图](../../../assets/images/ESP32-P4-Pi/Dimension.png)

### 2.5 功能框图
系统架构及 ESP32-P4 (主) 与 ESP32-C6 (从) 之间的连接关系：

![流程图](../../../assets/images/ESP32-P4-Pi/flowchart.png)


---

## 3. 软件开发

我们提供了一套基于 **ESP-IDF** 的完整示例代码。

### 3.1 快速入门

#### 3.1.1 准备工作

* **硬件**: ESP32-P4-Pi 开发板，USB-C 数据线。

* **软件**: **ESP-IDF v5.5** 或更高版本 (必须)。

#### 3.1.2 编译与烧录步骤

1.  **克隆代码仓库**
    ```bash
    git clone [https://github.com/VIEWESMART/ESP32-P4-Pi.git](https://github.com/VIEWESMART/ESP32-P4-Pi.git)
    ```

2.  **设置目标芯片**
    ```bash
    idf.py set-target esp32p4
    ```

3.  **Wi-Fi 配置 (重要)**
    由于 P4 使用 C6 通过 SDIO 进行 Wi-Fi 连接，必须添加以下依赖：
    ```bash
    idf.py add-dependency "espressif/esp_wifi_remote"
    idf.py add-dependency "espressif/esp_hosted"
    ```

4.  **编译、烧录与监视**
    ```bash
    idf.py build flash monitor
    ```

### 3.2 软件示例
在 [`https://github.com/VIEWESMART/ESP32-P4-Pi/tree/main/examples/esp-idf`](https://github.com/VIEWESMART/ESP32-P4-Pi/tree/main/examples/esp-idf) 目录下提供了 **13 个可运行的示例**。

| 序号 | 示例名称 | 说明 | 关键技术 / 特性 |
| :-: | :--- | :--- | :--- |
| **01** | [**HowToCreateProject**](https://github.com/VIEWESMART/ESP32-P4-SmartDisplay/tree/main/examples/esp-idf/01_HowToCreateProject) | **工程模板** | 最小化 CMake 设置指南。 |
| **02** | [**HelloWorld**](https://github.com/VIEWESMART/ESP32-P4-SmartDisplay/tree/main/examples/esp-idf/02_HelloWorld) | **基础测试** | 基础 UART 日志输出。 |
| **03** | [**attitude**](https://github.com/VIEWESMART/ESP32-P4-Pi/tree/main/examples/esp-idf/03-attitude) | **姿态传感器** | 收集传感器数据并打印 |
| **04** | [**i2c_tools**](https://github.com/VIEWESMART/ESP32-P4-SmartDisplay/tree/main/examples/esp-idf/03_i2c_tools) | **总线扫描** | 检测触摸 (GT911) 及音频芯片地址。 |
| **05** | [**sdmmc**](https://github.com/VIEWESMART/ESP32-P4-SmartDisplay/tree/main/examples/esp-idf/06_sdmmc) | **SD 卡** | 使用 SDMMC Host 读写文件。 |
| **06** | [**wifistation**](https://github.com/VIEWESMART/ESP32-P4-SmartDisplay/tree/main/examples/esp-idf/07_wifistation) | **Wi-Fi 6** | 通过 ESP32-C6 (SDIO) 联网。 |
| **07** | [**audio_es7210**](https://github.com/VIEWESMART/ESP32-P4-Pi/tree/main/examples/esp-idf/07-audio_es7210)| **ES7210音频采集** | 通过麦克风采集音频存储到SD卡（录音） |
| **08** | [**audio_es8311**](https://github.com/VIEWESMART/ESP32-P4-Pi/tree/main/examples/esp-idf/08-audio_es8311)| **ES8311音频播放** | 驱动音频编解码芯片播放音频 |
| **09** | [**ethernetbasic**](https://github.com/VIEWESMART/ESP32-P4-Pi/tree/main/examples/esp-idf/09_ethernetbasic)| **以太网** | 插上网线获取网络 |
| **10** | [**color_panel_jd9165**](https://github.com/VIEWESMART/ESP32-P4-Pi/tree/main/examples/esp-idf/10_color_panel_jd9165) | **LCD 测试** | 简单的 RGB 刷屏测试。 |
| **11** | [**mipi_lcd_camera**](https://github.com/VIEWESMART/ESP32-P4-Pi/tree/main/examples/esp-idf/11_mipi_lcd_camera) | **摄像头预览** | MIPI-CSI 输入 -> MIPI-DSI 输出。 |
| **12** | [**7inch_lvgl_demo_v9**](https://github.com/VIEWESMART/ESP32-P4-Pi/tree/main/examples/esp-idf/12_7inch_lvgl_demo_v9) | **出厂 UI** | **LVGL 9** 跑分与触摸演示。 |
| **13** | [**esp_brookesia_phone**](https://github.com/VIEWESMART/ESP32-P4-Pi/tree/main/examples/esp-idf/13_esp_brookesia_phone) | **综合演示** | 类似于手机系统示例。 |

> [!TIP]
> **Arduino 支持**: 我们正在积极开发 P4 的 Arduino BSP。敬请期待！
> **PlatformIO 支持**: 我们正在积极开发 P4 的 PlatformIO。敬请期待！

---

## 4. 相关文档与资源

### 📄 板载文档
| 文档标题 | 类型 | 说明 |
| :--- | :--- | :--- |
| **[ESP32-P4-Pi 规格书](https://github.com/VIEWESMART/ESP32-P4-Pi/blob/main/Datasheet/ESP32-P4-Pi-VIEWE_SPEC_V1.1.pdf)** | PDF | 产品规格书 |
| **[原理图](https://github.com/VIEWESMART/ESP32-P4-Pi/blob/main/Schematic/SCH_ESP32-ESP32-P4-Pi-VIEWE-V1.1_2025-10-23.pdf)** | PDF | 电路设计原理图 |
| **[显示屏规格书](https://github.com/VIEWESMART/ESP32-P4-Pi/blob/main/Datasheet/display/ALL-UE070WS-RB30-A106A_SPEC_V1.0.pdf)** | PDF | 7.0" 1024x600 显示屏规格书 |
| **[显示驱动芯片手册](https://github.com/VIEWESMART/ESP32-P4-Pi/blob/main/Datasheet/display/JD9165BA_DS_V0.0.3-0418(1).pdf)** | PDF | EK79007AD3 驱动手册 |
| **[摄像头规格书](../../../assets/datasheet/peripheral/camera_datasheet.pdf)** | PDF | MIPI-CSI 摄像头模组规格 |

### 🧠 芯片数据手册
| 芯片 | 文档 | 语言 |
| :--- | :--- | :--- |
| **ESP32-P4** | [数据手册](../../../assets/datasheet/chip/esp32-p4_datasheet_en.pdf) | 英文 |
| **ESP32-P4**| [数据手册](../../../assets/datasheet/chip/esp32-p4_datasheet_cn.pdf) | 中文 |
| **ESP32-P4**| [技术参考手册](../../../assets/datasheet/chip/Esp32-p4_technical_reference_manual_en.pdf) | 英文 |
| **ESP32-P4**| [技术参考手册](../../../assets/datasheet/chip/Esp32-p4_technical_reference_manual_cn.pdf) | 中文 |
| **ESP32-C6** | [数据手册](../../../assets/datasheet/chip/esp32-c6-wroom-1_wroom-1u_datasheet_en.pdf) | 英文 |
| **ESP32-C6** | [数据手册](../../../assets/datasheet/chip/esp32-c6-wroom-1_wroom-1u_datasheet_cn.pdf) | 中文 |
| **ESP32-P4-Core** | [数据手册](https://github.com/VIEWESMART/ESP32-P4-Pi/blob/main/Datasheet/P4-Core%20Datasheet/ESP32-P4-Core-VIEWE_SPEC_V1.0.pdf) | 英文 |
| **ESP32-P4-Core** | [原理图](https://github.com/VIEWESMART/ESP32-P4-Pi/blob/main/Schematic/SCH_ESP32-P4-Core_2025-11-24.pdf) | |

### 🛠️ 工具
* **[Flash 下载工具](../../../assets/software/flash_download_tool.zip)**: 用于手动烧录固件的工具。

> [!IMPORTANT]
> 更多资源，请探索 [**资源中心**](../../support/resource.md)。

---

## :material-face-agent: 技术支持

<div class="grid cards" markdown>

-   [**:material-github: GitHub Issues**](https://github.com/VIEWESMART/ESP32-P4-Pi/issues)
    ---
    提交 Bug 或请求新功能。跟踪开发进度。

-   [**:material-email: 邮件支持**](mailto:info@chinasunyee.com)
    ---
    获取直接的技术支持与商务咨询。

</div>