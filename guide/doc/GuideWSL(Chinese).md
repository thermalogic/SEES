# Windows Linux子系统(WSL)安装及开发环境建立

## 安装WSL

1. 安装WSL: [Install Windows Subsystem for Linux (WSL) on Windows 10(Chinese)](https://docs.microsoft.com/zh-cn/windows/wsl/install-win10)

   手动安装，建议安装WSL1 

   * 步骤 1 - 启用适用于Linux的Windows子系统

   * 步骤 6 - 安装所选的Linux分发版，建议安装Ubuntu20.04LTS 

2. 为新的Linux分发版创建用户帐户和密码

   https://docs.microsoft.com/zh-cn/windows/wsl/user-support

 3. 修改Ubuntu软件源

    WSL在电脑中的安装目录是：C:\Users\你的当前用户名\AppData\Local\Packages\

    用`sources.list`覆盖WSL原文件，配置软件源为aliyun.
```
C:\Users\你的当前用户名\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu20.04onWindows_79rhkp1fndgsc\LocalState\rootfs\etc\apt
```

4. 更新系统

在Ubuntu终端执行

```bash
$sudo apt update
$sudo apt upgrade
```

5. 安装开发软件

在Ubuntu终端执行

```bash
$sudo apt install build-essential
$sudo apt install python3-pip
$sudo apt install python-is-python3
```

## Visual Studio Code Remote

1. 安装Visual Studio Code Remote插件 [VS code: Developing in WSL](https://code.visualstudio.com/docs/remote/wsl)

2. 在Ubuntu终端执行
 
 ```bash
 $code .
```

## 参考链接

* [Windows Subsystem for Linux (WSL))](https://docs.microsoft.com/zh-cn/windows/wsl/)
   
  * [Install Windows Subsystem for Linux (WSL) on Windows 10(Chinese)](https://docs.microsoft.com/zh-cn/windows/wsl/install-win10)

* [VS code: Developing in WSL](https://code.visualstudio.com/docs/remote/wsl)

* [VS code: Using C++ and WSL in VS Code](https://code.visualstudio.com/docs/cpp/config-wsl#nodejs-articles)
