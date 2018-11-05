## Course Outline

* **Introduction of PySEE**

  * Goals,Grading,Practices

  * [Building Software Environment](./guide/BuildingSoftwareEnvironment.md) 

  * **Course Repositories**: Home,SEUIF97,PyRrankine

  * **Homework**
   
     * Read contents about  the course：Python，Jypyter,Markdown,Git/Github,Visual Studio Code

     * [Setup the working folder for the course](./guide/AdvWorkingDir.md)
     
     * [Install Softwares: Python,Jupyter,MinGW-W64,Visual Studio Code,Git](./guide/BuildingSoftwareEnvironment.md)

     * [Download the Home of PySEE, Using Juyter Notebooks of the course](https://github.com/PySEE/home)
   
     * [ebooks](./Reference.md)
   
       * John V. Guttag. Introduction to Computation and Programming Using Python: With Application to Understanding Data(Second Edition). MIT Press, 2016.

     * Do [Practice 1](https://github.com/PySEE/Practices/tree/S2019/P1)
   
* [PREFACE](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/00_PREFACE.ipynb)

   * **Overview** Introduction to Computation and Programming Using Python

* [02 INTRODUCTION TO PYTHON](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/02_INTRODUCTION_TO_PYTHON.ipynb)'

   * **Softwares**: Python Shell,IDLE,Jupyter,Visual Studio Code

   * **Python**: 
     
      * **The Basic Elements of Python**: Objects, Expressions, and Numerical Types; Variables and Assignment;
      
      * **Branching Programs** : `if-else `
     
      * **Strings and Input**: String Slicing, Input

      * **Iteration**:  `while `

      * **Python Developer's Guide**: The Zen of Python ,PEP20; Coding convention: PEP8
     
* [03 SOME SIMPLE NUMERICAL PROGRAMS](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/03_SOME_SIMPLE_NUMERICAL_PROGRAMS.ipynb)
 
   * Exhaustive Enumeration
 
   * `For Loops`

   * Approximate Solutions and Bisection Search

   * About Using Floats

   * Newton-Raphson

   * **Homework**
    
     * [Install Numpy,Scipy,Matplotlib](./guide/BuildingSoftwareEnvironment.md)

* [04 FUNCTIONS SCOPING AND ABSTRACTION](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/04_FUNCTIONS_SCOPING_AND_ABSTRACTION.ipynb)

   * Functions and Scoping: Definitions, Lambdas,Keyword Arguments and Default Values

   * Specifications, docstring

   * Recursion

   * Global Variables

   * Module, the interpreter search path, `sys.path`, Scipy

   * Files, Unicode

* [05 STRUCTURED TYPES MUTABILITY AND HIGHERORDER FUNCTIONS](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/05_STRUCTURED_TYPES_MUTABILITY_AND_HIGHERORDER_FUNCTIONS.ipynb)

   * Tuples, Multiple Assignment

   * **Lists**,  **Mutability**, Cloning,List Comprehension

   * Functions as Objects

   * Strings

   * **Dictionaries**,Mutability

   * **Homework**
    
     * [Install iapws](./guide/BuildingSoftwareEnvironment.md),[Download the SEUIF97](https://github.com/PySEE/SEUIF97)  

 * [PyThermo-IF97](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/PyThermo-IF97.ipynb)

    * IAPWS-IF97

    * Python library for IAPWS
    
    * SEUIF97
   
   * **Homework**

     * [Download the PyRankine](https://github.com/PySEE/SEUIF97)  
    
     * [ebook](./Reference.md)
   
       * Michael J . Moran. Fundamentals of Engineering Thermodynamics(7th Edition). John Wiley & Sons, Inc. 2011

* [PyThermo-IdealRankineCycle](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/PyThermo-IdealRankineCycle.ipynb)

   * the expression directly
   
   * List,Dict,Function

   * [MathJax,LaTeX](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/PyThermo-MathJax-LaTeX.ipynb)

  * **Homework**
    
     * Do [Practice 2](https://github.com/PySEE/Practices/tree/S2019/P2)  

* [08 CLASSES AND OBJECT-ORIENTED PROGRAMMING](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/08_CLASSES_AND_OBJECT-ORIENTED_PROGRAMMING.ipynb)

   * Abstract Data Types and Classes

   * Inheritance

   * Encapsulation and Information Hiding

   * Generators

* [11 PLOTTING AND MORE ABOUT CLASSES](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/11_PLOTTING_AND_MORE_ABOUT_CLASSES.ipynb)

   * **Matplotlib.pyplot**
    
     * `figure`, `plot`, `show`, (x,y), (y) 
     
     * line style and color: `'b-'`,`'ro'`
   
     * `title`,`xlabel`,`ylabel`,

     * type size and line width , `reParams`

     * `%matplotlib.pyplot inline`

  * **Examples**: IF97 T-S,H-S Diagram; The Rankine Cycle T-S  Diagrams

* **The General simulator of Rankine Cycle**

   * [The Object-oriented programming of Ideal Rankine Cycle](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/PyThermo-IdealRankineCycle.ipynb)

   * [The General simulator of Rankine Cycle](https://github.com/PySEE/PyRankine) 

     * [The CSV,JSON Representation of Rankine Cycle](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/PyThermo-CSV-JSON-RankineCycle.ipynb)

     * [JSON-Python](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/PyThermo-JSON-Python.ipynb)

     * [Python's Packages,Redirect stdout,glob](https://github.com/PySEE/PyRankine/step4)
  
   * **Homework**
  
     * Do [Practice 3](https://github.com/PySEE/Practices/tree/S2019/P3) 

   * [PyThermo-ReheatCycle-Optimization](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/PyThermo-ReheatCycle-Optimization.ipynb)

* [18 UNDERSTANDING EXPERIMENTAL DATA](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/18_UNDERSTANDING_EXPERIMENTAL_DATA.ipynb)

   * The Behavior of Springs： CSV File, Numpy's Linear Regression

   * The Behavior of Projectiles: Coefficient of Determination
 
* [21 LIES DAMNED LIES AND STATISTICS](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/21_LIES_DAMNED_LIES_AND_STATISTICS.ipynb)

   * It’s just as easy to **lie with numbers** as it is to lie with words
   
   * **Homework**

     * Do [Practice 4](https://github.com/PySEE/Practices/tree/S2019/P4)  

* [07 EXCEPTIONS AND ASSERTIONS](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/07_EXCEPTIONS_AND_ASSERTIONS.ipynb)

   * Built-In Exception, `try: except` 

   * Raising Exceptions: `raise`

   * User-defined Exceptions

   * `try:-except-else-finally`

   * Predefined Clean-up Actions:`with`

   * `assert` statement

* [06 TESTING AND DEBUGGING](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/06_TESTING_AND_DEBUGGING.ipynb)

   * Testing: test suite,Black-Box Testing,Glass-Box Testing,unit testing, integration testing

   * Debugging: bug:Overt,covert,Persistent,intermittent,dubugging process,`print`

   * The typical mistakes

* **Python's DevTools**

   * [unittest — Unit testing framework](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/DevTools_unittest.ipynb)

     * `unittest.TestCase`, test*，Asserting 

     * Test Fixtures:`Setup`,`tearDown`

     * Test Suites

     * `*args`，`**kwargs`

   * [doctest](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/DevTools_doctest.ipynb)

       * `doctest.testmod()`

   * [timeit](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/DevTools_timeit.ipynb)

       * `%time it`, `import timeit`

   * [Profilers](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/DevTools_Profilers.ipynb)

       * `cProfile.run`,pstats

       * `cProfile.Profile()`, `io` module

       * Improve the Performance: memoization, `__call__`
       
       * **Decorator**, **Property**,`@property`,Private Variables(`_`)

* [Version Control](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/DevTools_Git.ipynb)

   * [The Simple Guide to Git/Github](./guide/TheSimpleGuide2Github.md) 

   * **Homework**

     * [GCC for Windows](./guide/BuildingSoftwareEnvironment.md)

* [CPP_1_GCC_DLL](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/CPP_1_GCC_DLL.ipynb)

   * gcc/g++

     * C stdio.h: `scanf,printf`

   * GNU **Make**

   * the **Shared Library** 

* [CPP_2_DLL_Python](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/CPP_2_DLL_Python.ipynb)

   * Once-Only Headers

   * `ctypes`,`__cdecl`
  
   * **Homework**

     * Do [Practice 5](https://github.com/PySEE/Practices/tree/S2019/P5)

     * **Softwares**: SEUIF97 Dll, Office Excel 2013 above(64)

* [CPP_3_DLL_VBA_Python](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/CPP_3_DLL_VBA_Python.ipynb)

   * `__stdcall`,`windll.LoadLibrary`

   * Excel VBA 

   * **Homework**
    
     * [Install Ubuntu,GSL,Gnuplot](./guide/Ubuntu-Python-C-Chinese.md)

     * [Excel4Engineering](https://github.com/PySEE/Excel4Engineering)

* [CPP_4_GSL_GNUPLOT_Ubuntu](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/CPP_4_GSL_GNUPLOT_Ubuntu.ipynb)

   * [Ubuntu](./guide/Ubuntu-Python-C-Chinese.md)

   * GSL,Gnuplot
   
   * **Homework**

     * [Do Bonus](https://github.com/PySEE/Practices/tree/S2019/Bonus)

* **Appendix**

   * [Python35-Quick-Reference](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Python35-Quick-Reference.ipynb)

   * [1-Reading-and-Writing-Data-Files-Binary-Data-File](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/App-1-Reading-and-Writing-Data-Files-Binary-Data-Files.ipynb)

   * [2-GCC-GFortran)](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/App-2-GCC-GFortran.ipynb)
