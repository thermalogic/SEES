# Guide of  Building Software Environment for Beginners

https://github.com/PySEE/home/tree/S2019/guide/BuildingSoftwareEnvironment.md 

Firstly，You **MUST** setup the working directory for the course

https://github.com/PySEE/home/tree/S2019/guide/AdvWorkingDir.md

then,following the steps

* [A: Python](#A:Python) Python, Autopep8,Pylint,IDLE

* [B: Jupyter Notebook](#B:Jupyter):  Jupyter Notebook,PySEE/Home

* [C: Visual Studio Code](#C:VSCode): Markdown,Python
  
* [D: Science and Engineering](#D:ScienceEngineering)

  * Numpy, Scipy, Matplotlib

  * IAPWS, SEUIF97

* [E: Advanced](#E:Advanced)  Git(Github), Mingw-W64(GCC for Windows)

## A:Python

Goto the official Python site  https://www.python.org/downloads/ to download the suitable version Python，e.g.**Python for Windows**： https://www.python.org/downloads/windows/

Python 3.7.0 for Windows x86-64 executable installer 

https://www.python.org/ftp/python/3.7.0/python-3.7.0-amd64.exe

###  Customize Installation
      
* 1  Make sure you **check** option **Add Python 3.7 to PATH**

* 2  To change install location, click on **Customize installation** , then **Next** and enter **C:\python35** the item of  **Customize installation location**
            
 
![Python3-path](./img/python37-path.jpg)

![Python3-location](./img/python37-location.jpg)
   
### update pip to the most recent version

From a command prompt:

```bash
>python -m pip install -U pip -i  https://pypi.tuna.tsinghua.edu.cn/simple
```

![Python3-update](./img/python37-update-pip.jpg)

### Install Packages

The Python Package Index(PyPI) is a repository of software for the Python programming language.

https://pypi.org/

### Use **pip** to install packages

```bash
>pip  install packagename  
```

Install from the mirror site　@ tsinghua 

#### NOTE: you may use the mirror site to install for the speed

```bash
>pip  install packagename  -i  https://pypi.tuna.tsinghua.edu.cn/simple
```


* **Install autopep8, pylint**

```bash  
>pip install autopep8 -i  https://pypi.tuna.tsinghua.edu.cn/simple
>pip install pylint -i  https://pypi.tuna.tsinghua.edu.cn/simple
```

### Using IDLE

![idle](./img/idle.png)

## B:Jupyter

### Install 
  
```bash       
>pip install jupyter  -i  https://pypi.tuna.tsinghua.edu.cn/simple
```    

### Using

```bash       
>jupyter notebook
```    

![ipynb-1](./img/ipynb-1.png)

![ipynb-2](./img/ipynb-2.png)

### Using the Jupyter Notebook of  PySEE

https://github.com/PySEE/home


## C:VSCode

### Install

### Install VS Code

  https://code.visualstudio.com/

### Install Python Extension

https://code.visualstudio.com/docs/languages/python

### Using VS Code

![vscode](./img/vscode.png)

## D:ScienceEngineering

### Installing Scipy Packages(Numpy,scipy,matplotlib) 

Scipy  https://www.lfd.uci.edu/~gohlke/pythonlibs/ 
    
```bash
>pip install *.whl
```  
### Installing IAPWS-IF97

* Python's IAPWS

```bash
>pip install iapws -i  https://pypi.tuna.tsinghua.edu.cn/simple
```

* SEUIF97

```bash
>pip install seuif97 -i  https://pypi.tuna.tsinghua.edu.cn/simple
```
   
## E:Advanced

### Installing Git 
   
* Install Git for Windows: https://git-scm.com/download/win

* Clone the repos of https://github.com/PySEE to your computer

 ### GCC C/C++

* Install Mingw-W64(GCC for Windows)

* add C/C++ extensions of VS code

* Programming C/C++ with GCC 