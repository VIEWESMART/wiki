---
title: ESP-IDF 常见问题：环境搭建、固件烧录与调试
description: 优奕视界整理的 ESP-IDF 常见问题解答，涵盖环境搭建、固件下载与烧录，以及常见编译与运行时错误的排查方法。
---

# ESP-IDF 常见问题

关于 ESP-IDF 的常见问题，包含环境搭建、固件烧录与调试。

## 环境搭建

### 使用命令 `idf.py set-target esp32s2` 搭建 ESP32-S2 环境时，报错 "Error: No such command 'set-target'"，可能是什么原因？

!!! note
    ESP-IDF 从 release/v4.2 起才适配 ESP32-S2，因此在更早的版本中搭建 ESP32-S2 环境会报错。这种情况下，使用命令 `idf.py set-target esp32s2` 时会出现报错 "Error: No such command 'set-target'"。建议使用 ESP-IDF release/v4.2 及之后的版本对 ESP32-S2 进行测试和开发。

更多信息请参考 [ESP32-S2 Get Started](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s2/get-started/)。

!!! tip
    关于不同 ESP-IDF 版本对不同 ESP 芯片的支持情况，请参考 [ESP-IDF Release and SoC Compatibility](https://github.com/espressif/esp-idf/blob/master/README.md#esp-idf-release-and-soc-compatibility)。

---

### 在 Windows 系统中使用 ESP-IDF Tools 2.3 安装 ESP-IDF master 版本时，报错：Installation has failed with exit code 2。可能是什么原因？

!!! warning
    这与糟糕的网络环境有关。在这种网络环境下无法顺利下载 Github 仓库，导致你电脑上的 SDK 下载失败。如果遇到 Github 访问问题，建议使用最新版 [ESP-IDF Windows Installer](https://dl.espressif.com/dl/esp-idf/) 的**离线**版本。

---

### 在 Windows 上使用 [esp-idf-tools](https://dl.espressif.com/dl/esp-idf/?idf=4.4) 搭建环境时，运行 `make menuconfig` 报以下错误：

```shell
-- Warning: Did not find file Compiler/-ASM Configure
-- Configuring incomplete, errors occurred!
```

!!! tip
    这是因为系统找不到要编译的项目。你需要在运行命令配置和编译项目之前，先切换到 ESP-IDF 项目目录。例如，要构建 hello world 项目，需先进入 `esp-idf/examples/get-started/hello_world` 再运行相应命令。

---

### 在 Windows 上安装 [esp-idf-tools](https://dl.espressif.com/dl/esp-idf/?idf=4.4) 的过程中，Python 工具出现异常：

```
Installation has failed with exit code 1
```

!!! warning
    该错误由不合适的网络环境导致。使用该工具时请勾选 "Download via gitee" 选项。

---

### 在 Windows 系统安装编译环境时遇到 `Download failed: security channel support error`，该怎么办？

!!! warning
    这是因为 Windows 系统禁用了对 SSL 3.0 的默认支持。
    
    **解决方案：** 进入 `Control Panel`，找到 `Internet option`，选择 `Advanced`，并勾选 `use SSL 3.0` 选项。

---

### 在 Windows 系统中执行 export.bat 时，遇到 CMake 和 gdbgui 版本错误该怎么办？

```
C:\Users\xxxx\.espressif\tools\cmake\3.16.4\bin
The following Python requirements are not satisfied:
gdbgui>=0.13.2.0
```

!!! tip
    这是因为上游的 gdbgui 已更新，与低版本 Python 不兼容。目前的解决办法是手动修改 ESP-IDF 根目录下的 `requirements.txt` 文件，将 gdbgui 版本说明改为 `gdbgui==0.13.2.0`。

---

### 将 ESP-IDF 版本从 v3.3 升级到最新版后，使用 idf.menuconfig 和 idf.build 时报错：

!!! note
    - 请参考 [Quick Start Guide](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/index.html) 重新搭建环境。
    - 删除 hello_world 目录下的构建目录 `build` 和配置文件 `sdkconfig`。

---

### 同时开发 ESP32 和 ESP8266 时，如何配置 `PATH` 和 `IDF_PATH`？

!!! tip
    - 对于 `PATH`，无需做额外配置，将它们放在一起即可：
      ```bash
      export PATH="$HOME/esp/xtensa-esp32-elf/bin:$HOME/esp/xtensa-lx106-elf/bin:$PATH"
      ```
    - 对于 `IDF_PATH`，可以针对不同的芯片分别指定：
      
      在 ESP32 相关项目中，使用 `IDF_PATH = $(HOME)/esp/esp-idf`。在 ESP8266 相关项目中，使用 `IDF_PATH = $(HOME)/esp/ESP8266_RTOS_SDK`。

---

### 每次切换到另一个项目时都需要使用命令 `idf.py set-target` 吗？

!!! note
    使用 `idf.py build` 构建项目时，目标的确定方式如下：

    1. 如果构建目录 `build` 已存在，系统将使用该项目之前构建时所用的目标。它存储在 `build` 目录下的 CMakeCache.txt 文件中。
    2. 或者，如果构建目录不存在，系统将检查 `sdkconfig` 文件是否存在，并使用其中指定的目标。
    3. 如果构建目录和 `sdkconfig` 文件同时存在，且指定的目标不同，系统将报错。正常情况下不会出现这种情况，除非在未删除构建目录的情况下手动修改了 `sdkconfig`。
    4. 如果 `sdkconfig` 文件和构建目录都不存在，可以考虑使用 `IDF_TARGET` 将目标设置为 CMake 变量或环境变量。如果设置了该变量，且其与 `sdkconfig` 或构建目录中指定的目标不同，系统也会报错。
    5. 最后，如果 `sdkconfig` 不存在、构建目录不存在，且未通过 `IDF_TARGET` 设置目标，系统将使用默认值。默认值可在 `sdkconfig.defaults` 中设置。
    6. 如果未通过上述任何方式设置目标，系统将针对 ESP32 目标进行构建。

    **解答你的问题：**

    - `idf.py set-target` 会将所选目标存储在项目的构建目录和 `sdkconfig` 文件中，而不是终端环境中。因此，一旦项目针对某个目标完成一次配置和构建，即使你切换到其他目录构建另一个项目后再回来，该目标也不会改变，仍与该项目的先前设置相同。除了切换到不同的目标外，没有必要再次运行 `idf.py set-target`。
    - 如果你希望项目默认针对某个特定目标构建，可在项目的 `sdkconfig.defaults` 文件中添加 `CONFIG_IDF_TARGET="esp32s2"`。此后，如果 `sdkconfig` 文件不存在且构建目录不存在，idf.py build 命令将针对 `sdkconfig.defaults` 中指定的目标进行构建。
    - 仍可使用 `idf.py set-target` 命令覆盖 `sdkconfig.defaults` 中设置的默认目标。

---

### 如何查看 ESP-IDF 的版本，是否记录在某个文档中？

!!! tip
    - **命令行：** 在具备 IDF 环境的终端中输入 `idf.py --version` 即可获取版本号。
    - **CMake 脚本：** 可通过变量 `${IDF_VERSION_MAJOR}.${IDF_VERSION_MINOR}.${IDF_VERSION_PATCH}` 获取版本号。
    - **代码编译：** 可在代码编译期间调用 `esp_get_idf_version`，或直接使用 "components/esp_common/include/esp_idf_version.h" 中的版本宏定义来获取版本号。

---

### 如何在 Windows 环境下优化 ESP-IDF 编译？

!!! warning
    请将 ESP-IDF 源码目录和编译器 `.espressif` 目录添加到杀毒软件的排除项中。

---

### 有没有可以直接在 Windows 上使用的 esptool？

!!! tip
    你可以访问 [esptool --> Releases](https://github.com/espressif/esptool/releases)，在跳转页面的 Asset 栏中下载 Windows 版本的 esptool。

---

### 运行 `. /install.sh` 时报错 `KeyError: 'idfSelectedId'`，可能是什么原因？

!!! warning
    - 这是因为你的系统中安装了 ESP-IDF v5.0 或更高版本。你可以查看 `~/.espressif/idf-env.json` 文件中的配置。
    - 运行 `rm -rf ~/.espressif/idf-env.json` 即可解决该错误。

---

### 运行 `demo` 时，无法拉取包管理器组件依赖，失败信息为 `Invaild manifest format`、`Invalid dependency format` 和 `unknown keys in dependency details: override_path`。可能是什么原因？

!!! tip
    这是由于缺少组件依赖，更新 `component-manager` 后即可解决。对应命令为 `pip install --upgrade idf-component-manager`。

---

### 使用 [ESP-IDF v4.4.8-Offline Installer package](https://dl.espressif.com/dl/esp-idf/?idf=4.4) 安装 ESP-IDF CMD 环境后，为何直接编译 hello_world 示例时出现以下编译错误？

```
[1050/1065] Building C object esp-idf/main/CMakeFiles/__idf_main.dir/main.c.obj
FAILED: esp-idf/main/CMakeFiles/__idf_main.dir/main.c.obj
D:\esp\Espressif\tools\xtensa-esp32-elf\esp-2021r2-patch5-8.4.0\xtensa-esp32-elf\bin\xtensa-esp32-elf-gcc.exe: error: @-file refers to a directory
[1058/1065] Building C object esp-idf/wifi_provisioning/CMakeFiles/__idf_wifi_provisioning.dir/src/scheme_softap.c.obj
ninja: build stopped: subcommand failed.
ninja failed with exit code 1
```

!!! warning
    - 根据日志，编译过程中缓存 `build/esp-idf/main/CMakeFiles/__idf_main.dir/main.c.obj` 文件时发生错误。该文件是 ccache 调用编译器时生成的，与编译缓存有关。此问题已在 5.0 及更高版本中解决。
    - 在 v4.4 版本的 ESP-IDF CMD 环境中，请使用 `idf.py --no-ccache build` 命令来构建项目。

## 固件烧录

### 主机 MCU 如何通过串口为 ESP32 烧录固件？

!!! tip
    - 相关协议请参考 [ESP32 Serial Protocol](https://github.com/espressif/esptool)。
    - 对应文档请参考 [Serial Protocol](https://docs.espressif.com/projects/esptool/en/latest/esp32/advanced-topics/serial-protocol.html#serial-protocol)。
    - 代码示例请参考 [esp-serial-flasher](https://github.com/espressif/esp-serial-flasher)。

---

### 如何使用 USB-Serial 工具为 ESP32 系列模组下载固件？

!!! note
    连接方式如下：

    | 模组       | 3V3 | GND | TXD | RXD | IO0 | EN  |
    |-----------|-----|-----|-----|-----|-----|-----|
    | 串口工具   | 3V3 | GND | RXD | TXD | DTR | RTS |

!!! warning
    对于 ESP8266 模组，IO15 需要专门接地。

---

### 如何在 macOS 和 Linux 上烧录固件？

!!! tip
    - 对于 Apple 系统（macOS），可以使用通过 brew 或 git 下载的 [esptool](https://github.com/espressif/esptool) 来烧录固件。
    - 对于 Linux 系统（例如 Ubuntu），可以使用通过 apt-get 或 git 下载的 [esptool](https://github.com/espressif/esptool) 来烧录固件。

---

### ESP32 是否支持直接使用 JTAG 引脚进行烧录？

!!! tip
    支持，ESP32 可以使用 [JTAG Pins](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/jtag-debugging/configure-other-jtag.html#id1) 直接烧录。请参考 [Upload application for debugging](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/jtag-debugging/index.html#jtag-upload-app-debug)。

---

### ESP_Flash_Downloader_Tool 是否支持自定义烧录控制？

!!! note
    - 该 GUI 工具未开源，不支持内嵌执行脚本。
    - 底层组件 [esptool](https://github.com/espressif/esptool) 是开源的，可用于执行烧录、加密等所有功能。建议基于该组件进行二次开发。

---

### 能否通过 OTA 为 ESP32 启用 Secure Boot 功能？

!!! warning
    - 不建议通过 OTA 启用 Secure Boot，因为这存在操作风险，且需要多次 OTA 固件更新。
    - 由于 Secure Boot 功能位于 Bootloader 中，请先更新 Bootloader 以启用该功能。

    1. 首先，检查当前设备的分区表是否能够存储启用了 Secure Boot 的 Bootloader。
    2. 然后，更新一个可写入 Bootloader 分区的中间固件。默认情况下，Bootloader 分区无法擦除或写入，需要通过 `make menuconfig` 启用。
    3. 对中间固件进行签名，并通过 OTA 将其升级到目标设备。然后通过 OTA 升级该固件的 Bootloader 以及已签名的新固件。
    4. 如果在 Bootloader OTA 过程中出现断电或网络中断并重启等情况，设备将无法启动，需要重新烧录。

---

### 如何解决基于 ESP-IDF v4.1 为 ESP32-S2 烧录固件时出现的以下错误？

```shell
esptool.py v2.9-dev
Serial port /dev/ttyUSB0
Connecting....
Chip is ESP32S2 Beta
Features: Engineering Sample
Crystal is 40MHz
MAC: 7c:df:a1:01:b7:64
Uploading stub...
Running stub...

A fatal error occurred: Invalid head of packet (0x50)
esptool.py failed with exit code 2
```

!!! tip
    **解决方案：**
    
    如果您使用的是 ESP32-S2 而非 ESP32-S2 Beta，请将 ESP-IDF 更新到 v4.2 或更高版本。

    **注意事项：**
    
    - ESP-IDF v4.1 仅支持 ESP32-S2 Beta，与 ESP32-S2 不兼容。
    - ESP-IDF v4.1 自带的 esptool 版本为 v2.9-dev，同样仅支持 ESP32-S2 Beta。
    - ESP-IDF v4.2 及其 esptool v3.0-dev 均支持 ESP32-S2 系列芯片。

---

### 如何使用 flash_download_tool 基于 ESP-IDF 下载固件？

!!! tip
    - 首次构建 ESP-IDF 工程时，请参考 [get-started-guide](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/index.html)。
    - 以 hello-world 示例为例，运行 `idf.py build`（支持 ESP-IDF v4.0 及更高版本，v4.0 之前的版本请使用 `make`）。构建完成后，会生成如下针对 bin 文件的烧录命令：

    ```shell
    # Project build complete. To flash, run this command:
    ../../../components/esptool_py/esptool/esptool.py -p (PORT) -b 921600 write_flash --flash_mode dio --flash_size detect --flash_freq 40m 0x10000 build/hello-world.bin build 0x1000 build/bootloader/bootloader.bin 0x8000 build/partition_table/partition-table.bin
    or run 'idf.py -p PORT flash'
    ```

    您可以根据该命令提示的 bin 文件和烧录地址，使用 flash_download_tool 进行烧录。

---

### ESP 芯片烧录的通信协议是什么？

!!! tip
    - ESP 串口协议：[Serial Protocol](https://docs.espressif.com/projects/esptool/en/latest/esp32/advanced-topics/serial-protocol.html)。
    - 基于 Python 的实现：[esptool](https://github.com/espressif/esptool)。
    - 基于 C 语言的实现：[esp-serial-flasher](https://github.com/espressif/esp-serial-flasher)。

---

### 如何离线烧录 ESP32-C3 的固件？

!!! note
    - 目前没有工具支持 ESP32-C3 固件的离线烧录。不过，官方的 [Flash Download Tools](https://www.espressif.com/en/support/download/other-tools) 可以直接下载 bin 固件，并支持最多同时连接八台 ESP32-C3 设备进行量产下载。
    - 此外，我们还提供用于量产的 [Test Fixture](https://www.espressif.com/en/products/equipment/production-testing-equipment/overview)，最多支持同时为四个 ESP32-C3 模组下载固件。

---

### ESP32 如何将 Flash SPI 模式设置为 QIO 模式？

!!! tip
    可以通过 menuconfig 中的 `Serial flasher config` > `Flash SPI mode` 进行设置，对应的 API 为 [esp_image_spi_mode_t()](https://docs.espressif.com/projects/esp-idf/en/release-v4.4/esp32/api-reference/system/app_image_format.html?highlight=esp_image_spi_mode_t#_cppv420esp_image_spi_mode_t)。

---

### 下载程序并为 EPS8266 上电后，串口打印了如下日志。原因是什么？

```
ets Jan  8 2013,rst cause:1, boot mode:(7,7)
waiting for host
```

!!! warning
    `waiting for host` 表示 Boot 处于 SDIO 模式，说明 GPIO15（MTDO）被拉高（HIGH）。请参考 [ESP8266 Boot Mode Description](https://github.com/esp8266/esp8266-wiki/wiki/Boot-Process)。

---

### 乐鑫的模组烧录工具有哪些？

!!! tip
    - 乐鑫的烧录软件请前往 [Flash Download Tools](https://www.espressif.com/en/support/download/other-tools)。免安装 GUI 工具仅适用于 `Windows` 环境。
    - 乐鑫烧录工具 [esptool](https://github.com/espressif/esptool) 基于 `Python` 编写且代码开源，支持二次开发。

---

### flash download tool 的 Factory 模式和 Developer 模式有什么区别？

!!! note
    - Factory 模式支持多路下载，而 Developer 模式仅支持单路。
    - Factory 模式下 bin 文件的路径为相对路径，而 Developer 模式下为绝对路径。

---

### ESP32-C3 芯片应该能够通过 USB 进行固件下载，但我在 ESP-IDF v4.3 下未能成功。那么，我该如何使用 USB 进行固件下载？

!!! tip
    您需要在 ESP-IDF v4.4 或更高版本下编译。拉取最新分支并[更新 IDF 工具](https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/get-started/index.html)后，即可正常编译并使用 USB 下载。请参考 [usb-serial-jtag-console](https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/api-guides/usb-serial-jtag-console.html)。

---

### 为什么工厂模式下带 4 口 Hub 的夹具烧录会失败？

!!! warning
    **芯片：** ESP32 | ESP8266
    
    - 这是因为乐鑫产品在启动时会通过传输一些数据包来完成校准操作。该操作需要 3.3 V 电压并保证 500 mA 的峰值电流。因此，当接口数量超过一个时，通过连接电脑 USB 进行烧录，会因电脑 USB 供电不足而出现无法烧录或烧录中断的情况。建议使用 Hub 进行烧录，并同时为 Hub 供电。

---

### 我使用 ESP32-WROVER-B 模组通过 [flash download tool](https://www.espressif.com/en/support/download/other-tools) 下载 AT 固件。然而，写入 flash 后出现了错误。但将模组更换为 ESP32-WEOVER-E 后相同操作却成功了，这是什么原因？

!!! warning
    - ESP32-WROVER-B 模组引出了 SPI flash 引脚，而 ESP32-WROVER-E 模组则没有。请检查 ESP32-WROVER-B 模组的 SPI flash 引脚是否被其他外部应用电路复用。
    - 将 ESP32-WROVER-B 中 SPI flash 的 CMD 引脚连接到 GND 会导致 flash 无法启动，并会打印如下错误日志：

    ```shell
    rst:0x10 (RTCWDT_RTC_RESET),boot:0x1b (SPI_FAST_FLASH_BOOT)
    flash read err, 1000
    ets_main.c 371
    ets Jun 8 2016 00:22:57
    ```

---

### 为什么无法使用 [Flash Download Tools](https://www.espressif.com/en/support/download/other-tools) 重新烧录已启用 flash encryption 但未禁用 download mode 的设备上的固件？

!!! warning
    **芯片：** ESP32 | ESP32-S2
    
    - flash download tool 的默认配置已启用 eFuse 校验。如果您想重新烧录已启用 flash encryption 的设备固件，请修改以下配置：
    
      - 修改 `esp32 > security.conf` 文件中的默认配置，将 `flash_force_write_enable = False` 改为 `flash_force_write_enable = True`。
      - 修改 `esp32 > spi_download.conf` 文件中的默认配置，将 `no_stub = False` 改为 `no_stub = True`。
    
    - 注意：在已启用 flash encryption 的设备上重新烧录固件时，重新烧录的固件必须使用相同的 flash encryption 密钥。如果密钥不匹配，新固件将无法正常工作。

---

### 基于 [esptool serial port protocol](https://github.com/espressif/esptool) 通过 UART 接口更新 ESP32 固件时，我可以新增一个 app 分区吗？

!!! tip
    - flash 中的分区取决于 partition_table.bin 中的数据。如果 partition_table.bin 可以更新，就可以重新划分 bootloader.bin、app.bin 等其他数据的存储空间，从而新增一个 app 分区。

---

### 我使用 ESP8266 通过 [flash download tool](https://www.espressif.com/en/support/download/other-tools) 下载固件。下载固件后，没有烧录输出日志，且串口打印了如下信息。原因可能是什么？

```shell
ets Jan  8
2013,rst cause:1, boot mode:(3,7)
ets_main.c
```

!!! warning
    - 请检查硬件接线是否正确。参见 [Boot mode 接线说明](https://docs.espressif.com/projects/esptool/en/latest/esp8266/advanced-topics/boot-mode-selection.html)。
    - 请检查 `bootloader.bin` 的下载偏移地址是否正确。ESP8266 的 `bootloader.bin` 下载偏移地址为 “0x0”。如果偏移地址错误，flash 将无法启动。

---

### 为什么我的 USB 驱动无法被 Windows 7 系统识别？

!!! tip
    - 对于 Windows 7 系统，请手动下载并安装 [USB Serial JTAG driver](https://dl.espressif.com/dl/idf-driver/idf-driver-esp32-usb-jtag-2021-07-15.zip)。

---

### 使用 ESP32-WROVER-E 模组下载程序后，上电会打印如下日志。原因可能是什么？

```shell
rst：0x10 （RTCWDT_RTC_RESET），boot:0x37（SPI_FLASH_BOOT）
【2020-12-11 15:51:42 049】invalrd header：0xffffffff
invalrd header：0xffffffff
invalrd header：0xffffffff
```

!!! warning
    - 通常是因为 GPIO12 被拉高了。建议将其拉低并观察结果。请参见 [ESP32 Boot Log Guide](https://docs.espressif.com/projects/esptool/en/latest/esp32/advanced-topics/boot-mode-selection.html#select-bootloader-mode)。

---

### 使用 [Flash Download Tools](https://www.espressif.com/en/support/download/other-tools) 通过 USB 烧录 ESP32-C3 时，反复出现 8-download data fail。如何解决？

!!! tip
    - 请先完全擦除芯片再进行烧录。
    - 该问题已在 V3.9.4 及更高版本中解决。

---

### 在 ESP32 上，ESP-IDF v3.0 的 bootloader.bin 无法启动 ESP-IDF v5.0 的 app.bin。为什么？

!!! tip
    - 使用 ESP-IDF v3.0 的 bootloader.bin 启动 ESP-IDF v5.0 的 app.bin 时，需要在 ESP-IDF v5.0 上启用配置选项 `idf.py menuconfig` > `Build type` > `[*] App compatible with bootloader and partition table before ESP-IDF v3.1`。

---

### ESP32-C3 是否支持通过 OTA 禁用 ROM code 日志？

!!! tip
    支持。您可以在软件中启用 `Boot ROM Behavior → Permanently change Boot ROM output → (X) Permanently disable logging` 配置来禁用 ROM code 日志，然后通过 OTA 更新固件。

---

### 当芯片正在进行 OTA 固件升级（[`esp_ota_write()`](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/ota.html#_cppv413esp_ota_write16esp_ota_handle_tpkv6size_t)）时，其他任务的运行会受到影响吗？

!!! warning
    OTA 过程中，写入 flash 时缓存会被关闭，这会影响外设中断和部分 SPI 任务。因此，不建议在此期间执行其他任务。


## 调试

### ESP 设备的串口名称是什么？

!!! tip
    串口名称通常由操作系统分配，不同的操作系统和设备可能有不同的串口名称。常见如下：

    - **Windows 系统：** `COM*`
    - **Linux 系统：**
      - UART：`/dev/ttyUSB*`
      - USB：`/dev/ttyACM*`
    - **macOS 系统：** `/dev/cu.usbserial-*`

---

### 如何在 ESP32 中默认屏蔽通过 UART0 发送的调试信息？

!!! note
    - 对于一级 Bootloader 日志，可以通过将 GPIO15 接地来屏蔽日志。
    - 对于二级 Bootloader 日志，请进入 menuconfig 并配置 `Bootloader config` 选项。
    - 对于 ESP-IDF 日志，请进入 menuconfig > `Component config` 并配置 `Log output` 选项。

---

### 如何修改 ESP32 中射频校准的默认方式？

!!! tip
    - 在射频初始化期间，默认使用局部校准方案。请进入 menuconfig 并启用 `CONFIG_ESP32_PHY_CALIBRATION_AND_DATA_STORAGE` 选项。
    - 如果启动时间不重要，可以改用完整校准方案。请进入 menuconfig 并禁用 `CONFIG_ESP32_PHY_CALIBRATION_AND_DATA_STORAGE` 选项。
    - 建议使用**局部校准**方案，它能保证较短的启动时间，并使您能添加在 NVS 中擦除射频校准信息的功能，从而触发完整校准操作。

    详细信息请参考 [RF Calibration 文档](https://docs.espressif.com/projects/esp-idf/en/v4.4.4/esp32/api-guides/RF_calibration.html)。

---

### 如何修改 ESP8266 中射频校准的默认方式？

!!! tip
    在射频初始化期间，默认使用局部校准方案，其中 esp_init_data_default.bin 中第 115 字节的值为 `0x01`。初始化只需很短的时间。如果启动时间不重要，可以改用完整校准方案。

    **对于 NONOS SDK 和 RTOS SDK 3.0 之前的版本：**

    - 在函数 `user_pre_init` 或 `user_rf_pre_init` 中调用 `system_phy_set_powerup_option(3)`。
    - 在 phy_init_data.bin 中，将第 115 字节的值修改为 `0x03`。

    **对于 RTOS SDK 3.0 及更高版本：**

    - 进入 menuconfig 并禁用 `CONFIG_ESP_PHY_CALIBRATION_AND_DATA_STORAGE`。
    - 如果在 menuconfig 中启用了 `CONFIG_ESP_PHY_INIT_DATA_IN_PARTITION`，请将 phy_init_data.bin 中第 115 字节的值修改为 `0x03`。如果禁用了 `CONFIG_ESP_PHY_INIT_DATA_IN_PARTITION`，请将 phy_init_data.h 中第 115 字节的值修改为 `0x03`。

    **如果您使用默认的局部校准方案，并希望添加触发完整校准操作的功能：**

    - 对于 NONOS SDK 和 RTOS SDK 3.0 之前的版本，请擦除射频参数以触发完整校准操作。
    - 对于 RTOS SDK 3.0 及更高版本，请擦除 NVS 分区以触发完整校准操作。

---

### 如何在 ESP32 Boot 模式下进行排查？

!!! warning
    - ESP32-WROVER 系列使用 1.8 V flash 和 PSRAM，其在启动状态下默认为 `0x33`，在下载模式下为 `0x23`。
    - 其他模组使用 3.3 V flash 和 PSRAM，其在启动状态下默认为 `0x13`，在下载模式下为 `0x03`。
    - 详细信息请参考 [ESP32 Series Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf) 中的 Strapping Pins 章节。以 `0x13` 为例，引脚如下：

    | 引脚   | GPIO12 | GPIO0 | GPIO2 | GPIO4 | GPIO15 | GPIO5 |
    |--------|--------|-------|-------|-------|--------|-------|
    | 电平   | 0      | 1     | 0     | 0     | 1      | 1     |

    您也可以直接参考 [Boot Mode Selection 文档](https://docs.espressif.com/projects/esptool/en/latest/esp32/advanced-topics/boot-mode-selection.html)。

    > **注意：** ESP32-WROVER 系列表示该产品已处于 EOL 状态。

---

### 使用 ESP32 JLINK 调试时，出现错误：No Symbols For Freertos。如何解决该问题？

!!! tip
    该问题不会影响实际操作。解决方案请前往 [ST Community](https://community.st.com/s/question/0D50X0000BVp8RtSQJ/thread-awareness-debugging-in-freertos-stm32cubeide-110-has-a-bug-for-using-rtos-freertos-on-stlinkopenocd)。

---

### 如何监控任务栈的空闲空间？

!!! tip
    可以使用函数 `vTaskList()` 定期打印任务栈的可用空间。详细信息请参考 [CSDN Blog](https://blog.csdn.net/espressif/article/details/104719907)。

---

### ESP32-S2 是否可以使用 JTAG 进行调试？

!!! tip
    可以。详细信息请参考 [ESP32-S2 JTAG Debugging](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s2/api-guides/jtag-debugging/)。

---

### 如何在不修改 menuconfig 输出级别的情况下修改日志输出？

!!! tip
    要在不修改 menuconfig 输出级别的情况下修改日志输出，可以使用 `esp_log_level_set()` 函数。该函数允许您为特定模块或子系统设置日志级别，而不是修改全局日志级别。

    例如，要将 network 模块的日志级别设置为 `ESP_LOG_DEBUG`，可以使用以下代码：

    ```c
    esp_log_level_set("network", ESP_LOG_DEBUG);
    ```

    关于该功能的更多信息，请参考 [Logging library](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/log.html)。

---

### ESP8266 进入 boot 模式 (2,7) 并触发看门狗复位。可能出了什么问题？

!!! warning
    - 请确保 ESP8266 启动时，strapping 引脚保持在所需的逻辑电平。如果外部连接的外设将 strapping 引脚驱动到不合适的逻辑电平，ESP8266 可能会启动到错误的运行模式。在缺少有效程序的情况下，WDT 可能会复位芯片。
    - 因此，在设计实践中，建议仅将 strapping 引脚用于高阻态外部设备的输入，以免在上下电时强制将 strapping 引脚拉高/拉低。更多信息请参考 [ESP8266 Boot Mode Selection](https://github.com/espressif/esptool/wiki/ESP8266-Boot-Mode-Selection)。

---

### 使用 ESP-WROVER-KIT 板配合 OpenOCD 时，出现错误：Can't find board/esp32-wrover-kit-3.3v.cfg。如何解决该问题？

!!! tip
    - 对于 20190313 和 20190708 版本的 OpenOCD，请使用指令 `openocd -f board/esp32-wrover.cfg`。
    - 对于 20191114 和 20200420（2020 年及之后的版本）版本的 OpenOCD，请使用指令 `openocd -f board/esp32-wrover-kit-3.3v.cfg`。

---

### ESP32 SPI 启动期间 RTC_watch_dog 不断复位。原因可能是什么？

!!! warning
    **原因：** flash 对 VDD_SDIO 上电与首次访问之间的时间间隔有要求。例如，GD 的 1.8 V flash 要求 5 ms 的时间间隔，而 ESP32 的时间间隔约为 1 ms（XTAL 频率为 40 MHz）。在这种情况下，flash 访问将失败，并根据哪个先触发，触发 timer watchdog 复位或 RTC watchdog 复位。RTC watchdog 复位的阈值为 128 KB 周期，而 timer watchdog 复位的阈值为 26 MB 周期。以 40 MHz XTAL 时钟为例，当 RTC slow clock 的频率大于 192 KHz 时，会先触发 RTC watchdog 复位，否则会触发 timer watchdog 复位。当 timer watchdog 复位时，VDD_SDIO 会持续供电，因此访问 flash 不会出现问题，芯片会正常工作。当 RTC watchdog 复位时，VDD_SDIO 供电将被禁用，访问 flash 将失败，从而不断复位 RTC_watch_dog。

    **解决方案：** 当发生 RTC watchdog 复位时，VDD_SDIO 的供电被禁用。您可以在 VDD_SDIO 上添加一个电容，以确保在此期间 VDD_SDIO 的电压不会低于 flash 可承受的电压。

---

### 如何使用 ESP32 获取并解析 coredump？

!!! tip
    - 要从固件中获取 64 KB 的 coredump 文件，您需要从分区表中获知其偏移地址。假设偏移地址为 `0x3F0000`，运行以下命令读取固件：

    ```text
    python esp-idf/components/esptool_py/esptool/esptool.py -p /dev/ttyUSB* read_flash 0x3f0000 0x10000 coredump.bin
    ```

    - 使用 coredump 读取脚本将第一步获取的文件转换为可读信息。假设 coredump 文件为 coredump.bin，elf 文件为 hello_world.elf，运行以下命令转换文件：

    ```text
    python esp-idf/components/espcoredump/espcoredump.py info_corefile -t raw -c coredump.bin hello_world.elf
    ```

    更多信息请参考 [Core Dump 文档](https://docs.espressif.com/projects/esp-idf/en/v4.4.4/esp32/api-guides/core_dump.html)。

---

### 如何使用 ESP32、ESP8266 和 ESP32S2 进行射频性能测试？

!!! tip
    请参考 [ESP RF Test Guide](https://www.espressif.com/sites/default/files/tools/ESP_RF_Test_EN.zip) 的 `help` 文件夹中的文档。

---

### Win10 系统下无法识别 ESP 设备的原因有哪些？

!!! warning
    - 检查是否启用了任何安全防护软件。
    - 检查在 Win10 的 Linux 虚拟子系统中是否能识别该设备。
    - 如果仅在 Win10 系统中无法识别该设备，请转到设备管理器查看是否存在该设备（例如 COM x）。如果仍然没有，请检查线缆和驱动。
    - 如果仅在 Linux 虚拟子系统中无法识别该设备，以 VMWare 为例，请转到 `Settings` > `USB Controller` 并选择 `Show all USB input devices`。

---

### ESP32 出现一个错误：Core 1 paniced (Cache disabled but cache memory region accessed)。原因可能是什么？

!!! warning
    **原因：**

    - 在缓存被禁用期间（例如使用 API spi_flash 对 SPI flash 进行读/写/擦除/映射时），产生了中断，而中断程序访问了 flash 资源。
    - 通常是因为处理器从 flash 中调用程序并使用了其常量。重要的一点是，由于 Double 变量是通过软件实现的，因此当在中断程序中使用这类变量时，它也在 flash 中实现（例如强制类型转换操作）。

    **解决方案：**

    - 为中断期间被访问的函数添加 `IRAM_ATTR` 修饰符
    - 为中断期间被访问的常量添加 `DRAM_ATTR` 修饰符
    - 不要在中断程序中使用 Double 变量

    更多信息请参考 [Fatal error 文档](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/fatal-errors.html#cache-err-msg)。

---

### 如何读取模组的 flash 型号信息？

!!! tip
    - 请使用 python 脚本 [esptool](https://github.com/espressif/esptool) 读取乐鑫芯片和模组的信息。
    - 对于 Windows：

    ```text
    esptool.py -p COM* flash_id
    ```

    - 对于 Linux：

    ```text
    esptool.py -p /dev/ttyUSB* flash_id
    ```

---

### 在 ESP-IDF 中调试 [Ethernet Example](https://github.com/espressif/esp-idf/tree/master/examples/ethernet) 时，出现如下异常日志。如何解决该问题？

```text
emac: Timed out waiting for PHY register 0x2 to have value 0x0243(mask 0xffff). Current value:
```

!!! tip
    您可以参考开发板的以下配置。详情请参见原理图：

    - `CONFIG_PHY_USE_POWER_PIN=y`
    - `CONFIG_PHY_POWER_PIN=5`

---

### 我的 ESP32 上出现 “Brownout detector was triggered” 故障。如何解决该问题？

!!! warning
    - ESP32 内置了 brownout 检测器，可以检测电压是否低于特定值。如果发生这种情况，检测器会复位芯片以防止意外行为。
    - 该消息可能在各种情况下出现，但根本原因始终是带电源的芯片瞬时或持续跌落到 brownout 阈值以下。请尝试更换稳定的电源和 USB 线缆，或在模组电源端子上安装电容。
    - 对于电池供电的产品，请检查上电时序、更换电流更大的电池，或尝试增大电源的电容。
    - 除上述方案外，您还可以尝试配置复位阈值或禁用 brownout 检测器。更多信息请参考 [config-esp32-brownout-det](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/kconfig.html#brownout-detector)。
    - 关于 ESP32 上电和复位时序的说明，请参见 [ESP32 Series Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf)。

---

### ESP32 导入 protocol_examples_common.h 头文件后，编译时找不到该文件。原因可能是什么？

!!! tip
    - 请在工程下的 CMakeLists.txt 中添加 `set(EXTRA_COMPONENT_DIRS $ENV{IDF_PATH}/examples/common_components/protocol_examples_common)`。
    - 更多信息请参考 [构建系统文档](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/build-system.html)。

---

### 使用 ESP8266 NonOS v3.0 SDK 时，出现如下错误。原因可能是什么？

```text
E:M 536    E:M 1528
```

!!! warning
    任何以 `E:M` 开头的错误日志都表示内存不足。

---

### 使用 flash_download_tool 为 ESP8266 模组烧录固件时，如何解决以下错误？

```text
ESP8266 Chip efuse check error esp_check_mac_and_efuse
```

!!! warning
    **可能的原因：**

    - `efuse check error` 表示芯片内部的 eFuse 参数区域被意外修改。通常，eFuse 存储着芯片配置和 MAC 地址等关键信息。如果 eFuse 损坏，将导致芯片无法使用。
    - 通常，eFuse 损坏是由过压或静电引起的。

    **建议：**

    - 监控上电和掉电过程中的电压波动。
    - ESP32-C3/ESP32-C2 芯片已增强 eFuse 功能。未来您可以考虑更换为相关产品。

---

### 从 ESP-IDF v4.4 升级到 v5.0 及以上版本时，报错 `esp_log.h:265:27: error: format '%d' expects argument of type 'int', but argument 6 has type 'uint32_t' {aka 'long unsigned int'} [-Werror=format=]265 | #define LOG_COLOR(COLOR)  "\033[0;" COLOR "m"`。如何解决？

!!! tip
    - 该错误由乐鑫工具链变更引起。具体原因和解决方案请参考 [迁移指南：从 4.4 到 5.0](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/migration-guides/release-5.x/5.0/gcc.html#int32-t-and-uint32-t-for-xtensa-compiler)。
    - 如果您决定忽略该错误（不推荐），可以在编译出错文件对应的 cmake 中添加 `target_compile_options(${COMPONENT_LIB} PRIVATE -Wno-pointer-sign -Wno-format)`。

---

### ESP32 系列产品是否支持在 [boundary scan](https://www.jtag.com/boundary-scan/) 环境中使用 JTAG 功能？在哪里可以下载 BSDL 文件？

!!! warning
    由于硬件限制，目前 ESP32 系列产品不支持 boundary scan 功能，因此 JTAG 无法在 boundary scan 环境中使用，也没有 BSDL 文件。

!!! info "没找到需要的内容？"
    如需更多支持，请联系我们的工程团队：

    [Arduino 常见问题](./FAQ-Arduino-ESP32.md){ .md-button .md-button--primary }
    [联系技术支持](mailto:support@chinasunyee.com){ .md-button }
