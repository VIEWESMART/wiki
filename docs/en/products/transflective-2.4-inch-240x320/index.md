# UEED080FH-RB39-A003 | 8" FHD Transflective TFT Display

!!! info "产品概览"
    **型号:** UEED080FH-RB39-A003  
    **尺寸/分辨率:** 8.0 inch / 1200(RGB) × 1920 (FHD Portrait)  
    **核心技术:** Transflective TFT (Normally Black) + PCAP Touch  
    **接口:** MIPI DSI 4-Lane  
    **核心优势:** 阳光下可读 · 背光关闭功耗降低80% · -20~70℃工业级温宽  

---

## 🚀 Quick Start (5分钟上手)

### 1. 硬件连接清单
| 物料 | 型号/规格 | 备注 |
| :--- | :--- | :--- |
| 显示模组 | UEED080FH-RB39-A003 | 含FPC排线 |
| 驱动板(可选) | UEDX6911 HDMI-to-MIPI | 用于树莓派/HDMI设备调试 |
| 主控要求 | 支持MIPI DSI 4-Lane输出 | RK3568/RK3588/CM4等 |
| 电源 | 3.3V Logic + LED Backlight Drive | 详见电气规格章节 |

### 2. 首次点亮检查表
- [ ] 确认主控MIPI Lane数配置为 **4-Lane**
- [ ] 确认背光驱动PWM频率 ≥ 1kHz（避免低频闪烁）
- [ ] 确认FPC排线金手指朝向正确（丝印标识面朝向PCB）
- [ ] 上电前测量VDD电压在 **3.0~3.6V** 范围内
- [ ] 初始化代码中 `display_mode` 设为 **Normally Black**

!!! warning "⚠️ 关键注意"
    该屏为 **Transflective Normally Black** 模式。在纯黑环境且背光关闭时屏幕几乎不可见——这是正常物理特性，非故障。请在有环境光或开启背光状态下验证显示效果。

---

## 📐 Technical Specifications

### Optical Characteristics
| Parameter | Min | Typ | Max | Unit | Note |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Reflectance (Backlight OFF) | - | 7% × Ambient | - | - | 反射模式亮度与环境光正相关 |
| Luminance (Backlight ON) | 369 + 7%×Amb | - | - | cd/m² | 含触控盖板透过率损耗 |
| Contrast Ratio | - | 800:1 | - | - | 透射模式典型值 |
| Viewing Angle | - | 85/85/85/85 | - | Deg | CR≥10, 全视角 |
| Color Gamut | - | 70% NTSC | - | - | sRGB覆盖 |

### Electrical & Interface
| Parameter | Value | Note |
| :--- | :--- | :--- |
| Interface | MIPI DSI 4-Lane | Data Rate ≤ 1Gbps/lane |
| Logic Voltage | 3.3V ±10% | VDD Pin |
| Backlight Type | LED String | 恒流驱动推荐 |
| Touch Interface | I2C (PCAP) | 多点触控，支持手套/湿手 |
| Operating Temp | -20 ~ +70 ℃ | 工业级 |
| Storage Temp | -30 ~ +80 ℃ | - |

### Mechanical Outline
- **Active Area:** 107.64(W) × 172.224(H) mm
- **Outline Dimension:** 132.6(W) × 202.6(H) × 4.98(D) mm
- **Weight:** ~180g (含触控盖板)
- **FPC:** 40-pin MIPI + 6-pin Touch, 0.5mm pitch

---

## 💡 Transflective Working Principle

理解半反半透原理是正确使用该屏的前提：
┌─────────────────────────────────┐
│ Ambient Light ☀️ │ ← 强光下反射区主导
├──────────┬──────────────────────┤
│ Reflective│ Transmissive │
│ Area │ Area │
│ (Mirror) │ (Window) │
├──────────┴──────────────────────┤
│ Backlight 💡 │ ← 暗光下透射区主导
└─────────────────────────────────┘


| 光照条件 | 推荐模式 | 背光状态 | 功耗对比(vs 1000nit IPS) |
| :--- | :--- | :--- | :--- |
| 强日光 (>30k lux) | 纯反射 | OFF | **↓ 80%** |
| 阴天/室内 (300-3k lux) | 混合 | PWM 30-60% | ↓ 40-60% |
| 夜间/暗室 (<300 lux) | 纯透射 | PWM 100% | ≈ 持平 |

!!! tip "💡 自适应调光建议"
    建议在系统中集成环境光传感器(ALS)，根据lux值动态调节背光PWM占空比，实现功耗与可读性的最优平衡。参考公式：`Backlight_PWM = clamp(base_pwm + k × ambient_lux, 0, 100%)`

---

## 🔧 Integration Guide by Platform

### Raspberry Pi CM4 / Pi5
- 使用官方 `UEDX6911` HDMI转接板即插即用
- 或使用自定义MIPI overlay：[下载DT Overlay](https://github.com/VIEWESMART)
- 触控I2C地址默认 `0x38`，需在 `/boot/config.txt` 启用

### Rockchip RK3568 / RK3588
- MIPI初始化命令序列见规格书 Section 7
- DTS配置要点：`dsi_lane = 4`, `format = rgb888`, `mode = cmd/video`
- 触控驱动：`gt9xx` 或 `ft5x06` (以实际IC为准)

### ESP32-S3 (MIPI Variant)
- ⚠️ 仅适用于带MIPI DSI输出的ESP32-S3变体
- LVGL移植示例：[GitHub Repo](https://github.com/VIEWESMART)
- 注意PSRAM带宽分配，FHD@30fps需至少QSPI PSRAM

### Custom PCB Design Checklist
- [ ] MIPI差分走线阻抗 100Ω ±10%，等长误差 <5mil
- [ ] VDD去耦电容 ≥ 10μF + 100nF，靠近模组引脚放置
- [ ] 背光驱动回路独立铺铜，避免噪声耦合到MIPI信号
- [ ] TP I2C走线远离MIPI及电源线，串联33Ω匹配电阻

---

## 🎯 Application Scenarios & Optimization

### UAV Ground Station
- **痛点:** 户外强光下IPS屏泛白，高亮屏续航不足
- **优化:** 反射模式下完全关闭背光，FHD分辨率确保地图细节可读；搭配ALS实现进出隧道自动切换

### Agricultural/GIS Tablet
- **痛点:** 野外连续作业8h+，电池焦虑
- **优化:** 反射模式功耗降至传统方案1/5；PCAP支持戴手套操作；-20℃低温启动无延迟

### Vehicle/Marine Dashboard
- **痛点:** 阳光直射+隧道频繁切换，视觉适应滞后
- **优化:** Normally Black底色减少眩光；混合模式过渡平滑；FHD竖屏适配导航UI布局

### Outdoor Medical/Industrial HMI
- **痛点:** 消毒液体残留导致触控失灵
- **优化:** PCAP固件开启Wet Touch模式；盖板AG防眩光处理(定制选项)；宽温保证极端环境可靠性

---

## 📥 Resources & Support

| Resource | Link | Description |
| :--- | :--- | :--- |
| Datasheet | [ALL-UEED080FH-RB39-A003A SPEC v1.0](#) | 完整电气/光学/机械规格 |
| GitHub | [VIEWESMART](https://github.com/VIEWESMART) | 驱动代码、Demo、原理图 |
| Wiki Center | [Wiki](#) | 平台适配教程合集 |
| Tutorial Hub | [Tutorials](#) | 视频/图文上手指南 |
| Custom Request | [Contact Sales](#) | 盖板/触控/驱动板定制 |

### ❓ FAQ

??? question "为什么在室内暗处屏幕看起来很暗？"
    Transflective NB屏在无环境光且背光关闭时依赖反射层成像，此时亮度极低。请开启背光或移至有光源环境验证。如需纯暗室使用场景，建议选择纯透射IPS型号。

??? question "触控在雨天/戴手套时不灵敏怎么办？"
    PCAP控制器支持灵敏度寄存器配置。请联系技术支持获取Wet Touch / Glove Mode固件升级包及I2C调参指南。

??? question "能否提供SPI/RGB并行接口版本？"
    当前型号仅支持MIPI DSI 4-Lane。如需低带宽接口，请查看我们5"及以下尺寸的SPI/RGB产品线。8" FHD数据量超出SPI/RGB带宽上限。

??? question "背光寿命是多少？"
    LED背光典型寿命 ≥ 50,000小时 (Ta=25℃, IF=20mA)。高温环境下建议降额使用以延长寿命。

---

*Last Updated: 2025-01-XX | Document Version: 1.2 | Author: VIEWE Tech Support*