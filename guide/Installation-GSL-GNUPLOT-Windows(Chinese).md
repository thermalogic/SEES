
# Windows版GSL和Gnuplot安装

安装适用于MinGW-W64编译器的Windows版GSL和Gnuplot

## 安装适用于MinGW-W64编译器的GSL

从 https://github.com/PySEE/GSL4Windows 下载MinGW-W64编译的64位Windows版GSL 2.5库zip文件。

解压zip文件，然后，如下拷贝文件：

### 1 拷贝静态库和动态库导入库到lib目录

将 `GSL4Windows\lib`中的静态库和动态库导入库（import library）

* libgsl.a libgsl.dll.a 

* libgslcblas.a libgslcblas.dll.a

拷贝到MinGW-W64编译器的 `lib\gcc\x86_64-w64-mingw32\版本号` 子目录中。如MinGW-W64 8.1.0安装在`C:\mingw64\`，就是拷贝到`C:\mingw64\lib\gcc\x86_64-w64-mingw32\8.1.0`

### 2 拷贝动态库到系统默认路径

将`GSL4Windows\bin`中的

* libgsl-23.dll

* libgslcblas-0.dll

拷贝到`C:\Windows\System`中。

### 3 拷贝头文件到MinGW-W64编译器默认include目录

将`GSL4Windows\include`中的所有文件拷贝到`C:\mingw64\x86_64-w64-mingw32\include\gsl`

## 安装Gnuplot for Windows

 从 http://www.tatsuromatsuoka.com/gnuplot/Eng/winbin/ 下载MinGW-W64编译的Gnuplot for windows，然后，解压运行安装程序。
 
 安装后，将gnuplot.exe所在目录加到系统环境变量path中，如: `"C:\Program Files\gnuplot\bin\"`


 