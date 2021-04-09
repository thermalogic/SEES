
# Jupyter Notebook of the PySEE 

* [The non-interactive preview on nbviewer](http://nbviewer.ipython.org/github/PySEE/home/tree/B2021/notebook/) 

## [Introduction To Python](https://nbviewer.ipython.org/github/PySEE/home/tree/B2021/notebook/Unit1-1-Introduction_Python.ipynb)

* **Python**: The interpreted ,dynamically typed, scripting Language
   * Numerical Types, Operators and Expressions 
   * Variables and Assignment 
   * `print()` `input()`
   *  Comments：`#`
   * String, Slicing
   * Type Conversion
* Jupyter
   *  `magic` functions： `cell %%`, `line %`   
   *  `!`  Shell command
      
## [Control Flow](https://nbviewer.ipython.org/github/PySEE/home/tree/B2021/notebook/Unit1-2-Control_Flow.ipynb)

* `if`, `while loop`,`for loop`, `break`, `continue`

* `range(start,stop,step)`
     
* **Indentation**: delineate blocks of code
     
* Line Continuation: `() [] {}` , `\`

* `pass` as a placeholder
  
* **Python Style Guide**: The Zen of Python(`PEP20`); Coding convention(`PEP8`)

* Jupyter notebook extensions

## [Function, Module & Package](https://nbviewer.ipython.org/github/PySEE/home/tree/B2021/notebook/Unit1-3-Function_Module_Package.ipynb)

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

## [Tuple, Sequence unpacking](https://nbviewer.ipython.org/github/PySEE/home/tree/B2021/notebook/Unit1-4-1-Tuple.ipynb)

* (1,)  a,b=(1,2)

## [List,Range](https://nbviewer.ipython.org/github/PySEE/home/tree/B2021/notebook/Unit1-4-2-List.ipynb)

* List,List Comprehension

* mutability, object equality, aliasing, cloning: `L[:]` `copy()`, `deepcopy()`
      
* Sequence types(String,List,Tuple,Range): Operators and Functions

## [Dictionary](https://nbviewer.ipython.org/github/PySEE/home/tree/B2021/notebook/Unit1-4-3-Dict.ipynb)

* {key:value} ; mutability;  

* dict view objects

## [Files](https://nbviewer.ipython.org/github/PySEE/home/tree/B2021/notebook/Unit1-5-Files.ipynb)
   
* File

* Character Encoding, Unicode

* Table Data，CSV

# 2 Scipy

## [Plotting Using Matplotlib](https://nbviewer.ipython.org/github/PySEE/home/tree/B2021/notebook/Unit2-1-Plotting_Using_Matplotlib.ipynb)

* **Matplotlib.pyplot**
    
   * `figure`, `plot`, `show`, (x,y), (y)，

   * `title`,`xlabel`,`ylabel`,
   
   * write to file: png, svg
     
   * line style,color and width
   
   * type size

## [Understanding Examperimental Data](https://nbviewer.ipython.org/github/PySEE/home/blob/B2021/notebook/Unit2-2-Understanding_Experimental_Data.ipynb)

* The Behavior of Springs
   
* NumPy: polyfit

* The Behavior of Projectiles, Coefficient of Determination
 
## [Lies Namned Lies And Statictics](https://nbviewer.ipython.org/github/PySEE/home/tree/B2021/notebook/Unit2-3-Lies_Namned_Lies_And_Statictics.ipynb)

 * NumPy: genfromtxt, mean,var,corrcoef
   
 * Matplotlib: bar, subplot 

 * **It’s just as easy to `lie with numbers` as it is to lie with words**

## [LaTex Math](https://nbviewer.ipython.org/github/PySEE/home/tree/B2021/notebook/Unit2-A-LaTex_Math.ipynb)

## [Live_Interact_Plot](https://nbviewer.ipython.org/github/PySEE/home/tree/B2021/notebook/Unit2-B-Live_Interact_Plot.ipynb)

* Queue in Python

# 3 Class

## [Classes Object-Oriented Programming](https://nbviewer.ipython.org/github/PySEE/home/tree/B2021/notebook/Unit3-1-Classes_Object-Oriented_Programming.ipynb)

* `Computational thinking`

* Class, Inheritance

* Encapsulation and Information Hiding, Invisible `__name`

## [Exception  Assertion](https://nbviewer.ipython.org/github/PySEE/home/tree/B2021/notebook/Unit3-2-Exception_Assertion.ipynb)

* Built-In Exception, `try: except` `try:-except-else-finally`

* Raising Exceptions: `raise`

* User-defined Exceptions

* Predefined Clean-up Actions:`with`

*  `assert` statement

## [Iterator Generator](https://nbviewer.ipython.org/github/PySEE/home/tree/B2021/notebook/Unit3-A-Iterator_Generator.ipynb)

*  Iterator; `iter`, `__next__`

*  Generator：`yield`

* `%%timeit`
# 4 Refrigeration Cycle

## [Refrigeration Cycle](https://nbviewer.ipython.org/github/PySEE/home/tree/B2021/notebook/Unit4-1-RefrigerationCycle.ipynb)

* Modeling Simulation Engineering System

* Vapor-compression refrigeration cycle

## [Refrigeration Cycle Using OOP](https://nbviewer.ipython.org/github/PySEE/home/tree/B2021/notebook/Unit4-2-RefrigerationCycle_OOP.ipynb)

## [Refrigeration Cycle JSON](https://nbviewer.ipython.org/github/PySEE/home/tree/B2021/notebook/Unit4-A-RefrigerationCycle_json.ipynb)

* json
 
# 5 GCC and Make

## [GCC and MAKE](https://nbviewer.ipython.org/github/PySEE/home/tree/B2021/notebook/Unit5-1-GCC_Make.ipynb)

* GNU,GCC, GCC on Windows

* GNU **Make**
   
* C/C++ Preprocessor Directives, once-only headers 
   
## [GCC Library](https://nbviewer.ipython.org/github/PySEE/home/tree/B2021/notebook/Unit5-2-GCC_Library.ipynb)

* Static and Shared Library

## [GCC: C stdio](https://nbviewer.ipython.org/github/PySEE/home/tree/B2021/notebook/Unit5-A-C_stdio.ipynb)
 
* stdio.h: `scanf,printf`

## [Modern C++](https://nbviewer.ipython.org/github/PySEE/home/tree/B2021/notebook/Unit5-B-ModernCPP.ipynb)

* C++11 and above, std::tuple,std::vectors, std::unordered_map, std::any 

## [ctypes](https://nbviewer.ipython.org/github/PySEE/home/tree/B2021/notebook/Unit5-C-ctypes.ipynb)

* ctypes:  `__cdecl`,`cdll.LoadLibrary` 

* arrays,function

# 6  Version Control：Git

## [Version Control](https://nbviewer.ipython.org/github/PySEE/home/tree/B2021/notebook/Unit6-1-Git.ipynb)

* [The Simple Guide to Git/Github](./guide/doc/TheSimpleStepsGithub(Chinese).md)  

* Homework
   
   * [Install Windows Subsystem for Linux (WSL)](./guide/doc/GuideWSL(Chinese).md)
   
   * **Optional**: [Install Ubuntu](./guide/doc/Ubuntu-Python-CPP(Chinese).md)

# 7 Linux

## [Linux](https://nbviewer.ipython.org/github/PySEE/home/tree/B2021/notebook/Unit7-1-Linux.ipynb)

* Linux OS

## [Programming On Linux](https://nbviewer.ipython.org/github/PySEE/home/tree/B2021/notebook/Unit7-A-Programming_On_Linux.ipynb)

* C/C++, Python On Linux

* Shared Library on Linux