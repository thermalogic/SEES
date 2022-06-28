
# Using Software

<!-- TOC -->

- [Using Software](#using-software)
  - [A：The Python Packages](#athe-python-packages)
    - [A.1 Install](#a1-install)
    - [A.2 Upgrading](#a2-upgrading)
    - [A.3 Install from an alternate index site](#a3-install-from-an-alternate-index-site)
    - [A.4 uninstall](#a4-uninstall)
    - [A.5 set one alternate index site as the default site](#a5-set-one-alternate-index-site-as-the-default-site)
    - [A.6 Show help for commands](#a6-show-help-for-commands)
  - [B:Jupyter Notebook](#bjupyter-notebook)
    - [B.1 Start-up Jupyter Notebook](#b1-start-up-jupyter-notebook)
    - [B.2 Literate programming your Jupyter Notebook in the `specific working folder`](#b2-literate-programming-your-jupyter-notebook-in-the-specific-working-folder)
      - [B.2.1 Start Jupyter Notebook in a specific folder with `batch` file](#b21-start-jupyter-notebook-in-a-specific-folder-with-batch-file)
      - [B.2.2 Create a new notebook document](#b22-create-a-new-notebook-document)
    - [B.3 Using the Jupyter Notebook of thermalogic/SEES](#b3-using-the-jupyter-notebook-of-thermalogicsees)
  - [D:Visual Studio Code](#dvisual-studio-code)
    - [D.1 Getting Started with Python in VS Code](#d1-getting-started-with-python-in-vs-code)
    - [D.2 Getting Started with C/C++ in VS Code](#d2-getting-started-with-cc-in-vs-code)
  - [E: Using Git with  thermalogic/SEES](#e-using-git-with--thermalogicsees)
      - [E.1 Clone the thermalogic/SEES to your computer](#e1-clone-the-thermalogicsees-to-your-computer)
      - [E.2 Updating to The Latest Version](#e2-updating-to-the-latest-version)
      - [E.3 Discard Changes](#e3-discard-changes)
  - [References](#references)

<!-- /TOC -->
## A：The Python Packages

The Python Package Index(PyPI) is a repository of software for the Python programming language.: https://pypi.org/

`pip` is a package manage for Python. It makes installing and uninstalling Python packages

* Installing Python Modules : https://docs.python.org/3/installing/

pip is a command line program which can be run from the command prompt as follows in Windows:

```
python  -m pip <pip arguments>
```

### A.1 Install 

The most common scenario is to install from PyPI

```python
python -m pip install SomePackage            # latest version
python -m pip install SomePackage==1.0.4     # specific version
python -m pip install 'SomePackage>=1.0.4'     # minimum version
```

for example:
```
python -m pip install  coolprop 
```
 
Install the  `multiple` modules at the one `pip install` command

```bash
python -m pip install SomePackage1  SomePackage2 
```

for example:

```
python -m pip install  autopep8 pylint 
```

### A.2 Upgrading

Normally, if a suitable module is already installed, attempting to install it again will have no effect. Upgrading existing modules must be requested **explicitly**:


```bash
python -m pip install -U SomePackage  
```

for example:
```
python -m pip install  -U coolprop 
```

### A.3 Install from an alternate index site

```bash
>python -m pip install SomePackage  -i  the-url-of-an-alternate-index
``` 

for example:

```bash
python -m pip install -i https://test.pypi.org/simple/ CoolProp==6.4.2.dev0
```

### A.4 uninstall  

```bash
python -m pip uninstall packagename  
```

### A.5 set one alternate index site as the default site

```bash
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

### A.6 Show help for commands

```bash
pip  help  
```

## B:Jupyter Notebook

Interactive analysis and literate programming

http://jupyter.org/

The Jupyter Notebook is an open-source **web application** that allows you to create and share **`documents`** that contain **`live code`**, equations, visualizations and narrative **`text`**. 

Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.

   ![jupyter-demo](./img/jupyter-demo.png)

### B.1 Start-up Jupyter Notebook

To start up Jupyter, run the following command in a terminal:

```shell 
jupyter notebook
```

This will launch a new browser window (or a new tab) showing the Notebook Dashboard, a sort of control panel that allows (among other things) to select which notebook to open.

When started, the Jupyter Notebook can access only files within `its start-up folder (including any sub-folder)`.


### B.2 Literate programming your Jupyter Notebook in the `specific working folder`

#### B.2.1 Start Jupyter Notebook in a specific folder with `batch` file 

* `1` make **the specific folder** for  your Jupyter Notebook,for example: `D:/mynotebook`

* `2` make the **"start.bat"** batch file with the content **`jupyter notebook`** through Windows's **notepad.exe**(记录本)  in the working folder of your Jupyter Notebook

* `3` Double-click **`start.bat`**，the **Jupyter Notebook**  server will automatically open up in your default web browser

  ![jupyter-quick](./img/jupyter-bat.jpg) 

#### B.2.2 Create a new notebook document

To create a new notebook, click the `New` button on the top of the right hand side and select the `“Python 3”` option. You should see something like the follow Figure. 

If this is your first time, try clicking on the empty `Code cell` and entering a line of Python code. Then press `Shift-Enter` to execute it.

Notebooks consist of a linear sequence of cells. There are two basic cell types:

* `Code cells`: Input and output of live `code` that is run in the kernel

* `Markdown cells`: Narrative `text` with embedded `LaTeX` equations

You can change the cell type by using the `Cell` menu or the toolbar.

You may click  `File`->`Save As...` to save the notebook file as a given name with the extension `.ipynb`.

   ![jupyter-hello](./img/jupyter-hello.jpg) 
  
### B.3 Using the Jupyter Notebook of thermalogic/SEES

pre-installed:Python3 and Jupyter Notebook

**B.3.1**  Download the zip file

Go to the repo **SEES** on the Github: https://github.com/thermalogic/SEES ,then download `SEES.zip` to your computer

   ![download SEES.zip](./img/downloadSEES.jpg)

**B.3.2** Open the notebooks in Jupyter Notebook

 unzip `SEES.zip`, double-click  `nb.bat`(OS:Windows)  in the sub-folder of **notebook** of `SEES`. This will open a web page in your browser with a list of the available notebooks.

## D:Visual Studio Code

Visual Studio Code is a lightweight but powerful source code editor which runs on your desktop and is available for Windows, macOS and Linux. 

### D.1 Getting Started with Python in VS Code

 https://code.visualstudio.com/docs/python/python-tutorial

It's simple to run Python source code file. `Right-click` in the editor and select `Run Python File in Terminal` (which saves the file automatically):
 
   ![vscode-python-0](./img/vscode-python-0.jpg)

   ![vscode-python-1](./img/vscode-python-1.jpg)

### D.2 Getting Started with C/C++ in VS Code

* **1** Open the PowerShell terminal in the folder of C++ code file

   ![vscode-open-terminal](./img/vscode-open-terminal.jpg)

   ![vscode-terminal](./img/vscode-terminal.jpg)

* **2** Using g++ to compile the C++ code to the executable file,then running the exe file in the terminal

   ![vscode-gcc](./img/vscode-gcc.jpg)

## E: Using Git with  thermalogic/SEES 

We **recommend** that you use [git](https://git-scm.com) to handle everything in the course: the repositories of thermalogic,your projects,etc. 

After you have installed **git**, You may use the following **commands:** to clean,update and checkout 

#### E.1 Clone the thermalogic/SEES to your computer

```bash
git clone https://github.com/thermalogic/SEES.git
```

#### E.2 Updating to The Latest Version

As we release new files or  update files, you'll have to update your repository. You can do this by changing into the `SEES` directory and executing:

```bash
git pull
```

That's it - you'll have the latest version of the repository.

#### E.3 Discard Changes

If you change the contents of SEES, you may  `checkout` to discard all changes

```bash
>git checkout .
```

>You may also use any **Git GUI client** to clone, update and checkout this repository
> * For example:  [Visual Studio Code](https://code.visualstudio.com/)

## References

* Python3:  https://www.python.org/downloads/
  
* Jupyter: http://jupyter.org/

* Visual Studio Code：https://code.visualstudio.com/

* Git https://git-scm.com


  