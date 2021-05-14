
# Foundamentals and Practice of Software Engineering

[![DOI](https://zenodo.org/badge/43438544.svg)](https://zenodo.org/badge/latestdoi/43438544)

* [The non-interactive preview on nbviewer](http://nbviewer.ipython.org/github/PySEE/home/tree/B2021/notebook/) 

The branch **B2021** is intended to train **students in Building Environment and Energy Application Engineering** become skillful at computational techniques.

We will cover:

* [Python](https://www.python.org/)
* apply abstraction and decomposition to solve the complex problems 
* a useful set of algorithmic and data structure
* build C/C++ applications with [GCC and Make](https://gcc.gnu.org/) 
* version control with [Git](https://git-scm.com/) 
* introduction to [Linux](https://www.ubuntu.com/)

[Practices](https://github.com/PySEE/Practices/) are the very important part of the course. 

We highly recommend you practice coding whenever you have a few minutes.

* **行是知之始，知是行之成 - 陶行知**

* **项目驱动，边做边学**

If you have concerns about the course, please email(cmh@seu.edu.cn) to me. I value all suggestions.

## Required Materials

* A laptop **computer** will be needed in the classroom.

* **Softwares** : Python, GCC, Git, VS Code and WSL/Ubuntu etc.
   
* **Reference Textbooks**

  * John V. Guttag. [Introduction to Computation and Programming Using Python: With Application to Understanding Data(Second Edition)](https://mitpress.mit.edu/books/introduction-computation-and-programming-using-python-second-edition). MIT Press, 2016.

  * Neil Matthew, Richard Stones. [Beginning Linux Programming, 4th Edition](https://github.com/scnb/Beginning-Linux-Programming), Wiley Publishing, Inc., Indianapolis, Indiana,2008

## Contents

1. **PySEE/HOME**
   
   * [Jupyter Notebook for the course](./notebook) 
  
   * [Guide](./guide): [Install Software](./guide/doc/InstallSoftware.md),etc.

2. [PySEE/SimVCCE](https://github.com/PySEE/SimVCCE) The vapor-compression refrigeration cycle steady-state simulator in Python, C++ and Modelica

3. [PySEE/Practices](https://github.com/PySEE/Practices)  tasks

## Grading

The Course graded on the 100 point scale and then weighted according to the following distribution:

* In-class Exercises: 10
* [Practices:40](https://github.com/PySEE/Practices/)
* Final Exam: 50

## Using the Notebooks of PySEE/home 

`download/clone` the repository to your computer,then start Jupyter to  **interactive** with the notebooks.

* Download the *PySEE/home* Repository  

  You can manually download the `zip` file of the `PySEE/home` to your computer

* Using the Jupyter Notebooks of PySEE/home:  

   Unzip the **zip** file, then, in the sub-folder of **notebook** of home, double-click `nb.bat`(OS:Windows). This will open a web page in your browser with a list of the available notebooks.

>We **recommend** that you use [git](https://git-scm.com/) to clone and update the repository
>
>**Cloning the B2021 branch of repository shallowly for saving bandwidth**
>
>```bash
>git clone --depth 1 -b B2021 https://github.com/PySEE/home.git
>```
>**Updating to The Latest Version**
>
>```bash
>git pull
>```

## Cite as

Cheng Maohua. (2020, March 13). PySEE/home: First Release of Courseware (Version V1.0.0). Zenodo. http://doi.org/10.5281/zenodo.3709440
