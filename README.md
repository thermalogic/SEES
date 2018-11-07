
## Foundamentals and Practice of Software Engineering with Python

If you have concerns about the course, please email(cmh@seu.edu.cn) to me or open [the github issue](https://github.com/PySEE/home/issues). I value all suggestions.
 
### Goal

This course is intended to train **students majored in thermal energy engineering** in good software skills for producing code.

We will cover: 

* writing clean, testable, high quality code in [Python](https://www.python.org/)
* interactive analysis and literate programming with the [Jupyter Notebook](https://jupyter.org)
* training [computational thinking](https://en.wikipedia.org/wiki/Computational_thinking) to model and solve the complex problems
* **computational tools** to model and understand data [Numpy, Scipy,Matplotlib](https://www.scipy.org/)
* [debug programs](https://en.wikipedia.org/wiki/Debugging) using a standardized approach
* write [unit tests](https://en.wikipedia.org/wiki/Unit_testing) and evaluate software quality
* C/C++ programming with [GCC](https://gcc.gnu.org/)
* use [version control](https://git-scm.com/) 

### Required Materials

* A laptop **computer** will be needed in the classroom.

* **[Softwares](./guide/BuildingSoftwareEnvironment.md)**

   * Python, Jupyter,Numpy,Scipy,Matplotlib，Visual Studio Code,IAPWS,SEUIF97
   
   * GCC,GSL,Gnuplot
   
   * Git,Github
 
* **[Textbooks](./References.md)**

   * John V. Guttag. Introduction to Computation and Programming Using Python : With Application to Understanding Data(Second Edition). MIT Press, 2016.
  
   * Michael J . Moran. Fundamentals of Engineering Thermodynamics(7th Edition). John Wiley & Sons, Inc. 2011

### Contents

* [Lectures in Jupyter Notebook](./notebook)

  Please install Jupyter to read and **interactive** with the notebook.

   **Online read-only versions：**    http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/

* [Guide](./guide) Markdown,Git/Github,Ubuntu

   * [Software Environment](./guide/BuildingSoftwareEnvironment.md) Python,Jupyter,Scipy,GCC,etc.

* [SEUIF97](https://github.com/PySEE/SEUIF97) IAPWS-IF97 high-speed shared library (Windows32/64, Linux64); Python,Java,Excel Add-in Macro 

* [PyRankine](https://github.com/PySEE/PyRankine) The General Simulator of Rankine Cycle to Demonstrate:Data Structures+ Algorithms = Programs & Computational Thinking 

### Grading

The Course graded on an 100 point scale and then weighted according to the following distribution:

  * In-class Exercises: 15%
  * **Practices(5):65%**, Bonus: +5
  * Final Exam: 20%
  
### Practices(65)
    
https://github.com/PySEE/Practices/

  1. **Basic Programming**(15)：[Github,Python,Jupyter,MinGW-w64,Visual Studio Code，Markdown](https://github.com/PySEE/Practices/tree/S2019/P1)

  2. **Python and Interactive Computing**(15)：[The Simple Simulator of Rankine cycle](https://github.com/PySEE/Practices/tree/S2019/P2)
   
  3. **The Object-oriented Programming**(20)： [The General Simulator of Rankine cycle](https://github.com/PySEE/Practices/tree/S2019/P3)  
  
  4. **Data Analysis**(10)：[Statistics, regression and visualization](https://github.com/PySEE/Practices/tree/S2019/P4)

  5. **C/C++ Programming**(5)：[C/C++ Programming with MinGW-w64](https://github.com/PySEE/Practices/tree/S2019/P5)

  6. **Bonus**(+5): [C/C++ Programming with GCC, Ubuntu,Version Control ](https://github.com/PySEE/Practices/tree/S2019/Bonus) 

## Clone & Update Course

### Download the zip file of repository 

This repository contain all files of the course. You can manually download these files, 

![download](./guide/img/downloadhome.jpg)

### Using Git to clone a branch of repository to your computer 

We **recommend** that you use [git](https://git-scm.com/download/) to **clone** and **update** this repository.

After you have installed **git**, You may use the following **commands:**

#### clone a branch of repository:

shallowly cloning the S2019 branch of repository for saving bandwidth

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

# [行是知之始，知是行之成 - 陶行知](http://yuedu.163.com/source/2963f558d8cc47dda31faa19c4e776e9_4)

