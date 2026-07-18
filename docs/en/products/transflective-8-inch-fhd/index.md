# 8" FHD Transflective TFT Touch Display


!!! info "Product Overview & Core Value"
    **Model:** UEED080FH-RB39-A003 (8.0-inch FHD Portrait Display)  
    **Key Technology:** Transflective TFT (Normally Black) + PCAP Multi-touch  
    **Target Applications:** UAV Ground Stations, Rugged GIS Tablets, Marine Instruments, Field Surveying Devices.  
    **Core Value:** Native sunlight readability without a sunshade. By leveraging ambient light reflection, total display power consumption is **reduced by up to 80%** in outdoor environments, effectively doubling device battery life.



<!-- 优化方案 B：左侧紧凑并排布局 -->
<div class="viewe-action-bar" style="margin-bottom: 25px; display: flex; gap: 16px; align-items: center; flex-wrap: wrap;">
    <!-- 主动作 -->
    <a href="https://viewedisplay.com/product/8-inch-1200x1920-transflective-tft-sunlight-readable-and-low-power-high-resolution-touch-display/" target="_blank" class="md-button md-button--primary" style="margin: 0;">🌐 Official Store</a>
    
    <!-- 次动作 -->
    <a href="../" class="md-button" style="margin: 0; border-color: transparent; color: var(--md-default-fg-color--light);">← Back to Series</a>
</div>


---

## 1. Key Features & Working Principle

### 1.1 Technical Specifications
| Parameter | Specifications | Note |
| :--- | :--- | :--- |
| **Resolution / Outline** | 1200(RGB) × 1920 (FHD 竖屏) | 视网膜级高清晰度显示 |
| **Active Area (AA)** | 107.64(W) × 172.224(H) mm | 8.0 英寸对角线 |
| **Module Dimension** | 132.6(W) × 202.6(H) × 4.98(D) mm | 重量约 0.51 kg (含高强度触控盖板) |
| **Display Interface** | MIPI DSI 4-Lane | 差分信号带宽 ≤ 1Gbps/lane |
| **Touch Panel (PCAP)** | I2C Interface | 内置驱动 IC，支持湿手与厚橡胶手套操作 |
| **Temperature Range** | Operating: -20 ~ +70 ℃ \| Storage: -30 ~ +80 ℃ | 工业级宽温，240小时加速老化认证 |

### 1.2 Optical Performance & Adaptive Dimming
Owing to the micro-granular **Transflective** structure (50% Transmissive Window + 50% Reflective Mirror per pixel), this module dynamic adapts to ambient lighting:

```text
┌───────────────────────────────────────────┐
│         Ambient Light ☀️ (Direct Sunlight) │ ◄── Outdoor: Reflective mode takes over
├─────────────────────┬─────────────────────┤
│   Reflective Area   │  Transmissive Area  │
│      (Mirror)       │      (Window)       │
├─────────────────────┴─────────────────────┤
│         Backlight 💡 (LED Array)          │ ◄── Indoor/Night: Transmissive mode active
└───────────────────────────────────────────┘

```

| Environment | Optimal Mode | Backlight Status | Power Comparison (vs 1000nit IPS) |
| --- | --- | --- | --- |
| **Direct Sunlight (>30k lux)** | Pure Reflective | **OFF (0% PWM)** | **Saved 80% (2.4W vs 12.6W)** |
| **Cloudy / Indoor Daylight** | Mixed Hybrid | PWM 30% - 60% | Saved 40% - 60% |
| **Dark Room / Night (<300 lux)** | Pure Transmissive | PWM 100% (369 cd/m²) | Equivalent (~5.8W) |

💡 **ALS Optimization Tip:** Integrate an Ambient Light Sensor (ALS) on your host platform. Use the formula `Backlight_PWM = clamp(base_pwm + k * ambient_lux, 0, 100%)` to smoothly fade out the backlight as outdoor light increases, maximizing power efficiency.

---

## 2. Hardware Interface & Power Sequences

### 2.1 Critical Pin Definitions (40-Pin MIPI + 6-Pin Touch)

Hardware designers must isolate high-speed MIPI differential signals from noisy backlight lines.

* **VDD (Pins 1-2):** Main Logic Power Supply (**3.3V ±10%**, Ripple < 50mV). Recommend 10µF + 100nF decoupling capacitors placed near the connector.
* **MIPI_CLK / MIPI_D0~D3 (Pins 4-13):** 4-Lane differential pairs. **Impedance control: 100Ω ±10%**. Loop length tolerance < 5mil.
* **RST_N (Pin 15):** Global Hardware Reset. Active Low.
* **BL_PWM (Pin 28):** Backlight dimming input. Constant current driver recommended, frequency ≥ 1kHz to avoid flickering.
* **TP_SDA / TP_SCL / TP_INT:** Capacitive touch I2C bus (Default Address: `0x14` or `0x38` based on firmware). INT triggers on falling edge.

### 2.2 🚨 Mandatory Power-Up Sequence

To prevent screen latch-up, artifacting, or permanent panel damage, the host system board **MUST** execute power rails in this exact chronological order:

```text
3.3V Logic VDD  ──────┐________________________________________
                      │<- Min 10ms ->
Hardware RST_N  ______┌──────────────┐_________________________
                                     │<- Min 20ms panel init ->
MIPI DSI Clock  _____________________┌_________________________
                                     │<- Send Init Command Sequence
Backlight PWM   _____________________ _________________┌_______

```

1. Turn on **3.3V Logic VDD**.
2. Pull **RST_N LOW for ≥ 10ms**, then release to HIGH.
3. Wait **≥ 20ms** for panel internal stabilization.
4. Enable **MIPI DSI signal clock** output and stream the registers.
5. Finally, enable **Backlight PWM** driver. *Reversing this sequence will cause permanent display corruption.*

---

## 3. Reference Software Driver

### 3.1 Kernel Device Tree (DTS) Parameter Guidelines

For Rockchip (RK3568/RK3588) or NXP i.MX8 platforms, configure the MIPI controller node as follows:

```dts
&dsi {
    status = "okay";
    dsi,lanes = <4>;
    dsi,format = <MIPI_DSI_FMT_RGB888>;
    dsi,mode-flags = <MIPI_DSI_MODE_VIDEO MIPI_DSI_MODE_VIDEO_BURST |>;
    
    panel@0 {
        compatible = "viewe,ueed080fh-rb39";
        reg = <0>;
        reset-gpios = <&gpio1 RK_PC2 GPIO_ACTIVE_LOW>;
        /* 1200 x 1920 @ 60Hz Portrait Video Timing Specs */
        panel-timing {
            clock-frequency = <154000000>; // 154 MHz Typical
            hactive = <1200>;
            vactive = <1920>;
            hback-porch = <40>;
            hfront-porch = <40>;
            hsync-len = <20>;
            vback-porch = <16>;
            vfront-porch = <16>;
            vsync-len = <4>;
        };
    };
};

```

### 3.2 Reference Initialization Command Sequence

```c
// Official VIEWE Initial Code Fragment for UEED080FH-RB39-A003
void Init_UEED080FH_Transflective(void) 
{
    // 1. Hardware Triggered Reset Line
    GPIO_Write(RST_N, LOW);
    delay_ms(15);
    GPIO_Write(RST_N, HIGH);
    delay_ms(25);

    // 2. Transflective Operating Mode Register Setup
    // Reg 0x05: 0x00 = Pure Reflective (Eco Outdoor) / 0x01 = Hybrid / 0x02 = Pure Transmissive
    MIPI_Write_Reg(0x05, 0x01); 

    // 3. Dynamic Gamma Setup tailored for Sunlight Sunlight Readability
    MIPI_Write_Reg(0xC0, 0xA2, 0x02, 0x84); 
    MIPI_Write_Reg(0xB1, 0x01, 0x1C, 0x1C); 

    // 4. Exit Sleep Mode & Command Display Panel On
    MIPI_Write_Cmd(0x11); // Exit Sleep
    delay_ms(120);
    MIPI_Write_Cmd(0x29); // Display ON
    delay_ms(20);
}

```

---

## 4. Mechanical & Assembly Guidelines

!!! warning "Mechanical Enclosure Best Practices"
*   **Bezel Pressure:** The front casing bezel must **NOT** exert localized, uneven pressure onto the edges of the PCAP Touch Glass. Over-tightening assembly screws will warp the stack, leading to ghost touches or light leakage under transmissive mode.
*   **Light Sealing:** For rugged outdoor products, employ an opaque sponge gasket around the frame perimeter. Light bleeding from the lateral edges will dramatically lower the outdoor contrast ratio ($CR$) under reflective mode.

---

## 5. Troubleshooting & FAQ (FAE Field Ledger)

??? question "为什么屏幕在室内不插背光或者背光设为0时非常暗？"
这是全反透（Transflective）常黑（Normally Black）屏幕的正统物理特性。在完全没有外界环境光（如室内暗处）的情况下，反射层没有可以反射的光子。若需在纯暗室环境使用，请务必保证开启背光（透射模式）。对于不需要阳光下可视的纯室内项目，建议选择我司纯透射 IPS 系列。

??? question "触控面板（TP）在雨天户外或操作员戴着厚手套时发生断触、无响应怎么解决？"
该模组的投射电容屏（PCAP）内置了专为恶劣工业环境定制的算法固件。你可以通过 I2C 总线向触摸 IC 写入特定的工作模式寄存器：
*   **雨天/湿手模式:** 写入寄存器 `TP_WET_EN = 0x01` 激活抗水滴噪点滤除。
*   **手套操作模式:** 写入寄存器 `TP_GLOVE_MODE = 0x01` 提高底层电容感应互感系数。
*   *注意：请确保 TP 供电纹波控制在合理范围，若出现触控坐标漂移，请首选在靠近 FPC 触控引脚端并联 10µF 滤波电容。*

??? question "屏幕点亮时出现闪烁（Flicker）或者大面积花屏、横纹现象？"
硬件上，请优先使用示波器捕获 **VDD 3.3V 供电线**，确认是否存在由于背光恒流源大电流抽头导致的低频纹波抖动。软件上，请复核上电时序是否颠倒（必须遵循 VDD -> RST -> MIPI -> Backlight），并确认内核中 MIPI 差分线的时钟频率与引脚前沿参数（Porch Settings）完全匹配。

---

## 6. Resources & Downloads

| File Asset Name | Format | Version | Link / Action |
| --- | --- | --- | --- |
| **Complete Engineering Datasheet** | `.PDF` | v1.2 (2026) | [📄 Download Datasheet](https://www.google.com/search?q=%23) |
| **3D CAD Outline Model** | `.STEP` | v1.0 | [📦 Download STEP File](https://www.google.com/search?q=%23) |
| **Linux / Android Reference Kernel Patch** | `.patch` | For RK3588 | [💻 View GitHub Repo](https://www.google.com/search?q=https://github.com/VIEWESMART) |
| **Display Panel Driver IC Register Map** | `.txt` | Full List | [📝 Download Registry File](https://www.google.com/search?q=%23) |

---

*Document ID: VW-WIKI-UEED080FH | Version: 2.0 (Merged) | Last Updated: 2026-07-18 | Maintainer: VIEWE Tech Support Team*