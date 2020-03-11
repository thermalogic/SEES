
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

 ## [INTRODUCTION TO PYTHON](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit1-1-INTRODUCTION_TO_PYTHON.ipynb)

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
      
## [Control Flow](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit1-2-Control-Flow.ipynb)

* `if`, `while loop`,`for loop`, `break`, `continue`

* `range(start,stop,step)`
     
* **Indentation**: delineate blocks of code
     
* Line Continuation: `() [] {}` , `\`
   
* **Python Style Guide**: The Zen of Python(`PEP20`); Coding convention(`PEP8`)
      
## [Function, Module & Package](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit1-3-Function-Module_Package.ipynb)

* Function definitions, Positional, Keyword Arguments and Default Values

* Functions as Objects, Lambdas

* Scoping, Global Variablesn

* Specifications, 

* `docstring`,`pydoc`

* Module: `import M`,`from M import *`

* The interpreter search path, `sys.path`

* Package, `__init__.py`

## [Tuple, Sequence unpacking](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit1-4-1-Tuple.ipynb)

* (1,)  a,b=(1,2)

## [List,Range](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit1-4-2-List.ipynb)

* List,List Comprehension

* mutability, object equality, aliasing, cloning: `L[:]`
      
* Range

* Sequence types(String,List,Tuple,Range): Operators and Functions

* High-order function; map, filter, functools,reduce

## [Dictionary](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit1-4-3-Dict.ipynb)

* {key:value} ; mutability;  cloning: `copy()`, `deepcopy()`

## [Modern C++](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit1-4-4-ModernCPP.ipynb)

* `std::tuple`, `std::verctor`, `std::unordered_map`

*  auto, {}, any 

## [Files](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit1-5-Files.ipynb)
   
* File, Unicode, Table Data，CSV

* **Homework** 

   * Install Numpy,Scipy,Matplotlib

         > python -m pip install numpy scipy matplotlib

## [Numpy](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit2-1-Numpy-Basic.ipynb)

   * array class, arithmetic operations: elementwise, index,slicing

## [PLOTTING USING MATPLOTLIB](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit2-2-PLOTTING-USING-MATPLOTLIB.ipynb)

* **Matplotlib.pyplot**
    
   * `figure`, `plot`, `show`, (x,y), (y)，

   * `title`,`xlabel`,`ylabel`,
   
   * write to file: png, svg
     
   * line style,color and width
   
   * type size, `reParams`

   * `%matplotlib inline`

## [UNDERSTANDING EXPERIMENTAL DATA](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit2-3-UNDERSTANDING_EXPERIMENTAL_DATA.ipynb)

* The Behavior of Springs：
   
* NumPy: polyfit

* The Behavior of Projectiles, Coefficient of Determination
 
## [LIES DAMNED LIES AND STATISTICS](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit2-4-LIES_DAMNED_LIES_AND_STATISTICS.ipynb)

 * NumPy: genfromtxt, mean,var,corrcoef
   
 * Matplotlib: bar, subplot 

 * **It’s just as easy to `lie with numbers` as it is to lie with words**

## [Scipy](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit2-5-Scipy.ipynb)

## [LaTeX-Math](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit2-6-LaTeX-Math.ipynb)

## [Live Updating and Interactive Plots](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit2-7-Live_Interact_Plot.ipynb)

* matplotlib.pyplot.ion(), matplotlib.animation

* `interactive plots`： from IPython import display, from ipywidgets import *, %matplotlib notebook
   
* psutil

## [The-SIR-epidemic-model](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit2-8-Special-Example-The-SIR-epidemic-model.ipynb)

* SIR

* NUmpy,Scipy,Matplotlib

* LaTex-Math

## [CLASSES AND OBJECT-ORIENTED PROGRAMMING](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit3-1-CLASSES_AND_OBJECT-ORIENTED_PROGRAMMING.ipynb)

* Abstract Data Types and Classes, Inheritance, 

* Encapsulation and Information Hiding, Invisible `__name`

* `pass`

## [Iterator Generator](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit3-2-Iterator-Generator.ipynb)

*  Iterator; `iter`, `__next__`

*  Generator：`yield`

* `%%timeit`

## [UML Class Diagram](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit3-3-UML.ipynb)

* **Homework**
 
   * Install iapws: 
     
         >python -m pip install iapws
    
  * [Download and Install SEUIF97](https://github.com/PySEE/SEUIF97)  
      
         > python -m pip install seuif97

  * **Optional** [Creating UML diagrams for Python code](./guide/UMLPython.md) 

## [IAPWS-IF97](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit4-1-IF97.ipynb)

* IAPWS-IF97

* Python library for IAPWS，SEUIF97

* `print(str.format())`
   
* **Homework**

   * [Download the PyRankine](https://github.com/PySEE/PyRankine)  
 
## [RankineCycle 8.1.8.2: SimFUN](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit4-2-RankineCycle-SimFun.ipynb)

   * Rankine Cycle 8.1,8.2：the expression directly; the simple abstraction using List,Dict and Function
  
   * Data file(I/O), Redirect **stdout** to a file, pprint

   * glob

   * Matplotlib：T-S Diagram of Rankine Cycle

## [The simple Rankine Cycle simulator using OOP](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit4-3-RankineCycle-OOP.ipynb)

* OOP: The Rankine Cycle 8.1,8.2 with csv files

## [The General Simulator of Rankine Cycle](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit4-4-RankineCycle-General.ipynb)

* Rankine Cycle: JSON,`json.loads()`

* UML Class Diagram

* jump table
 
## [Modeling and Simulation Methods of Engineering Systems](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit4-5-ModelingSimulation_EngineeringSystems.ipynb)

*  The brief introduction of simulation software and Modelica

* **Homework**
  
   * [Rankine Cycle](https://github.com/PySEE/PyRankine)
 
   * Do [Practice 3](https://github.com/PySEE/Practices/tree/S2020/P3) 
   
   * **Optional**
       
      * [Install OpenModelica](./guide/InstallOpenModelica.md) 

## [EXCEPTIONS AND ASSERTIONS](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit5-1-EXCEPTIONS_AND_ASSERTIONS.ipynb)

* Built-In Exception, `try: except` 

* Raising Exceptions: `raise`

* User-defined Exceptions

* `try:-except-else-finally`

* Predefined Clean-up Actions:`with`

*  `assert` statement

## [TESTING AND DEBUGGING](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit5-2-TESTING_AND_DEBUGGING.ipynb)

   * Testing: test suite,Black-Box Testing,Glass-Box Testing,unit testing, integration testing

   * Debugging: bug:Overt,covert,Persistent,intermittent,dubugging process,`print`

   * The typical mistakes

## [Unit testing framework：unittest](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit6-1-DevTools_unittest.ipynb)

* `unittest.TestCase`, test*，Asserting 

* Test Fixtures:`setUp`,`tearDown`

* Test Suites

* `*args`，`**kwargs` ， `__call__`, unittest in IAPWS Package

## [doctest](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit6-2-DevTools_doctest.ipynb)
     
## [Profilers](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit6-3-DevTools_Profilers.ipynb)

* `cProfile.run`, pstats

* `cProfile.Profile()`, `io` module

* Improve the Performance: memoization
       
* **Decorator**, **Property**,`@property`,Private Variables(`_`)

## [timeit](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit6-4-DevTools_timeit.ipynb)
   
## [GCC and MAKE](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit7-1-GCC_MAKE.ipynb)

* GNU,GCC,MinGW-W64

* GNU **Make**
   
* C/C++ Preprocessor Directives, once-only headers 
   
## [GCC: C stdio](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit7-2-C_stdio.ipynb)
 
    * stdio.h: `scanf,printf`

## [Fortran: using gfortran](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit7-3-Fortran_gfortran.ipynb)    

    * program, subroutine, function, module

## [GCC Shared Library](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit8-1-GCC_Lib.ipynb)

* **Shared Library** :Windows  and Linux

## [ctypes: variable](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit8-2-1-ctypes-var.ipynb)

* ctypes: `__cdecl`,`cdll.LoadLibrary` 

* one/two dimension array, structure

* C code: Polynomial Regression; CSV's reader

## [ctypes: function](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit8-2-1-ctypes-fun.ipynb)

*  `CDLL`,`WinDLL`

* call Python function in C

* C code: bisection

## [Winndows DLL, Excel VBA](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit8-3-DLL_VBA.ipynb)

* Building Windows DLL: `__stdcall`,`windll.LoadLibrary`
  
* Excel VBA(Excel 2013 above, 64bit)

    * https://github.com/thermalogic/Excel4Engineering  

## [CPP Plotting with Matplotlib](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit8-4-CPP=Matplotlib.ipynb)

* Using Matplotlib through C/C++ API

* C++ reader of CSV；`std::istringstream, std::vector, std::string`

## [Version Control](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit9-1-Git.ipynb)

* [The Simple Guide to Git/Github](./guide/doc/TheSimpleStepsGithub(Chinese).md)  

* Homework
  
   * Install pypistats: >python -m pip install pypistats

   * **Optional**:
   
      * [Install Ubuntu](./guide/doc/Ubuntu-Python-CPP(Chinese).md)

      * [Install Windows Subsystem for Linux (WSL) on Windows 10(Chinese)](https://docs.microsoft.com/zh-cn/windows/wsl/install-win10)

         * [VS code: Developing in WSL](https://code.visualstudio.com/docs/remote/wsl)

         * [VS code: Using C++ and WSL in VS Code](https://code.visualstudio.com/docs/cpp/config-wsl#nodejs-articles)

## [Linux/Ubuntu](https://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit9-2-Linux.ipynb)

* [Ubuntu](./guide/doc/Ubuntu-Python-CPP(Chinese).md), Ubuntukylin

## [Outlook: Further Studing](./guide/doc/FurtherStuding.md)

## Recap

* Python, GCC, Practices
 
* **Homework**
  
    * https://github.com/PySEE/Practices


