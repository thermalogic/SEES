
# FAQ 

* **1 pip install  --upgrade pip 失败** 

  原因：pip的bug
 
  解决方法：
    
     python -m pip install -U pip
 
  参见： https://pip.pypa.io/en/stable/installing/

* **2 在Windows系统下安装Python3.x，提示： Installation Fail 0x80240017** 

    原因： Windows系统中缺少Python3.x需要的C运行时库

    解决方法： 使用管理员权限、联网，然后，运行Python安装软件 

* **3 命令行执行>jupyter notebook后，jupyter总是启动到C:\Windows\system32** 

   原因：使用管理员权限运行cmd,都启动到C:\Windows\system32

   解决方法：使用普通用户权限运行jupyter notebook

* **4 Windows安全防护**

   *  微软提供的security essentials是Windows最好的安全防护软件
  
        可从下面网址下载和操作系统对应的版本（Windows 10默认已经安装），然后，安装security essentials

        http://windows.microsoft.com/zh-cn/windows/security-essentials-download
      
        安装security essentials，卸载所有其他各种"安全”软件。
   
* **5 Python源码文件中含中文字符**

     需指定源码文件的编码方式为 utf-8

     在Python源码文件的第一行加上

 ```python
	       # -*- coding: utf-8 -*-
 ```

* **6 module ‘unittest’hasn't the attribute of ‘TestCase’**

03014311 骆应东

我在一开始写单元测试的程序时将其写在一个命名为unittest的程序文件里，这个时候运行程序会出现错误 module ‘unittest’hasn't the attribute of ‘TestCase’提示

通过请教老师、同学，最后发现是因为文件命名为unittest，然后当运行程序import unittest时系统会‘迷路’，因为文件名和Python的自带包unittest发生混淆，系统无法正确引用Python的unittest包。所以解决办法是：将文件名修改为非unittest即可。


* **7 Windows环境下Jupyter notebook文件转换pdf失败**

Jupyter notebook中可以ipynb转换为pdf

1 Windows环境下需要安装MikTex

2 安装 pip install pandoc

3 upyter nbconvert  --to pdf  需要转换的ipynb文件名

这时从MikTex的远程仓库下载资源，会出现失败的问题，转换终端

* 解决的方法很笨：

多试验几次

```bash   
>jupyter nbconvert  --to pdf  需要转换的ipynb文件名
```

从源头下载.


