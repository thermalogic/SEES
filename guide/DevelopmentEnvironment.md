# Development Environment

## A OS：

  Windows10 64

* 1 Southeast University

  * January 2015, Southeast University and Microsoft Corp provide legitimate Windows, Office for the staffs and students.

  http://nic.seu.edu.cn/2015/0113/c12333a115289/page.htm
  
* 2 Microsoft Corp
  
   * https://www.microsoft.com/en-gb/software-download/windows10
     * Do you want to install Windows 10 on your PC?
       
       download and run the media creation tool: http://go.microsoft.com/fwlink/?LinkId=691209
 
## B Development tools and packages

* Python3:  https://www.python.org/downloads/
* Python Packages
  * Scipy for Windows:  http://www.lfd.uci.edu/~gohlke/pythonlibs/ 
  * Jupyter: http://jupyter.org/
     ```
         >pip install jupyter
     ```
  * IAPWS-IF97:
     * https://github.com/PySEE/EDUIF97
     * https://github.com/jjgomera/iapws
      ```
          >pip install iapws
      ```

* Visual Studio Code：https://code.visualstudio.com/

* MinGW-W64 (GCC) Compiler Suite: https://sourceforge.net/projects/mingw-w64/files/

* Git for Windows.  https://github.com/git-for-windows/git/releases

## C Set up your development environment

### 1 安装Python3.5
    
* 从Python官网下载Windows 64位Python3.5.2：  https://www.python.org/downloads/

  * 定制方式安装: 
      
      1) 安装软件到目录： C:\python35
            
      2) 勾选“Add Python3.5 to Path” 

![Python352](./img/python352.jpg)
   
* 更新pip到新版本:DOS命令行下
```bash
  >python -m pip install -U pip
```

### 2 安装Jupyter Notebook

* 安装：命令行

```bash       
    >pip install jupyter
```      

* 启动Jupyter notebook： 命令行

```bash       
    >jupyter notebook     
```

*   建立Jupyter Notebook目录和快速启动Jupyter Notebook

    * 指定某个文件夹为自己的Jupyter Notebook工作目录，在该文件夹下启动Jupyter Notebook服务，存放用Jupyter Notebook建立的项目。

    * 快速启动Jupyter Notebook：

      在指定的Jupyter Notebook工作文件夹中，新建一空白文本文档，输入内容"jupyter notebook"

      将文本文件另存，文件名自定义，但必须加上".bat"后缀，如"start.bat"，文件类型选择""所有文件"

      双击"start.bat"文件，启动Jupyter Notebook 

### 3 科学计算包 
   
        numpy,scipy, matplotlib

从  http://www.lfd.uci.edu/~gohlke/pythonlibs/ 下载Windows64位包, 然后,pip命令安装（*指下载的软件包名）

```bash       
   > pip install *.whl
```       

### 4 IF97物性计算

* 4.1 Python版IF97

预先安装好numpy和scipy

```bash       
   > pip install iapws
``` 

* 4.2 C共享库版

从github的课程仓库：https://github.com/PySEE/EDUIF97 下载仓库zip文件

![下载仓库zip文件](./img/downloadseuif97.jpg)
   
*  解压下载的zip文件，然后：
   
        1)将libseuif97.dll拷贝到 c:\windows\system
        2)将seuif97.py拷贝到python安装目录的lib子目录下，如C:\python35\Lib
 
### 5 Visual Studio Code

Visual Studio Code is a lightweight but powerful source code editor which runs on your desktop and is available for Windows, macOS and Linux. It comes with built-in support for JavaScript, TypeScript and Node.js and has a rich ecosystem of extensions for other languages (such as C++, C#, Python, PHP, Go) and runtimes (such as .NET and Unity). 

1  Download and Installl Visual Studio Code 
 
   https://code.visualstudio.com/

2 Install Python Extension in  Visual Studio Code

    https://code.visualstudio.com/docs/languages/python

3 Install the Microsoft C/C++ extension

    https://code.visualstudio.com/docs/languages/cpp

### 6  Version control with GIT

* Git for Windows.  https://github.com/git-for-windows/git/releases

### 7 Eclipse IDE
  
  * Java JDK: http://www.oracle.com/technetwork/java/javase/downloads/index.html
  
  * Eclipse CDT: http://www.eclipse.org/
  
  * Pydev: http://pydev.org/

## D 使用课件

 预先安装好Python和Jupyter Notebook
 
* 从github下载课程home仓库zip文件: https://github.com/PySEE/home

![下载课程home仓库zip文件](./img/downloadhome.jpg)

* 启动课程Jupyter Notebook
 
  解压下载的 zip 文件,运行notebook子目录下的批处理文件: **StartNB.bat**，启动课程Jupyter Notebook服务

## E 其他

