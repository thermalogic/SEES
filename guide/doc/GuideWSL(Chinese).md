# WSL开发环境

## 安装WSL

1. 安装WSL: [Install Windows Subsystem for Linux (WSL) on Windows 10(Chinese)](https://docs.microsoft.com/zh-cn/windows/wsl/install-win10)

建议使用Ubuntu20.04 LTS 

2. 建立用户

在Windows的cmd/powershell终端输入

```text
>wsl
```

启动新安装的 Linux 分发版, 在Linux系统终端，创建用户帐户和密码

3. 修改ubuntu软件源

WSL在电脑中的安装目录是：C:\Users\你的当前用户名\AppData\Local\Packages\

用`sources.list`覆盖WSL原文件，配置软件源为aliyun.

* C:\Users\你的当前用户名\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu20.04onWindows_79rhkp1fndgsc\LocalState\rootfs\etc\apt

4. 更新系统

在Ubuntu终端执行

```bash
$sudo apt update
$sudo apt upgrade
```

5. 安装开发软件

在Ubuntu终端执行

```bash
$sudo apt install g++ gcc
$sudo apt install python3-pip
```

## Visual Studio Code Remote

1. 安装Visual Studio Code Remote  [VS code: Developing in WSL](https://code.visualstudio.com/docs/remote/wsl)

2. 在Ubuntu终端执行
 
 ```bash
 $code .
```

## 参考链接

* [Windows Subsystem for Linux (WSL))](https://docs.microsoft.com/zh-cn/windows/wsl/)
   
* [Install Windows Subsystem for Linux (WSL) on Windows 10(Chinese)](https://docs.microsoft.com/zh-cn/windows/wsl/install-win10)

* [VS code: Developing in WSL](https://code.visualstudio.com/docs/remote/wsl)

* [VS code: Using C++ and WSL in VS Code](https://code.visualstudio.com/docs/cpp/config-wsl#nodejs-articles)
