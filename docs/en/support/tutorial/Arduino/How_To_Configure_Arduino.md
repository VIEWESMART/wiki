# Arduino IDE Installation & Configuration Guide
Step-by-Step Arduino IDE Configuration

---

!!! success "Officially Supported by Espressif Arduino"
    [VIEWE ESP32 Series](https://viewedisplay.com/iot_aiot-smart-display/): Officially Supported by [Espressif ESP32 Arduino](https://github.com/esp-arduino-libs/ESP32_Display_Panel/blob/master/docs/board/board_viewe.md).      
    One-click core & driver installation, no pin configuration needed, ready to develop in Arduino IDE.  


## 📥 1. Download & Install
Visit the [Official Arduino Downloads](https://www.arduino.cc/en/software) page to download the latest IDE version.

* **Choose your OS**: Select the version that matches your operating system (Windows, macOS, or Linux).
    ![Download Version](../../../../assets/images/Arduino/1%20Install%20Arudino%20.png)
* **Start Download**: On the following page, simply click **"Just Download"** to begin.
    ![Just Download](../../../../assets/images/Arduino/2%20Install%20Arudino%20.png)

---

## 🛠️ 2. Initial Configuration

### 2.1 Launch the IDE
After installation, open the Arduino IDE. 
![Open IDE](../../../../assets/images/Arduino/3%20Open%20Arduino%20IDE.png)

!!! warning "USB Driver Installation"
    If prompted to install a **USB Driver**, click **Install**. Without these drivers, your computer will not recognize your ESP32 development board.  
    ![Install Drivers](../../../../assets/images/Arduino/4%20Install%20Arduino%20USB%20driver.png)

### 2.2 Set Interface Language
1.  Navigate to **File** > **Preferences**.
2.  Select your preferred language from the **Language** dropdown menu.
    ![Set Language](../../../../assets/images/Arduino/5%20Set%20Arduino%20IDE%20language.png)
    ![Confirm Language](../../../../assets/images/Arduino/6%20Set%20Arduino%20IDE%20language.png)

### 2.3 Set Sketchbook Location
The **Sketchbook location** is the default directory where your projects and libraries are stored. 

!!! tip "Organizing Libraries"
    Arduino automatically creates a `libraries` folder inside this directory. Any libraries downloaded via the IDE or added manually should be kept here to ensure they are accessible to your projects.
    ![Sketchbook Path](../../../../assets/images/Arduino/7%20Set%20Arduino%20IDE%20Sketchbook.png)

---

## ⚡ 3. ESP32 Environment Setup

### 3.1 Add Boards Manager URLs
To enable ESP32 support, you must provide the IDE with the correct index URL.

1.  Go to **File** > **Preferences**.
2.  Locate the **Additional boards manager URLs** field and paste the following:

```https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_dev_index.json```

![Manage Board](../../../../assets/images/Arduino/8%20Set%20Additional%20boards%20manager%20.png)

!!! info "Troubleshooting URL Failures"    
    If the primary download fails, try these alternative URLs:    
        - https://espressif.github.io/arduino-esp32/package_esp32_index.json    
        - https://espressif.github.io/arduino-esp32/package_esp32_dev_index.json

### 3.2 Install ESP32 Boards
1.  Open the Board Manager from the left sidebar.
2.  Search for esp32.
3.  Find esp32 by Espressif Systems and click Install.

![Load Board](../../../../assets/images/Arduino/9%20boards%20manage%20add%20viewe%20esp32%20boards.png)    

Note: This process may take several minutes depending on your internet speed.


!!! info "Can't find what you need?"
    If you need more support, please contact our engineering team:
    
    [Contact Support](mailto:support@viewedisplay.com){ .md-button }