# Python学习和开发环境的建立

操作系统： Windows10  64位；计算机联网
 
## 1 安装Python3.5
    
* 从Python官网下载Windows 64位Python3.5.2：  https://www.python.org/downloads/

  * 定制方式安装: 
      
      1) 安装软件到目录： C:\python35
            
      2) 勾选“Add Python3.5 to Path” 

![Python352](./guide/img/python352.jpg)
   
* 更新pip到新版本:DOS命令行下
```bash
  >python -m pip install -U pip
```

## 2 安装Jupyter Notebook

* 安装：命令行

```bash       
    >pip install jupyter
```      

* 启动Jupyter notebook： 命令行

```bash       
    >jupyter notebook     
```
## 3 科学计算包 
   
        scipy
        numpy
        matplotlib

从  http://www.lfd.uci.edu/~gohlke/pythonlibs/ 下载Windows 64位包, 然后pip命令安装（*指下载的软件包名）

```bash       
   > pip install *.whl
```       

## 4 IF97物性计算
    
*  从github下载课程SEUIF97仓库zip文件：https://github.com/PySEE/SEUIF97 

![下载课程SEUIF97仓库zip文件](./guide/img/downloadseuif97.jpg)
   
*  解压下载的zip文件，然后：
   
        1)将SEUIF97.dll拷贝到 c:\windows\system
        2)将seuif97.py拷贝到python安装目录的lib子目录下，如C:\python35\Lib

## 5 课件

* 从github下载课程home仓库zip文件: https://github.com/PySEE/home

![下载课程home仓库zip文件](./guide/img/downloadhome.jpg)

* 启动课程Jupyter Notebook

解压下载的 zip 文件,运行notebook子目录下的批处理文件: **StartNB.bat**

启动课程Jupyter Notebook服务



