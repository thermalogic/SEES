
# 计算机终端和程序设计过程

## 1 计算机终端 Computer Terminal

https://en.wikipedia.org/wiki/Computer_terminal

A computer **terminal** is an electronic or electromechanical **hardware device** that is used for **entering data into, and displaying or printing data** from, a computer or a computing system. The teletype was an example of an early day hardcopy terminal, and predated the use of a computer screen by decades.

The terminal of the first working programmable, fully automatic digital Turing-complete computer, the Z3, had a keyboard and a row of lamps to show results

![terminal](./codingterminal/ASR-33_1.jpg)

A personal computer can run **terminal emulator software** that replicates the **function of a terminal**, sometimes allowing concurrent use of local programs and access to a distant terminal host system.

When using a **graphical user interface** (or GUI) like the X Window System, one's display is typically occupied by a collection of windows associated with various applications, rather than a single stream of text associated with a single process. In this case, one may use a **terminal emulator** application within the windowing environment. This arrangement permits **terminal-like interaction** with the computer (for running **a command line interpreter**, for example) without the need for a physical terminal device; it can even allow the running of multiple terminal emulators on the same device.

![terminalemulator](./codingterminal/terminal-emulator.jpg)

## 2 Windows Command-Line "CMD" or "PowerShell" Shell

http://www3.ntu.edu.sg/home/ehchua/programming/howto/CMD_Survival.html

Programmers use a command-line interface (CLI) to issue text-commands to the Operating System, instead of clicking or double-clicking on a Graphical User Interface (GUI). This is because command-line is much more powerful than the graphical interface.

The CMD/Powershell is a command-line Interface. It supports a set of commands and utilities; and has its own programming language for writing batch files (or shell scripts).

You can launch a CMD/Powershell via:
```
"Win+R" ⇒ Enter "cmd/powershell"
```
The terminal shell displays a prompt which ends with a ">", in the form of "drive:\current-directory>". You can enter your command after the prompt.


## 3 程序源码编辑和运行

编写源码 -> 编译、链接/解释器 -> 运行

其中：

* 程序设计语言源码可以使用任意`纯文本`编辑软件编写

* 运行一个程序设计语言源码的过程：使用编程语言的编译/解释器命令，对源码进行处理：

   * 编译型语言：用该语言的编译器将源码编译、链接为可运行文件，然后，运行该运行文件

   * 解释型语言： 该语言的解释器对源码边解释，边运行

## 4 集成开发环境

集成开发环境（IDE)对`编写源码 -> 编译、链接/解释器 -> 运行`过程进行了集成，以提高程序开发效率。

 * 编码：提供语言的语法高亮、提示，补全等功能

 * 对**源码->运行**的命名过程用封装为图形用户界面。用户点击鼠标，软件帮用户完成命名行的编译/解释、运行工作。

## 5 终端中使用命令`编译/解释源码->运行`过程示例

### Windows终端中示例

Open a Terminal in the folder in Windows10

* If you're already in the folder you want, you do `Shift+[mouse right-click]` on the background of the Explorer window, then click on `"Open command window here"` or `"Open PowerShell window here"`

![Window操作系统终端中，命令行运行过程示例](./codingterminal/demo-windows-shell.jpg)

### Visual Studio Code终端中示例

![Visual Studio Code **终端** 中，命令行运行过程示例](./codingterminal/demo-vscode-terminal.jpg)

