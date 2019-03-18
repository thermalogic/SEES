## Course Outline

* **Introduction of PySEE**

  * Goals,Grading,Practices

  * **Repositories**: Home,SEUIF97,PyRrankine,Practices,GSL4Windows,Googletest4Windows

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

* [PREFACE](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit1-1-00_PREFACE.ipynb)

   * **Overview** Introduction to Computation and Programming Using Python

* [02 INTRODUCTION TO PYTHON](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit1-2-02_INTRODUCTION_TO_PYTHON.ipynb)'

   * **Softwares**: Python Shell,IDLE,Jupyter,Visual Studio Code

   * **Python**: 
     
      * **The Basic Elements of Python**: Objects, Expressions, and Numerical Types; Variables and Assignment;
      
      * **Branching Programs** : `if-else `
     
      * **Strings and Input**: String, Slicing, Input, Unicode

      * **Iteration**:  `while `

      * **Python Style Guide**: The Zen of Python(PEP20); Coding convention(PEP8)
     
* [03 SOME SIMPLE NUMERICAL PROGRAMS](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit1-3-03_SOME_SIMPLE_NUMERICAL_PROGRAMS.ipynb)
 
   * Exhaustive Enumeration
 
   * **Loop**：`For Loops`,`range(start,stop,step)`

   * Approximate Solutions and Bisection Search, Fancier Output Formatting, `str.format()` 

   * About Using Floats,`round(x, numDigits)`

   * Newton-Raphson

   * **Homework**
    
     * [Install Numpy,Scipy,Matplotlib](./guide/BuildingSoftwareEnvironment.md)

           > python -m pip install numpy scipy matplotlib

* [04 FUNCTIONS SCOPING AND ABSTRACTION](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit1-4-04_FUNCTIONS_SCOPING_AND_ABSTRACTION.ipynb)

   * Functions and Scoping: Definitions, Positional, Keyword Arguments and Default Values

   * Specifications, docstring

   * Recursion

   * Global Variables

   * Module, the interpreter search path, `sys.path`, Scipy

   * Files

* [05 STRUCTURED TYPES MUTABILITY AND HIGHERORDER FUNCTIONS](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit1-5-05_STRUCTURED_TYPES_MUTABILITY_AND_HIGHERORDER_FUNCTIONS.ipynb)

   * **Tuple**, Multiple Assignment

   * **List**,  **Mutability**, Cloning, List Comprehension

   * Functions as Objects, Lambdas

   * Strings

   * **Dictionary**, Mutability

   * **Homework**
     
     * DO [Your Python Quick Review](https://nbviewer.ipython.org/github/PySEE/Practices/blob/S2019/self-exercises/Python-Quick-Review.ipynb)
 
     * Install iapws: 
     
           >python -m pip install iapws
    
     * [Download and Install SEUIF97](https://github.com/PySEE/SEUIF97)  
      
           > python -m pip install seuif97

 * [PyThermo-IF97](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit2-1-PyThermo-IF97.ipynb)

    * IAPWS-IF97

    * Python library for IAPWS，SEUIF97
   
   * **Homework**

     * [Download the PyRankine](https://github.com/PySEE/PyRankine)  
    
     * [ebook](./Reference.md)
   
       * Michael J . Moran. Fundamentals of Engineering Thermodynamics(7th Edition). John Wiley & Sons, Inc. 2011

* [PyThermo: Rankine Cycle](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit2-2-PyThermo-RankineCycle.ipynb)

   * Ideal Rankine Cycle：the expression directly, List,Dict,Function

   * [MathJax,LaTeX](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit2-3-PyThermo-MathJax-LaTeX.ipynb)

   * pprint，Matplotlib, SVG

  * **Homework**

     * Do [Practice 2](https://github.com/PySEE/Practices/tree/S2019/P2)  

* [08 CLASSES AND OBJECT-ORIENTED PROGRAMMING](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit3-1-08_CLASSES_AND_OBJECT-ORIENTED_PROGRAMMING.ipynb)

   * Abstract Data Types and Classes

   * Inheritance

   * Encapsulation and Information Hiding

   * `pass`,Generators
  
* [11.1 PLOTTING USING MATPLOTLIB](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit3-2-11-1_PLOTTING-USING-MATPLOTLIB.ipynb)

   * **Matplotlib.pyplot**
    
     * `figure`, `plot`, `show`, (x,y), (y) 
     
     * line style and color: `'b-'`,`'ro'`
   
     * `title`,`xlabel`,`ylabel`,

     * type size and line width , `reParams`

     * `%matplotlib inline`

  * **Examples**: IF97 T-S,H-S Diagram; The Rankine Cycle T-S  Diagrams

  * **Homework**
  
     * DO [Your Python Quick Review](https://nbviewer.ipython.org/github/PySEE/Practices/blob/S2019/self-exercises/Python-Quick-Review.ipynb)

* [The General simulator of Rankine Cycle](https://github.com/PySEE/PyRankine)

   * [The Object-oriented programming of Ideal Rankine Cycle](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit4-1-PyThermo-IdealRankineCycle-OOP.ipynb)

   * [JSON of Rankine Cycle, UML Class Diagram, Python's super()](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit4-2-PyThermo-RankineCycle-JSON-UML.ipynb)

      * [Creating UML diagrams for Python code](./guide/UMLPython.md) 

   * [Python JSON](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit4-3-PyThermo-Python-JSON.ipynb)

   * [Python Package,Redirect stdout,glob](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit4-4-PyThermo-Pythons.ipynb)
 
  * **Homework**
  
     * Do [Practice 3](https://github.com/PySEE/Practices/tree/S2019/P3) 

* [18 UNDERSTANDING EXPERIMENTAL DATA](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit5-1-18_UNDERSTANDING_EXPERIMENTAL_DATA.ipynb)

   * The Behavior of Springs： CSV File 
   
       * NumPy: array, polyfit, Arithmetic Operations: elementwise

   * The Behavior of Projectiles: Coefficient of Determination
 
* [21 LIES DAMNED LIES AND STATISTICS](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit5-2-21_LIES_DAMNED_LIES_AND_STATISTICS.ipynb)

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

* [06 TESTING AND DEBUGGING](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit6-2-06_TESTING_AND_DEBUGGING.ipynb)

   * Testing: test suite,Black-Box Testing,Glass-Box Testing,unit testing, integration testing

   * Debugging: bug:Overt,covert,Persistent,intermittent,dubugging process,`print`

   * The typical mistakes

* **Python's DevTools**

   * [unittest — Unit testing framework](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit7-1-DevTools_unittest.ipynb)

     * `unittest.TestCase`, test*，Asserting 

     * Test Fixtures:`setUp`,`tearDown`

     * Test Suites

     * `*args`，`**kwargs`

   * [doctest](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit7-2-DevTools_doctest.ipynb)
     
     * `import doctest`

   * [timeit](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit7-3-DevTools_timeit.ipynb)

       * `%timeit`, `import timeit`

   * [Profilers](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit7-4-DevTools_Profilers.ipynb)

       * `cProfile.run`,pstats

       * `cProfile.Profile()`, `io` module

       * Improve the Performance: memoization, `__call__`
       
       * **Decorator**, **Property**,`@property`,Private Variables(`_`)

* [Version Control](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit7-5-DevTools_Git.ipynb)

   * [The Simple Guide to Git/Github](./guide/TheSimpleStepsGithub(Chinese).md) 

* **Homework**

   * DO [Your Python Quick Review](https://nbviewer.ipython.org/github/PySEE/Practices/blob/S2019/self-exercises/Python-Quick-Review.ipynb)
  
   * [GCC for Windows](./guide/BuildingSoftwareEnvironment.md)

* [GCC_MAKE](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit8-1-GCC_MAKE.ipynb)

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
        
       * [Excel4Engineering](https://github.com/thermalogic/Excel4Engineering)

       * [Install Ubuntu,GSL,Gnuplot](./guide/Ubuntu-Python-CPP(Chinese).md)
     
* [Ubuntu_GSL_GNUPLOT](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit8-5-Ubuntu_GSL_GNUPLOT.ipynb)

   * [Ubuntu](./guide/Ubuntu-Python-CPP(Chinese).md), Ubuntukylin

   * GSL: statistical functions, linear least-Squares fitting
   
   * Gnuplot: plotting function,data file, point and line style，multiple plots,curve fitting

       * C/C++ Plotting : pipe
   
   * **Homework**

     * DO [Your  Python Quick Review](https://nbviewer.ipython.org/github/PySEE/Practices/blob/S2019/self-exercises/Python-Quick-Review.ipynb)

     * **Optional**: [Do Bonus](https://github.com/PySEE/Practices/tree/S2019/Bonus)

* **Recap, Outlook**

  * [Python Quick Review](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit9-1-Recap-Python-Quick-Reference.ipynb)

  * [Python35 Quick Reference](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/UnitA-1-Recap-Python35-Quick-Reference.ipynb)
  
  * [Further Studing](./guide/FurtherStuding.md)
    
* **Appendix**

   * [Python:Reading-and-Writing-Data-Files-Binary-Data-File](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/UnitA-2-Reading-and-Writing-Data-Files-Binary-Data-Files.ipynb)

   * [GCC: C stdio](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/UnitA-5-GCC-C_stdio.ipynb)
