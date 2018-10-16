
# Foundamentals and Practice of Software Engineering with Python

* If you have concerns about the course, please email to me or open [the github issue](https://github.com/PySEE/home/issues). I value all suggestions.
 
  * Email: cmh@seu.edu.cn. 

## Goal

This course is intended to train **students majored in thermal energy engineering** in good software skills for producing code.

We will cover: 

* writing clean, testable, high quality code in Python
* interactive analysis and literate programming with the IPython Notebook
* a useful set of algorithmic and apply abstraction and decomposition to solve the complex problems
* computational tools to model and understand data(numpy, matplotlib, scipy)
* debug programs using a standardized approach
* write unit tests and evaluate software quality
* use version control 
* C/C++ programming with GCC

### Required Materials and Textbooks

* A laptop computer will be needed in the classroom.

* Guttag, John. Introduction to Computation and Programming Using Python: With Application to Understanding Data. MIT Press, 2016.

   * 陈光欣译. Python编程导论.  人民邮电出版社(第2版). 2018年2月1日

   * John V. Guttag. Introduction to Computation and Programming Using Python. Revised and expanded edition. MIT Press. 2013.08.  

      * 梁杰译. 编程导论. 人民邮电出版社(第1版) .  2015.03

   * https://mitpress.mit.edu/index.php?q=books/introduction-computation-and-programming-using-python-0

   * Accompanying Python3 Code：https://mitpress.mit.edu/sites/all/modules/patched/pubdlcnt/pubdlcnt.php?file=/sites/default/files/code-978-0-262-52962-4_0.zip&nid=321887

* Python 3 documentation. https://docs.python.org/3/

* Michael J . Moran. Fundamentals of Engineering Thermodynamics(7th Edition). John Wiley & Sons, Inc. 2011 

                       Principles of Engineering Thermodynamics(8th Edition. John Wiley & Sons, Inc. 2015

  * the ebook at SEU: http://www.lib.seu.edu.cn/ （查找资源->外文电子书->Wiley电子教材->T(工业技术)->TK(能源与动力工程)->TK1(热力工程,热机)）

* An Introduction to GCC  http://www.network-theory.co.uk/docs/gccintro/index.html.

* Scott Chacon，Ben Straub. Pro Git. https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control

## Contents

* [Lectures in Jupyter Notebook](https://github.com/PySEE/home/tree/S2018/notebook)

  Please install Jupyter to read and interactive with the notebook.

   **Online read-only versions：**

    > http://nbviewer.ipython.org/github/PySEE/home/tree/S2018/notebook/
 
* [Guide](https://github.com/PySEE/home/tree/S2018/guide)

   1. [Building Software Environment](https://github.com/PySEE/home/tree/S2018/guide/BuildingSoftwareEnvironment.md) 
    
   2. [Introduction to Markdown](https://github.com/PySEE/home/tree/S2018/guide/Introduction2Markdown.md)

## Course Grades

The Course graded on an 100 point scale and then weighted according to the following distribution:

  * In-class Exercises: 20%
  * **Practices(5):60%**, Bonus Points: +5
  * Final Exam: 20%
  
## [Practices(60)](https://github.com/PySEE/Practices/tree/S2018/)
    
  Please Visit **Practices** for details: https://github.com/PySEE/Practices/

  1. **Github**(5)：[Github、Git](https://github.com/PySEE/Practices/tree/S2018/P1)

  2. **Python and Interactive Computing**(15)：[The Simple Simulator of Rankine cycle](https://github.com/PySEE/Practices/tree/S2018/P2)
   
  3. **The Object-oriented Programming**(20)： [The General Simulator of Rankine cycle](https://github.com/PySEE/Practices/tree/S2018/P3)  
  
  4.  **Data Analysis**(15)：[Statistics, regression and visualization](https://github.com/PySEE/Practices/tree/S2018/P4)

  5.  **Unit Test**(5)：[IAPWS-IF97 physical properties calculation and unit test](https://github.com/PySEE/Practices/tree/S2018/P5)

  6. **Bonus Points**(+5): [C/C++ Programming with GCC, Ubuntu](https://github.com/PySEE/Practices/tree/S2018/Bonus) 

# Update Course

## Download the zip file of repository 

This repository contain all files of the course. You can manually download these files, 

![download](./guide/img/downloadhome.jpg)

## Using Git to clone a branch of repository to your computer 

We **recommend** that you use [git](https://github.com/git-for-windows/git/releases) to **clone** and **update** this repository.

After you have installed **git**, You may use the following **commands:**

#### clone a branch of repository:

* shallowly cloning the branch of repository for saving bandwidth
```bash
>git clone --depth 1 -b S2018 https://github.com/PySEE/home.git
```

This will create a folder **home** on your computer  with the files in subdirectories.

#### Updating to The Latest Version

As we release new files, or if we update an already released files, you'll have to update your repository.

You can do this by changing into the **home** directory and executing:

```bash
>git pull
```
That's it - you'll have the latest version of the repository.

![download](./guide/img/clonehomedir.jpg)

>you may also use any GUI git client to clone and update this repository, for example:  [Visual Studio Code](https://code.visualstudio.com/) ,or  [GitHub Desktop](https://desktop.github.com/)

## TIPS

We highly recommend you practice coding whenever you have a few minutes.

You **NEED** to **get your hands dirty** and **practice**

