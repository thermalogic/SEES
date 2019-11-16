# Use the Microsoft C++ toolset from the command line

https://docs.microsoft.com/en-us/cpp/build/building-on-the-command-line?view=vs-2019

You can build C and C++ applications on the command line by using tools that are included in Visual Studio(https://visualstudio.microsoft.com/). The Microsoft C++ (MSVC) compiler toolset is also downloadable as a standalone package that doesn't include the Visual Studio IDE.

## Download and Install Microsoft C++ (MSVC) toolset

If you've installed Visual Studio and a C++ workload, you have all the command-line tools. For information on how to install C++ and Visual Studio, see [Install C++ support in Visual Studio](https://docs.microsoft.com/en-us/cpp/build/vscpp-step-0-installation?view=vs-2019). If you only want the command-line toolset, download the [Build Tools for Visual Studio]https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019). When you run the downloaded executable, it updates and runs the Visual Studio Installer. To install only the tools you need for C++ development, select the C++ build tools workload. You can select optional libraries and toolsets to include under Installation details.

## Set the Compiler,Lib and Include path

For MSVC, the path should look something like follow(Windows 10.0.18362.0, Microsoft Visual Studio Community 2019), depending on which specific version you have installed

### Set the Compiler path

Add the Compiler path to the system environment variable `Path`：
```
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.23.28105\bin\Hostx64\x64
```

### Set the Lib path

1. Add the system environment variable:`LIB`

2. Add three paths in the `LIB`：
```
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.23.28105\lib\x64

C:\Program Files (x86)\Windows Kits\10\Lib\10.0.14393.0\ucrt\x64; 

C:\Program Files (x86)\Windows Kits\10\Lib\10.0.18362.0\um\x64
```

### Set the Include path

1. Add the system environment variable:`INCLUDE`

2. Add three paths in the `INCLUDE`：

```
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.23.28105\include

C:\Program Files (x86)\Windows Kits\10\Include\10.0.18362.0\ucrt

C:\Program Files (x86)\Windows Kits\10\Include\10.0.18362.0\um
```