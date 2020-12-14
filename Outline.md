
# Course Outline

## Introduction of the Course

* Goals,Grading,Practices

* **Repositories**: Home, Practices, SEUIF97, PyRankine

* [Building Software Environment: Python, VS Code, GCC，Git](./guide/BuildingSoftwareEnvironment.md) 

  * [Computer Terminal](./ComputerTerminal.md/)

  * [Windows File System](./guide/WindowsFileSystem.md) 
  
* [Introduction to Markdown](./guide/Introduction2Markdown(Chinese).md)

* [Resources On Github](./guide/ResourcesOnGithub.md)

* **Homework**
   
   * [Setup the working folder for the course](./guide/doc/AdvWorkingDir.md)
     
   * [Install Softwares: Python,MinGW-W64(GCC), VS Code, Git](./guide/doc/BuildingSoftwareEnvironment.md)

   * [Download the Home of PySEE, Using Jupyter Notebooks of the course](https://github.com/PySEE/home)

# 1 Python Basic

## [INTRODUCTION TO PYTHON](https://nbviewer.ipython.org/github/PySEE/home/tree/S2021/notebook/Unit1-1-INTRODUCTION_TO_PYTHON.ipynb)

* **Python**: The interpreted ,dynamically typed, scripting Language
   * Variables and Assignment 
   * Output: `print()` Comments：`#`
   * Numerical Types, Operators and Expressions 
   * String, Slicing
   * Input：`input()`
   * Type Conversion
* Jupyter
   *  `magic` functions： `cell`, `line`   
   *  `!`  Shell command
      
## [Control Flow](https://nbviewer.ipython.org/github/PySEE/home/tree/S2021/notebook/Unit1-2-Control-Flow.ipynb)

* `if`, `while loop`,`for loop`, `break`, `continue`

* `range(start,stop,step)`
     
* **Indentation**: delineate blocks of code
     
* Line Continuation: `() [] {}` , `\`

* `pass` as a placeholder
  
* **Python Style Guide**: The Zen of Python(`PEP20`); Coding convention(`PEP8`)

* Jupyter notebook extensions

## [Function, Module & Package](https://nbviewer.ipython.org/github/PySEE/home/tree/S2021/notebook/Unit1-3-Function-Module_Package.ipynb)

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

## [Tuple, Sequence unpacking](https://nbviewer.ipython.org/github/PySEE/home/tree/S2021/notebook/Unit1-4-1-Tuple.ipynb)

* (1,)  a,b=(1,2)

## [List,Range](https://nbviewer.ipython.org/github/PySEE/home/tree/S2021/notebook/Unit1-4-2-List.ipynb)

* List,List Comprehension

* mutability, object equality, aliasing, cloning: `L[:]` `copy()`, `deepcopy()`
      
* Sequence types(String,List,Tuple,Range): Operators and Functions

## [Dictionary](https://nbviewer.ipython.org/github/PySEE/home/tree/S2021/notebook/Unit1-4-3-Dict.ipynb)

* {key:value} ; mutability;  

* dict view objects

## [Files](https://nbviewer.ipython.org/github/PySEE/home/tree/S2021/notebook/Unit1-5-Files.ipynb)
   
* File

* Character Encoding, Unicode

* Table Data，CSV

* **Homework** 

   * Install Numpy,Scipy,Matplotlib

         > python -m pip install numpy scipy matplotlib

# 2 Scipy

## [PLOTTING USING MATPLOTLIB](https://nbviewer.ipython.org/github/PySEE/home/tree/S2021/notebook/Unit2-1-PLOTTING-USING-MATPLOTLIB.ipynb)

* **Matplotlib.pyplot**
    
   * `figure`, `plot`, `show`, (x,y), (y)，

   * `title`,`xlabel`,`ylabel`,
   
   * write to file: png, svg
     
   * line style,color and width
   
   * type size, `reParams`

## [UNDERSTANDING EXPERIMENTAL DATA](https://nbviewer.ipython.org/github/PySEE/home/tree/S2021/notebook/Unit2-2-UNDERSTANDING_EXPERIMENTAL_DATA.ipynb)

* The Behavior of Springs：
   
* NumPy: polyfit

* The Behavior of Projectiles, Coefficient of Determination
 
## [LIES DAMNED LIES AND STATISTICS](https://nbviewer.ipython.org/github/PySEE/home/tree/S2021/notebook/Unit2-3-LIES_DAMNED_LIES_AND_STATISTICS.ipynb)

 * NumPy: genfromtxt, mean,var,corrcoef
   
 * Matplotlib: bar, subplot 

 * **It’s just as easy to `lie with numbers` as it is to lie with words**

## [MathJax](https://nbviewer.ipython.org/github/PySEE/home/tree/S2021/notebook/Unit2-A-MathJax.ipynb)

# 3 Class

## [CLASSES AND OBJECT-ORIENTED PROGRAMMING](https://nbviewer.ipython.org/github/PySEE/home/tree/S2021/notebook/Unit3-1-CLASSES_AND_OBJECT-ORIENTED_PROGRAMMING.ipynb)

* `Computational thinking`

* Class, Inheritance

* Encapsulation and Information Hiding, Invisible `__name`

* `pass` as a placeholder

## [Iterator Generator](https://nbviewer.ipython.org/github/PySEE/home/tree/S2021/notebook/Unit3-2-Iterator-Generator.ipynb)

*  Iterator; `iter`, `__next__`

*  Generator：`yield`

* `%%timeit`

* **Homework**
 
   * Install coolprop
     
         >python -m pip install coolprop

# 4 Refrigeration Cycle

## [Refrigeration Cycle](https://nbviewer.ipython.org/github/PySEE/home/tree/S2021/notebook/Unit4-1-RefrigerationCycle.ipynb)

## [Refrigeration Cycle using OOP](https://nbviewer.ipython.org/github/PySEE/home/tree/S2021/notebook/Unit4-2-RefrigerationCycle-OOP.ipynb)

* **Homework**

   * **Optional**: [Download FREE TRIAL VERSION Dymola](https://www.3ds.com/products-services/catia/products/dymola/latest-release/)
     
     * http://www.3ds.com/fileadmin/PRODUCTS-SERVICES/CATIA/Dymola/dymola-demo.zip

## [Modelica](https://nbviewer.ipython.org/github/PySEE/home/tree/S2021/notebook/Unit4-3-ModelingSimulation_EngineeringSystems.ipynb)

*  Modelica

## Software Enginering Tools

## [EXCEPTIONS AND ASSERTIONS](https://nbviewer.ipython.org/github/PySEE/home/tree/S2021/notebook/Unit5-1-EXCEPTIONS_AND_ASSERTIONS.ipynb)

* Built-In Exception, `try: except` 

* Raising Exceptions: `raise`

* User-defined Exceptions

* `try:-except-else-finally`

* Predefined Clean-up Actions:`with`

*  `assert` statement

## [TESTING AND DEBUGGING](https://nbviewer.ipython.org/github/PySEE/home/tree/S2021/notebook/Unit5-2-TESTING_AND_DEBUGGING.ipynb)

   * Testing: Black-Box Testing,Glass-Box Testing,unit testing, integration testing

   * Debugging: bug:Overt,covert,Persistent,intermittent,dubugging process, `print`

   * The typical mistakes

## [unittest](https://nbviewer.ipython.org/github/PySEE/home/tree/S2021/notebook/Unit5-3-DevTools_unittest.ipynb)

* `unittest.TestCase`, test*，Asserting 

* Test Fixtures:`setUp`,`tearDown`

* Test Suites

* `*args`，`**kwargs` 

## [doctest](https://nbviewer.ipython.org/github/PySEE/home/tree/S2021/notebook/Unit5-A-DevTools_doctest.ipynb)

# 6 GCC and Make

## [GCC and MAKE](https://nbviewer.ipython.org/github/PySEE/home/tree/S2021/notebook/Unit6-1-GCC_MAKE.ipynb)

* GNU,GCC,MinGW-W64

* GNU **Make**
   
* C/C++ Preprocessor Directives, once-only headers 
   
## [GCC: C stdio](https://nbviewer.ipython.org/github/PySEE/home/tree/S2021/notebook/Unit6-2-C_stdio.ipynb)
 
    * stdio.h: `scanf,printf`

## [GCC Shared Library](https://nbviewer.ipython.org/github/PySEE/home/tree/S2021/notebook/Unit6-3-GCC_Lib.ipynb)

* **Shared Library**: Windows, Linux

## [ctypes](https://nbviewer.ipython.org/github/PySEE/home/tree/S2021/notebook/Unit6-4-ctypes.ipynb)

* ctypes:  `__cdecl`,`cdll.LoadLibrary` 

## [ctypes-fun](https://nbviewer.ipython.org/github/PySEE/home/tree/S2021/notebook/Unit6-5-ctypes-fun.ipynb)

## [Windows DLL, Excel VBA](https://nbviewer.ipython.org/github/PySEE/home/tree/S2021/notebook/Unit6-A-DLL_VBA.ipynb)

* Building Windows DLL: `__stdcall`,`windll.LoadLibrary`
  
* Excel VBA(Excel 2013 above, 64bit)

    * https://github.com/thermalogic/Excel4Engineering  

# 7  Version Control：Git

## [Version Control](https://nbviewer.ipython.org/github/PySEE/home/tree/S2021/notebook/Unit7-1-Git.ipynb)

* [The Simple Guide to Git/Github](./guide/doc/TheSimpleStepsGithub(Chinese).md)  

* Homework
  
   * Install pypistats: >python -m pip install pypistats
  
   *  [Windows Subsystem for Linux (WSL))](https://docs.microsoft.com/zh-cn/windows/wsl/)
   
      * [Install Windows Subsystem for Linux (WSL) on Windows 10(Chinese)](https://docs.microsoft.com/zh-cn/windows/wsl/install-win10)

      * [VS code: Developing in WSL](https://code.visualstudio.com/docs/remote/wsl)

      * [VS code: Using C++ and WSL in VS Code](https://code.visualstudio.com/docs/cpp/config-wsl#nodejs-articles)

   * **Optional**: [Install Ubuntu](./guide/doc/Ubuntu-Python-CPP(Chinese).md)

# 8 Linux

## [Linux/Ubuntu](https://nbviewer.ipython.org/github/PySEE/home/tree/S2021/notebook/Unit8-1-Linux.ipynb)

* Linux OS

* [Ubuntu](./guide/doc/Ubuntu-Python-CPP(Chinese).md)

# Outlook

## [Outlook: Further Studing](./guide/doc/FurtherStuding.md)



