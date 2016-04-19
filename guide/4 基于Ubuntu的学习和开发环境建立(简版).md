# 基于Ubuntu的学习和开发环境建立

Linux操作系统是目前开源软件技术开发的主流平台，Ubuntu是多种Linux发行版中用户较多的一种。

建立Ubuntu下的开发环境，就迈出了学习Linux环境下的开发技术，感受日新月异的IT技术发展的第一步。

## 安装Ubuntu系统

### 安装方式

Windows是目前同学们的主要工作环境，因此，在目前已经安装了Windows系统基础上，安装双系统是较好的安装模式。

安装前，在Windows环境下，从空余的硬盘空间中划分出一个空的独立分区，供安装Ubuntu使用。

基本安装空间10G左右就可以了，为了以后工作方便，更大些为好，如：50G


### 安装版本

因为同学们需要使用中文，建议使用“中国味”的UbuntuKylin。

UbuntuKylin 官网：http://www.ubuntukylin.com/

使用2016年4月发布的UbuntuKylin16.04 LTS版(64位)。

## 建立Python3开发环境

Ubuntu16.04系统缺省安装有Python3.5.1，但不完整，需补充: pip3、idle3。

在线安装：
```bash
    sudo apt install python3-pip
    sudo apt install idle3
```

### 安装scipy

Scipy系列软件包，使用apt在线安装安装。apt安装的是编译好的库
```bash
sudo apt install python3-numpy python3-scipy python3-matplotlib
```

### 安装Jupyter

pip3在线安装
 
首先安装setuptools：
```bash
   sudo –H pip3 install setuptools  
 ```  
然后，再安装Jupyter

```bash
sudo –H pip3 install jupyter
```

## Eclipse开发环境

###  安装JDK

Ubuntu16.04缺省没有安装JDK，在线安装openjdk-8-jre
```bash
sudo apt install openjdk-8-jre
```

###  安装Eclipse IDE
    
    1. 下载Linux版的Eclipse CDT，解压
   
    2. 安装Pydev插件
    
    3. 支持C/C++: Ubuntu16.04系统内置gcc编译器。
