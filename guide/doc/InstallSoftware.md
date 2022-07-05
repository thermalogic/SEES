

**Install Software**


<!-- TOC -->

- [A: Python & Package](#a-python--package)
  - [A.1 Installing Python](#a1-installing-python)
  - [A.2 Install Package using pip](#a2-install-package-using-pip)
    - [A.2.1 set the faster mirror index site of PyPi](#a21-set-the-faster-mirror-index-site-of-pypi)
    - [A.2.2 update pip to the most recent version](#a22-update-pip-to-the-most-recent-version)
    - [A.2.3 Install  Packages](#a23-install--packages)
- [B: Install Jupyter Notebook](#b-install-jupyter-notebook)
- [C: Install GCC for Windows：TDM-GCC](#c-install-gcc-for-windowstdm-gcc)
- [D: Visual Studio Code](#d-visual-studio-code)
  - [D.1 Install Visual Studio Code](#d1-install-visual-studio-code)
  - [D.2 Install Extensions](#d2-install-extensions)
- [E: Install Git for Windows](#e-install-git-for-windows)
- [F: PlantUML](#f-plantuml)

<!-- /TOC -->
## A: Python & Package

### A.1 Installing Python 

Goto [the official Python site](https://www.python.org/downloads/) to download the suitable version of Python.

In the course ,we use [Python 3.10.5 for Windows x86-64](https://www.python.org/ftp/python/3.10.5/python-3.10.5-amd64.exe)  

* Firstly, make sure you **check** option **Add Python 3.10 to PATH**

  ![Python3-install-path](./img/python38-install-path.jpg) 

>**注意**：最新版Python解释器可能会存在软件包兼容性问题，这时建议安装稍旧版本的解释器

### A.2 Install Package using pip

#### A.2.1 set the faster mirror index site of PyPi

```shell
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

#### A.2.2 update pip to the most recent version

```shell
python -m pip install -U pip
```

#### A.2.3 Install  Packages

```shell
python -m pip install autopep8 pylint
```

```shell 
python -m pip install numpy scipy matplotlib
``` 

```shell 
python -m pip install prettytable
```

```shell 
python -m pip install  coolprop 
``` 

```shell 
python -m pip install  phyprops 
```
```shell
python -m pip install  psutil pypistats   
```

```shell
python -m pip install PyQt6  
```

## B: Install Jupyter Notebook

To install Jupyter,run the following command in a terminal:

```shell 
python -m pip install jupyter
```

Install Jupyter Notebook extension

```shell 
python -m pip install jupyter_contrib_nbextensions
```

Install javascript and css files

```shell 
jupyter contrib nbextension install --user
```

## C: Install GCC for Windows：TDM-GCC

Goto [TDM-GCC](https://jmeubank.github.io/tdm-gcc/) to download the latest available version of gcc compiler for **Windows64**,run the installer.

After the install, **copy**  `.\bin\mingw32-make.exe` to  `.\bin\make.exe`

## D: Visual Studio Code

### D.1 Install Visual Studio Code 
 
* Download  Visual Studio Code https://code.visualstudio.com/, then install

   ![vscode](./img/vscode.jpg)

* Add the shortcut of VS code to `Task bar`

   ![vscode-taskbar](./img/vscode-taskbar.jpg)
 
### D.2 Install Extensions

* [Python](https://code.visualstudio.com/docs/languages/python)

* [C/C++](https://code.visualstudio.com/docs/languages/cpp)

* [Markdown preview enhanced](https://shd101wyy.github.io/markdown-preview-enhanced/#/zh-cn/)

* [PlantUML](https://github.com/qjebbs/vscode-plantuml/)

* **vscode-pdf**

* **Rainbow CSV**

Open VS Code, then **search** the name of extension, then click **Install** button.

For example:

  ![vscode-ext-python](./img/vscode-ext-python.jpg)


## E: Install Git for Windows

Download Git for Windows: https://git-scm.com/ ,then install

## F: PlantUML

Install: Java, Graphviz

* [Java](https://www.java.com/en/download/)

* [Graphviz](https://graphviz.org/download/)

   * [graphviz-4.0.0(64-bit) EXE installer](https://gitlab.com/api/v4/projects/4207231/packages/generic/graphviz-releases/4.0.0/windows_10_cmake_Release_graphviz-install-4.0.0-win64.exe)