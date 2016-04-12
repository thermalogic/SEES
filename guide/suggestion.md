
#### pip install  --upgrade pip  有时失败

 原因：pip 包bug
 
 解决方法：
    
     python -m pip install -U pip
 
 参见：
 
   https://pip.pypa.io/en/stable/installing/

#### Python3.*  Windows 7/8 - Installation Fail 0x80240017 

原因：Python的编译时使用的C运行时库和 Windows系统中的不一致

解决方法：

   1）更换Python3.*版本，如3.5改为3.4
   
   2）升级操作系统到Windows10
   
   3) 手工更新 windows的通用C运行时库
    
      https://support.microsoft.com/en-us/kb/2999226

参见：    

   http://bugs.python.org/issue25157
   
#### 命令行>jupyter notebook后，jupyter总是启动到C:\Windows\system32 

原因：Windows的一个bug，使用管理员权限运行cmd,都启动到C:\Windows\system32

解决方法：使用普通用户权限运行jupyter notebook

#### Windows安装防护

1 微软提供的security essentials是Windows最好的安全防护软件。从下面网站下载和操作系统对应的版本安装，

http://windows.microsoft.com/zh-cn/windows/security-essentials-download

2 安装security essentials，卸载所有其他各种"安全”软件。

#### Mathjax安装失败

2016年在线安装的Jupyter已经默认安装了mathjax，无需再安装

#### EGIT

EGIT已经是Eclipse的默认插件，无需再安装

#### Python文件中含中文的编码方式

务必使用


```
	# -*- coding: utf-8 -*-
```

以保持高兼容性


