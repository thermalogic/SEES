
# Foundamentals and Practice of Software Engineering

Jupyter Notebook for Foundamentals and Practice of Software Engineering

* visit the Notebooks at [nbviewer](http://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/) 
      
 * run the Notebooks in a browser by pressing the Binder button： [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/PySEE/home/S2020) 

If you have concerns about the course, please email(cmh@seu.edu.cn) to me or open [the github issue](https://github.com/PySEE/home/issues). I value all suggestions.

## Overview

This course is intended to train **students majored in thermal energy engineering** become skillful at making productive use of computational techniques. 

We will cover: 

* write clean, testable, high quality code in [Python](https://www.python.org/)
* interactive analysis and literate programming with the [Jupyter Notebook](https://jupyter.org)
* apply [computational thinking](https://en.wikipedia.org/wiki/Computational_thinking) to model and solve the complex problems
* use **computational tools** to model and understand data [Numpy, Scipy, Matplotlib](https://www.scipy.org/)
* [debug programs](https://en.wikipedia.org/wiki/Debugging) using a standardized approach
* write [unit tests](https://en.wikipedia.org/wiki/Unit_testing) and analysis software performance
* C/C++ programming with [GCC](https://gcc.gnu.org/)，[GSL](https://www.gnu.org/software/gsl/) and [Gnuplot](http://www.gnuplot.info/)，
* C/C++ and Python programming in [Ubuntu](https://www.ubuntu.com/)
* Version control with [Git/Github](https://git-scm.com/) 

We emphasize breadth rather than depth on the these topics. The goal is to provide you with a brief introduction to more essential topics of computer knowledge and keep pace with the latest developments in computer technology in the short course. 

**[行是知之始，知是行之成 - 陶行知](http://yuedu.163.com/source/2963f558d8cc47dda31faa19c4e776e9_4)**

[Practices](https://github.com/PySEE/Practices/) are the very important part of the course. You will have to spend a lot of time and effort to do challenging enough practices.

We highly recommend you practice coding whenever you have a few minutes.

After successfully completing the course, We wish you have a broad spectrum of of computer knowledge and is a good programmer in the context of using computation to solve complex problems.

## Required Materials

* A laptop **computer** will be needed in the classroom.

* **[Softwares](./guide/BuildingSoftwareEnvironment.md)**

   * Python,Jupyter,NumPy,SciPy,Matplotlib,SEUIF97
   
   * Visual Studio Code,MinGW-W64(GCC),GSL,Gnuplot,Ubuntu
   
   * Git,Github
 
* **[Textbooks](./References.md)**

   * John V. Guttag. Introduction to Computation and Programming Using Python : With Application to Understanding Data(Second Edition). MIT Press, 2016.
  
   * Michael J. Moran. Fundamentals of Engineering Thermodynamics(7th Edition). John Wiley & Sons, Inc. 2011

## Contents

* **PySEE/HOME**
   
   * [Jupyter Notebook for the course](./notebook) 

      * [nbviewer](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/) 
      
      * [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/PySEE/home/S2019)

   * [Guide of Softwares](./guide) 

      * [Building Software Environment](./guide/BuildingSoftwareEnvironment.md) Python,Jupyter,SciPy,GCC,etc.

* [PySEE/SEUIF97](https://github.com/PySEE/SEUIF97) IAPWS-IF97 high-speed shared library (Windows32/64, Linux64); API: Python,C/C++,Excel VBA,MATLAB,Java,Fortran,C#

* [PySEE/PyRankine](https://github.com/PySEE/PyRankine) The step-by-step codes of the rankine cycle simulator from zero abstraction to the general abstraction 

* [PySEE/GSL4Windows](https://github.com/PySEE/GSL4Windows) The GNU Scientific Library(GSL) for Windows build with MinGW-W64(64) 

* [PySEE/Googletest4Windows](https://github.com/PySEE/Googletest4Windows) Googletest for Windows compiled with MinGW-W64(64) 

* [PySEE/Practices](https://github.com/PySEE/Practices) The information of practices: tasks, grading standards and submission(5 projects,1 Bonus) 

## Grading

The Course graded on an 100 point scale and then weighted according to the following distribution:

  * In-class Exercises: 20
  * [Practices:50](https://github.com/PySEE/Practices/)
  * Final Exam: 30

## Schedule and Structure

* The course schedule and structure are listed in the [**Outline**](./Outline.md)

## Readings and resources 

* Please visit [References](./References.md) and [Guide](./guide) for details

## Using the Notebooks of PySEE/home 

`download/clone` the repository to your computer,then start Jupyter to  **interactive** with the notebooks.

* Download the *PySEE/home* Repository  

  You can manually download the `home.zip` file of the `PySEE/home` to your computer

  ![download](./guide/img/downloadhome.jpg)

   >We **recommend** that you use [git](https://git-scm.com/) to clone and update the home repository
   >
   >**Cloning the S2020 branch of repository shallowly for saving bandwidth**
   >
   >```bash
   >git clone --depth 1 -b S2020 https://github.com/PySEE/home.git
   >```
   >**Updating to The Latest Version**
   >
   >```bash
   >git pull
   >```
   >

* Open the Notebooks of PySEE/home in Jupyter Notebook

   Unzip **home.zip**.In the sub-folder of **notebook** of home, double-click `StartNB.bat`(OS:Windows) or run the command:`jupyter notebook` in a terminal. This will open a web page in your browser with a list of the available notebooks.


