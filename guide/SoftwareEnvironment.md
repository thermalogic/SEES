# Software Environment 

## A  Windows10

  64-bit Windows10 

* 1 Southeast University

  * January 2015, Southeast University and Microsoft Corp provide legitimate Windows, Office for the staffs and students.

  http://nic.seu.edu.cn/2015/0113/c12333a115289/page.htm
  
* 2 Microsoft
  
   * https://www.microsoft.com/en-gb/software-download/windows10
     * Do you want to install Windows 10 on your PC?
       
       download and run the media creation tool: 
       https://go.microsoft.com/fwlink/?LinkId=691209
 
## B Development tools and packages

* 1 Python3:  https://www.python.org/downloads/

* 2 Python Packages

  * 2.1 Jupyter: http://jupyter.org/

  * 2.2 Numpy、Scipy and Matplotlib http://www.scipy.org/ 

  * 2.3 IAPWS-IF97:

     * Shared Lib: https://github.com/PySEE/SEUIF97

     * Python: https://github.com/jjgomera/iapws
 
* 3 Visual Studio Code：https://code.visualstudio.com/

* 4 Git for Windows:  https://github.com/git-for-windows/git/releases

* 5 MinGW-W64(GCC) Compiler Suite: https://sourceforge.net/projects/mingw-w64/files/

## C Set up your development environment

### 1 Install Python
    
Goto the official Python site  https://www.python.org/downloads/ to download the suitable version Python，e.g.**Python for Windows** ：https://www.python.org/downloads/windows/

Python 3.7.0 for Windows x86-64 executable installer 

https://www.python.org/ftp/python/3.7.0/python-3.7.0-amd64.exe

####  Customize Installation

* 1  Make sure you **check** option **Add Python 3.7 to PATH**

* 2  To change install location, click on **Customize installation** , then **Next** and enter **C:\python37** the item of  **Customize installation location**

![Python3-path](./img/python37-path.jpg)

![Python3-location](./img/python37-location.jpg)
   
* update pip to the most recent version

From a command prompt:
```bash
  >python -m pip install -U pip -i  https://pypi.tuna.tsinghua.edu.cn/simple/
```

### 2 Install Jupyter Notebook

* From a command prompt, install using pip：

Install from the mirror site　@ tsinghua

```bash  
>python -m pip install jupyter -i  https://pypi.tuna.tsinghua.edu.cn/simple/
```  
* From a command prompt,start **Jupyter notebook**

```bash       
>jupyter notebook     
```

* Setup the  working dir for your **Jupyter Notebook**：

  * `1` the dir of start `>jupyter notebook` is the default dir of your Jupyter Notebook 

* start **Jupyter Notebook** quickly 

  * `2` make the **"start.bat"** batchfile with the content **`jupyter notebook`** through Windows's **notepad.exe**(记录本)  in the working dir of your Jupyter Notebook

  * `3` Double-click **"start.bat"**，Start **Jupyter Notebook** 

 ![jupyter-quick](./img/jupyter-bat.jpg)

### 3 Scientific Computation Packages
   
   Numpy,Scipy, Matplotlib https://www.scipy.org/install.html 

```bash       
> python -m pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple/
> python -m pip install scipy -i  https://pypi.tuna.tsinghua.edu.cn/simple/
> python -m pip install matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple/
``` 

or 

```bash       
> python -m pip install numpy scipy matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple/
``` 
### 4 IAPWS-IF97 Packages

* 4.1 Python IAPWS-IF97

   pre-installed:numpy and scipy

```bash       
   > python -m pip install iapws https://pypi.tuna.tsinghua.edu.cn/simple/
``` 

* 4.2 Shared Lib IAPWS-IF97

```bash       
> python -m pip install seuif97 https://pypi.tuna.tsinghua.edu.cn/simple/
``` 

or

Go to the repo on the Github：https://github.com/PySEE/SEUIF97 , download SEUIF97.zip

![Download SEUIF97.zip](./img/downloadseuif97.jpg)
   
*  Unzip the downloaded file,then：
   
   * 1 copy **libseuif97.dll** to c:\windows\system
   * 2 copy **seuif97.py** to the **Lib** dir of installed Python. If you have install Python3.7 in the C:\Python37\, copt to `C:\python37\Lib`
 

**NOTE: Install Packages** 

* `1` Binary packages are also available from third parties, such as the Python distributions above. For Windows, Christoph Gohlke provides [Unofficial Windows Binaries for Python Extension Packages](https://www.lfd.uci.edu/~gohlke/pythonlibs/).

```bash 
>pip install *.whl
```

* `2` Requirements file [requirements.txt](./requirements.txt) is the file containing a list of items to be installed for the course:

```bash 
>python -m pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 5 Visual Studio Code

Visual Studio Code is a lightweight but powerful source code editor which runs on your desktop and is available for Windows, macOS and Linux. It comes with built-in support for JavaScript, TypeScript and Node.js and has a rich ecosystem of extensions for other languages (such as C++, C#, Python, PHP, Go) and runtimes (such as .NET and Unity). 

* 1 Download and Install Visual Studio Code 
 
    https://code.visualstudio.com/

* 2 Install Python Extension

    https://code.visualstudio.com/docs/languages/python

* 3 Install the Microsoft C/C++ extension

    https://code.visualstudio.com/docs/languages/cpp

* 4 Install Visual Studio Code Tools for AI extension

    https://github.com/Microsoft/vscode-tools-for-ai/blob/master/docs/installation.md
 
  * Open Jupyter notebooks in VS Code

    https://github.com/Microsoft/vscode-tools-for-ai/blob/master/docs/quickstart-06-jupyter.md
  
     * Set Python path properly in VS Code，for example: C:/python37/python.exe

     * Open Jupyter notebooks in VS Code
  
       Launch Visual Studio Code and select File > Open Folder (Ctrl+K Ctrl+O)
       Select a folder which contains the Jupyter notebook file (.pynb) you want to open.

       Select command in context menu
       Right click the Jupyter notebook file node and select "AI: View in Jupyter Server" command.

### 6  Version control with Git

* Git for Windows:  https://git-scm.com/download/win

### 7 MinGW-W64 (GCC) Compiler Suite

* 1 Goto MinGW mother site at：https://sourceforge.net/projects/mingw-w64/files/?source=navbar

    * sjlj: 32 and 64 bits,but it incurs a minor performance penalty
     
    * seh：64 bits only
  
  Download： **GCC 8.1.0 x86_64-win32-sjlj**
  
  ![mingw-w64](./img/mingw-w64.jpg)

* 2 unzip the ziped MinGW-w64 to **C:\mingw64**

* 3 Add **C:\mingw64\bin** to the system environment variable **Path**

    For Windows 10: 

    start  "Windows Start Menu" ⇒ "Settings" ⇒ "About"(at the bottom) ⇒ "System Info"(scroll down)  ⇒ Switch to "Advanced System Settings"  ⇒  "Environment Variables"  ⇒  Choose "System Variables" (for all users) ⇒ Choose the System Variable "**Path**" ⇒ Choose "New" (add a new dir to  **Path** variable) > Enter the value: **C:\mingw64\bin**.

![mingw-w64-path](./img/mingw-w64-path.jpg)

* 4 Verify the GCC installation by listing the version of gcc, g++ and gdb:
  ```bash
  > gcc --version
  > g++ --version
  > gdb --version
  ``` 

## D Using Courseware

  pre-installed:Python and Jupyter Notebook
 
* Go to the repo **home** on the Github: https://github.com/PySEE/home download home.zip

![download home.zip](./img/downloadhome.jpg)

* Start Jupyter Notebook of the course
 
  unzip home.zip, double-click  **StartNB.bat**  under the dir **notebook** to run start **Jupyter Notebook** server

## References

* Guido van Rossum. Python Tutorial. https://docs.python.org/3/tutorial/index.html

* Jupyter：http://jupyter.org/

    * Documentation. http://jupyter.readthedocs.org/en/latest/

* Scipy. http://www.scipy.org/

* Numpy. http://www.numpy.org/
  
* Matplotlib.  http://matplotlib.org/

* Visual Studio Code: https://code.visualstudio.com/
  
   * Documentation: https://code.visualstudio.com/docs

   * **Markdown** and VS Code： https://code.visualstudio.com/docs/languages/markdown

   * Getting Started with **Python** https://code.visualstudio.com/docs/python/python-tutorial

   * **C/C++** for VS Code： https://code.visualstudio.com/docs/languages/cpp

   * **Git** Version Control in VS Code：https://code.visualstudio.com/docs/editor/versioncontrol

* GCC, the GNU Compiler Collection：http://gcc.gnu.org/

   * GCC for Windows 64 & 32 bits：http://mingw-w64.org/

   * GCC and Make：Compiling, Linking and Building C/C++ Applications http://www3.ntu.edu.sg/home/ehchua/programming/cpp/gcc_make.html