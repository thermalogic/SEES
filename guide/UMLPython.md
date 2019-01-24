
# Creating UML diagrams for Python code

## 1 Softwares

### 1.1 Creating UML diagram for Python code

Pylint is shipped with Pyreverse which creates UML diagram for python code

```bash
python -m pip install pylint
```

**pyreverse** can generates the UML diagrams in all formats that [graphviz/dot](https://en.wikipedia.org/wiki/DOT_(graph_description_language)) knows, or in VCG

Here, we use the [graphviz/dot](https://en.wikipedia.org/wiki/DOT_(graph_description_language)) format file as the output.

### 1.2 Graph Visualization of UML diagram in the `dot` format

#### 1.2.1 graphviz

[Graphviz](http://www.graphviz.org/) is open source graph visualization software. Graph visualization is a way of representing structural information as diagrams of abstract graphs and networks.

#### 1.2.2 VS Code extension of Graphviz(dot)

[João Pinto: Graphviz(dot) language support for Visual Studio Code](https://github.com/joaompinto/vscode-graphviz)

```bash
ext install joaompinto.vscode-graphviz
```

## 2 Generation of UML diagrams with Pyreverse

Pyreverse analysis Python code and extracts UML class diagrams and package depenndencies.

Pyreverse builds a diagram representation of the source code with:

* class attributes, if possible with their type
* class methods
* inheritance links between classes
* association links between classes
* representation of Exceptions and Interfaces

The Usage of `pyreverse` is:

```bash
>pyreverse [options] <packages>
```

If we want to generate the UML class diagrams in `dot` format files of Python packages or modules

```bash
pyreverse -o dot  python-package/module-name
```

**pyreverse** will creates one or two dot format files:

* classes.dot : UML Classes diagrams
* packages.dot: UML Classes Association diagrams  

The [PyRankine/step5](https://github.com/PySEE/PyRankine/tree/master/step5) is used as the example  
to show the usage of `Pyreverse` 

```
PyRankine
 │
 ├──step5
 │    │
 │    ├──components   
 │    │      
 │    ├──cyclefiles
 │    │        
 │    |── rankine_cycle.py
 │    │
 │    |── rankine.py
```     

### 2.1 Generating the UML diagrams of a Python package

* A Python package must has the file `__init__.py`

Example: Generating the UML diagrams of `components` package

In the parent folder of `components` package: `/step5/` , run the command:

```bash
> pyreverse -o dot components/
```

Two dot files are created in the folder `/step5/`

* classes.dot, packages.dot 

### 2.2 Generating the UML diagrams of the Python modules(files)

Example 1: Generating the UML diagrams of `rankine_cycle.py`

In the folder `./step5/`, run the command:

```bash
> pyreverse -o dot rankine_cycle.py
```

The dot file is generated in the folder `/step5/`

* classes.dot: 

Example2 : Generating the UML diagrams of `rankine_cycle.py` and `rankine.py`

In the folder `./step5/`, run the command:

```bash
pyreverse -o dot rankine.py rankine_cycle.py
```
The two dot files are generated in the folder `./step5/`
* classes.dot, packages.dot  

### 2.3 Generating the UML diagrams of the Python Projects

#### 2.3.1 Add `__init__.py` in the root folder of the Python Projects

 Example: `./step5/__init__.py`

 then,`step5` is a Python package analysis by pyreverse

### 2.3.2 Generating the UML diagrams of the Python Projects 

In the parent folder `PyRankine` of `step5`,run the command:

```
pyreverse -o dot step5/
```

The two dot files are generated in the folder `./Pyrankine/`

## 3 The Simple Python interface for Graphviz

https://graphviz.readthedocs.io

Install

```bash
python -m pip install graphviz
```
To render the generated DOT source code, you need to install [Graphviz](https://www.graphviz.org/download/e).

Make sure that the directory containing the **dot** executable is on your systems' path.

```python
from graphviz import Source
Source.from_file("./img/classes.dot")
```
