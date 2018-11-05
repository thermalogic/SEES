# Guide of  Building Software Environment for Beginners

Firstly，You **MUST** setup the working directory for the course

https://github.com/PySEE/home/tree/S2019/guide/AdvWorkingDir.md

then,following the steps

* [A: Python](#A:Python) Python, Autopep8,Pylint,IDLE

* [B: Jupyter Notebook](#B:Jupyter): Jupyter Notebook, PySEE/Home

* [C: Visual Studio Code](#C:VSCode): Markdown,Python
  
* [D: Git/Github](#D:Git): `Clone` PySEE/home

## A:Python

Goto the official Python site  https://www.python.org/downloads/ to download the suitable version Python，e.g.**Python for Windows**： https://www.python.org/downloads/windows/

Python 3.7.0 for Windows x86-64 executable installer：
https://www.python.org/ftp/python/3.7.0/python-3.7.0-amd64.exe

###  Customize Installation
      
* 1  Make sure you **check** option **Add Python 3.7 to PATH**

* 2  To change install location, click on **Customize installation** , then **Next** and enter **C:\python37** the item of  **Customize installation location**
            
 
![Python3-path](./img/python37-path.jpg)

![Python3-location](./img/python37-location.jpg)
   

### Install Packages

The Python Package Index(PyPI) is a repository of software for the Python programming language.

https://pypi.org/

#### Use `pip` to install packages

`pip` is a package manage for Python. It makes installing and uninstalling Python packages

**install** 

The following command will install the latest version of a module and its dependencies from the Python Packaging Index:

```bash
>python -m pip install SomePackage  
```

**Upgrading**
Normally, if a suitable module is already installed, attempting to install it again will have no effect. Upgrading existing modules must be requested explicitly:

```bash
>python -m pip install --upgrade SomePackage  
```

**use the `mirror site`  to install for the speed**

```bash
>python -m pip install SomePackage  -i  mirrorsite  
``` 

install from the mirror site `@tsinghua`: https://pypi.tuna.tsinghua.edu.cn/simple

```bash
>pip  install packagename  -i  https://pypi.tuna.tsinghua.edu.cn/simple
```

**uninstall**  

```bash
>pip uninstall packagename  
```

**Show help for commands**

```bash
>pip  help  
```

#### update `pip` to the most recent version

```bash
>python -m pip install -U pip -i  https://pypi.tuna.tsinghua.edu.cn/simple
```
![Python3-update](./img/python37-update-pip.jpg)

#### Install autopep8, pylint

```bash  
>python -m pip install autopep8 -i  https://pypi.tuna.tsinghua.edu.cn/simple
>python -m pip install pylint -i  https://pypi.tuna.tsinghua.edu.cn/simple
```

or

```bash  
>python -m pip install autopep8 pylint -i  https://pypi.tuna.tsinghua.edu.cn/simple
```

### Using IDLE

![idle](./img/idle.png)

## B:Jupyter

### Install 
  
```bash       
>python -m pip install jupyter  -i  https://pypi.tuna.tsinghua.edu.cn/simple
```    

### Using

```bash       
>jupyter notebook
```    

![ipynb-1](./img/ipynb-1.png)

![ipynb-2](./img/ipynb-2.png)

* Literate programming your Jupyter Notebook in the `specific working folder`：

  * `1` make the specific folder for  your **Jupyter Notebook**,for example: `D:/mynotebook`

  * `2` **Open a cmd window in the folder**:  If you're already in the folder you want, you do `Shift+[mouse right-click]` on the background of the Explorer window, then click on "Open command window here" or "Open PowerShell window here"

  * `3` Enter `jupyter notebook` in cmd window of the folder,you will see the active jupyter server. the folder is the default  folder of your Jupyter Notebook 

   ![jupyter-cmd](./img/jupyter-cmd.jpg) 

     *  start **Jupyter Notebook** quickly 

         * `1` make the **"start.bat"** batch file with the content **`jupyter notebook`** through Windows's **notepad.exe**(记录本)  in the working folder of your Jupyter Notebook

         * `2` Double-click **`start.bat`**，Start **Jupyter Notebook**  server

 ![jupyter-quick](./img/jupyter-bat.jpg) 

### Using the Jupyter Notebook of  PySEE/hone

* Go to the repo **home** on the Github: https://github.com/PySEE/home download `home.zip`

![download home.zip](./img/downloadhome.jpg)

* Start Jupyter Notebook of the course
 
  unzip home.zip, double-click  `StartNB.bat`  under the folder of **notebook** to start **Jupyter Notebook** 

## C:VSCode

Visual Studio Code is a lightweight but powerful source code editor which runs on your desktop and is available for Windows, macOS and Linux. It comes with built-in support for JavaScript, TypeScript and Node.js and has a rich ecosystem of extensions for other languages (such as C++, C#, Python, PHP, Go) and runtimes (such as .NET and Unity). 

### Download and Install Visual Studio Code 
 
    https://code.visualstudio.com/

### Install Python Extension

    https://code.visualstudio.com/docs/languages/python

### Using VS Code

![vscode](./img/vscode.png)

## D:Git

**`1`** Install Git for Windows: https://git-scm.com/download/win

**`2`** Clone the S2019 branch of the [home](https://github.com/PySEE/home) to your computer

```bash
>git clone --depth 1 -b S2019 https://github.com/PySEE/home.git
```

## More

https://github.com/PySEE/home/tree/S2019/guide/BuildingSoftwareEnvironment.md 