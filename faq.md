
# Foundamentals and practice of software engineering with Python

#### pip install  --upgrade pip  有时失败

 原因：pip 包bug
 
 解决方法：
    
     python -m pip install -U pip
 
 参见：
 
   https://pip.pypa.io/en/stable/installing/

#### Python3.*  Windows 7/8 - Installation Fail 0x80240017 

原因：Python 包使用的编译器和 Windows 7/8系统包不一致

解决方法：

   1）更换Python3.*版本，如3.5改为3.4
   
   2）升级操作系统到Windows10

参见：    

   http://bugs.python.org/issue25157
   
#### 命令行>jupyter notebook,总是启动到C：\Windows\system32 

原因：Window的一个bug，使用管理员权限运行cmd,都启动到C：\Windows\system32

解决方法：使用普通用户权限运行jupyter notebook