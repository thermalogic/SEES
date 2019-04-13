## Course Outline

* **Introduction of PySEE**

  * Goals,Grading,Practices

  * **Repositories**: Home,SEUIF97,PyRankine,Practices,GSL4Windows,Googletest4Windows

  * [Building Software Environment](./guide/BuildingSoftwareEnvironment.md) 

    * [File Path of Windows](./guide/FilePath(Chinese).md) 

    * [Computer Terminal](./CodingWithTerminal.md/)
  
  * [Introduction to Markdown](./guide/Introduction2Markdown(Chinese).md)

  * [Resources On Github](./guide/ResourcesOnGithub.md)

  * **Homework**
   
     * Read the contents：Python, Jypyter, MinGW-W64(GCC), Visual Studio Code，Git, Github, Markdown,
   
     * [ebooks](./Reference.md)
   
       * John V. Guttag. Introduction to Computation and Programming Using Python: With Application to Understanding Data(Second Edition). MIT Press, 2016.

     * Do [Practice 1](https://github.com/PySEE/Practices/tree/S2019/P1)
   
       * [Setup the working folder for the course](./guide/AdvWorkingDir.md)
     
       * [Install Softwares: Python,Jupyter, MinGW-W64(GCC), Visual Studio Code, Git](./guide/BuildingSoftwareEnvironment.md)

       * [Download the Home of PySEE, Using Jupyter Notebooks of the course](https://github.com/PySEE/home)

* [1 INTRODUCTION TO PYTHON](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit1-1-02-INTRODUCTION_TO_PYTHON.ipynb)

   * **Softwares**: Python Shell,IDLE,Jupyter,Visual Studio Code

   * **Python**: the interpreted ,dynamically typed, scripting Language
     
      * Objects, Numerical Types, Operators and Expressions 
      
      * Variables and Assignment; Comments：`#`

      * String, Slicing, Input, 
      
      * Type Conversion
   
   * Jupyter's `magic` functions： cell, line   
      
* [2.1 Control Flow](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit1-2-1-Control_Flow.ipynb)

   * `if`, `while`,`for loops`, `break`, `continue`

   * `range(start,stop,step)`
     
   * **Indentation**: delineate blocks of code
     
   * Line Continuation

   * Exhaustive Enumeration
    
   * **Python Style Guide**: The Zen of Python(PEP20); Coding convention(PEP8)
      
* [2.2 SOME SIMPLE NUMERICAL PROGRAMS](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit1-2-2-03-SOME_SIMPLE_NUMERICAL_PROGRAMS.ipynb)
 
   * Bisection，Newton-Raphson
   
   * Using Floats,`round(x, numDigits)`

   * **Homework**
    
     * [Install Numpy,Scipy,Matplotlib](./guide/BuildingSoftwareEnvironment.md)

           > python -m pip install numpy scipy matplotlib

* [3 FUNCTIONS](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit1-3-04_FUNCTIONS_SCOPING_AND_ABSTRACTION.ipynb)

   * Function definitions, Positional, Keyword Arguments and Default Values

   * Functions as Objects, Lambdas

   * Specifications, docstring

   * Scoping, Global Variables, Recursion

   * Module: `import M`,`from M import *`; the interpreter search path, `sys.path`, Scipy

* **4 Structured types**

   * [4.1 Tuple, Sequence unpacking](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit1-4-1-05-Tuple.ipynb)

   * [4.2 List,Range](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit1-4-2-05-List.ipynb)

      * List, mutability, object equality, aliasing, cloning, 
      
      * List Comprehension

      * Range

      * Sequence types(String,List,Tuple,Range): Operators and Functions

      * High-order function; map, filter, functools,reduce

   * [4.3 Dictionary, Mutability](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit1-4-3-05-Dict.ipynb)
   
   * **Homework**

     * DO [Your Python Quick Review](https://nbviewer.ipython.org/github/PySEE/Practices/blob/S2019/self-exercises/Python-Quick-Review.ipynb)
 
* [5 Files](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit1-5-Files.ipynb)
   
   * File, Unicode, Table Data，CSV

   * **Homework** 
  
     * Install iapws: 
     
           >python -m pip install iapws
    
     * [Download and Install SEUIF97](https://github.com/PySEE/SEUIF97)  
      
           > python -m pip install seuif97


 * [PyThermo-IF97](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit2-1-PyThermo-IF97.ipynb)

    * IAPWS-IF97

    * Python library for IAPWS，SEUIF97

    * `print(str.format())`
   
   * **Homework**

     * [Download the PyRankine](https://github.com/PySEE/PyRankine)  
    
     * [ebook](./Reference.md)
   
       * Michael J . Moran. Fundamentals of Engineering Thermodynamics(7th Edition). John Wiley & Sons, Inc. 2011
       
         Download the ebook from SEU: http://www.lib.seu.edu.cn/ （查找资源->外文电子书->Wiley电子教材->T(工业技术)->TK(能源与动力工程)->TK1(热力工程,热机)）

* [RankineCycle 8.1.8.2: SimVer](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit2-2-PyThermo-RankineCycle-SimVer.ipynb)

   * Rankine Cycle 8.1,8.2：the expression directly; the simple abstraction using List,Dict and Function
  
   * Data file(I/O), Redirect **stdout** to a file, pprint

   * [LaTeX-Math](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit2-4-PyThermo-LaTeX-Math.ipynb)

   * Matplotlib：T-S Diagram of Rankine Cycle

* [RankineCycle 8.5: AdvVer](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit2-3-PyThermo-RankineCycle-AdvVer.ipynb)

   * Rankine Cycle 8.5：the expression directly; the general abstraction using List,Dict and Function
 
   * **Homework**

     * Do [Practice 2](https://github.com/PySEE/Practices/tree/S2019/P2)  

* [08 CLASSES AND OBJECT-ORIENTED PROGRAMMING](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit3-1-08_CLASSES_AND_OBJECT-ORIENTED_PROGRAMMING.ipynb)

   * Abstract Data Types and Classes, Inheritance, Encapsulation and Information Hiding

   * `pass`,Invisible `__name`, Generators：`yield`

   * `import datetime`,`from dateutil.relativedelta import relativedelta`

   * `%%timeit`

* [Package, UML Class Diagram](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit3-2-Package-UML.ipynb)

   * **Homework**
   
     * [Creating UML diagrams for Python code](./guide/UMLPython.md) 

     * DO [Your Python Quick Review](https://nbviewer.ipython.org/github/PySEE/Practices/blob/S2019/self-exercises/Python-Quick-Review.ipynb)

* [The OOP of Rankine Cycle](https://github.com/PySEE/PyRankine)

   * [OOP:Rankine Cycle 8.1,8.2 with csv files](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit4-1-PyThermo-RankineCycle-OOP.ipynb)

      * `glob`

   * [The General simulator](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit4-2-PyThermo-RankineCycle-General.ipynb)

       * Rankine Cycle: JSON,UML Class Diagram
       
       * `super().*`, `__dict__.update()`

       * jump table

    * [Python JSON](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit4-3-PyThermo-Python-JSON.ipynb)

  * **Homework**
  
     * [Rankine Cycle：Step4,Step5](https://github.com/PySEE/PyRankine)
 
     * Do [Practice 3](https://github.com/PySEE/Practices/tree/S2019/P3) 
   
     * (Optional) [Install OpenModelica](./guide/InstallOpenModelica.md) 

* [Modeling and Simulation Methods of Engineering Systems](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit4-4-ModelingSimulation_EngineeringSystems.ipynb)
 
   * Modelica, Jupyter OpenModelica kernel

* [11.1 PLOTTING USING MATPLOTLIB](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit5-1-11-1_PLOTTING-USING-MATPLOTLIB.ipynb)

   * **Matplotlib.pyplot**
    
     * `figure`, `plot`, `show`, (x,y), (y)，
     
     * write to file: png, svg
     
     * line style and color: `'b-'`,`'ro'`
   
     * `title`,`xlabel`,`ylabel`,

     * type size and line width , `reParams`

     * `%matplotlib inline`

  * **Examples**: IF97 T-S,H-S Diagram; The Rankine Cycle T-S  Diagrams

* [18 UNDERSTANDING EXPERIMENTAL DATA](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit5-2-18_UNDERSTANDING_EXPERIMENTAL_DATA.ipynb)

   * The Behavior of Springs：
   
   * NumPy: array, polyfit, Arithmetic Operations: elementwise

   * The Behavior of Projectiles: Coefficient of Determination
 
* [21 LIES DAMNED LIES AND STATISTICS](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit5-3-21_LIES_DAMNED_LIES_AND_STATISTICS.ipynb)

   * NumPy: genfromtxt,mean,var,corrcoef
   
   * Matplotlib: bar, subplot 

   * It’s just as easy to **lie with numbers** as it is to lie with words

   * **Homework**

     * Do [Practice 4](https://github.com/PySEE/Practices/tree/S2019/P4)  

* [07 EXCEPTIONS AND ASSERTIONS](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit6-1-07_EXCEPTIONS_AND_ASSERTIONS.ipynb)

   * Built-In Exception, `try: except` 

   * Raising Exceptions: `raise`

   * User-defined Exceptions

   * `try:-except-else-finally`

   * Predefined Clean-up Actions:`with`

   * `assert` statement

   * **Homework**
     
       * [06 TESTING AND DEBUGGING](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit6-2-06_TESTING_AND_DEBUGGING.ipynb)

         * Testing: test suite,Black-Box Testing,Glass-Box Testing,unit testing, integration testing

         * Debugging: bug:Overt,covert,Persistent,intermittent,dubugging process,`print`

         * The typical mistakes

* [Unit testing framework：unittest](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit7-1-DevTools_unittest.ipynb)

   * `unittest.TestCase`, test*，Asserting 

   * Test Fixtures:`setUp`,`tearDown`

   * Test Suites

   * `*args`，`**kwargs`

   * **Homework**
      
      * [doctest](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit7-2-DevTools_doctest.ipynb)
     
* [Profilers](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit7-3-DevTools_Profilers.ipynb)

   * `cProfile.run`,pstats

   * `cProfile.Profile()`, `io` module

   * Improve the Performance: memoization, `__call__`
       
   * **Decorator**, **Property**,`@property`,Private Variables(`_`)
   
   * **Homework**

       * [timeit](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit7-4-DevTools_timeit.ipynb)

  [GCC_MAKE](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit8-1-GCC_MAKE.ipynb)

   * GNU,GCC,MinGW-W64

   * GNU **Make**
   
   * C/C++ Preprocessor Directives, once-only headers 
   
      * C :stdio.h: `scanf,printf`

* [GCC_DLL](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit8-2-GCC_DLL.ipynb)

  * the **Shared Library** :Linux,Windows
  
  * **Homework**

      * Install [Googletest for Windows](https://github.com/PySEE/Googletest4Windows)

      * Do [Practice 5](https://github.com/PySEE/Practices/tree/S2019/P5)

* [Python_ctypes](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit8-3-Python_ctypes.ipynb)

  * ctypes: `__cdecl`,`__stdcall`,`windll.LoadLibrary`
  
 * [DLL_VBA_Python](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit8-4-DLL_VBA_Python.ipynb)

   * Building Windows DLL
   
   * Excel VBA(Excel 2013 above, 64bit)

   * Unit Test for C/C++:  Unity, Googletest

   * **Homework**

     * [Install GSL & GNUPLOT for Windows](./guide/BuildingSoftwareEnvironment.md#ginstall-gsl-and-gnuplot-for-windows) 

     * Install pypistats: >python -m pip install pypistats

     * **Optional**: 
        
       * [Install Ubuntu,GSL,Gnuplot](./guide/Ubuntu-Python-CPP(Chinese).md)
     
* [Ubuntu_GSL_GNUPLOT](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit8-5-Ubuntu_GSL_GNUPLOT.ipynb)

   * [Ubuntu](./guide/Ubuntu-Python-CPP(Chinese).md), Ubuntukylin

   * GSL: statistical functions, linear least-Squares fitting
   
   * Gnuplot: plotting function,data file, point and line style，multiple plots,curve fitting

       * C/C++ Plotting : pipe

* [Version Control](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit9-1-Git.ipynb)

   * [The Simple Guide to Git/Github](./guide/TheSimpleStepsGithub(Chinese).md)   

   * **Homework**

     * **Optional**: [Do Bonus](https://github.com/PySEE/Practices/tree/S2019/Bonus)

* **Recap, Outlook**

  * [Python35 Quick Reference](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/UnitA-1-Python35-Quick-Reference.ipynb)
  
  * [Further Studing](./guide/FurtherStuding.md)

  * **Homework**
  
     * DO [Your Python Quick Review](https://nbviewer.ipython.org/github/PySEE/Practices/blob/S2019/self-exercises/Python-Quick-Review.ipynb)
    
* **Appendix**

   * [Python:Reading-and-Writing-Data-Files-Binary-Data-File](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/UnitA-2-Reading-and-Writing-Binary-Data-Files.ipynb)

   * [GCC: C stdio](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/UnitA-3-GCC-C_stdio.ipynb)
