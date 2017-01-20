
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

   原因：使用管理员权限运行cmd,都启动到C:\Windows\system32（Windows的一个bug）

   解决方法：使用普通用户权限运行jupyter notebook

* **4 Windows安全防护**

   *  微软提供的security essentials是Windows最好的安全防护软件
  
        可从下面网址下载和操作系统对应的版本（Windows 10默认已经安装），然后，安装security essentials

        http://windows.microsoft.com/zh-cn/windows/security-essentials-download
      
        安装security essentials，卸载所有其他各种"安全”软件。
   
* **5 Python源码文件中含中文字符**

     需指定源码文件的编码方式为 utf-8

     在Python源码文件的第一行加上

 ```
	       # -*- coding: utf-8 -*-
 ```





