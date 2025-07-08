# 🐯ADB控制手机的神器

ADB（Android Debug Bridge）是一个用于与 Android 设备通信的命令行工具。通过它，你可以安装应用、运行 shell 命令、查看日志、传输文件等。

------

## 准备工作

### 安装 ADB

- **Windows** : 
	1.下载 [Platform Tools ](https://developer.android.com/studio/releases/platform-tools)并解压。
	2.解压到任意目录，例如`D:\Android\platform-tools`。
	3.将该目录添加到系统的环境变量`PATH`中。
	
- **MacOS/Linux** ：使用包管理器安装：

```bash
# MacOS (Homebrew)
brew install --cask android-platform-tools

# Ubuntu/Debian
sudo apt install adb
```

### 设备管理

1. 在设备上启用 **开发者选项** 和 **USB调试模式** ，不同型号的收集开启开发者模式的方式不同，具体请自行百度。

2. 通过 USB 将设备连接到电脑。

3. 检查设备是否被识别：

```bash
# 查看已连接设备
adb devices

# 无线调试（需先用 USB 连接授权）
adb tcpip 5555      # 设置监听端口
adb connect <设备IP地址>:<端口号>  # 连接无线设备

# 断开设备连接
adb disconnect <设备IP地址>:<端口号>
```
------

## 常用 ADB 命令

### 安装/卸载应用

```bash

# 安装 APK
adb install app-release.apk

# 覆盖安装
adb install -r app-release.apk

# 卸载应用
adb uninstall com.example.app

# 卸载并保留数据
adb uninstall -r com.example.app
```

### 启动设备Shell

```bash
adb shell
```

启动了shell命令就可以用cd、mv、rm等Linux基本命令了，但并不是所有的命令都支持。

### 文件传输

```bash
# 从电脑复制文件到设备
adb push local_file_path /sdcard/

# 从设备复制文件到电脑
adb pull /sdcard/file_name local_path
```

### 查看 Logcat 日志

```bash
adb logcat
```

过滤日志（按标签和等级）：
```bash
adb logcat -s "MyTag:V *:S"
```

清空日志缓冲区：
```bash
adb logcat -c
```

### 重启设备

```bash
adb reboot
```

进入 Recovery 或 Bootloader：

```bash
adb reboot recovery/bootloader
```

### 截图与录屏

```bash
# 截图
adb shell screencap /sdcard/screen.png
adb pull /sdcard/screen.png

# 录屏（最长 180 秒）
adb shell screenrecord /sdcard/demo.mp4
adb pull /sdcard/demo.mp4
```

### 输入模拟

```bash
# 模拟点击
adb shell input tap 500 500

# 模拟滑动
adb shell input swipe 100 200 300 400

# 输入文本（需焦点在输入框）
adb shell input txt "HelloWorld"

# 按键事件
adb shell input keyevent KEYCODE_HOME
```

### 强制停止应用

```bash
adb shell am force-stop com.example.app
```

### 发送广播

```bash
adb shell am broadcast -a com.example.MY_ACTION
```

------

## 进阶技巧

### 端口转发

```bash
adb forward tcp:8080 tcp:8080
```

### 查看设备信息

```bash
# 获取序列号
adb get-serialno

# 获取设备型号
adb shell getprop ro.product.model

# 获取 Android 版本
adb shell getprop ro.build.version.release
```

### 应用数据备份/恢复
```bash
# 备份应用数据
adb backup -f backup.ab -apk com.example.package

# 恢复备份
adb restore backup.ab
```

------

## 常见问题

### 设备未列出？

- 确保 USB 调试已开启。
- 尝试更换 USB 数据线或端口。
- 重启 ADB 服务：
```bash
adb kill-server
adb start-server
```

### 权限不足怎么办？

部分操作需要 root 权限：

```bash
adb root
adb remount
```

------

## 📘参考资料

- ***adb --help***查看命令帮助
- [Android 官方 ADB 文档](https://developer.android.com/studio/command-line/adb)
- [Logcat 命令详解](https://developer.android.com/studio/command-line/logcat)

