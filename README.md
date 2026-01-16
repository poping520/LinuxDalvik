# LinuxDalvik

本项目将 **AOSP Android 4.4.4_r2.0.1** 的部分源码（主要为 Dalvik VM 及其依赖组件）抽取出来，以 **Linux** 作为目标运行环境，脱离 AOSP 原生构建系统，使用 **CMake** 进行编译与运行。

项目主要用于：

- 理解与研究 Dalvik 虚拟机的工作原理
- 在 Linux 上以更轻量的方式调试/阅读 Dalvik 相关实现

## 代码来源与范围

- 源码来源：AOSP `android-4.4.4_r2.0.1`
- 主要涉及模块：
  - `dalvik/`（Dalvik VM 核心）
  - `libnativehelper/`
  - `external/zlib/`
  - `external/libffi/`
  - `compat/`（为 host/Linux 环境补齐部分 Android 接口/行为）
  - `art/dalvikvm/`（dalvikvm 启动程序）
  - `libcore/`（提供部分 Java 层源码参考；运行时使用的 `core.jar` 位于 `framework-dex/`）

## 构建说明

### 构建依赖

- CMake >= 3.10
- 支持 32-bit 编译的工具链与依赖（本项目默认通过 `-m32` 构建）
  - 常见需要安装 32-bit 相关库/工具链（不同发行版包名不同）

### 编译

本项目顶层 `CMakeLists.txt` 默认追加了：

- `CMAKE_C_FLAGS += -m32`
- `CMAKE_CXX_FLAGS += -m32`
- `CMAKE_ASM_FLAGS += -m32`

示例：

```bash
cmake -S . -B build
cmake --build build -j
```

### 安装路径

顶层 `CMakeLists.txt` 中默认安装路径：

- `INSTALL_DIR = /tmp/linux-dalvik`

并会安装 `framework-dex/core.jar` 至：

- `/tmp/linux-dalvik/framework/core.jar`

如需修改安装目录，请直接调整 `CMakeLists.txt` 中的 `INSTALL_DIR`。

## 运行示例

`dalvikvm` 位于构建输出目录下（不同构建目录名称不同）。示例：

```bash
/path/to/build/art/dalvikvm/dalvikvm \
  -Xbootclasspath:/tmp/linux-dalvik/framework/core.jar \
  -cp classes.dex \
  test.HelloWorld
```

其中：

- `-Xbootclasspath:.../core.jar` 指定 Dalvik 启动所需的核心类库
- `-cp classes.dex` 指定待执行的 dex

## 目录结构

- `dalvik/`
  - Dalvik VM 核心实现
- `art/dalvikvm/`
  - `dalvikvm` 启动程序（host 侧入口）
- `compat/`
  - Android/host 兼容层实现
- `framework-dex/`
  - 运行所需的 `core.jar`
- `libcore/`
  - AOSP libcore 的部分源码（主要用于参考与对照）

## 免责声明

本项目用于学习与研究目的。AOSP 相关代码版权归原作者/Android Open Source Project 所有。
