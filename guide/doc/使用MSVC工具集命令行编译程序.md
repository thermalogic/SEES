#  使用MSVC工具集(CL,LINK,NMAKE)命令行编译程序

MSVC工具集: CL,LINK,NMAKE

 * Use the Microsoft C++ toolset from the command line

https://docs.microsoft.com/en-us/cpp/build/building-on-the-command-line?view=vs-2019

You can build C and C++ applications on the command line by using tools that are included in Visual Studio(https://visualstudio.microsoft.com/). The Microsoft C++ (MSVC) compiler toolset is also downloadable as a standalone package that doesn't include the Visual Studio IDE.

## Install Microsoft C++ (MSVC) toolset and Setup Environment

### Download and Install Microsoft C++ (MSVC) toolset

If you've installed Visual Studio and a C++ workload, you have all the command-line tools. For information on how to install C++ and Visual Studio, see [Install C++ support in Visual Studio](https://docs.microsoft.com/en-us/cpp/build/vscpp-step-0-installation?view=vs-2019). If you only want the command-line toolset, download the [Build Tools for Visual Studio](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019). When you run the downloaded executable, it updates and runs the Visual Studio Installer. To install only the tools you need for C++ development, select the C++ build tools workload. You can select optional libraries and toolsets to include under Installation details.

### Set the Compiler,Lib and Include path

For MSVC, the path should look something like follow(Windows 10.0.18362.0, Microsoft Visual Studio Community 2019), depending on which specific version you have installed

#### Set the Compiler path

Add the Compiler path to the system environment variable `Path`：
```
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.23.28105\bin\Hostx64\x64
```

#### Set the Lib path

1. Add the system environment variable:`LIB`

2. Add three paths in the `LIB`：
```
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.24.28314\lib\x64
C:\Program Files (x86)\Windows Kits\10\Lib\10.0.18362.0\ucrt\x64; 
C:\Program Files (x86)\Windows Kits\10\Lib\10.0.18362.0\um\x64
```

#### Set the Include path

1. Add the system environment variable:`INCLUDE`

2. Add three paths in the `INCLUDE`：

```
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.24.28314\include

C:\Program Files (x86)\Windows Kits\10\Include\10.0.18362.0\ucrt

C:\Program Files (x86)\Windows Kits\10\Include\10.0.18362.0\um
```

## MSVC工具集参数

### CL

https://docs.microsoft.com/en-us/cpp/build/reference/compiling-a-c-cpp-program?view=vs-2019

Use the compiler (cl.exe) to compile and link source code files into apps, libraries, and DLLs.

### Link

https://docs.microsoft.com/en-us/cpp/build/reference/linking?view=vs-2019

Use the linker (link.exe) to link compiled object files and libraries into apps and DLLs.

### NMAKE

https://docs.microsoft.com/en-us/cpp/build/reference/nmake-reference?view=vs-2019

Use NMAKE (nmake.exe) on Windows to build C++ projects based on a traditional makefile.

### 按类别列出的编译器选项

* 中文 https://docs.microsoft.com/zh-cn/cpp/build/reference/compiler-options-listed-by-category?view=vs-2019

* 英文 Compiler options listed by category  https://docs.microsoft.com/en/cpp/build/reference/compiler-options-listed-by-category?view=vs-2019

### 链接器选项

* 中文：https://docs.microsoft.com/zh-cn/cpp/build/reference/linker-options?view=vs-2019

* 英文 Linker options ：https://docs.microsoft.com/en-us/cpp/build/reference/linker-options?view=vs-2019

## 用cl、link工具编译生成 dll 与 lib

### 代码：

 dllTest.c

```c

__declspec(dllexport) int GetNumber(); 


int GetNumber()

{

	return 20;

}
```

### 方案一

#### 在命令行中使用 cl.exe 编译成 dllTest.obj 文件

```
>cl -c dllTest.c
```

#### 在命令行中使用 link.exe 创建 dllTest.lib 与 dllTest.dll 文件

```
>link -dll dllTest.obj
```

查看文件夹，可见生成了3个文件：

* dllTest.dll //动态库

* dllTest.lib //静态库

* dllTest.exp //导出库文件，包含导出函数与导出数

### 方案二：
···
cl /LDd dllTest.c
···

## 使用库

### 代码

```c
#include <stdio.h>
#include <stdlib.h>

_declspec(dllimport) int GetNumber();

int main()
{

	printf("%d", GetNumber());
	return 0;
}
```

### 编译链接库

···
>cl demo.c dllTest.lib 
···


## 使用nmake

### 生成dll的makefile

makefiledll.mk

```makefile
all : dllTest

dllTest : dllobj
	link  /DLL /OUT:dllTest.dll dllTest.obj  

dllobj: demo.c
	cl /c /FodllTest.obj dllTest.c
```

使用nmake编译

```
>nmake -f makefiledll.mk
```

### 使用dll的makefile

makefiledemo.mk

```makefile
all : demoexe
	demo.exe

demoexe : demoobj
	link  /OUT:demo.exe demo.obj  dllTest.lib
	del *.obj

demoobj: demo.c
	cl /c /Fodemo.obj demo.c 
```	

使用nmake编译运行

```
>nmake -f makefiledemo.mk
```



