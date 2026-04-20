---
title:ESP-IDF FAQ: Environment Setup & Firmware Update & Debugging FAQ
---
# ESP-IDF FAQ
FAQ about ESP-IDF, including Environment Setup & Firmware Update & Debugging.

## Environment Setup

### When setting up ESP32-S2 environment using command `idf.py set-target esp32s2`, an error occurred as "Error: No such command 'set-target'". What could be the reason?

!!! note
    The ESP-IDF is adapted to ESP32-S2 from release/v4.2, thus setting up ESP32-S2 environment in previous versions will cause errors. In this case, when using command `idf.py set-target esp32s2`, there will be error as "Error: No such command 'set-target'". It is recommended to perform tests and development on ESP32-S2 using ESP-IDF release/v4.2 and later versions.

For more information, please refer to [ESP32-S2 Get Started](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s2/get-started/).

!!! tip
    For information on the support of different ESP chips by different ESP-IDF versions, please refer to [ESP-IDF Release and SoC Compatibility](https://github.com/espressif/esp-idf/blob/master/README.md#esp-idf-release-and-soc-compatibility).

---

### When installing ESP-IDF version master using ESP-IDF Tools 2.3 in Windows system, an error occurred as: Installation has failed with exit code 2. What could be the reason?

!!! warning
    This is related to the bad network environment. The Github repository cannot be downloaded smoothly under such network environment, causing SDK download failure on your PC. If you encounter Github access problems, it is recommended to use the **offline** version of the latest [ESP-IDF Windows Installer](https://dl.espressif.com/dl/esp-idf/).

---

### On Windows, when setting up the environment using [esp-idf-tools](https://dl.espressif.com/dl/esp-idf/?idf=4.4), the following error occurs when running `make menuconfig`:

```shell
-- Warning: Did not find file Compiler/-ASM Configure
-- Configuring incomplete, errors occurred!
```

!!! tip
    This is because the system could not find the project to be compiled. You need to change directory to the ESP-IDF project before running commands to configure and compile the project. For example, to build the project hello world, go to `esp-idf/examples/get-started/hello_world` before running the commands.

---

### During the installation process of [esp-idf-tools](https://dl.espressif.com/dl/esp-idf/?idf=4.4) on Windows, an exception occurs with the Python tool:

```
Installation has failed with exit code 1
```

!!! warning
    This error is caused by an unsuitable network environment. Please check the "Download via gitee" option when using the tool.

---

### What should I do if I get `Download failed: security channel support error` when installing build environment in the Windows system?

!!! warning
    This is because the Windows system has disabled the default support for SSL 3.0.
    
    **Solution:** Go to `Control Panel` and find `Internet option`, select `Advanced`, and check the `use SSL 3.0` option.

---

### When executing export.bat in Windows system, what should I do if I get CMake and gdbgui version errors?

```
C:\Users\xxxx\.espressif\tools\cmake\3.16.4\bin
The following Python requirements are not satisfied:
gdbgui>=0.13.2.0
```

!!! tip
    This is because the upstream gdbgui has been updated, thus it is not compatible with the low version of python. The current solution is to manually modify the root file `requirements.txt` in ESP-IDF by changing the description of gdbgui version to `gdbgui==0.13.2.0`.

---

### Errors occurred when using idf.menuconfig and idf.build after updating the ESP-IDF version from v3.3 to the latest one:

!!! note
    - Please refer to the [Quick Start Guide](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/index.html) to set up the environment again.
    - Remove build directory `build` and configuration file `sdkconfig` under the hello_world directory.

---

### How to configure `PATH` and `IDF_PATH` when developing ESP32 and ESP8266 simultaneously?

!!! tip
    - For `PATH`, there is no need to do extra configurations. You can put them together as: 
      ```bash
      export PATH="$HOME/esp/xtensa-esp32-elf/bin:$HOME/esp/xtensa-lx106-elf/bin:$PATH"
      ```
    - For `IDF_PATH`, you can specify it for separate chips as:
      
      In ESP32 related projects, use `IDF_PATH = $(HOME)/esp/esp-idf`. In ESP8266 related projects, use `IDF_PATH = $(HOME)/esp/ESP8266_RTOS_SDK`.

---

### Do I need to use command `idf.py set-target` every time when switching to another project?

!!! note
    When building the project with `idf.py build`, the target is determined as follows:

    1. If the build directory `build` already exists, the system will use the target the project was previously built for. It is stored in CMakeCache.txt file in the `build` directory.
    2. Alternatively, if the build directory doesn't exist, the system will check if the `sdkconfig` file exists, and use the target specified there.
    3. If both the build directory and `sdkconfig` file exist with different targets specified, the system will report an error. This shouldn't happen normally, unless `sdkconfig` was changed manually without deleting the build directory.
    4. If neither `sdkconfig` file nor build directory exists, it can be considered to use `IDF_TARGET` to set the target as a CMake variable or environment variable. If this variable is set and is different from the target specified in `sdkconfig` or in the build directory, the system will also report an error.
    5. Finally, if `sdkconfig` doesn't exist, build directory doesn't exist, and the target is not set via `IDF_TARGET`, then the system will use the default value. The default value can be set in `sdkconfig.defaults`.
    6. If the target isn't set using any of the above methods, then the system will build for ESP32 target.

    **To answer your question:**

    - `idf.py set-target` stores the selected target in the project's build directory and `sdkconfig` file, not in the terminal environment. So, once the project is configured and built once for a certain target, if you switch to a different directory and build another project, then come back, the target will not change, and will be the same as previously set for this project. And it's not necessary to run `idf.py set-target` again other than to switch to a different target.
    - If you want to make the project built for certain target by default, add `CONFIG_IDF_TARGET="esp32s2"` to the `sdkconfig.defaults` file of the project. After this, if `sdkconfig` file doesn't exist and build directory doesn't exist, idf.py build command will build for that target specified in `sdkconfig.defaults`.
    - `idf.py set-target` command can still be used to override the default target set in `sdkconfig.defaults`.

---

### How to know the version of ESP-IDF, is it recorded in a certain document?

!!! tip
    - **Command line:** You can obtain the version number by inputting `idf.py --version` in the terminal with an IDF environment. 
    - **CMake script:** You can obtain the version number through the variable `${IDF_VERSION_MAJOR}.${IDF_VERSION_MINOR}.${IDF_VERSION_PATCH}`.
    - **Code compilation:** You can obtain the version number by calling `esp_get_idf_version` during code compilation or directly using the macro definition of version in "components/esp_common/include/esp_idf_version.h".

---

### How to optimize ESP-IDF compilation in Windows environment?

!!! warning
    Please add the directories of ESP-IDF source code and compiler `.espressif` to the exclusions of anti-virus program.

---

### Is there an esptool that can be used directly on Windows?

!!! tip
    You can go to [esptool --> Releases](https://github.com/espressif/esptool/releases) and download the Windows version of the esptool from the Asset column on the drop-down page.

---

### What could be the cause of the error `KeyError: 'idfSelectedId'` when running `. /install.sh`?

!!! warning
    - This is because ESP-IDF v5.0 or above is installed on your system. You can check the configuration in the `~/.espressif/idf-env.json` file.
    - This error can be solved by running `rm -rf ~/.espressif/idf-env.json`.

---

### When running `demo`, the package manager component dependency cannot be pulled, with the failure information `Invaild manifest format`, `Invalid dependency format`, and `unknown keys in dependency details: override_path`. What could be the reason?

!!! tip
    This is due to missing component dependencies and can be solved after updating `component-manager`. The corresponding command is `pip install --upgrade idf-component-manager`.

---

### After installing the ESP-IDF CMD environment using the [ESP-IDF v4.4.8-Offline Installer package](https://dl.espressif.com/dl/esp-idf/?idf=4.4), why does the following compilation error occur when directly compiling the hello_world example?

```
[1050/1065] Building C object esp-idf/main/CMakeFiles/__idf_main.dir/main.c.obj
FAILED: esp-idf/main/CMakeFiles/__idf_main.dir/main.c.obj
D:\esp\Espressif\tools\xtensa-esp32-elf\esp-2021r2-patch5-8.4.0\xtensa-esp32-elf\bin\xtensa-esp32-elf-gcc.exe: error: @-file refers to a directory
[1058/1065] Building C object esp-idf/wifi_provisioning/CMakeFiles/__idf_wifi_provisioning.dir/src/scheme_softap.c.obj
ninja: build stopped: subcommand failed.
ninja failed with exit code 1
```

!!! warning
    - According to the logs, an error occurred while caching the `build/esp-idf/main/CMakeFiles/__idf_main.dir/main.c.obj` file during the compilation process. This file is generated when ccache calls the compiler and is related to the compilation cache. This issue has been resolved in versions 5.0 and later.
    - In the ESP-IDF CMD environment of version v4.4, please use the `idf.py --no-ccache build` command to build the projects.



## Firmware Update

### How does the host MCU flash ESP32 via serial interfaces?

!!! tip
    - For the related protocol, please refer to [ESP32 Serial Protocol](https://github.com/espressif/esptool).
    - For the corresponding documentation, please refer to [Serial Protocol](https://docs.espressif.com/projects/esptool/en/latest/esp32/advanced-topics/serial-protocol.html#serial-protocol).
    - For code examples, please refer to [esp-serial-flasher](https://github.com/espressif/esp-serial-flasher).

---

### How to download firmware for ESP32 series modules using the USB-Serial tool?

!!! note
    The connection methods are as follows:

    | Modules   | 3V3 | GND | TXD | RXD | IO0 | EN  |
    |-----------|-----|-----|-----|-----|-----|-----|
    | Serial tool | 3V3 | GND | RXD | TXD | DTR | RTS |

!!! warning
    For the ESP8266 modules, IO15 should be specially connected to ground.

---

### How to flash firmware on macOS and Linux?

!!! tip
    - For the Apple system (macOS), you can use [esptool](https://github.com/espressif/esptool) downloaded via brew or git to flash firmware.
    - For the Linux system (e.g., Ubuntu), you can use [esptool](https://github.com/espressif/esptool) downloaded via apt-get or git to flash firmware.

---

### Does ESP32 support programming using JTAG pins directly?

!!! tip
    Yes, ESP32 supports using [JTAG Pins](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/jtag-debugging/configure-other-jtag.html#id1) to flash directly. Please refer to [Upload application for debugging](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/jtag-debugging/index.html#jtag-upload-app-debug).

---

### Does ESP_Flash_Downloader_Tool support customized programming control?

!!! note
    - The GUI tool is not open-sourced and does not support embedded executive script.
    - The low-level component [esptool](https://github.com/espressif/esptool) is open-sourced and can be used to perform all functions such as flashing and encryption. It is recommended to conduct secondary development based on this component.

---

### Can I enable the Secure Boot function for ESP32 via OTA?

!!! warning
    - It is not recommended to enable Secure Boot through OTA, as it poses operational risks and requires multiple OTA firmware updates.
    - Since the Secure Boot function is in Bootloader, please update Bootloader first to enable this function.

    1. First, check whether the partition table of your current device can store the Bootloader with Secure Boot enabled.
    2. Then, update an intermediate firmware which can be written in the Bootloader partition. By default, the Bootloader partition cannot be erased or written, you need to enable them via `make menuconfig`.
    3. Sign the intermediate firmware and upgrade it to the target device through OTA. Then upgrade the Bootloader of this firmware and the signed new firmware through OTA.
    4. If there are situations such as powered-down or network break-down and restart during the Bootloader OTA process, the device will not be booted and needs to be re-flashed.

---

### How to resolve the following error that occurred when flashing firmware to ESP32-S2 based on ESP-IDF v4.1?

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
    **Solution:**
    
    If you are using ESP32-S2 instead of ESP32-S2 Beta, please update ESP-IDF to v4.2 or later versions.

    **Notes:**
    
    - ESP-IDF v4.1 only supports ESP32-S2 Beta, which is not compatible with ESP32-S2.
    - The version of esptool that comes with ESP-IDF v4.1 is v2.9-dev, which only supports ESP32-S2 Beta as well.
    - Both ESP-IDF v4.2 and its esptool v3.0-dev support ESP32-S2 series chips.

---

### How to download firmware based on ESP-IDF using flash_download_tool?

!!! tip
    - Please refer to [get-started-guide](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/index.html) when building an ESP-IDF project for the first time.
    - Taken hello-world example for instance, run `idf.py build` (supports ESP-IDF v4.0 and later versions, for versions before v4.0, please use `make`). After building, the following flash command for the bin file will be generated:

    ```shell
    # Project build complete. To flash, run this command:
    ../../../components/esptool_py/esptool/esptool.py -p (PORT) -b 921600 write_flash --flash_mode dio --flash_size detect --flash_freq 40m 0x10000 build/hello-world.bin build 0x1000 build/bootloader/bootloader.bin 0x8000 build/partition_table/partition-table.bin
    or run 'idf.py -p PORT flash'
    ```

    You can use flash_download_tool to flash according to the bin file and flash address prompted by this command.

---

### What is the communication protocol for flashing ESP chips?

!!! tip
    - ESP Serial Protocol: [Serial Protocol](https://docs.espressif.com/projects/esptool/en/latest/esp32/advanced-topics/serial-protocol.html).
    - Python-based implementation: [esptool](https://github.com/espressif/esptool).
    - C-language-based implementation: [esp-serial-flasher](https://github.com/espressif/esp-serial-flasher).

---

### How to program ESP32-C3's firmware offline?

!!! note
    - Currently, no tool supports the offline programming of ESP32-C3's firmware. However, the official [Flash Download Tools](https://www.espressif.com/en/support/download/other-tools) can directly download binary firmware and support mass production download mode for up to eight ESP32-C3 devices at the same time.
    - In addition, we also provide [Test Fixture](https://www.espressif.com/en/products/equipment/production-testing-equipment/overview) for mass production, which supports up to four ESP32-C3 modules to download firmware simultaneously.

---

### How does ESP32 set the Flash SPI mode to QIO mode?

!!! tip
    It can be set in menuconfig through `Serial flasher config` > `Flash SPI mode`, the corresponding API is [esp_image_spi_mode_t()](https://docs.espressif.com/projects/esp-idf/en/release-v4.4/esp32/api-reference/system/app_image_format.html?highlight=esp_image_spi_mode_t#_cppv420esp_image_spi_mode_t).

---

### After downloading the program and powering on EPS8266, the serial port printed the following log. What is the reason?

```
ets Jan  8 2013,rst cause:1, boot mode:(7,7)
waiting for host
```

!!! warning
    `waiting for host` means the Boot is in SDIO mode, indicating that GPIO15 (MTDO) is pulled up (HIGH). Please refer to [ESP8266 Boot Mode Description](https://github.com/esp8266/esp8266-wiki/wiki/Boot-Process).

---

### What are the Espressif module programming tools?

!!! tip
    - For Espressif programming software, please go to [Flash Download Tools](https://www.espressif.com/en/support/download/other-tools). Installation-free GUI tools are for the `Windows` environment only.
    - Espressif programming tool [esptool](https://github.com/espressif/esptool) is written based on `Python` with open-source code, supporting secondary development.

---

### What is the difference between the Factory mode and Developer mode of the flash download tool?

!!! note
    - Factory mode supports multi-channel downloads, while Developer mode only supports single channel.
    - The path of bin files under the Factory mode is relative, while under Developer is absolute.

---

### The ESP32-C3 chip should be able to conduct firmware download through USB, but I failed to do so under ESP-IDF v4.3. So, how can I use USB for firmware download?

!!! tip
    You need to compile under ESP-IDF v4.4 or above versions. After pulling the latest branch and [updating the IDF tool](https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/get-started/index.html), you can compile normally and use USB for download. Please refer to [usb-serial-jtag-console](https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/api-guides/usb-serial-jtag-console.html).

---

### Why does the programming fail for the jig with a 4-port hub in factory mode?

!!! warning
    **Chip:** ESP32 | ESP8266
    
    - It is because Espressif products complete the calibration operation by transmitting some packets when starting up. This operation requires a 3.3 V voltage and a guaranteed peak current of 500 mA. Therefore, when it comes to more than one port, there will be situations where the computer cannot program or the programming is interrupted due to the insufficient power supply of the computer's USB when programming via connecting to a computer's USB. It is recommended to use the hub for programming and supply power to the hub in the meantime.

---

### I'm using an ESP32-WROVER-B module to download the AT firmware via the [flash download tool](https://www.espressif.com/en/support/download/other-tools). However, an error occurred after writing to flash. But the same operation succeeded when replacing the module with ESP32-WEOVER-E, what is the reason?

!!! warning
    - The ESP32-WROVER-B module leads out the SPI flash pin, but the ESP32-WROVER-E module does not. Please check whether the SPI flash pin of the ESP32-WROVER-B module is re-used by other external application circuits.
    - Connecting the CMD pin of the SPI flash in ESP32-WROVER-B to GND will cause the flash to fail to start. The following error log will be printed:

    ```shell
    rst:0x10 (RTCWDT_RTC_RESET),boot:0x1b (SPI_FAST_FLASH_BOOT)
    flash read err, 1000
    ets_main.c 371
    ets Jun 8 2016 00:22:57
    ```

---

### Why can't the [Flash Download Tools](https://www.espressif.com/en/support/download/other-tools) be used to reflash the firmware on a device that has enabled flash encryption but not disabled the download mode?

!!! warning
    **Chip:** ESP32 | ESP32-S2
    
    - The default configuration of the flash download tool has enabled eFuse verification. If you want to reflash the firmware of a device that has already enabled flash encryption, please modify the following configuration:
    
      - Modify the default configuration in the `esp32 > security.conf` file, change `flash_force_write_enable = False` to `flash_force_write_enable = True`.
      - Modify the default configuration in the `esp32 > spi_download.conf` file, change `no_stub = False` to `no_stub = True`.
    
    - Note: When reflashing the firmware on devices with flash encryption enabled, the reflashed firmware must use the same flash encryption key. If the keys do not match, the new firmware will not function properly.

---

### When updating ESP32 firmware through the UART interface based on [esptool serial port protocol](https://github.com/espressif/esptool), can I add a new app partition?

!!! tip
    - The partitions in flash depend on the data in partition_table.bin. If partition_table.bin can be updated, the storage space of other data, such as bootloader.bin and app.bin, can be redivided to create an app partition.

---

### I am using ESP8266 to download the firmware via the [flash download tool](https://www.espressif.com/en/support/download/other-tools). After downloading the firmware, there is no programming output log, and the serial port prints the following messages. What could be the reason?

```shell
ets Jan  8
2013,rst cause:1, boot mode:(3,7)
ets_main.c
```

!!! warning
    - Please check whether the hardware wiring is correct. See [Boot mode wiring instructions](https://docs.espressif.com/projects/esptool/en/latest/esp8266/advanced-topics/boot-mode-selection.html).
    - Please check whether the download offset address of `bootloader.bin` is correct. The offset address downloaded from `bootloader.bin` of ESP8266 is "0x0". If the offset address is wrong, the flash cannot be started.

---

### Why does my USB driver fail to be recognized by the Windows 7 system?

!!! tip
    - Please download and install the [USB Serial JTAG driver](https://dl.espressif.com/dl/idf-driver/idf-driver-esp32-usb-jtag-2021-07-15.zip) manually for the Windows 7 system.

---

### After using the ESP32-WROVER-E module to download the program, the following log is printed after powered on. What could be the reason?

```shell
rst：0x10 （RTCWDT_RTC_RESET），boot:0x37（SPI_FLASH_BOOT）
【2020-12-11 15:51:42 049】invalrd header：0xffffffff
invalrd header：0xffffffff
invalrd header：0xffffffff
```

!!! warning
    - Generally, it is because the GPIO12 was pulled high. It is recommended to pull it low and see the results. Please see [ESP32 Boot Log Guide](https://docs.espressif.com/projects/esptool/en/latest/esp32/advanced-topics/boot-mode-selection.html#select-bootloader-mode).

---

### When using the [Flash Download Tools](https://www.espressif.com/en/support/download/other-tools) to flash ESP32-C3 via USB, 8-download data fail occurs repeatedly. How can I solve it?

!!! tip
    - Please erase the chip completely first before flashing.
    - This problem has been solved in V3.9.4 and above versions.

---

### On ESP32, the bootloader.bin of ESP-IDF v3.0 can not start app.bin of ESP-IDF v5.0. Why?

!!! tip
    - When booting the app.bin of ESP-IDF v5.0 with the bootloader.bin of ESP-IDF v3.0, it is necessary to enable the configuration option `idf.py menuconfig` > `Build type` > `[*] App compatible with bootloader and partition table before ESP-IDF v3.1` on ESP-IDF v5.0.

---

### Does ESP32-C3 support disabling ROM code logs via OTA?

!!! tip
    Yes. You can disable the ROM code log by enabling the `Boot ROM Behavior → Permanently change Boot ROM output → (X) Permanently disable logging` configuration in the software, and then update the firmware via OTA.

---

### Will the operation of other tasks be affected when the chip is undergoing an OTA firmware upgrade ([`esp_ota_write()`](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/ota.html#_cppv413esp_ota_write16esp_ota_handle_tpkv6size_t))?

!!! warning
    During the OTA process, the cache will be turned off when writing to the flash, which will affect peripheral interrupts and some SPI tasks. Therefore, it is not recommended to perform other tasks during this period.


## Debugging

### What is the serial port name of ESP devices?

!!! tip
    The serial port name is usually assigned by the operating system, and different operating systems and devices may have different serial port names. Common ones are as follows:

    - **Windows system:** `COM*`
    - **Linux system:**
      - UART: `/dev/ttyUSB*`
      - USB: `/dev/ttyACM*`
    - **macOS system:** `/dev/cu.usbserial-*`

---

### How to block debugging messages sent through UART0 by default in ESP32?

!!! note
    - For first-stage Bootloader log, you could block the logs by connecting GPIO15 to Ground.
    - For second-stage Bootloader log, go to menuconfig and configure the `Bootloader config` option.
    - For ESP-IDF log, go to menuconfig > `Component config` and configure the `Log output` option.

---

### How to modify the default method of RF calibration in ESP32?

!!! tip
    - During RF initialization, the partial calibration solution is used by default. Go to menuconfig and enable the `CONFIG_ESP32_PHY_CALIBRATION_AND_DATA_STORAGE` option.
    - If the boot time is not critical, the full calibration solution can be used instead. Go to menuconfig and disable the `CONFIG_ESP32_PHY_CALIBRATION_AND_DATA_STORAGE` option.
    - It is recommended to use the **partial calibration** solution, which ensures less boot time and enables you to add the function of erasing RF calibration information in NVS so as to trigger the full calibration operation.

    For detailed information, please refer to the [RF Calibration documentation](https://docs.espressif.com/projects/esp-idf/en/v4.4.4/esp32/api-guides/RF_calibration.html).

---

### How to modify the default method of RF calibration in ESP8266?

!!! tip
    During RF initialization, the partial calibration solution is used by default, in which the value of byte 115 in esp_init_data_default.bin is `0x01`. The initialization only takes a short time. If the boot time is not critical, the full calibration solution can be used instead.

    **For NONOS SDK and earlier versions of RTOS SDK 3.0:**

    - Call `system_phy_set_powerup_option(3)` in function `user_pre_init` or `user_rf_pre_init`.
    - In phy_init_data.bin, modify the value of byte 115 to `0x03`.

    **For RTOS SDK 3.0 and later versions:**

    - Go to menuconfig and disable `CONFIG_ESP_PHY_CALIBRATION_AND_DATA_STORAGE`.
    - If `CONFIG_ESP_PHY_INIT_DATA_IN_PARTITION` is enabled in menuconfig, please modify the value of byte 115 in phy_init_data.bin to `0x03`. If `CONFIG_ESP_PHY_INIT_DATA_IN_PARTITION` is disabled, please modify the value of byte 115 in phy_init_data.h to `0x03`.

    **If you use the default partial calibration solution, and want to add the function of triggering the full calibration operation:**

    - For NONOS SDK and earlier versions of RTOS SDK 3.0, please erase the RF parameters to trigger the full calibration operation.
    - For RTOS SDK 3.0 and later versions, please erase the NVS partition to trigger the full calibration operation.

---

### How to troubleshoot in ESP32 Boot mode?

!!! warning
    - The ESP32-WROVER series uses 1.8 V flash and PSRAM, which is `0x33` by default in boot status and `0x23` in download mode.
    - Other modules use 3.3 V flash and PSRAM, which are `0x13` by default in boot status and `0x03` in download mode.
    - For detailed information, please refer to Section Strapping Pins in [ESP32 Series Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf). Taking `0x13` as an example, the pins are as follows:

    | Pins   | GPIO12 | GPIO0 | GPIO2 | GPIO4 | GPIO15 | GPIO5 |
    |--------|--------|-------|-------|-------|--------|-------|
    | Level  | 0      | 1     | 0     | 0     | 1      | 1     |

    You can also refer to the [Boot Mode Selection documentation](https://docs.espressif.com/projects/esptool/en/latest/esp32/advanced-topics/boot-mode-selection.html) directly.

    > **Note:** ESP32-WROVER series indicates that the product is in EOL status.

---

### When debugging with ESP32 JLINK, an ERROR occurs as: No Symbols For Freertos. How can I resolve such issue?

!!! tip
    This issue will not affect actual operations. For solutions, please go to the [ST Community](https://community.st.com/s/question/0D50X0000BVp8RtSQJ/thread-awareness-debugging-in-freertos-stm32cubeide-110-has-a-bug-for-using-rtos-freertos-on-stlinkopenocd).

---

### How to monitor the free space of the task stack?

!!! tip
    The function `vTaskList()` can be used to print the available space of the task stack regularly. For detailed information, please refer to [CSDN Blog](https://blog.csdn.net/espressif/article/details/104719907).

---

### Is it possible to use JTAG to debug with ESP32-S2?

!!! tip
    Yes. For detailed information, please refer to [ESP32-S2 JTAG Debugging](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s2/api-guides/jtag-debugging/).

---

### How to modify the log output without changing the output level of menuconfig?

!!! tip
    To modify the log output without changing the output level of menuconfig, you can use the `esp_log_level_set()` function. This function allows you to set the log level for a specific module or subsystem, rather than changing the global log level.

    For example, to set the log level for the network module to `ESP_LOG_DEBUG`, you can use the following code:

    ```c
    esp_log_level_set("network", ESP_LOG_DEBUG);
    ```

    For more information about this functionality, please refer to [Logging library](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/log.html).

---

### ESP8266 enters boot mode (2,7) and hits a watchdog reset. What could be wrong?

!!! warning
    - Please make sure that when ESP8266 boots, the strapping pins are held in the required logic levels. If externally connected peripherals drive the strapping pins to an inappropriate logic level, ESP8266 may boot into a wrong mode of operation. With the absence of a valid program, the WDT may then reset the chip.
    - Thus, in design practices, it is recommended to only use the strapping pins for input to high resistive external devices so that the strapping pin is not forced high/low at power-up. For more information, please refer to [ESP8266 Boot Mode Selection](https://github.com/espressif/esptool/wiki/ESP8266-Boot-Mode-Selection).

---

### When using the ESP-WROVER-KIT board with OpenOCD, an error occurred as: Can't find board/esp32-wrover-kit-3.3v.cfg. How can I resolve such issue?

!!! tip
    - With 20190313 and 20190708 versions of OpenOCD, please use instruction `openocd -f board/esp32-wrover.cfg`.
    - With 20191114 and 20200420 (2020 later versions) versions of OpenOCD, please use instruction `openocd -f board/esp32-wrover-kit-3.3v.cfg`.

---

### The RTC_watch_dog keeps resetting during ESP32 SPI boot. What could be the reason?

!!! warning
    **Reason:** The flash has a requirement for time interval between VDD_SDIO power-up and the first access. For example, GD's 1.8 V flash requires 5 ms of time interval, while the time interval of ESP32 is about 1 ms (XTAL frequency is 40 MHz). Under such condition, the flash access will fail and either timer watchdog reset or RTC watchdog reset is triggered, depending on which one is triggered first. The threshold for RTC watchdog reset is 128 KB cycle, while the threshold for timer watchdog reset is 26 MB cycle. Taking the 40 MHz XTAL clock as an example, when the frequency of RTC slow clock is greater than 192 KHz, an RTC watchdog reset will be triggered first, otherwise a timer watchdog reset will be triggered. VDD_SDIO will be continuously powered when the timer watchdog is reset, so there will be no problem in accessing flash and the chip will work normally. When the RTC watchdog is reset, the VDD_SDIO power supply will be disabled and the access to flash will fail, resetting the RTC_watch_dog continuously.

    **Solution:** When an RTC watchdog reset occurs, the power supply to VDD_SDIO is disabled. You can add a capacitor to VDD_SDIO to ensure that the voltage of VDD_SDIO does not drop below the voltage that the flash can tolerate during this period.

---

### How to obtain and parse coredump with ESP32?

!!! tip
    - To obtain the 64 KB coredump file from the firmware, you need to know its offset from the partition table. Assuming the offset is `0x3F0000`, run the following command to read the firmware:

    ```text
    python esp-idf/components/esptool_py/esptool/esptool.py -p /dev/ttyUSB* read_flash 0x3f0000 0x10000 coredump.bin
    ```

    - Use the coredump reading script to convert the file obtained at the first step into readable messages. Assuming the coredump file is coredump.bin and the elf file is hello_world.elf, run the following command to convert the file:

    ```text
    python esp-idf/components/espcoredump/espcoredump.py info_corefile -t raw -c coredump.bin hello_world.elf
    ```

    For more information, please refer to the [Core Dump documentation](https://docs.espressif.com/projects/esp-idf/en/v4.4.4/esp32/api-guides/core_dump.html).

---

### How to do RF performance test with ESP32, ESP8266, and ESP32S2?

!!! tip
    Please refer to the documentation in the `help` folder of the [ESP RF Test Guide](https://www.espressif.com/sites/default/files/tools/ESP_RF_Test_EN.zip).

---

### What are the reasons for not being able to recognize ESP devices under the Win10 system?

!!! warning
    - Check if any security protection software has been activated.
    - Check if the device is identified in the Linux virtual subsystem of Win10.
    - If the device cannot be identified only in Win10 system, go to Device Manager to see whether such device exists (e.g., COM x). If the answer is still no, please check your cable and driver.
    - If the device cannot be identified only in Linux virtual subsystem, taken VMWare as an example, please go to `Settings` > `USB Controller` and select `Show all USB input devices`.

---

### One error occurred with ESP32 as: Core 1 paniced (Cache disabled but cache memory region accessed). What could be the reason?

!!! warning
    **Reasons:**

    - During the time when cache is disabled (e.g., when using the API spi_flash to read/write/erase/map the SPI flash), an interrupt is generated and the interrupt program accesses the flash resources.
    - It is usually because the processor called programs from the flash and used its constants. One important thing is that since the Double variable is implemented through software, thus when this kind of variable is used in the interrupt programs, it is also implemented in the flash (e.g., forced type conversion operation).

    **Solution:**

    - Add an `IRAM_ATTR` modifier to the accessed function during interrupt
    - Add an `DRAM_ATTR` modifier to the accessed constant during interrupt
    - Do not use Double variable in the interrupt programs

    For more information, please refer to the [Fatal error documentation](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/fatal-errors.html#cache-err-msg).

---

### How to read the flash model information of the modules?

!!! tip
    - Please use the python script [esptool](https://github.com/espressif/esptool) to read information of Espressif's chips and modules.
    - For Windows:

    ```text
    esptool.py -p COM* flash_id
    ```

    - For Linux:

    ```text
    esptool.py -p /dev/ttyUSB* flash_id
    ```

---

### When debugging the [Ethernet Example](https://github.com/espressif/esp-idf/tree/master/examples/ethernet) in ESP-IDF, the following exception log appears. How can I resolve such issue?

```text
emac: Timed out waiting for PHY register 0x2 to have value 0x0243(mask 0xffff). Current value:
```

!!! tip
    You can refer to the following configurations of the development board. Please see the schematics for details:

    - `CONFIG_PHY_USE_POWER_PIN=y`
    - `CONFIG_PHY_POWER_PIN=5`

---

### I found a "Brownout detector was triggered" failure on my ESP32. How to resolve such issue?

!!! warning
    - ESP32 has a built-in brownout detector which can detect if the voltage is lower than a specific value. If it happens, the detector will reset the chip to prevent unintended behavior.
    - This message may be reported in various scenarios, while the root cause should always be that the chip with a power supply has momentarily or permanently dropped below the brownout threshold. Please try replacing stable power supply and USB cable, or installing capacitor on power supply terminals of your module.
    - For products powered by batteries, please check the power-on sequence, replace a battery with a higher current, or try to increase the capacitance of the power supply.
    - Apart from the above solution, you can also try to configure the reset threshold value or disable the brownout detector. For more information, please refer to [config-esp32-brownout-det](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/kconfig.html#brownout-detector).
    - For ESP32 power-up and reset timing descriptions, see [ESP32 Series Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf).

---

### After ESP32 imported the protocol_examples_common.h header file, the file cannot be found while compiling. What could be the reason?

!!! tip
    - Please add `set(EXTRA_COMPONENT_DIRS $ENV{IDF_PATH}/examples/common_components/protocol_examples_common)` in CMakeLists.txt under the project.
    - For more information, please refer to the [Build system documentation](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/build-system.html).

---

### When using ESP8266 NonOS v3.0 SDK, the following error occurred. What could be the reason?

```text
E:M 536    E:M 1528
```

!!! warning
    Any error logs beginning with `E:M` indicates insufficient memory.

---

### When using flash_download_tool to flash firmware to the ESP8266 module, how to solve the following error?

```text
ESP8266 Chip efuse check error esp_check_mac_and_efuse
```

!!! warning
    **Potential reasons:**

    - `efuse check error` indicates that the internal eFuse parameter area of the chip has been unintentionally modified. Typically, eFuse stores critical information, such as chip configuration and MAC address. If the eFuse is damaged, it will disable the chip.
    - Generally, eFuse damage would be caused by overvoltage or static electricity.

    **Suggestions:**

    - Monitor voltage fluctuations during power-up and power-down processes.
    - The eFuse functionality has been enhanced in ESP32-C3/ESP32-C2 chips. You may consider replacing with the relevant products in the future.

---

### When upgrading from ESP-IDF v4.4 to v5.0 and above, the error `esp_log.h:265:27: error: format '%d' expects argument of type 'int', but argument 6 has type 'uint32_t' {aka 'long unsigned int'} [-Werror=format=]265 | #define LOG_COLOR(COLOR)  "\033[0;" COLOR "m"` is reported. How can this be resolved?

!!! tip
    - This error is caused by Espressif toolchain changes. For specific reasons and solutions, please refer to the [Migration Guide: From 4.4 to 5.0](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/migration-guides/release-5.x/5.0/gcc.html#int32-t-and-uint32-t-for-xtensa-compiler).
    - If you decide to ignore this error (not recommended), you can add `target_compile_options(${COMPONENT_LIB} PRIVATE -Wno-pointer-sign -Wno-format)` in the corresponding cmake of the file where the compilation error occurred.

---

### Do ESP32 series products support the use of JTAG functionality in a [boundary scan](https://www.jtag.com/boundary-scan/) environment? Where can I download the BSDL files?

!!! warning
    Due to hardware limitations, currently ESP32 series products do not support boundary scan functions, therefore JTAG can not be used in a boundary scan environment, and there are no BSDL files.

!!! info "Can't find what you need?"    
    If you need more support, please contact our engineering team:    

    [Arduino FAQ](./FAQ-Arduino-ESP32.md){ .md-button .md-button--primary }
    [Contact Support](mailto:support@viewedisplay.com){ .md-button }