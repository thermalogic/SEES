
## Contents

* [The Guide of Building Software Environment](./BuildingSoftwareEnvironment.md)

   * [The Computer Terminal](./ComputerTerminal.md/)

   * [Windows File System](./WindowsFileSystem.md)

* [Introduction to Markdown](./Introduction2Markdown(Chinese).md) 

* [Resources On Github](./ResourcesOnGithub.md)

* [The Simple Guide to Github](./TheSimpleStepsGithub(Chinese).md) 

* [Creating UML diagrams for python code](./UMLPython.md) 

* [Ubuntu，Python and GCC](./Ubuntu-Python-CPP(Chinese).md) 

* [Install OpenModelica](./InstallOpenModelica.md) 

* [Further Studing](./FurtherStuding.md)

## 软件安装建议

###  安装顺序

    1. Python解释器    2. VS Code代码编写软件及Python和C/C++插件

    3. Git版本控制软件  4. Python各种软件包  5. MinGW-W64(GCC)

###  安装要点

#### Python解释器

1. `勾选`,将解释器安装路径加入系统环境变量Path: `Add Python 3.* to PATH`

2.  选择自定义安装：`Customize Installation`，勾选相关项目
  
3. 按照Python解释器版本号，自定义`简短`的安装目录(`Customize Install location`)，如：
      
    *  Python3.7，定义为 `C:\Python37`；Python3.8，定义为 `C:\Python38`

#### Python各种软件包
 
##### 设定`tsinghua`为软件包的源 

如在终端逐个使用`pip`安装软件包，安装前，务必设定`tsinghua`为软件包的源 

```bash
>pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

##### 快速安装Python软件包

将 [installpackage.bat](./bat/installpackage.bat)和 [requirements.txt](./bat/requirements.txt) 保存到本地电脑的同一个目录中，然后，双击 [installpackage.bat](./bat/installpackage.bat)，即可一次性完成：

* 设定tsinghua`为软件包的源；安装课程需要的Python软件包的工作

### MinGW-W64(GCC)

* 将安装路径加入系统环境变量`Path`

* 重命名 `mingw32-make.exe` 为 `make.exe`

## 历史问题及答案

* [Problem and Answer](./Problem_Solution.md)

