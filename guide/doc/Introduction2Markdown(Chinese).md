# Markdown文档

## 1 简介

Markdown是一种轻量级「标记语言」.

Markdown文件是`纯文本`文档，不同于 `富媒体`文档，如Word、PowerPoint

* 内容字符

* 标志字符

Markdown的`常用标记符号`不超过十个，相对于其他复杂的标记语言，如：HTML来说，Markdown十分轻量，学习成本很低。

目前被越来越多领域的人使用，是互联网上最流行的写作语言。

* `软件文档`主要形式

  * Github中最常见的Markdown文档是仓库中的`README.md`

* Jupyter Notebook文档单元中的文本格式是Markdown
   
## 2 Markdown编辑

[Visual Studio Code 支持Markdown编辑](https://code.visualstudio.com/docs/languages/markdown/)

  * Visual Studio Code文档默认UTF-8编码，在其他软件中需用UTF-8编码打开.

Markdown是`纯文本`文档，不同于 `富媒体`的 `所见即所得` 文档，如Word、PowerPoint

* **Markdown文档 `撰写`、 `预览` 是分开的**

![](./img/vscode-markdown.jpg)


## 3 Markdown语法简要

### 3.1 标题

在Markdown中，如果一段文字被定义为标题：文字前加一个 # 号 和 一个空格。

    # 一级标题

    ## 二级标题

    ### 三级标题

# 一级标题

## 二级标题

### 三级标题

以此类推，总共六级标题

### 3.2 列表

#### 无序列表

无序列表的显示只需要在文字前加上 - 或 * 

    * 1AA
    * 3CA
    * 2BD

* 1AA
* 3CA
* 2BD

  
#### 有序列表

有序列表：在文字前加序号符号1. 2. 3; 序号符号和文字之间加上 **一个空格**.

    1. 1AA
    2. 3CA
    3. 2BD

1. 1AA
2. 3CA
3. 2BD


### 3.3 引用

如果需要引用一小段别处的句子，就要用引用格式。在文本前加入  > (大于号):

     > 这里是引用

引用显示效果如下：

> 这里是引用

### 3.4 链接与图片

#### 插入链接

```
 [东南大学](http://www.seu.edu.cn)
```

[东南大学](http://www.seu.edu.cn)

#### 插入图片

插入图片与插入链接与的语法很像，区别在加一个 ! 号

     ![Python Install](./img/python38-install-path.jpg)

![Python Install](./img/python38-install-path.jpg)

### 3.5 粗体与斜体

两个星号包含一段文本是粗体，一个星号包含一段文本是斜体，三个星号包含一段文本是粗斜体

例如：

    **这里是粗体**  

    *这里是斜体*

    ***这里是粗斜体***

**这里是粗体**  

*这里是斜体*

***这里是粗斜体***

### 3.6 表格

    | 序号 |课程         | 学分 |
    |:----:|:----------:|:----:|
    | 1    |  工程热力学 | 4 |
    | 2    |  流体力学  | 3 |


| 序号  |课程         | 学分 |
|:-----:|:----------:|:----:| 
| 1   |  工程热力学 | 4    |
| 2   |  流体力学   | 3    | 


### 3.7 代码框

如果要标记一小段**行内**代码，用 反引号` 把它包起来。

例如：
       
      学习Python的第一句：`print('Hello World!')`

学习Python的第一句:`print('Hello World!')`

如果是一个**代码块**，用两组3个连续的反引号```, 把代码包裹起来形成 **代码框** 

如果需要句法高亮，3个连续的反引号后加`语言`名称，
  
     ```codetype
         code block
     ```

如：python

        ```python
        x = 4  
        print("x= ",x)   
        ```


```python
x = 4  
print("x= ",x)   
```

如：cpp

      ```cpp
        #include <iostream>
        using namespace std;

        int main()
        {
            int x = 12;
            cout <<x%2<<endl; 
            return 0;
        }  
        ```

```cpp
#include <iostream>
using namespace std;

int main()
{
    int x = 12;
    cout <<x%2<<endl; 
    return 0;
}  
```

**常用codetype**

|codetype   |Language  |
|:---------:|:--------|
|python     | python language|
|cpp        | C++ language|
|c          | C language|
|json       | json content|
|dos        | DOS commands and programming|
|bash       | bash commands programming|
|shell      | Shell programming|


### 3.8 段落

通过在文本行之间留一个空白行，可创建新段落

### 3.9 分割线

分割线用三个 --- 号，例如：

     ---
     * 到这里，**Markdown**的基本语法就可以满足***日常***大部分文档要求了。

---
* 到这里，**Markdown**的基本语法就可以满足**日常**大部分文档要求了。


### 3.10 Markdown增强

Markdown格式没有统一标准，有多种增强格式，让你拥有飘逸的Markdown写作体验

[Markdown Preview Enhanced](https://shd101wyy.github.io/markdown-preview-enhanced/#/zh-cn/)是一款为 Visual Studio Code 编辑器编写的超级强大的 Markdown 插件。

如：

LaTex数学公式:$\color{blue}{y = ax^2 + bx + c}$

表情符号 :smile:  :car:

标志：==marked==

HTML: <font color=red>Test</font> , <span style="color:green;font-weight:700;font-size:20px">color font styles</span>

文本描述图形
```flow
start=>start: 开始
respondSuccess=>operation: 运行分析
end=>end: 结束

start->respondSuccess->end
```

