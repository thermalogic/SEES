
# Foundamentals and Practice of Software Engineering

[![DOI](https://zenodo.org/badge/43438544.svg)](https://zenodo.org/badge/latestdoi/43438544)

* [The non-interactive preview on nbviewer](http://nbviewer.ipython.org/github/PySEE/home/tree/BEFE2021/notebook/) 

This course is intended to train **students in building environment and facilities engineering** become skillful at making productive use of computational techniques. 

We will cover: 

* write clean, testable, high quality code in [Python](https://www.python.org/)
* using [Numpy, Scipy, Matplotlib](https://www.scipy.org/) to model and understand data
* apply [Computational thinking](https://baike.baidu.com/item/计算思维) to model and solve the industrial process
* write [unit tests](https://baike.baidu.com/item/单元测试) 
* using [GCC and Make](https://gcc.gnu.org/) to build C/C++ applications
* version control with [Git/Github](https://git-scm.com/) 
* Introduction to [Linux/Ubuntu](https://www.ubuntu.com/)

We emphasize breadth rather than depth on these topics. The goal is to provide you with a brief introduction to more essential topics of computer knowledge and keep pace with the latest developments in computer technology in the short course. 

If you have concerns about the course, please email(cmh@seu.edu.cn) to me or open [the github issue](https://github.com/PySEE/home/issues). I value all suggestions.

**行是知之始，知是行之成 - 陶行知**

[Practices](https://github.com/PySEE/Practices/) are the very important part of the course. You will have to spend a lot of time and effort to do challenging enough practices.

We highly recommend you practice coding whenever you have a few minutes.

After successfully completing the course, We wish you have a broad spectrum of computer knowledge and is a good programmer in the context of using computation to solve complex problems.

## Required Materials

* A laptop **computer** will be needed in the classroom.

* **Softwares** : Python, GCC, Git, VS Code and WSL/Ubuntu etc.
   
* **Reference Textbooks**

   * John V. Guttag. [Introduction to Computation and Programming Using Python : With Application to Understanding Data(Second Edition)](https://mitpress.mit.edu/books/introduction-computation-and-programming-using-python-second-edition). MIT Press, 2016.
  
   * Neil Matthew, Richard Stones. [Beginning Linux Programming, 4th Edition](https://github.com/scnb/Beginning-Linux-Programming), Wiley Publishing, Inc., Indianapolis, Indiana,2008

## Contents

1. **PySEE/HOME**
   
   * [Jupyter Notebook for the course](./notebook) 

      * [The non-interactive preview on nbviewer](http://nbviewer.ipython.org/github/PySEE/home/tree/BEFE2021/notebook/) 

   * [Guide](./guide)  

      * [Building Software Environment](./guide/doc/BuildingSoftwareEnvironment.md) Python,Jupyter,SciPy,GCC,etc.

2. [PySEE/PySimVCR](https://github.com/PySEE/Practices) The demo vapor-compression refrigeration cycle simulator of steady-state

3. [PySEE/Practices](https://github.com/PySEE/Practices)  tasks, grading standards 

## Grading

The Course graded on the 100 point scale and then weighted according to the following distribution:

  * In-class Exercises: 10
  * [Practices:40](https://github.com/PySEE/Practices/)
  * Final Exam: 50

## Using the Notebooks of PySEE/home 

`download/clone` the repository to your computer,then start Jupyter to  **interactive** with the notebooks.

* Download the *PySEE/home* Repository  

  You can manually download the `zip` file of the `PySEE/home` to your computer

  ![download](./guide/doc/img/downloadhome.jpg)

* Using the Jupyter Notebooks of PySEE/home:  

   Unzip the **zip** file, then, in the sub-folder of **notebook** of home, double-click `nb.bat`(OS:Windows). This will open a web page in your browser with a list of the available notebooks.

>We **recommend** that you use [git](https://git-scm.com/) to clone and update the home repository
>
>**Cloning the BEFE2021 branch of repository shallowly for saving bandwidth**
>
>```bash
>git clone --depth 1 -b BEFE2021 https://github.com/PySEE/home.git
>```
>**Updating to The Latest Version**
>
>```bash
>git pull
>```

## Cite as

Cheng Maohua. (2020, March 13). PySEE/home: First Release of Courseware (Version V1.0.0). Zenodo. http://doi.org/10.5281/zenodo.3709440
