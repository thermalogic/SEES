## Course Outline

* **Introduction of PySEE**

  * Goals,Grading,Practices

  * [Building Software Environment](./guide/BuildingSoftwareEnvironment.md) 

  * **Course Repositories**: Home,SEUIF97,PyRrankine

  * **Homework**
   
     * Read the contents：Python, Jypyter, Markdown, Git, Github, Visual Studio Code

     * [Setup the working folder for the course](./guide/AdvWorkingDir.md)
     
     * [Install Softwares: Python,Jupyter,MinGW-W64,Visual Studio Code,Git](./guide/BuildingSoftwareEnvironment.md)

     * [Download the Home of PySEE, Using Juyter Notebooks of the course](https://github.com/PySEE/home)
   
     * [ebooks](./Reference.md)
   
       * John V. Guttag. Introduction to Computation and Programming Using Python: With Application to Understanding Data(Second Edition). MIT Press, 2016.

     * Do [Practice 1](https://github.com/PySEE/Practices/tree/S2019/P1)
   
* [PREFACE](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Lecture1-1-00_PREFACE.ipynb)

   * **Overview** Introduction to Computation and Programming Using Python

* [02 INTRODUCTION TO PYTHON](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Lecture1-2-02_INTRODUCTION_TO_PYTHON.ipynb)'

   * **Softwares**: Python Shell,IDLE,Jupyter,Visual Studio Code

   * **Python**: 
     
      * **The Basic Elements of Python**: Objects, Expressions, and Numerical Types; Variables and Assignment;
      
      * **Branching Programs** : `if-else `
     
      * **Strings and Input**: String, Slicing, Input, Unicode

      * **Iteration**:  `while `

      * **Python Developer's Guide**: The Zen of Python ,PEP20; Coding convention: PEP8
     
* [03 SOME SIMPLE NUMERICAL PROGRAMS](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Lecture1-3-03_SOME_SIMPLE_NUMERICAL_PROGRAMS.ipynb)
 
   * Exhaustive Enumeration
 
   * `For Loops`,`range(start,stop,step)`

   * Approximate Solutions and Bisection Search, Fancier Output Formatting, `str.format()` 

   * About Using Floats,`round(x, numDigits)`

   * Newton-Raphson

   * **Homework**
    
     * [Install Numpy,Scipy,Matplotlib](./guide/BuildingSoftwareEnvironment.md)

* [04 FUNCTIONS SCOPING AND ABSTRACTION](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Lecture1-4-04_FUNCTIONS_SCOPING_AND_ABSTRACTION.ipynb)

   * Functions and Scoping: Definitions,  Positional, Keyword Arguments and Default Values

   * Specifications, docstring

   * Recursion

   * Global Variables

   * Module, the interpreter search path, `sys.path`, Scipy

   * Files

* [05 STRUCTURED TYPES MUTABILITY AND HIGHERORDER FUNCTIONS](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Lecture1-5-05_STRUCTURED_TYPES_MUTABILITY_AND_HIGHERORDER_FUNCTIONS.ipynb)

   * Tuples, Multiple Assignment

   * **Lists**,  **Mutability**, Cloning, List Comprehension

   * Functions as Objects，Lambdas

   * Strings

   * **Dictionaries**,Mutability

   * **Homework**
    
     * [Install iapws](./guide/BuildingSoftwareEnvironment.md),[Download the SEUIF97](https://github.com/PySEE/SEUIF97)  

 * [PyThermo-IF97](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Lecture2-1-PyThermo-IF97.ipynb)

    * IAPWS-IF97

    * Python library for IAPWS
    
    * SEUIF97
   
   * **Homework**

     * [Download the PyRankine](https://github.com/PySEE/SEUIF97)  
    
     * [ebook](./Reference.md)
   
       * Michael J . Moran. Fundamentals of Engineering Thermodynamics(7th Edition). John Wiley & Sons, Inc. 2011

* [PyThermo-IdealRankineCycle](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Lecture2-2-PyThermo-IdealRankineCycle.ipynb)

   * the expression directly
   
   * List,Dict,Function

   * [MathJax,LaTeX](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Lecture2-3-PyThermo-MathJax-LaTeX.ipynb)

  * **Homework**
    
     * Do [Practice 2](https://github.com/PySEE/Practices/tree/S2019/P2)  

* [08 CLASSES AND OBJECT-ORIENTED PROGRAMMING](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Lecture3-1-08_CLASSES_AND_OBJECT-ORIENTED_PROGRAMMING.ipynb)

   * Abstract Data Types and Classes

   * Inheritance

   * Encapsulation and Information Hiding

   * Generators

* [11.1 PLOTTING USING MATPLOTLIB](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Lecture3-2-11-1_PLOTTING-USING-MATPLOTLIB.ipynb)

   * **Matplotlib.pyplot**
    
     * `figure`, `plot`, `show`, (x,y), (y) 
     
     * line style and color: `'b-'`,`'ro'`
   
     * `title`,`xlabel`,`ylabel`,

     * type size and line width , `reParams`

     * `%matplotlib.pyplot inline`

  * **Examples**: IF97 T-S,H-S Diagram; The Rankine Cycle T-S  Diagrams

* **The General simulator of Rankine Cycle**

   * [The Object-oriented programming of Ideal Rankine Cycle](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Lecture4-1-PyThermo-IdealRankineCycle-OOP.ipynb)

     * Computational thinking

   * [The General simulator of Rankine Cycle](https://github.com/PySEE/PyRankine) 

     * [The CSV,JSON Representation of Rankine Cycle](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Lecture4-2-PyThermo-CSV-JSON-RankineCycle.ipynb)

     * [JSON-Python](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Lecture4-4-PyThermo-JSON-Python.ipynb)

     * [Python's Packages,Redirect stdout,glob](https://github.com/PySEE/PyRankine/step4)
  
   * **Homework**
  
     * Do [Practice 3](https://github.com/PySEE/Practices/tree/S2019/P3) 

   * [PyThermo-ReheatCycle-Optimization](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Lecture4-4-PyThermo-ReheatCycle-Optimization.ipynb)

* [18 UNDERSTANDING EXPERIMENTAL DATA](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Lecture5-1-18_UNDERSTANDING_EXPERIMENTAL_DATA.ipynb)

   * The Behavior of Springs： CSV File 
   
       * Numpy: array,polyfit,Arithmetic Operations : elementwise

   * The Behavior of Projectiles: Coefficient of Determination
 
* [21 LIES DAMNED LIES AND STATISTICS](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Lecture5-2-21_LIES_DAMNED_LIES_AND_STATISTICS.ipynb)

   * It’s just as easy to **lie with numbers** as it is to lie with words
   
   * **Homework**

     * Do [Practice 4](https://github.com/PySEE/Practices/tree/S2019/P4)  

* [07 EXCEPTIONS AND ASSERTIONS](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Lecture6-1-07_EXCEPTIONS_AND_ASSERTIONS.ipynb)

   * Built-In Exception, `try: except` 

   * Raising Exceptions: `raise`

   * User-defined Exceptions

   * `try:-except-else-finally`

   * Predefined Clean-up Actions:`with`

   * `assert` statement

* [06 TESTING AND DEBUGGING](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Lecture6-2-06_TESTING_AND_DEBUGGING.ipynb)

   * Testing: test suite,Black-Box Testing,Glass-Box Testing,unit testing, integration testing

   * Debugging: bug:Overt,covert,Persistent,intermittent,dubugging process,`print`

   * The typical mistakes

* **Python's DevTools**

   * [unittest — Unit testing framework](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Lecture7-1-DevTools_unittest.ipynb)

     * `unittest.TestCase`, test*，Asserting 

     * Test Fixtures:`setUp`,`tearDown`

     * Test Suites

     * `*args`，`**kwargs`

   * [doctest](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Lecture7-2-DevTools_doctest.ipynb)
     
     * `import doctest`

   * [timeit](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Lecture7-3-DevTools_timeit.ipynb)

       * `%time it`, `import timeit`

   * [Profilers](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Lecture7-4-DevTools_Profilers.ipynb)

       * `cProfile.run`,pstats

       * `cProfile.Profile()`, `io` module

       * Improve the Performance: memoization, `__call__`
       
       * **Decorator**, **Property**,`@property`,Private Variables(`_`)

* [Version Control](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Lecture7-5-DevTools_Git.ipynb)

   * [The Simple Guide to Git/Github](./guide/TheSimpleStepsGithub(Chinese).md) 

   * **Homework**

     * [GCC for Windows](./guide/BuildingSoftwareEnvironment.md)

* [CPP_1_GCC_DLL](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Lecture8-1-CPP_1_GCC_DLL.ipynb)

   * gcc/g++, once-only headers

     * C stdio.h: `scanf,printf`

   * GNU **Make**

   * the **Shared Library** 
   
   * **Homework**

        * Do [Practice 5](https://github.com/PySEE/Practices/tree/S2019/P5)

* [CPP_2_DLL_Python](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Lecture8-2-CPP_2_DLL_Python.ipynb)

  * `ctypes`,`__cdecl`
  
  * **Softwares**: SEUIF97 Dll, Office Excel 2013 above(64)

* [CPP_3_DLL_VBA_Python](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Lecture8-3-CPP_3_DLL_VBA_Python.ipynb)

   * `__stdcall`,`windll.LoadLibrary`

   * Excel VBA 

   * **Homework**
    
     * [Install Ubuntu,GSL,Gnuplot](./guide/Ubuntu-Python-C-Chinese.md)

     * [Excel4Engineering](https://github.com/PySEE/Excel4Engineering)

* [CPP_4_GSL_GNUPLOT_Ubuntu](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Lecture8-4-CPP_4_GSL_GNUPLOT_Ubuntu.ipynb)

   * [Ubuntu](./guide/Ubuntu-Python-C-Chinese.md)

   * GSL,Gnuplot
   
   * **Homework**

     * [Do Bonus](https://github.com/PySEE/Practices/tree/S2019/Bonus)

* **Recap, Outlook**

  * [Python35-Quick-Reference](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/LectureApp-1-Python35-Quick-Reference.ipynb)
  
  * [Further Studing](./guide/FurtherStuding.md)     
  
* **Appendix**

   * [Python:Reading-and-Writing-Data-Files-Binary-Data-File](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/LectureApp-2-Reading-and-Writing-Data-Files-Binary-Data-Files.ipynb)

   * [Python: Stack Queues, Set)](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/LectureApp-3-Stack_Queues_Set.ipynb)

   * [Python: 11.2 Plotting Mortgages](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/LectureApp-4-11-2_Plotting_Mortgages.ipynb)

   * [GCC: GFortran)](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/LectureApp-5-GCC-GFortran.ipynb)

 

  