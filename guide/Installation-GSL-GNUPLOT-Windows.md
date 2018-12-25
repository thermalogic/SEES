
# The Guide to install GSL and Gnuplot for Windows

Install GSL and Gnuplot for Windows compiled with MinGW-W64

## GSL for Windows

Goto https://github.com/PySEE/GSL4Windows download the zip file,then unzip it，copy the files as the following steps：

### 1 Copy Static and import libraries to the default path of MinGW-W64's lib

Copy static and import libraries in  `GSL4Windows\lib`

* libgsl.a libgsl.dll.a 

* libgslcblas.a libgslcblas.dll.a

To the subfolder `lib\gcc\x86_64-w64-mingw32\Version` of  MinGW-W64.

For Example: MinGW-W64 8.1.0 is installed in `C:\mingw64\`, copy to `C:\mingw64\lib\gcc\x86_64-w64-mingw32\8.1.0`

### 2 Copy dynamic libraries to the default path of Windows

Copy `GSL4Windows\bin` 

* libgsl-23.dll

* libgslcblas-0.dll

TO `C:\Windows\System`

### 3 Copy header files to the default path of MinGW-W64's include

Copy all *.h in the folder `GSL4Windows\include` to `C:\mingw64\x86_64-w64-mingw32\include\gsl`

### Gnuplot for Windows

Goto http://www.tatsuromatsuoka.com/gnuplot/Eng/winbin/ download Gnuplot for windows compiled withMinGW-W64，then unzip and run.
 
After installed, add the path of gnuplot.exe to the system environment variable **Path**，e.g: `"C:\Program Files\gnuplot\bin\"`

 