
# Windows版GSL和Gnuplot安装

安装适用于MinGW-W64编译器的Windows版GSL和Gnuplot

## 安装适用于MinGW-W64编译器的GSL

### 下载GSL

从 https://sourceforge.net/projects/mingw-w64/files/ 的 `Home/External binary packages(Win64 hosted)/Binaries (64-bit)`目录中,下载MinGW-W64编译好的GSL库压缩文件

下载后，解压压缩文件，可见库文件在 `gsl-1.16-mingw-w64-winpthread-seh\gsl-1.16` 目录中。由文件名可见，编译好的GSL库适用于win64-seh版编译器，GSL版本是1.16，较旧。

* 库可以用于非win64-seh版的64位MinGW-W64编译器

* GSL 1.16版软件库可满足工作需要

### 安装GSL

#### 1 拷贝静态文件

将 `gsl-1.16-mingw-w64-winpthread-seh\gsl-1.16\lib`中的动态库导入库

libgsl-1.16.dll.a和libgslcblas-1.16.dll.a

拷贝到MinGW-W64安装目录下的 `lib\gcc\x86_64-w64-mingw32\版本号` 子目录中。如MinGW-W64 8.1.0安装在`C:\mingw64\`，就是拷贝到`C:\mingw64\lib\gcc\x86_64-w64-mingw32\8.1.0`

然后，删除文件名中的版本号，即修改2个文件名为 libgsl.dll.a和libgslcblas.dll.a 

#### 2 拷贝动态库文件

将`gsl-1.16-mingw-w64-winpthread-seh\gsl-1.16\bin`中的

gsl-1.16.dll和gslcblas-1.16.dll拷贝到`C:\Windows\System`中，注意不要改文件名。

## 安装Gnuplot for Windows

 从 http://www.tatsuromatsuoka.com/gnuplot/Eng/winbin/ 下载MinGW-W64编译器适用的Gnuplot for windows，然后，解压运行安装程序。
 
 安装后，将gnuplot.exe所在目录加到系统环境变量path中，如`C:\Program Files (x86)\gnuplot\bin`


 