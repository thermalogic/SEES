# C/C++ Programming with GCC (for Windows)

## 1. GCC: GNU Compiler Collection

### 1.1 A Brief History and Introduction to GCC

* The original GNU C Compiler (GCC) is developed by Richard Stallman, the founder of the GNU Project. Richard Stallman founded the GNU project in 1984 to create a complete Unix-like operating system as free software, to promote freedom and cooperation among computer users and programmers.

  GCC, formerly for "GNU C Compiler", has grown over times to support many languages such as C++, Objective-C, Java, Fortran and Ada. It is now referred to as "GNU Compiler Collection". 
  The mother site for GCC is **http://gcc.gnu.org/**.

  GCC is a key component of "GNU Toolchain", for developing applications, as well as operating systems. 

  GCC is portable and run in many operating platforms. GCC (and GNU Toolchain) is currently available on all Unixes. They are also ported to Windows by MinGW and Cygwin. GCC is also a cross-compiler, for producing executables on different platform.

### 1.2  Installing MinGW GCC

GCC (GNU Toolchain) is included in all Unixes. For Windows, you could either install **MinGW GCC** or **Cygwin GCC**.

* MinGW-w64 GCC

  MinGW (short for "Minimalist GNU for Windows"), is a minimalist (i.e., small but fewer features compared with cygwin) development environment for native Microsoft Windows applications, in particular:
   * 1.A port of the GNU Compiler Collection (GCC), including C, C++, ADA and Fortran compilers;
   * 2.GNU Binutils for Windows (assembler, linker, archive manager).
   * 3.MSYS (short for "Minimal SYStem"), is a bash Shell command line interpreter.

* To install MinGW-w64: http://mingw-w64.org/ 
  
  * 1.Goto https://sourceforge.net/projects/mingw-w64/files/?source=navbar 
  
      Downloads x86_64-6.3.0-release-win32-sjlj or seh 
      
       * sjlj: 32 and 64,but it incurs a minor performance penalty  
        
       * seh：64 only

      ![MinGW-w64](./img/mingw-w64.jpg) 
    
  * 2.unzip the ziped MinGW-w64 to C:\mingw64

  * 3.Setup **C:\mingw6\bin** to PATH  
      ```bash
      >set PATH=C:\mingw64\bin;%PATH%
      >echo %PATH%
      ```

   * 4.Verify the GCC installation by listing the version of gcc, g++ and gdb: 
      ```bash
      > gcc --version
      > g++ --version
      > gdb --version
      ```

### 1.3  Getting Started

The GNU C and C++ compiler are gcc and g++, respectively.

**Compile/Link a Simple C Program - hello.c**

Below is the Hello-world C program hello.c:
```c
 // hello.c
#include <stdio.h>
 
int main() {
    printf("Hello, world!\n");
    return 0;
}

```
To compile the hello.c:
```bash
> gcc -o hello.exe hello.c
```
The output executable is called "hello.exe".

To run the program:
```bash
>hello
```

**Compile/Link a Simple C++ Program - hello.cpp**

Below is the Hello-world C++ program hello.cpp:
```c
// hello.cpp
#include <iostream>
using namespace std;
 
int main() {
   cout << "Hello, world!" << endl;
   return 0;
}
```
You need to use g++ to compile C++ program, as follows. We use the -o option to specify the output file name.
```bash
 >g++ -o hello.exe hello.cpp
```
To run the program:
```bash
>hello
```

## 2.  GNU Make

The "make" utility automates the mundane aspects of building executable from source code. "make" uses a so-called makefile, which contains rules on how to build the executables.

You can issue "make --help" to list the command-line options; or "man make" to display the man pages.

**First Makefile By Example**

Let's begin with a simple example to build the Hello-world program (hello.c) into executable (hello.exe) via make utility.
```c
 // hello.c
#include <stdio.h>
 
int main() {
    printf("Hello, world!\n");
    return 0;
}

```
Create the following file named **"makefile"** (without any file extension), which contains rules to build the executable, 
and save in the same directory as the source file. Use **"tab"** to indent the command (NOT spaces).

A makefile consists of a set of rules. A rule consists of 3 parts:**a target**, **a list of pre-requisites** and **a command**, as follows:

 ```bash

target: pre-req-1 pre-req-2 ...
	  command

 ```
The target and pre-requisites are separated by **a colon (:)**. The command must be preceded by **a tab** (NOT spaces).


```bash
all: hello.exe

hello.exe: hello.o
	 gcc -o hello.exe hello.o

hello.o: hello.c
	 gcc -c hello.c
     
clean:
	 rm hello.o hello.exe

```
Run the "make" utility without argument starts the target "all" in the makefile:
 
 * rename `C:\mingw64\bin\mingw32-make.exe` to `C:\mingw64\bin\make.exe`

```bash
> make
```

## 3. Development Environment for Windows

### 3.1 Visual Studio Code for C/C++ Programming

A program editor (or source code editor) is programming language sensitive and context-aware. 
It highlights the syntax elements of your programs; and provides many features that aid in your program development (such as auto-complete, compile/build/run, help menu, etc.). 

It is important to use a mono-space font (such as "Courier New", "Consola") for programming, so that the columns are properly aligned.

Visual Studio Code https://code.visualstudio.com/  is a lightweight but powerful source code editor which runs on your desktop and is available for Windows, Mac and Linux. It comes with built-in support for JavaScript, TypeScript and Node.js and has a rich ecosystem of extensions for other languages (such as C++, C#, Python, PHP, Go) and runtimes.

**C/C++ for VS Code** : https://code.visualstudio.com/docs/languages/cpp

For full-scale software development, you should use an appropriate IDE (Integrated Development Environment).

###  3.2 Eclipse for C/C++ Programming

Eclipse is an open-source Integrated Development Environment (IDE) supported by IBM. The mother site is http://www.eclipse.org.

Eclipse is popular for Java project development. It also supports C/C++, PHP, Python, Perl, and other web project developments via extensible plug-ins. Eclipse is cross-platform and runs under Windows, Linux and Mac OS.

## Reference

* MinGW-W64 (GCC) Compiler Suite: https://sourceforge.net/projects/mingw-w64/files/

* GCC for Windows 64 & 32 bits：http://mingw-w64.org/

* GCC (GNU compilers) http://gcc.gnu.org

* GCC Manual  http://gcc.gnu.org/onlinedocs

* An Introduction to GCC  http://www.network-theory.co.uk/docs/gccintro/index.html.

* GCC and Make：Compiling, Linking and Building C/C++ Applications http://www3.ntu.edu.sg/home/ehchua/programming/cpp/gcc_make.html

* Eclipse 4.3 (Kepler) for C/C++ Programming http://www3.ntu.edu.sg/home/ehchua/programming/howto/EclipseCpp_HowTo.html

* Eclipse's "C/C++ Development Tool User Guide", accessible via Eclipse's Help menu

* Simple Unit Testing for C：https://github.com/ThrowTheSwitch/Unity

* How to C https://matt.sh/howto-c

