
## Foundamentals and Practice of Software Engineering with Python

If you have concerns about the course, please email(cmh@seu.edu.cn) to me or open [the github issue](https://github.com/PySEE/home/issues). I value all suggestions.
 
### Goal

This course is intended to train **students majored in thermal energy engineering** in good software skills for producing code.

We will cover: 

* writing clean, testable, high quality code in Python
* interactive analysis and literate programming with the IPython Notebook
* a useful set of algorithmic and apply abstraction and decomposition to solve the complex problems
* computational tools to model and understand data(numpy, matplotlib, scipy)
* debug programs using a standardized approach
* write unit tests and evaluate software quality
* C/C++ programming with GCC
* use version control 

### Required Materials

* A laptop **computer** will be needed in the classroom.

* **Softwares**(https://github.com/PySEE/home/blob/S2019/guide/Beginner2BuildeSoftwareEnvironment.md) 

   * Python, Jupyter, Numpy,Scipy,matplotlib,iapws,seuif97
   
   * GCC,Gnuplot
   
   * Git,Github
   
   * Visual Studio Code

* **Textbooks**(https://github.com/PySEE/home/blob/S2019/guide/References.md)

   * Guttag, John. **Introduction to Computation and Programming Using Python**
  
   * Michael J . Moran. **Thermodynamics**

   * Brian Gough. An Introduction to **GCC** - for the GNU compilers gcc and g++  

   * Scott Chacon，Ben Straub. Pro **Git**

### Contents

* [Lectures in Jupyter Notebook](https://github.com/PySEE/home/tree/S2019/notebook)

  Please install Jupyter to read and **interactive** with the notebook.

   **Online read-only versions：**    http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/
 
* [Guide](https://github.com/PySEE/home/tree/S2019/guide)

   1 [Building Software Environment](https://github.com/PySEE/home/tree/S2019/guide/BuildingSoftwareEnvironment.md) 
    
   2 [Introduction to Markdown](https://github.com/PySEE/home/tree/S2019/guide/Introduction2Markdown.md)

### Course Grades

The Course graded on an 100 point scale and then weighted according to the following distribution:

  * In-class Exercises: 20%
  * **Practices(5):60%**, Bonus Points: +5
  * Final Exam: 20%
  
### [Practices(60)](https://github.com/PySEE/Practices/tree/S2019/)
    
  Please Visit **Practices** for details: https://github.com/PySEE/Practices/

  1. **Basic Programming**(10)：[Github,Python,Jupyter,Markdown](https://github.com/PySEE/Practices/tree/S2019/P1)

  2. **Python and Interactive Computing**(15)：[The Simple Simulator of Rankine cycle](https://github.com/PySEE/Practices/tree/S2019/P2)
   
  3. **The Object-oriented Programming**(20)： [The General Simulator of Rankine cycle](https://github.com/PySEE/Practices/tree/S2019/P3)  
  
  4.  **Data Analysis**(10)：[Statistics, regression and visualization](https://github.com/PySEE/Practices/tree/S2019/P4)

  5.  **C/C++ Programming**(5)：[C/C++ Programming with MinGW-w64](https://github.com/PySEE/Practices/tree/S2019/P5)

  6. **Bonus**(+5): [C/C++ Programming with GCC, Ubuntu,Version Control ](https://github.com/PySEE/Practices/tree/S2019/Bonus) 

## Update Course

### Download the zip file of repository 

This repository contain all files of the course. You can manually download these files, 

![download](./guide/img/downloadhome.jpg)

### Using Git to clone a branch of repository to your computer 

We **recommend** that you use [git](https://github.com/git-for-windows/git/releases) to **clone** and **update** this repository.

After you have installed **git**, You may use the following **commands:**

#### clone a branch of repository:

* shallowly cloning the branch of repository for saving bandwidth
```bash
>git clone --depth 1 -b S2019 https://github.com/PySEE/home.git
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