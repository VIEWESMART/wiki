---
title: MIPI DSI 显示屏
hide:
  - toc
---

# MIPI DSI 接口显示屏

**原生 DSI 接口。一块屏幕，兼容双生态。**

优奕视界 MIPI DSI 显示屏系列专为高性能 HMI 打造。
凭借统一的接口设计，单个显示模组即可原生兼容 **树莓派** 与 **ESP32-P4**，兼具高带宽、低功耗与低 EMI。

<div class="grid cards" markdown>

-   :material-link-variant: **双平台支持**
    ---
    **树莓派 + ESP32-P4**。可直连树莓派 DSI 接口与 ESP32-P4 的 MIPI 接口。

-   :material-cable-data: **一线通方案**
    ---
    告别凌乱走线。
    单根 FPC 排线同时传输**视频**、**触摸**与**供电**。

-   :material-speedometer: **高带宽**
    ---
    支持最高 **1920x720** 分辨率与高刷新率 (60FPS+)，远超 SPI 屏。

</div>

<br>

---

## :material-view-dashboard: 产品展示

=== "🖥️ 标准屏 (HD/FHD)"
    **适用于 HMI 与平板的标准高清显示屏。**

    <div class="grid cards" markdown>

    -   **7.0" 标准屏**
        ---
        **分辨率**: 1024x600
        **注意**: P4 与树莓派上最受欢迎的尺寸。
        [:arrow_right: 查看规格](#matrix)

    -   **10.1" WXGA**
        ---
        **分辨率**: 800x1280
        **方向**: 竖屏 (可旋转)
        [:arrow_right: 查看规格](#matrix)

    -   **5.0" HD 手机屏**
        ---
        **分辨率**: 720x1280
        **方向**: 竖屏 (可旋转)
        [:arrow_right: 查看规格](#matrix)

    </div>

=== "🎨 创意屏 (圆形与方形)"
    **为智能旋钮、86 盒与温控器打造的独特 1:1 比例屏幕。**

    <div class="grid cards" markdown>

    -   **4.0" 圆形屏**
        ---
        **分辨率**: 720x720
        **形状**: 纯圆形
        **像素密度**: 高 PPI
        [:arrow_right: 查看规格](#matrix)

    -   **4.0" 方形屏**
        ---
        **分辨率**: 720x720
        **形状**: 1:1 方形
        **特性**: 对称边框
        [:arrow_right: 查看规格](#matrix)

    </div>

=== "📏 条形屏 (超宽)"
    **面向车载仪表盘与副屏的超宽比例屏幕。**

    <div class="grid cards" markdown>

    -   **12.3" 车载条形屏**
        ---
        **分辨率**: 720x1920
        **尺寸**: 大尺寸座舱屏
        **应用**: 数字仪表盘
        [:arrow_right: 查看规格](#matrix)

    -   **6.8" 长条屏**
        ---
        **分辨率**: 480x1280
        **尺寸**: 紧凑长条屏
        **应用**: 智能家居中控 / 机架显示
        [:arrow_right: 查看规格](#matrix)

    </div>


<br>

---

## :material-table-search: 型号规格矩阵 {: #matrix }

| 尺寸 | 分辨率 | 形状 | 比例 | 触摸 | 兼容性 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **4.0"** | 720x720 | **Round** | 1:1 | Cap (I2C) | RPi / P4 |
| **4.0"** | 720x720 | **Square**| 1:1 | Cap (I2C) | RPi / P4 |
| **5.0"** | 720x1280 | Rect | 9:16 | Cap (I2C) | RPi / P4 |
| **6.8"** | 480x1280 | **Bar** | 3:8 | Cap (I2C) | RPi / P4 |
| **7.0"** | 1024x600 | Rect | 16:9 | Cap (I2C) | RPi / P4 |
| **10.1"**| 800x1280 | Rect | 10:16| Cap (I2C) | RPi / P4 |
| **12.3"**| 720x1920 | **Bar** | ~3:8 | Cap (I2C) | RPi / P4 |

> **说明**：
> * **方向**：5.0"、10.1" 与 12.3" 原生为竖屏，可通过树莓派或 ESP-IDF 的软件配置轻松旋转为横屏。
> * **触摸接口**：触摸信号通过 I2C 传输，已集成到 FPC 排线中。

<br>

## :material-developer-board: 驱动与上手

借助开箱即用的驱动，上手非常简单。

=== "Raspberry Pi"
    在 `/boot/config.txt` 中添加 overlay 即可启用显示与触摸驱动。
    ```ini
    dtoverlay=viewe-mipi-4inch
    # （具体型号的 overlay 请参考对应的 wiki 页面）
    ```

=== "ESP32-P4"
    我们提供 **ESP-IDF** 组件 (`esp_lcd_dsi`)。
    * **示例代码**：[:simple-gitee: 在 Gitee 查看](https://gitee.com/VIEWESMART)
    * **驱动库**：内置全部 7 款型号的初始化序列。

<br>

## :material-download: 相关资源

[下载规格书](../../support/resource.md){ .md-button .md-button--primary }
[联系技术支持](mailto:support@chinasunyee.com){ .md-button }
