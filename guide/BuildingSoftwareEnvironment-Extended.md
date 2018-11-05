# The Guide of Building Software Environment - Extended 

## A  Windows10

  64-bit Windows10 

**1 Southeast University**

January 2015, Southeast University and Microsoft Corp provide legitimate Windows, Office for the staffs and students.

  http://nic.seu.edu.cn/2015/0113/c12333a115289/page.htm
  
**2 Microsoft**
  
https://www.microsoft.com/en-gb/software-download/windows10

Do you want to install Windows 10 on your PC?
       
* download and run the media creation tool: 
       https://go.microsoft.com/fwlink/?LinkId=691209
 
## B SEUIF97 Shared Library

Go to the repo on the Github：https://github.com/PySEE/SEUIF97 , download SEUIF97.zip

![Download SEUIF97.zip](./img/downloadseuif97.jpg)
   
*  Unzip the downloaded file,then：
   
   * 1 copy **libseuif97.dll** to c:\windows\system
   * 2 copy **seuif97.py** to the **Lib** dir of installed Python. If you have install Python3.7 in the C:\Python37\, copt to `C:\python37\Lib`

## C Install Python Packages-Extended

* `1` Binary packages are also available from third parties, such as the Python distributions above. For Windows, Christoph Gohlke provides [Unofficial Windows Binaries for Python Extension Packages](https://www.lfd.uci.edu/~gohlke/pythonlibs/).

```bash 
>pip install *.whl
```

* `2` Requirements file [requirements.txt](./requirements.txt) is the file containing a list of items to be installed for the course:

```bash 
>python -m pip install -r requirements.txt 
```

## D Visual Studio Code and  Jupyter notebooks

* Install Visual Studio Code Tools for AI extension

https://github.com/Microsoft/vscode-tools-for-ai/blob/master/docs/installation.md

* Open Jupyter notebooks in VS Code
https://github.com/Microsoft/vscode-tools-for-ai/blob/master/docs/quickstart-06-jupyter.md

   * Set Python path properly in VS Code，for example: C:/python37/python.exe


   * Open Jupyter notebooks in VS Code

     Launch Visual Studio Code and select File > Open Folder (Ctrl+K Ctrl+O) Select a folder which contains the Jupyter notebook file (.pynb) you want to open.
    Select command in context menu Right click the Jupyter notebook file node and select "AI: View in Jupyter Server" command.