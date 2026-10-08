---
title: Arduino IDE 安装与配置指南
description: 优奕视界 ESP32 智能屏 Arduino IDE 从零安装与配置指南，包含 IDE 安装、语言与路径设置、ESP32 开发板管理器配置与开发板安装。
---

# Arduino IDE 安装与配置指南
逐步配置 Arduino IDE

---

!!! success "获得 Espressif Arduino 官方支持"
    [优奕视界 ESP32 系列](https://www.chinasunyee.com/)：已获得 [Espressif ESP32 Arduino](https://github.com/esp-arduino-libs/ESP32_Display_Panel/blob/master/docs/board/board_viewe.md) 官方支持。      
    一键安装核心与驱动，无需配置引脚，即可在 Arduino IDE 中开始开发。  


## 📥 1. 下载并安装 { #step-1-download-install }
访问 [Arduino 官方下载页面](https://www.arduino.cc/en/software) 下载最新版本的 IDE。

* **选择操作系统**：选择与你的操作系统相匹配的版本（Windows、macOS 或 Linux）。
    ![下载版本](../../../../assets/images/Arduino/1%20Install%20Arudino%20.png)
* **开始下载**：在随后的页面中，直接点击 **"Just Download"** 即可开始。
    ![直接下载](../../../../assets/images/Arduino/2%20Install%20Arudino%20.png)

---

## 🛠️ 2. 初始配置

### 2.1 启动 IDE
安装完成后，打开 Arduino IDE。
![打开 IDE](../../../../assets/images/Arduino/3%20Open%20Arduino%20IDE.png)

!!! warning "USB 驱动安装"
    如果提示安装 **USB 驱动**，请点击 **Install**。没有这些驱动，你的电脑将无法识别 ESP32 开发板。  
    ![安装驱动](../../../../assets/images/Arduino/4%20Install%20Arduino%20USB%20driver.png)

### 2.2 设置界面语言
1.  依次点击 **文件** > **首选项**。
2.  在 **Language**（语言）下拉菜单中选择你偏好的语言。
    ![设置语言](../../../../assets/images/Arduino/5%20Set%20Arduino%20IDE%20language.png)
    ![确认语言](../../../../assets/images/Arduino/6%20Set%20Arduino%20IDE%20language.png)

### 2.3 设置 Sketchbook 位置
**Sketchbook 位置**是用于存放你的项目和库的默认目录。

!!! tip "整理库文件"
    Arduino 会在该目录内自动创建一个 `libraries` 文件夹。通过 IDE 下载或手动添加的库都应放在这里，以确保你的项目能够访问到它们。
    ![Sketchbook 路径](../../../../assets/images/Arduino/7%20Set%20Arduino%20IDE%20Sketchbook.png)

---

## ⚡ 3. ESP32 环境搭建

### 3.1 添加开发板管理器网址
要启用 ESP32 支持，你必须为 IDE 提供正确的索引网址。

1.  依次点击 **文件** > **首选项**。
2.  找到 **附加开发板管理器网址** 字段，并粘贴以下内容：

```https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_dev_index.json```

![管理开发板](../../../../assets/images/Arduino/8%20Set%20Additional%20boards%20manager%20.png)

!!! info "网址下载失败排查"    
    如果主下载地址失败，可以尝试以下备用网址：    
        - https://espressif.github.io/arduino-esp32/package_esp32_index.json    
        - https://espressif.github.io/arduino-esp32/package_esp32_dev_index.json

### 3.2 安装 ESP32 开发板
1.  从左侧边栏打开开发板管理器。
2.  搜索 esp32。
3.  找到由 Espressif Systems 提供的 esp32，然后点击 Install（安装）。

![加载开发板](../../../../assets/images/Arduino/9%20boards%20manage%20add%20viewe%20esp32%20boards.png)    

注意：根据你的网络速度，此过程可能需要几分钟。


!!! info "没找到需要的内容？"
    如需更多支持，请联系我们的工程团队：
    
    [联系技术支持](mailto:support@chinasunyee.com){ .md-button }
