# The Software for Programming C/C++ and  Python on Linux

## 1 C/C++

Most Linux distributions, such as Ubuntu, have built-in GCC compilers and do not require additional installation

If you use the Debian/Ubuntu distribution do not has built-in GCC compilers. you can install the folloing command
 
```bash 
$sudo apt install build-essential
```
The command installs a bunch of new packages including gcc, g++ and make.

## 2 Python

All Linux distributions have built-in Python2 and Python3. However, it is incomplete

For Python3, we need to be supplemented with `pip3` and `idle3`.

```bash
$sudo apt install python3-pip
$sudo apt install idle3
```

>  Add 3 to the relevant commands of Python3

**Install Python3 packages:**

* set `tsinghua` as the mirror site of Pypi

```bash
$sudo -H python3 -m pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

* upgrade pip3

```bash
$sudo -H python3 -m  pip install pip -U
```
* Installing Packages

```bash
$sudo -H python3 -m pip install jupyter 
```

```bash
$sudo -H  python3 -m pip install coolprop 
```

## 3 The text editor and programming environment

**Visual Studio Code**

From  https://code.visualstudio.com/docs/?dv=linux64_deb  download VS Code for Debian/Ubuntu,

then install in the terminal

```bash
$sudo dpkg -i [vscode filename].deb
```

## 4 Version Control:Git

```bash 
$sudo apt install git
```
