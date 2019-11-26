#  OpenModelica and Jupyter OpenModelica Kernel

https://github.com/OpenModelica/jupyter-openmodelica

An OpenModelica Kernel for Jupyter Notebook. All commands are interpreted by OMPython which communicates with OpenModelica Compiler and the result is presented to user.

This requires [Jupyter Notebook](https://jupyter.org), [OpenModelica](https://openmodelica.org), and [OMPython](https://github.com/OpenModelica/OMPython) to be installed.

## Install for Windows

### 1 Install OpenModelica 

Download the latest [OpenModelica](https://openmodelica.org),thn install

### 2 Make sure the environment variable for OpenModelica 

Make sure the environment variable for OpenModelica is set e.g.:

`OPENMODELICAHOME=C:/OpenModelica1.13.264bit/` or similar.

![OpenModelica](./img/openmodelica-variable.jpg)

### 3 Install OMPython 

Install the version as packaged with your OpenModelica installation by running:
```
cd %OPENMODELICAHOME%\share\omc\scripts\PythonInterface
python -m pip install -U .
```

### 4 Install Jupyter OpenModelica Kernel

1. clone the project

2. cd jupyter-openmodelica

3. python setup.py install

## 5 Using OpenModelica Kernel

To use it, run:
```
>jupyter notebook
```
In the notebook interface, select` OpenModelica` from the 'New' menu