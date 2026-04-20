---
title: 常见问题解答与故障排除
hide:
  - toc
---

# :material-frequently-asked-questions: 常见问题解答与故障排除 (FAQ)

快速查找关于硬件、软件和订单的常见问题解答。

!!! tip "快速搜索"
    使用页面顶部的 **搜索栏 (Ctrl+F)** 查找特定错误，或查看我们的 [GitHub Issues](https://github.com/VIEWESMART/VIEWE-FAQ/issues) 获取社区解决方案。

---

## 🚀 快速导航

<div class="grid cards" borderless markdown>

-   :material-code-braces: __软件开发 FAQ__
    ---
    关于 Arduino、ESP-IDF、PlatformIO 和 LVGL 框架的常见问题。
    [:octicons-arrow-right-24: 查看 FAQ](#software-development)

-   :material-chip: __硬件与接线 FAQ__
    ---
    显示类型、引脚定义、电源要求和触摸问题。
    [:octicons-arrow-right-24: 查看 FAQ](#hardware-wiring)

-   :material-cart-check: __订单与定制 FAQ__
    ---
    批量订购、定制 PCB/屏幕以及保修政策。
    [:octicons-arrow-right-24: 查看政策](#orders-customization)

</div>

---

## 🔥 热门常见问题

以下是用户反馈最多的问题。点击展开查看解决方案。

??? question "1. 我应该使用哪个库：LVGL 还是 Arduino_GFX？"
    * **Arduino_GFX**：最适合简单的绘图（圆、线、文本）和追求极致的原始驱动性能。
    * **LVGL**：复杂 UI 的行业标准（按钮、图表、动画）。对于专业产品，我们强烈推荐使用 **LVGL**。

??? question "2. 是否支持 MicroPython 或 CircuitPython？"
    是的，我们的硬件完全兼容。虽然官方教程侧重于 **C++**，但社区已经为我们模块中使用的 ST7701/ST7789 屏幕提供了相关驱动。

??? bug "3. 屏幕不显示（黑屏），但背光已经亮了。"
    1.  **检查 PSRAM**：对于 RGB 屏幕，必须启用 PSRAM（在 Arduino IDE 中：`工具` -> `PSRAM` -> `OPI PSRAM`）。
    2.  **检查库**：确保使用 [Arduino_GFX](https://github.com/moononournation/Arduino_GFX) 库以获得最佳兼容性。
    3.  **检查分辨率**：验证代码中的分辨率是否与硬件匹配（例如 800x480）。

??? bug "4. 触摸功能失效或方向相反（镜像）。"
    1.  **I2C 地址**：GT911 芯片通常使用 `0x5D` 或 `0x14` 地址。
    2.  **排线连接**：确保 6-pin FPC 触摸排线完全插入（金手指朝下）。
    3.  **触摸镜像**：如果 X/Y 轴相反，请在代码中使用 `touch.setRotation()` 函数，或在 LVGL 的 `indev_drv` 中交换坐标映射。

??? failure "5. 编译错误：找不到 `esp_lcd_panel_io.h`。"
    这通常是因为您的 **ESP32 开发板包** 版本过低。请在 Arduino IDE 开发板管理器中将 `esp32` 更新至 **2.0.14** 或 **3.0.x** 版本。

??? info "6. 树莓派 HDMI 显示“无信号 (No Signal)”。"
    您需要在 `config.txt` 中强制指定 HDMI 分辨率。请参阅 [HDMI 配置指南](../products/hdmi/index.md#configuration-guide)。

??? tip "7. 如何从 SquareLine Studio 导出 UI 到 VIEWE 屏幕？"
    选择 **Arduino** 协议 -> 导出 UI 文件 -> 将文件复制到项目的 `libraries` 文件夹 -> 在 `setup()` 中调用 `ui_init()`。

---

## 💻 软件开发 {: #software-development}

选择您偏好的开发框架。以下每个板块都指向详细的设置和优化指南。

### 📦 开发框架

<div class="grid cards" markdown>

-   :simple-arduino: __Arduino__
    ---
    最适合快速原型开发。

    [:octicons-link-external-16: **Arduino FAQ**](FAQ-Arduino-ESP32.md)

-   :simple-espressif: __ESP-IDF__
    ---
    专业的原生开发环境。

    [:octicons-link-external-16: **ESP-IDF FAQ**](../software/esp-idf/index.md)

-   :simple-platformio: __PlatformIO__
    ---
    适合团队协作的现代 IDE。

    [:octicons-link-external-16: **PlatformIO FAQ**](../software/platformio/index.md)

</div>

## 🛠️ 硬件与接线 {: #hardware-wiring}

详细的硬件规格和接线图位于各子页面中。

| 主题 | 内容摘要 | 完整链接 |
| :--- | :--- | :--- |
| **面板类型** | IPS (178° 视角) vs TN (经济型) | [:octicons-arrow-right-24: 对比](../knowledge/posts/ips-vs-tn.md) |
| **电源供应** | **必须 5.0V**。3.3V 仅供逻辑电平使用。 | [:octicons-arrow-right-24: 电源详情](../hardware/power.md) |
| **接口类型** | RGB (40P/50P), SPI, I2C, HDMI, SDMMC | [:octicons-arrow-right-24: 引脚定义](../hardware/wiring.md) |

### ⚡ 快速技巧
* **屏幕闪烁？** 检查 USB 电流是否低于 500mA。请尝试使用 5V/2A 电源适配器。
* **逻辑电平？** 引脚电平均为 **3.3V**。将 5V 直接连接到 ESP32 的 IO 口会造成硬件损坏。

---

## 💼 订单与定制 {: #orders-customization}

<div class="grid cards" markdown>

-   __如何订购__
    - [优奕视界官方网站](https://www.chinasunyee.com/)
    - [淘宝店](https://shop277726935.taobao.com/)
    - 服务热线：400-660-3306

-   __定制服务__
    - PCB 重新设计 (RS485/CAN)
    - 高亮度定制 (1000 nits+)
    - 触摸盖板玻璃定制 (MOQ > 3000)
    - [了解更多定制信息](https://Chinasunyee.com/)
    - [联系销售团队](mailto:info@chinasunyee.com)

</div>

---

## :material-lifebuoy: 支持中心

[ :material-github: 提交 GitHub Issue](https://github.com/VIEWESMART/VIEWE-FAQ/issues){ .md-button }
[ :material-email: 联系技术支持](mailto:support@chinasunyee.com){ .md-button }
[ :material-file-download: 下载中心](../support/resource.md){ .md-button }
