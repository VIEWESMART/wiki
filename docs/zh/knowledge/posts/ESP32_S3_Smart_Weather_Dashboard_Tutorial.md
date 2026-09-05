---
title: "ESP32-S3 智能气象站仪表盘教程"
description: "基于 ESP32-S3 智能显示屏搭建离线气象站仪表盘：集成 BME280、雨量与光照传感器，LVGL 仪表盘界面，完整接线指引与可复用采集代码。"
date: 2025-12-10
categories:
  - 接口和电子
tags:
  - 嵌入式
  - ESP32
  # - 工程应用
  # - FAQ
authors:
  - viewe_expert
---

# ESP32-S3 智能气象站仪表盘教程

!!! abstract "快速结论"
    本项目把 ESP32-S3 智能显示屏、BME280、模拟雨量传感器与 LDR 组合到一起，无需依赖云服务即可在 LVGL 仪表盘上呈现本地环境数据。

## 核心要点

- 按本指南给出的引脚分配，把 I2C 与模拟传感器接入 ESP32-S3 智能显示屏。
- 将"传感器采集"、"单位换算"、"LVGL 界面刷新"三层解耦，保持界面响应顺滑。
- 在把读数当作正式测量值之前，先按安装现场标定雨量、光照与海平面气压。

![Weather-Monitoring-System](./20200606%20Weather-Monitoring-System.webp){ width="80%" align="center" }


搭建一台本地化的气象站，是 IoT 开发者绕不开的一课。但比起用一块独立 MCU 加一块颗粒感十足的分体屏幕、在面包板上乱糟糟地接线，现代嵌入式开发更讲究一体化集成。

本教程将带你从零设计一套进阶的 **智能气象站仪表盘**，实时呈现温度、湿度、气压、海拔、雨量以及昼夜状态。整套系统的"大脑"是 **VIEWE 2.8 寸 ESP32-S3 智能显示屏**——一款集成度极高的 HMI（人机界面）模块，兼顾数据处理与图形显示双重负载。

依托 **LVGL（Light and Versatile Graphics Library，轻量级多功能图形库）** 与 ESP-IDF 框架，我们将构建一套动态、可交互的 UI，把环境数据"画"出来。
无论你是爱好者、学生还是电子发烧友，气象监测系统都是理解环境感知、嵌入式系统与图形用户界面的绝佳练手项目。

---

## 系统架构：各部分如何协同

与传统的分体方案不同，本项目将环境传感器直接挂载在智能显示屏内部的 ESP32-S3 SoC 上，硬件占用最小化。

数据流如下：

1. **环境感知层：** 用一颗高精度 **BME280 传感器**（经 I2C）采集温、湿、气压，并据此计算海拔；模拟量由 **雨量传感器** 检测降水，**LDR（光敏电阻）** 检测环境光强。
2. **边缘处理层：** 双核 ESP32-S3 对原始的模拟与数字信号进行处理，完成单位换算（如由气压推算海拔），并判断环境状态。
3. **HMI 可视化层：** 处理后的指标送入 **LVGL 引擎**，在 2.8 寸 TFT 触摸屏上动态刷新卡片与图标。

![Circuit-Diagram](./20200606%20Circuit-Diagram-for-ESP32-based-Weather-Monitoring-System.jpg){ width="80%" align="center" }

## 硬件清单

要复现本项目，你至少需要以下元器件：

* **HMI 模块：** [VIEWE 2.8 寸 ESP32-S3 MCU IPS TFT 显示屏](https://viewedisplay.com/product/esp32-2-8-inch-240x320-mcu-ips-tft-display-touch-screen-arduino-lvgl-wifi-ble-uart-smart-module/)
* **大气传感器：** BME280 分线板
* **降水传感器：** 标准模拟雨量传感器
* **环境光传感器：** LDR 光敏电阻模块
* **辅助材料：** 面包板、杜邦线，以及用于烧录的 USB Type-C / Type-A 线缆。

### 为什么以 ESP32-S3 智能显示屏为核心？

传统方案往往需要独立的开发板、显示模块和复杂的排线，不仅占用空间大，也容易引入信号干扰。ESP32-S3 智能显示屏通过 **高集成度** 解决了这些痛点：

-   **计算与图形加速：** 双核 LX7 处理器搭配 PSRAM，可流畅驱动 LVGL 图形库，在 240×320 IPS 屏上支持局部刷新与动画。
-   **原生外设接口：** 关键引脚（I2C、ADC）直接外露，BME280、雨量传感器与 LDR 都能直接接入，无需转接板。
-   **离线优先架构：** 内置 Wi-Fi/蓝牙可选用，默认纯本地运行，在无网络环境下依然稳定可靠。

### 如何挑选传感器组合

一套耐用的气象站不是简单的传感器堆叠，而是环境状态的多维度建模。本项目采用三种互补的传感器类型：

### 1. BME280：微气候核心指标

不同于 DHT11/22，BME280 在一颗芯片里输出温度、湿度、气压的高精度数字量。更关键的是，**气压数据是计算海拔与短期天气预报的基础**。它通过 I2C 通信，只占用两个 GPIO，并支持强制采样模式以减小自热对温度读数的影响。

### 2. 模拟雨量传感器：定性优于定量

雨量传感器本质是一个可变电阻网络。ADC 读数受水质、器件老化影响很大，**别追求精确的降雨毫米数——把它当作一个二值状态机**（干/湿）即可。设计时通过实验标定阈值（如 ADC > 1000 视为有雨），并加入软件去抖以防滑动水滴造成误触发。

### 3. LDR 模块：低成本的昼夜感知

RTC 只能告诉你"时钟意义上的白天"，LDR 反映的却是 **真实的环境光照**。在阴天或室内阴影处，RTC 定义的"白天"可能与实际感受不符。LDR 的模拟输出经 ADC 读取后，可以与 BME280 的温湿度数据交叉验证，提高环境状态的鲁棒性。

### 接线

ESP32-S3 智能显示屏作为中央枢纽，向所有外接传感器提供 3.3V 电源。GPIO 映射如下：

**1. I2C 总线（BME280）**
* `3.3V` → BME280 VCC
* `GND` → BME280 GND
* `GPIO9` → BME280 SDA（数据）
* `GPIO10` → BME280 SCL（时钟）

**2. 模拟传感器（ADC 通道）**
* `GPIO7`（ADC_CHANNEL_6）→ 雨量传感器模拟输出（AO）
* `GPIO6`（ADC_CHANNEL_5）→ LDR 传感器模拟输出（AO）
* *注意：两个模拟传感器共用 VIEWE 板上的 3.3V 与 GND。*


## LVGL 仪表盘设计：信息密度与可读性的平衡

在 2.8 寸小屏上同时呈现 6 项环境参数，必须避免视觉拥挤。本项目采用 **卡片式栅格布局**，遵循以下原则：

| 设计要素        | 实现方式                                  | 用户体验收益                  |
| :-------------- | :---------------------------------------- | :----------------------------- |
| 色彩语义        | 温度=红、湿度=蓝、气压=紫、海拔=绿        | 凭色彩定位数据，无需阅读文字  |
| 图标优先        | 每张卡片底部锚定 PNG 图标                 | 降低认知负担，提升扫读速度    |
| 动态标签刷新    | 仅刷新数值标签，不重绘整张卡片            | 消除闪烁，保证视觉连续性      |
| 显式错误状态    | 传感器异常时显示"ERROR"，绝不空白         | 用户一眼区分"无数据"与"故障"  |

## 数据处理策略：从原始值到可读信息

原始传感器数据要经过三层处理后才能呈现给用户：

1.  **物理换算层：** BME280 的气压值除以 100 转换为 hPa；海拔由国际标准大气公式实时计算 $h = 44330 \times (1 - (P/P_0)^{0.1903})$，其中 $P_0$ 为标准海平面气压（1013.25 hPa）。
2.  **状态决策层：** 雨量与光照传感器的原始 ADC 值经阈值比较器转换为布尔状态。阈值不应硬编码；保留串口调试输出，便于在安装位置就地标定。
3.  **容错层：** 每次传感器读取都检查返回值。I2C 通信失败或 ADC 超时时，UI 层做优雅降级（显示 ERROR），而不是阻塞主循环或显示陈旧数据。


## 开发环境准备

推荐使用 **Visual Studio Code** 配合 **ESP-IDF 框架（v5.3.5）**。
请确保已安装 Python（v3.11+）并在 VS Code 中配置好 ESP-IDF 扩展。UI 部分使用 LVGL v8.4.0。

## 核心应用代码

软件架构拆分为两个主要文件：`main.cpp`（负责 LVGL GUI 与主循环）和 `sensors.c`（负责 I2C 与 ADC 数据采集）。

### 1. 数据采集层（`sensors.c`）

本模块配置 BME280 的 I2C 主机，并初始化模拟输入所用的一次触发 ADC 通道。

```c
#include "sensors.h"
#include "esp_log.h"
#include "driver/gpio.h"
#include <math.h>
#include "esp_adc/adc_oneshot.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include <string.h>
#include "bme280.h"
#include "driver/i2c.h"

static char TAG[100] = "SENSORS";

// Hardware Mappings
#define BME280_I2C_PORT         I2C_NUM_1
#define BME280_I2C_SCL          GPIO_NUM_10
#define BME280_I2C_SDA          GPIO_NUM_9
#define BME280_I2C_ADDRESS      0x76

#define LDR_ADC_CHANNEL       ADC_CHANNEL_5   // GPIO 6
#define RAIN_ADC_CHANNEL      ADC_CHANNEL_6   // GPIO 7

static struct bme280_dev g_Bme280Device;
struct bme280_settings settings;
static adc_oneshot_unit_handle_t g_AdcHandle;

// [Refer to original source for complete I2C and ADC initialization routines]

E_STATUS getBME280Data(float *pTemperature, unsigned char *pHumidity, float *pPressure, unsigned int *pAltitude) {
    E_STATUS eRet_Status = eSTATUS_OK;
    struct bme280_data sensor_data;
    int8_t rslt;

    rslt = bme280_set_sensor_mode(BME280_POWERMODE_FORCED, &g_Bme280Device);
    if (rslt == BME280_OK) {
        vTaskDelay(pdMS_TO_TICKS(100)); // Delay for measurement
        rslt = bme280_get_sensor_data(BME280_ALL, &sensor_data, &g_Bme280Device);
        if (rslt == BME280_OK) {
            *pTemperature = sensor_data.temperature;
            *pHumidity = (char) sensor_data.humidity;
            float pressure_hpa = sensor_data.pressure / 100.0f;
            *pPressure = pressure_hpa;
            // Barometric formula for altitude
            *pAltitude = (unsigned int)(44330.0f * (1.0f - powf((pressure_hpa / 1013.25f), 0.1903f)));
        } else { eRet_Status = eSTATUS_ERROR; }
    } else { eRet_Status = eSTATUS_ERROR; }
    return eRet_Status;
}

E_STATUS getRainStatus(bool *boIsItRaining) {
    int adc_raw;
    if (adc_oneshot_read(g_AdcHandle, RAIN_ADC_CHANNEL, &adc_raw) == ESP_OK) {
        *boIsItRaining = (adc_raw > 1000) ? true : false;
        return eSTATUS_OK;
    }
    return eSTATUS_ERROR;
}

E_STATUS getLightStatus(bool *boIsItDay) {
    int adc_raw;
    if (adc_oneshot_read(g_AdcHandle, LDR_ADC_CHANNEL, &adc_raw) == ESP_OK) {
        *boIsItDay = (adc_raw > 2000) ? false : true;
        return eSTATUS_OK;
    }
    return eSTATUS_ERROR;
}
```

### 2. UI 与主程序（`main.cpp`）

主循环使用 LVGL 绘制差异化的指标"卡片"。通过线程安全锁（`lvgl_port_lock`）从 FreeRTOS 任务更新 GUI，避免画面撕裂或内核崩溃。

```cpp
#include "esp_check.h"
#include "esp_display_panel.hpp"
#include "lvgl.h"
#include "lvgl_v8_port.h"
#include "sensors.h"

using namespace esp_panel::drivers;
using namespace esp_panel::board;

// Global LVGL Label Pointers
static lv_obj_t *temp_value_label, *humidity_value_label, *pressure_value_label;
static lv_obj_t *altitude_value_label, *rainy_label, *light_label;

// Dynamic Card Generator
static void create_card(lv_obj_t *parent, int x, int y, int w, int h, const lv_img_dsc_t *icon, const char *title, const char *value, lv_color_t border_color, lv_obj_t **value_label_out) {
    lv_obj_t *card = lv_obj_create(parent);
    lv_obj_set_size(card, w, h);
    lv_obj_set_pos(card, x, y);
    lv_obj_clear_flag(card, LV_OBJ_FLAG_SCROLLABLE);
    lv_obj_set_style_radius(card, 12, 0);
    lv_obj_set_style_border_color(card, border_color, 0);
    // [Styling omitted for brevity...]
    
    lv_obj_t *value_label = lv_label_create(card);
    lv_label_set_text(value_label, value);
    lv_obj_align(value_label, LV_ALIGN_CENTER, 0, 30);
    *value_label_out = value_label;
}

extern "C" void app_main(void) {
    Board *board = new Board();
    board->init();
    board->begin();
    lvgl_port_init(board->getLCD(), board->getTouch());
    lv_disp_set_rotation(lv_disp_get_default(), LV_DISP_ROT_270);

    BME280_SensorInit();
    ADC_Init();

    lvgl_port_lock(-1);
    lv_obj_t *scr = lv_scr_act();
    // Generate UI Grid
    create_card(scr, 6, 35, 96, 100, &temp, "Temperature", "...", lv_palette_main(LV_PALETTE_RED), &temp_value_label);
    // [Additional cards created here...]
    lvgl_port_unlock();

    // Polling Loop
    while (1) {
        float temp=0, press=0; unsigned char hum=0; unsigned int alt=0;
        bool bIsRaining=false, bIsDay=false;
        char buf[32];

        if (getBME280Data(&temp, &hum, &press, &alt) == eSTATUS_OK) {
            lvgl_port_lock(-1);
            sprintf(buf, "%.1f C", temp); lv_label_set_text(temp_value_label, buf);
            sprintf(buf, "%u %%", hum); lv_label_set_text(humidity_value_label, buf);
            lvgl_port_unlock();
        }
        
        // Polling logic for ADC sensors with 10ms delays...
        vTaskDelay(pdMS_TO_TICKS(10));
    }
}
```

## 离线气象站的实际应用场景

本系统的价值不止于嵌入式学习，更在于 **脱离云端的自主性**：

-   **农业温室监测：** 在网络覆盖差的地区，为农户提供即时决策依据。
-   **实验室环境记录：** 避免 Wi-Fi 射频干扰敏感设备，同时满足数据本地化合规要求。
-   **教学演示工具：** 学生可以直观观察传感器变化与 UI 响应的因果关系，跳过云端往返延迟。
-   **户外探险装备：** 搭配电池可作为便携气象仪；海拔与气压趋势对登山安全尤为关键。

## 为什么要用 ESP32-S3 智能显示屏做这个项目？

如果你正在为这类想法挑选硬件，市面上的显示板琳琅满目。但当项目从面包板原型走向批量部署时，可靠性就成了决定性因素。

Waveshare、Elecrow 这类品牌主要面向爱好者和临时实验场景，而 **[VIEWE](https://viewedisplay.com/)** 则把智能显示屏定位为 **工业级解决方案**。这意味着什么？

* **耐受严苛工况：** 光学贴合等特性可防止凝露，保证户外或工业环境下的可读性。
* **可商用与可量产：** 与创客板可能存在的供应链波动不同，VIEWE 自有工厂，长期供货稳定，质量管理严格。
* **专业级接口：** 原生支持 RS485、CAN 总线、UART 等工业协议，摆脱标准爱好级 GPIO 的限制。

👉 查看更多 [ESP32 显示屏](https://viewedisplay.com/iot_aiot-smart-display/)

## :material-video: 项目演示视频


<div class="video-wrapper">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/od5DNXViYqA?si=4Y1v1y1R9HUNPVuB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>


下方视频展示了智能气象监测系统的实时运行效果。改变周边条件，可以观察到传感器如何响应、ESP32-S3 显示屏如何动态刷新气象仪表盘。演示中也包含 LDR 的自动昼夜检测以及系统的实时监测能力。


<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "这台气象仪表盘不连 Wi-Fi 能工作吗？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "可以。传感器直接接入 ESP32-S3，采集与显示都跑在本地。只有在需要网络校时、云端记录或远程访问时才用到 Wi-Fi。"
      }
    },
    {
      "@type": "Question",
      "name": "为什么算出来的海拔和实际海拔不一致？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "气压海拔依赖海平面基准气压与当前天气。如果对海拔精度有要求，需要在本地标定基准气压。"
      }
    },
    {
      "@type": "Question",
      "name": "我能换成其他传感器吗？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "可以。保持采集层解耦，替换对应传感器的初始化与读取函数即可，LVGL 界面读取的数值接口保持不变。"
      }
    },
    {
      "@type": "Question",
      "name": "仪表盘应该多久刷新一次传感器读数？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "按传感器响应时间与 UI 需求选取合适的间隔。环境传感器不需要按帧率轮询；降低采集频率也有助于减少噪声与负载。"
      }
    },
    {
      "@type": "Question",
      "name": "把气象站部署到户外前要检查什么？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "做好电子器件的防潮，避免外壳热与阳光直射影响读数，并在预期工况下完成标定验证。"
      }
    }
  ]
}
</script>

## 常见问题

??? question "这台气象仪表盘不连 Wi-Fi 能工作吗？"
    可以。传感器直接接入 ESP32-S3，采集与显示都跑在本地。只有在需要网络校时、云端记录或远程访问时才用到 Wi-Fi。

??? question "为什么算出来的海拔和实际海拔不一致？"
    气压海拔依赖海平面基准气压与当前天气。如果对海拔精度有要求，需要在本地标定基准气压。

??? question "我能换成其他传感器吗？"
    可以。保持采集层解耦，替换对应传感器的初始化与读取函数即可，LVGL 界面读取的数值接口保持不变。

??? question "仪表盘应该多久刷新一次传感器读数？"
    按传感器响应时间与 UI 需求选取合适的间隔。环境传感器不需要按帧率轮询；降低采集频率也有助于减少噪声与负载。

??? question "把气象站部署到户外前要检查什么？"
    做好电子器件的防潮，避免外壳热与阳光直射影响读数，并在预期工况下完成标定验证。

!!! info "没有找到您需要的内容？"
    如果您需要更多产品、资源或技术支持，请联系我们的团队：

    [**:material-archive-arrow-down: 知识库**](../../knowledge/tags.md){ .md-button .md-button--primary }
    [**:material-magnify: 产品与解决方案**](https://chinasunyee.com){ .md-button }
    [**:material-email: 联系技术支持**](mailto:info@chinasunyee.com){ .md-button }