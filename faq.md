
# FAQ 

* **pip install  --upgrade pip ** 失败

  原因：pip的bug
 
  解决方法：
    
     python -m pip install -U pip
 
  参见：
 
   https://pip.pypa.io/en/stable/installing/

*  **在Windows 7/8系统下安装Python3.x，提示： Installation Fail 0x80240017 ** 

    原因： Windows7/8系统中缺少Python3.x需要的C运行时库

   解决方法：
   
    * 升级操作系统到Windows10
   
    * 当前操作系统打更新补丁/手工更新补充缺少的C运行时库
    
      https://support.microsoft.com/en-us/kb/2999226

   参见：   http://bugs.python.org/issue25157
   
* **命令行执行>jupyter notebook后，jupyter总是启动到C:\Windows\system32** 

   原因：使用管理员权限运行cmd,都启动到C:\Windows\system32（Windows的一个bug）

   解决方法：使用普通用户权限运行jupyter notebook

* **Windows安装防护**

   *  微软提供的security essentials是Windows最好的安全防护软件
  
     可从下面网址下载和操作系统对应的版本，然后，安装security essentials

      http://windows.microsoft.com/zh-cn/windows/security-essentials-download
      
 * 安装security essentials，卸载所有其他各种"安全”软件。



