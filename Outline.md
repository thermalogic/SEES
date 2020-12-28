
# Outline

## Introduction of the Course

* Goals,Grading,Practices

* **Repositories**: Home,  PySimVCR, Practices

* [Building Software Environment: Python, VS Code, GCC, Git](./guide/BuildingSoftwareEnvironment.md) 

  * [Windows File System](./guide/WindowsFileSystem.md) 
  
* [Introduction to Markdown](./guide/Introduction2Markdown(Chinese).md)

* **Homework**
   
   * [Setup the working folder for the course](./guide/doc/AdvWorkingDir.md)
     
   * [Install Softwares: Python,VS Code,MinGW-W64(GCC),Git](./guide/doc/BuildingSoftwareEnvironment.md)

   * [Download the Home of PySEE, Using Jupyter Notebooks of the course](https://github.com/PySEE/home)

# 1 Python Basic

## [Introduction To Python](https://nbviewer.ipython.org/github/PySEE/home/tree/BEFE2021/notebook/Unit1-1-Introduction_To_Python.ipynb)

* **Python**: The interpreted ,dynamically typed, scripting Language
   * Numerical Types, Operators and Expressions 
   * Variables and Assignment 
   * Output: `print()` Comments：`#`
   * String, Slicing
   * Input：`input()`
   * Type Conversion
* Jupyter
   *  `magic` functions： `cell`, `line`   
   *  `!`  Shell command
      
## [Control Flow](https://nbviewer.ipython.org/github/PySEE/home/tree/BEFE2021/notebook/Unit1-2-Control_Flow.ipynb)

* `if`, `while loop`,`for loop`, `break`, `continue`

* `range(start,stop,step)`
     
* **Indentation**: delineate blocks of code
     
* Line Continuation: `() [] {}` , `\`

* `pass` as a placeholder
  
* **Python Style Guide**: The Zen of Python(`PEP20`); Coding convention(`PEP8`)

* Jupyter notebook extensions

## [Function, Module & Package](https://nbviewer.ipython.org/github/PySEE/home/tree/BEFE2021/notebook/Unit1-3-Function_Module_Package.ipynb)

* Function definitions, Positional, Keyword Arguments and Default Values, Functions as Objects, 

* Scoping

* Lambdas

* `docstring`,`pydoc`

* `%load`

* `print(str.format())`

* Module: `import M`,`from M import *` `import as`

* The interpreter search path, `sys.path`

* if __name__ == '__main__':

* Package, `__init__.py`

## [Tuple, Sequence unpacking](https://nbviewer.ipython.org/github/PySEE/home/tree/BEFE2021/notebook/Unit1-4-1-Tuple.ipynb)

* (1,)  a,b=(1,2)

## [List,Range](https://nbviewer.ipython.org/github/PySEE/home/tree/BEFE2021/notebook/Unit1-4-2-List.ipynb)

* List,List Comprehension

* mutability, object equality, aliasing, cloning: `L[:]` `copy()`, `deepcopy()`
      
* Sequence types(String,List,Tuple,Range): Operators and Functions

## [Dictionary](https://nbviewer.ipython.org/github/PySEE/home/tree/BEFE2021/notebook/Unit1-4-3-Dict.ipynb)

* {key:value} ; mutability;  

* dict view objects

## [Files](https://nbviewer.ipython.org/github/PySEE/home/tree/BEFE2021/notebook/Unit1-5-Files.ipynb)
   
* File

* Character Encoding, Unicode

* Table Data，CSV

* **Homework** 

   * Install Numpy,Scipy,Matplotlib

         > python -m pip install numpy scipy matplotlib

# 2 Scipy

## [Plotting Using Matplotlib](https://nbviewer.ipython.org/github/PySEE/home/tree/BEFE2021/notebook/Unit2-1-Plotting_Using_Matplotlib.ipynb)

* **Matplotlib.pyplot**
    
   * `figure`, `plot`, `show`, (x,y), (y)，

   * `title`,`xlabel`,`ylabel`,
   
   * write to file: png, svg
     
   * line style,color and width
   
   * type size

## [Understanding Examperimental Data](https://nbviewer.ipython.org/github/PySEE/home/tree/BEFE2021/notebook/Unit2-2-Understanding_Examperimental_Data.ipynb)

* The Behavior of Springs：
   
* NumPy: polyfit

* The Behavior of Projectiles, Coefficient of Determination
 
## [Lies Namned Lies And Statictics](https://nbviewer.ipython.org/github/PySEE/home/tree/BEFE2021/notebook/Unit2-3-Lies_Namned_Lies_And_Statictics.ipynb)

 * NumPy: genfromtxt, mean,var,corrcoef
   
 * Matplotlib: bar, subplot 

 * **It’s just as easy to `lie with numbers` as it is to lie with words**

## [Latex Math](https://nbviewer.ipython.org/github/PySEE/home/tree/BEFE2021/notebook/Unit2-A-Latex_Math.ipynb)

# 3 Class

## [Classes And Object-Oriented Programming](https://nbviewer.ipython.org/github/PySEE/home/tree/BEFE2021/notebook/Unit3-1-Classes_And_Object-Oriented_Programming.ipynb)

* `Computational thinking`

* Class, Inheritance

* Encapsulation and Information Hiding, Invisible `__name`

## [Iterator Generator](https://nbviewer.ipython.org/github/PySEE/home/tree/BEFE2021/notebook/Unit3-2-Iterator_Generator.ipynb)

*  Iterator; `iter`, `__next__`

*  Generator：`yield`

* `%%timeit`

## [Exception And Assertion](https://nbviewer.ipython.org/github/PySEE/home/tree/BEFE2021/notebook/Unit5-1-Exception_And_Assertion.ipynb)

* Built-In Exception, `try: except` `try:-except-else-finally`

* Raising Exceptions: `raise`

* User-defined Exceptions

* Predefined Clean-up Actions:`with`

*  `assert` statement

* **Homework**
 
   * Install coolprop
     
         >python -m pip install coolprop

# 4 Refrigeration Cycle

## [Refrigeration Cycle](https://nbviewer.ipython.org/github/PySEE/home/tree/BEFE2021/notebook/Unit4-1-RefrigerationCycle.ipynb)

* Modeling Simulation Engineering System

* Vapor-compression refrigeration cycle

## [Refrigeration Cycle Using OOP](https://nbviewer.ipython.org/github/PySEE/home/tree/BEFE2021/notebook/Unit4-2-RefrigerationCycle_OOP.ipynb)

# 5 GCC and Make

## [GCC and MAKE](https://nbviewer.ipython.org/github/PySEE/home/tree/BEFE2021/notebook/Unit5-1-GCC_Make.ipynb)

* GNU,GCC,MinGW-W64

* GNU **Make**
   
* C/C++ Preprocessor Directives, once-only headers 
   
## [GCC: C stdio](https://nbviewer.ipython.org/github/PySEE/home/tree/BEFE2021/notebook/Unit5-2-C_stdio.ipynb)
 
* stdio.h: `scanf,printf`

## [GCC Shared Library](https://nbviewer.ipython.org/github/PySEE/home/tree/BEFE2021/notebook/Unit5-3-GCC_Lib.ipynb)

* **Shared Library**: Windows, Linux

## [ctypes](https://nbviewer.ipython.org/github/PySEE/home/tree/BEFE2021/notebook/Unit5-4-ctypes.ipynb)

* ctypes:  `__cdecl`,`cdll.LoadLibrary` 

## [ctypes-fun](https://nbviewer.ipython.org/github/PySEE/home/tree/BEFE2021/notebook/Unit5-5-ctypes-fun.ipynb)

## [Modern C++](https://nbviewer.ipython.org/github/PySEE/home/tree/BEFE2021/notebook/Unit5-A-ModernCPP.ipynb)

* C++11 and above, std::tuple,std::vectors, std::unordered_map, std::any 

# 6  Version Control：Git

## [Version Control](https://nbviewer.ipython.org/github/PySEE/home/tree/BEFE2021/notebook/Unit6-1-Git.ipynb)

* [The Simple Guide to Git/Github](./guide/doc/TheSimpleStepsGithub(Chinese).md)  

* Homework
  
   * Install pypistats: >python -m pip install pypistats
  
   * [Windows Subsystem for Linux (WSL))](https://docs.microsoft.com/zh-cn/windows/wsl/)
   
      * [Install Windows Subsystem for Linux (WSL) on Windows 10(Chinese)](https://docs.microsoft.com/zh-cn/windows/wsl/install-win10)

      * [VS code: Developing in WSL](https://code.visualstudio.com/docs/remote/wsl)

      * [VS code: Using C++ and WSL in VS Code](https://code.visualstudio.com/docs/cpp/config-wsl#nodejs-articles)

   * **Optional**: [Install Ubuntu](./guide/doc/Ubuntu-Python-CPP(Chinese).md)

# 7 Linux

## [Linux/Ubuntu](https://nbviewer.ipython.org/github/PySEE/home/tree/BEFE2021/notebook/Unit7-1-Linux.ipynb)

* Linux OS

* [Ubuntu](./guide/doc/Ubuntu-Python-CPP(Chinese).md)

