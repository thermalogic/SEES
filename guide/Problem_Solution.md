
# Problem and Solution
<!-- TOC -->

- [Problem and Solution](#problem-and-solution)
    - [报没有错误语句的“SyntaxError"](#报没有错误语句的syntaxerror)
    - [pip安装时,提示Permission denied](#pip安装时提示permission-denied)
    - [Windows下，MinGW-W64编译UTF-8编码的C++源码，生成的运行文件向终端输出中文乱码](#windows下mingw-w64编译utf-8编码的c源码生成的运行文件向终端输出中文乱码)
    - [Mar 1, 2019后安装的Jupyter运行异常](#mar-1-2019后安装的jupyter运行异常)
        - [Mar 1, 2019后安装的Jupyter连接Python3内核时异常](#mar-1-2019后安装的jupyter连接python3内核时异常)
        - [Mar 10, 2019后安装的Jupyter运行自动打开浏览器时异常](#mar-10-2019后安装的jupyter运行自动打开浏览器时异常)
    - [Jupyter软件包安装中断后，再次安装中使用cache造成安装过程停滞](#jupyter软件包安装中断后再次安装中使用cache造成安装过程停滞)
    - [命令行执行>jupyter notebook后，jupyter总是启动到C:\Windows\system32](#命令行执行jupyter-notebook后jupyter总是启动到c\windows\system32)
    - [Windows安全防护](#windows安全防护)
    - [module ‘unittest’hasn't the attribute of ‘TestCase’](#module-unittesthasnt-the-attribute-of-testcase)
    - [Windows环境下Jupyter notebook文件转换pdf失败](#windows环境下jupyter-notebook文件转换pdf失败)

<!-- /TOC -->

## 报没有错误语句的“SyntaxError"

![syntaxerror](./img/syntaxerror.jpg)

Python是解释性语言，前一句错误，会报下面没有错误语言的:`SyntaxError`。 **很常见的情况**。


## pip安装时,提示Permission denied

pip安装时,提示Permission denied

![Permision denied](./img/pipuser.jpg)

根据pip给出的提示加上--user

    >python -m pip install --user  <packagename>

## Windows下，MinGW-W64编译UTF-8编码的C++源码，生成的运行文件向终端输出中文乱码

VS Code是跨平台软件，所有的纯文本类型文件的默认字符集编码都是UTF-8,但是Windows终端的默认字符集编码GBK。两者的默认字符集编码不同，C/C++程序输出UTF-8编码字符不能被GBK编码正确解析，就显示乱码.

UTF-8是Linux默认编码方式，也是很多编程软件默认的编码方式。

趋势是UTF-8会成为各种操作系统(包括Windows)和软件的默认字符集编码方式。

* Windows10已经提供了Beta版的配置UTF-8为默认字符集编码的功能

因此，宜保持VS Code中程序源码文件的字符集编码为UTF-8，选择采用以下推荐方案之一，输出中文到Windows终端。

* 1 修改Windows终端的字符集编码为UTF-8。在终端执行

      >chcp 65001

* 2 使用gcc编译选项，编译生成输出字符的中文编码为GBK的运行文件

      >g++ -o hello hello.cpp -fexec-charset=GBK

## Mar 1, 2019后安装的Jupyter运行异常

2019.3月以来Jupyter软件包，因为Tornado版本升级带来的Bug比较多。

安装后需要对Jupyte依赖的软件包Tornado,Notebook做降低版本处理

### Mar 1, 2019后安装的Jupyter连接Python3内核时异常

https://github.com/jupyter/notebook/issues/2664

Tornado had a release `6.0.0` on **Mar 1 2019**, which triggered this problem recently

The previous tornado release was `5.1.1`, then,downgrading tornado 6 to 5.1.1 

    >python -m pip uninstall tornado
   
    >python -m pip install tornado==5.1.1

### Mar 10, 2019后安装的Jupyter运行自动打开浏览器时异常

https://github.com/jupyter/notebook/issues/4467

    >python -m pip uninstall notebook
   
    >python -m pip install notebook==5.7.2

>github issue: github仓库的问题提出，讨论等

## Jupyter软件包安装中断后，再次安装中使用cache造成安装过程停滞

使用 --no-cache-dir 选项安装

```bash
   python -m pip --no-cache-dir install jupyter
```   

##  命令行执行>jupyter notebook后，jupyter总是启动到C:\Windows\system32

原因：使用管理员权限运行cmd,都启动到C:\Windows\system32

解决方法：使用普通用户权限运行jupyter notebook

## Windows安全防护

微软提供的security essentials是Windows最好的安全防护软件
  
从下面网址下载和操作系统对应的版本的security essentials（**Windows 10默认已经安装**），安装

http://windows.microsoft.com/zh-cn/windows/security-essentials-download
      
安装security essentials后，卸载所有其他各种"安全”软件。
   
## module ‘unittest’hasn't the attribute of ‘TestCase’

03014311 骆应东

我在一开始写单元测试的程序时将其写在一个命名为unittest的程序文件里，这个时候运行程序会出现错误 module ‘unittest’hasn't the attribute of ‘TestCase’提示

通过请教老师、同学，最后发现是因为文件命名为unittest，然后当运行程序import unittest时系统会‘迷路’，因为文件名和Python的自带包unittest发生混淆，系统无法正确引用Python的unittest包。所以解决办法是：将文件名修改为非unittest即可。

##  Windows环境下Jupyter notebook文件转换pdf失败

Jupyter notebook中可以ipynb转换为pdf

* 1 Windows环境下需要安装MikTex

* 2 安装pandoc

```bash
>pip install pandoc
```

* 3 ipynb转换为pdf

```bash
>jupyter nbconvert  --to pdf  需要转换的ipynb文件名
```

转换程序从MiKTex的远程仓库下载包时，可能会出现下载失败的问题，导致文档转换中断

* 4 解决方法：

多试验几次

```bash   
>jupyter nbconvert  --to pdf  需要转换的ipynb文件名
```

从源下载包.

