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

