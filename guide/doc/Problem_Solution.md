
# Problem and Solution
<!-- TOC -->

- [Problem and Solution](#problem-and-solution)
  - [报没有错误语句的“SyntaxError"](#报没有错误语句的syntaxerror)
  - [pip安装时,提示Permission denied](#pip安装时提示permission-denied)
  - [print('{:>7.3f}'.format(h)输出运行错误](#print73fformath输出运行错误)
  - [VS Code中makefile报错分隔符](#vs-code中makefile报错分隔符)
  - [Windows下，MinGW-W64编译UTF-8编码的C++源码，生成的运行文件向终端输出中文乱码](#windows下mingw-w64编译utf-8编码的c源码生成的运行文件向终端输出中文乱码)
  - [Jupyter软件包安装中断后，再次安装中使用cache造成安装过程停滞](#jupyter软件包安装中断后再次安装中使用cache造成安装过程停滞)

<!-- /TOC -->

## 报没有错误语句的“SyntaxError"

![syntaxerror](./img/syntaxerror.jpg)

**很常见的情况**： 前一句错误，报下面没有错误语言的:`SyntaxError`

因为，Python解释器认为前面一句还没有结束，将前面语言和当前被报错语言作为一个`多行`语句解析，所以，报错在解释器认为的多行语句结束行处 。

>如上图的`（）`配对错误, 报下面的语句 ```Cycle['bwr']=...``` 错误。 Python语言`（）`中可以多行语言。

**改错：** 检查被报错误语句的前面语言，存在什么错误：使得解释器认为前面语言没有结束，是`多行`语句.  

## pip安装时,提示Permission denied

pip安装时,提示Permission denied

![Permision denied](./img/pipuser.jpg)

根据pip给出的提示加上--user

    >python -m pip install --user  <packagename>

## print('{:>7.3f}'.format(h)输出运行错误

`print(str.format)`,输出时，会根据str给出的格式，将变量先转换为对应数据类型，再按照格式要求输出

如：`print('{:>6.3f}'.format(h)`，即： `float(h) -> print`, 如果变量不能转换为对应类型，就会输出运行错误.

**修改**

 数据类型转换异常时，不使用str.format方式输出

```python
try:
    print('{:>7.3f}'.format(h))
except:
    print(h)
```

## VS Code中makefile报错分隔符

VS Code中makefile报错分隔符
```
*** missing separator.  Stop.
```

原因：vscode默认tab键是4个空格，导致make的时候没法识别

解决方法： setting选项里,

1. 搜索`renderControlCharacters`，`勾`选选项

2. 然后`renderWhitespace`，选成`all`

或者：

click the `Space: 4` on the downright corner and change it to `tab` when editing your Makefile.

## Windows下，MinGW-W64编译UTF-8编码的C++源码，生成的运行文件向终端输出中文乱码

VS Code是跨平台软件，所有的纯文本类型文件的默认字符集编码都是UTF-8,但是Windows终端的默认字符集编码GBK。两者的默认字符集编码不同，C/C++程序输出UTF-8编码字符不能被GBK编码正确解析，就显示乱码.

使用gcc编译选项，编译生成输出字符的中文编码为GBK的运行文件

```
g++ -o hello hello.cpp -fexec-charset=GBK
```

## Jupyter软件包安装中断后，再次安装中使用cache造成安装过程停滞

使用 --no-cache-dir 选项安装

```bash
python -m pip --no-cache-dir install jupyter
```   

