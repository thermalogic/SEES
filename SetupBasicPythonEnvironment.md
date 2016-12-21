# 建立课程的基本学习环境

操作系统： Windows10,64位
 
## 1 安装Python3.5
    
* 从Python官网下载Windows 64位ython3.5软件：  https://www.python.org/downloads/

* 定制方式安装: 
      
   1) 加环境变量PATH; 
   2) 目录： C:\python35

* 更新pip到新版本: 
  
      在DOS命令行下， 更新pip到新版本：

          >python -m pip install -U pip

## 2：安装Jupyter Notebook

*  1) 安装,命令行下:
        
       > pip install jupyter 
       
*  2) 启动Jupyter notebook,   命令行：
      
      >jupyter notebook     

## 3： 科学计算包 
   
        scipy
        numpy
        matplotlib
     
     从
     
     http://www.lfd.uci.edu/~gohlke/pythonlibs/
     
     下载Windows 64位计算包
    
    命令行下:
    
       > pip install *.whl
       
    逐个本地安装

## 4： IF97物性计算
    
*  从github下载
    
       https://github.com/Py03013052/SEUIF97 
   
*  解压下载的zip文件，然后：
   
        1)将SEUIF97.dll拷贝到 c:\windows\system
        2)将seuif97.py拷贝到python安装目录的lib子目录下，如C:\python35\Lib

## 5：课件

* 从github下载课件
    
      https://github.com/Py03013052/home

* 启动课程Jupyter Notebook

    解压下载的 zip 文件,运行notebook子目录下的批处理文件
      
          StartNB.bat
   
    启动课程Jupyter Notebook服务



