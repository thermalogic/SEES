# Guide of  Building Software Environment for Beginners

https://github.com/PySEE/home/tree/S2019/guide/BuildingSoftwareEnvironment.md 

* [A: Basic](#A:Basic) Python, IDLE

* [B: Enhanced](#B:Enhanced): 
  
  * Visual Studio Code(Markdown,Python),
  
  * autopep8,Pylint

* [C: Jupyter Notebook](#C:jupyter):  Jupyter Notebook,PySEE/Home
  
* [D: Science and Engineering](#D:ScienceandEngineering)

  * Numpy, Scipy, Matplotlib

  * IAPWS, SEUIF97

* [E: Advanced](#E:Advanced)  Git(Github), Mingw-W64(GCC for Windows)

## A:Basic

Goto the official Python site  https://www.python.org/downloads/ to download the suitable version Python，e.g.**Python for Windows**

https://www.python.org/downloads/windows/

Download Python 3.5.4 for Windows x86-64 executable installer 

https://www.python.org/ftp/python/3.5.4/python-3.5.4-amd64.exe

###  The custom install: 
      
  * 1 Install to dir： C:\python35
            
  * 2 check “Add Python3.5 to Path” 

![Python3](./img/python35.jpg)
   
### update pip to the most recent version

From a command prompt:
```bash
  >python -m pip install -U pip
```

### Using IDLE

![idle](./img/idle.png)


## B:Enhanced

### Install  VS Code

  https://code.visualstudio.com/

### Install Python Extension

https://code.visualstudio.com/docs/languages/python

### Using VS Code

![vscode](./img/vscode.png)

### install autopep8, pylint
```bash  
>pip install autopep8
>pip install pylint
```

## C:Jupyter

### install
  
```bash       
>pip install jupyter
```    
#### NOTE: you may use the mirror site to install for the high speed

Install from the mirror site　@ tsinghua

```bash  
>pip install jupyter -i  https://pypi.tuna.tsinghua.edu.cn/simple
```  

### using

```bash       
>jupyter notebook
```    
![ipynb-1](./img/ipynb-1.png)

![ipynb-2](./img/ipynb-2.png)

### using the Jupyter Notebook of  PySEE

https://github.com/PySEE/home

## D:Science and Engineering

### Installing Scipy Packages(Numpy,scipy,matplotlib) 

Scipy  https://www.lfd.uci.edu/~gohlke/pythonlibs/ 
    
```bash
>pip install *.whl
```  
### Installing IAPWS-IF97

* Python's IAPWS

```bash
>pip install iapws
```

* SEUIF97

```bash
>pip install seuif97
```
   
## E:Advanced

### Installing Git 
   
* Install Git for Windows: https://github.com/git-for-windows/git/releases

* Clone the repos of https://github.com/PySEE to your computer

 ### GCC C/C++

* Install Mingw-W64(GCC for Windows)

* add C/C++ extensions of VS code

* Programming C/C++ with GCC 