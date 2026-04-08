# 7" 1024x600 ESP32-P4 WiFi6 触控智能屏


<div class="grid cards" markdown>

-   **UEP4S070H1024V600C-WBA**
    ---
    基于 **ESP32-P4** + **ESP32-C6** 的**旗舰**开发板和智能屏，
    配备 7 英寸 **1024x600** IPS 显示屏，支持 Wi-Fi 6、H.264 硬件编码及丰富的工业接口。

    [:material-arrow-left: 返回系列列表](../esp32/){ .md-button }
    [:material-cart: 官方商城](https://viewedisplay.com/product/7-inch-1024x600-esp32-p4-wifi6-touch-smart-hmi-uart-display/){ .md-button .md-button--primary }
    [:material-github: GitHub 仓库](https://github.com/VIEWESMART/ESP32-P4-SmartDisplay){ .md-button }

</div>

<div align="center"> 
  <img src="../../../assets/images/UEP4S070H1024V600C/70E.png" width="45%" alt="正面视图">
  <img src="../../../assets/images/UEP4S070H1024V600C/70E-1.png" width="45%" alt="背面视图">
</div>

---

## 1. 产品简介

**ESP32-P4-SmartDisplay** 是一款配备 7 英寸 MIPI 屏幕 (1024x600) 的高性能智能屏。优奕视界设计创新性地结合了 **ESP32-P4** (高性能 MCU) 与 **ESP32-C6** (Wi-Fi6 + BT5 模组)。

该主板集成了丰富的外设，包括 USB OTG 2.0、MIPI-CSI 摄像头接口、H.264 编码器及工业接口 (RS485)，是 **HMI 人机交互**、**边缘计算**和**多媒体**应用的理想平台。

### 1.1 产品特性
* **处理器**:
    * **ESP32-P4**: RISC-V 双核高性能核心 @ 400MHz + 低功耗核心 @ 40MHz。
    * **ESP32-C6**: Wi-Fi 6 / BLE 5.0 协处理器 (通过 SDIO 连接)。
* **存储**:
    * 32MB PSRAM (合封)，16MB NOR Flash。
* **多媒体**:
    * **显示**: 7 英寸 IPS (1024x600)，MIPI-DSI (2-Lane) 接口。
    * **摄像头**: MIPI-CSI 接口 (支持 1080P @ 30fps 输入)。
    * **视频**: 硬件 H.264 编码 / JPEG 解码。
    * **音频**: 数字麦克风 (MSM2641D) + 扬声器功放 (NS4168)。
* **外设接口**:
    * **连接**: USB 2.0 OTG (Type-C)，RS485 (板载收发器)。
    * **存储**: microSD 卡槽 (SDIO 3.0 高速模式)。
    * **扩展**: 2x20 Pin 排针 (引出 GPIO, I2C, SPI, UART)。
    * **其他**: WS2812B RGB 灯珠，板载 USB 转 UART 调试桥。

### 1.2 应用场景
* 智能家居中控屏
* 工业 HMI 与自动化控制
* 边缘 AI 视觉与多媒体播放器

---

## 2. 硬件说明

### 2.1 模块概览
详细的板载元件布局如下图所示：

![板载布局](../../../assets/images/UEP4S070H1024V600C/70E-3.png)

| 编号 | 元件 | 说明 |
| :--- | :--- | :--- |
| **①** | **ESP32-P4NRW32** | 主控芯片 (合封 32MB PSRAM)。 |
| **②** | **ESP32-C6** | Wi-Fi 6 / 蓝牙 5 协处理器 (SDIO)。 |
| **③** | **屏幕接口** | MIPI-DSI 2-Lane (兼容 VIEWE 4"/7"/10.1" 屏幕)。 |
| **④** | **15-Pin FPC** | 通用 MIPI-DSI 接口。 |
| **⑤** | **5B-MIPI** | 备用显示接口。 |
| **⑥** | **Universal MIPI** | 通用 MIPI 连接器。 |
| **⑦** | **摄像头接口** | MIPI-CSI 2-Lane (支持 1080P 输入)。 |
| **⑧** | **触摸接口** | I2C 电容触摸接口 (适配 7 寸屏)。 |
| **⑨** | **USB Type-C** | **供电 / UART / USB OTG 2.0**。 |
| **⑩** | **RESET 按键** | 硬件复位键。 |
| **⑪** | **BOOT 按键** | 上电时按住可进入下载模式。 |
| **⑫** | **RS485** | 工业串行接口 (板载收发器)。 |
| **⑬** | **麦克风** | 数字麦克风 (MSM2641D)。 |
| **⑭** | **RGB LED** | WS2812B 可编程灯珠。 |
| **⑮** | **扬声器** | 外接扬声器接口 (NS4168 功放)。 |
| **⑯** | **TF 卡槽** | SDIO 3.0 接口。 |
| **⑰** | **P4 GPIO** | ESP32-P4 引脚扩展排针。 |
| **⑱** | **C6 GPIO** | ESP32-C6 引脚扩展排针。 |
| **⑲** | **电源指示灯** | 5V 电源指示。 |

### 2.2 GPIO 定义 (引脚图)
2x20 排针的完整引脚映射如下：

![引脚定义](../../../assets/images/UEP4S070H1024V600C/pin_definition.png)

### 2.3 GPIO 功能详情
P4 和 C6 GPIO 的详细功能列表：

![引脚介绍](../../../assets/images/UEP4S070H1024V600C/pin_introduction.png)

> **LED 指示灯颜色代码:**
> ![模块颜色](../../../assets/images/UEP4S070H1024V600C/module_color.png)

### 2.4 机械尺寸
物理尺寸及安装孔位：

![尺寸图](../../../assets/images/UEP4S070H1024V600C/size.png)

### 2.5 功能框图
系统架构及 ESP32-P4 (主) 与 ESP32-C6 (从) 之间的连接关系：

![流程图](../../../assets/images/UEP4S070H1024V600C/Flowchart.png)

!!! note "硬件版本说明"
    本开发板为标准版，不包含板载以太网 PHY (可通过 SPI/RMII 扩展)。
    音频电路采用 **MSM261D** (麦克风) 和 **NS4168** (功放)。

---

## 3. 软件开发

我们提供了一套基于 **ESP-IDF** 的完整示例代码。

### 3.1 快速入门

#### 3.1.1 准备工作

* **硬件**: ESP32-P4-SmartDisplay 开发板，USB-C 数据线。

* **软件**: **ESP-IDF v5.2** 或更高版本 (必须)。

#### 3.1.2 编译与烧录步骤

1.  **克隆代码仓库**
    ```bash
    git clone [https://github.com/VIEWESMART/ESP32-P4-SmartDisplay.git](https://github.com/VIEWESMART/ESP32-P4-SmartDisplay.git)
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
在 [`https://github.com/VIEWESMART/ESP32-P4-SmartDisplay/tree/main/examples/esp-idf/`](https://github.com/VIEWESMART/ESP32-P4-SmartDisplay/tree/main/examples/esp-idf/) 目录下提供了 **11 个可运行的示例**。

| 序号 | 示例名称 | 说明 | 关键技术 / 特性 |
| :-: | :--- | :--- | :--- |
| **01** | [**HowToCreateProject**](https://github.com/VIEWESMART/ESP32-P4-SmartDisplay/tree/main/examples/esp-idf/01_HowToCreateProject) | **工程模板** | 最小化 CMake 设置指南。 |
| **02** | [**HelloWorld**](https://github.com/VIEWESMART/ESP32-P4-SmartDisplay/tree/main/examples/esp-idf/02_HelloWorld) | **基础测试** | 基础 UART 日志输出。 |
| **03** | [**i2c_tools**](https://github.com/VIEWESMART/ESP32-P4-SmartDisplay/tree/main/examples/esp-idf/03_i2c_tools) | **总线扫描** | 检测触摸 (GT911) 及音频芯片地址。 |
| **04** | [**mic_msm261d**](https://github.com/VIEWESMART/ESP32-P4-SmartDisplay/tree/main/examples/esp-idf/04-mic_msm261d) | **麦克风** | 通过 PDM/I2S 录制音频。 |
| **05** | [**I2SCodec_ns4168**](https://github.com/VIEWESMART/ESP32-P4-SmartDisplay/tree/main/examples/esp-idf/05_I2SCodec_ns4168) | **扬声器** | 通过 I2S 功放播放音频。 |
| **06** | [**sdmmc**](https://github.com/VIEWESMART/ESP32-P4-SmartDisplay/tree/main/examples/esp-idf/06_sdmmc) | **SD 卡** | 使用 SDMMC Host 读写文件。 |
| **07** | [**wifistation**](https://github.com/VIEWESMART/ESP32-P4-SmartDisplay/tree/main/examples/esp-idf/07_wifistation) | **Wi-Fi 6** | 通过 ESP32-C6 (SDIO) 联网。 |
| **08** | [**color_panel**](https://github.com/VIEWESMART/ESP32-P4-SmartDisplay/tree/main/examples/esp-idf/08_color_panel) | **LCD 测试** | 简单的 RGB 刷屏测试。 |
| **09** | [**camera_dsi**](https://github.com/VIEWESMART/ESP32-P4-SmartDisplay/tree/main/examples/esp-idf/09_camera_dsi) | **摄像头预览** | MIPI-CSI 输入 -> MIPI-DSI 输出。 |
| **10** | [**lvgl_demo_v9**](https://github.com/VIEWESMART/ESP32-P4-SmartDisplay/tree/main/examples/esp-idf/10_7inch_lvgl_demo_v9) | **出厂 UI** | **LVGL 9** 跑分与触摸演示。 |
| **11** | [**RS485_Test**](https://github.com/VIEWESMART/ESP32-P4-SmartDisplay/tree/main/examples/esp-idf/11_RS485_Test) | **工业接口** | UART RS485 通信测试。 |

> [!TIP]
> **Arduino 支持**: 我们正在积极开发 P4 的 Arduino BSP。敬请期待！

---

## 4. 相关文档与资源

### 📄 板载文档
| 文档标题 | 类型 | 说明 |
| :--- | :--- | :--- |
| **[Smart Display 规格书](../../../assets/datasheet/ESP32-P4-SmartDisplay_V1.1_SPEC.pdf)** | PDF | 产品规格书 |
| **[原理图](../../../assets/schematic/ESP32-P4-SmartDisplay.sch.pdf)** | PDF | 电路设计原理图 |
| **[显示屏规格书](../../../assets/datasheet/display/HT070IBC-27N7EK-HD%2030PTT3558%20MiPi%2030%E7%9B%B4.pdf)** | PDF | 7.0" 1024x600 显示屏规格书 |
| **[显示驱动芯片手册](../../../assets/datasheet/display/EK79007AD3_DS_REV1.0(1).pdf)** | PDF | EK79007AD3 驱动手册 |
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

### 🛠️ 工具
* **[Flash 下载工具](../../../assets/software/flash_download_tool.zip)**: 用于手动烧录固件的工具。

> [!IMPORTANT]
> 更多资源，请探索 [**资源中心**](../../support/resource.md)。

---

## :material-face-agent: 技术支持

<div class="grid cards" markdown>

-   [**:material-github: GitHub Issues**](https://github.com/VIEWESMART/ESP32-P4-SmartDisplay/issues)
    ---
    提交 Bug 或请求新功能。跟踪开发进度。

-   [**:material-email: 邮件支持**](mailto:info@chinasunyee.com)
    ---
    获取直接的技术支持与商务咨询。

</div>