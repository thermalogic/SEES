#  MathJax使用LaTeX语法编写数学公式

MathJax是一款在网页显示数学公式的插件。Jupyter Notebook中的Makedown同样使用MathJax作为显示数学公式的插件。
* 参考：

   * [Latex](http://www.latex-project.org/)

  *  [MathJax](https://www.mathjax.org/)
  *  [老黄博客教程](http://iori.sinaapp.com/17.html) （本文档基于此网页版改编）

## 1．插入公式

LaTeX的数学公式有两种：行中公式和独立公式。

**行中公式**  放在文中与其它文字混编，

**独立公式**  单独成行。

* **行中公式**用:　```$数学公式$```

 例如：
```
   我们定义:$f(x) = \sum_{i=0}^{N}\int_{a}^{b} g(t,i) \text{ d}t$.
 ```

  我们定义: $f(x) = \sum_{i=0}^{N}\int_{a}^{b} g(t,i) \text{ d}t$.


* **独立公式**用: ```$$数学公式$$```

 例如：
```
$$J_\alpha(x) = \sum_{m=0}^\infty \frac{(-1)^m}{m! \Gamma (m + \alpha + 1)} {\left({ \frac{x}{2} }\right)}^{2m + \alpha}$$
```
显示：

$$J_\alpha(x) = \sum_{m=0}^\infty \frac{(-1)^m}{m! \Gamma (m + \alpha + 1)} {\left({ \frac{x}{2} }\right)}^{2m + \alpha}$$


## 2．上下标

^ 表示上标,
_ 表示下标。

如果上下标的内容多于一个字符，要用{}把这些内容括起来当成一个整体。上下标是可以嵌套的，也可以同时使用。

例如：
```
$x^{y^z}=(1+{\rm e}^x)^{-2xy^w}$
```
显示:

$x^{y^z}=(1+{\rm e}^x)^{-2xy^w}$

另外，如果要在左右两边都有上下标，可以用\sideset命令。

例如：
```
$\sideset{^1_2}{^3_4}\bigotimes$
```
显示：

$\sideset{^1_2}{^3_4}\bigotimes$  

## 3．括号和分隔符

()、[]和|表示自己，`\{\}`表示{}。

当要显示大号的括号或分隔符时，要用\left和\right命令。

例如：
```
$f(x,y,z) = 3y^2z \left( 3+\frac{7x+5}{1+y^2} \right)$
```

显示：

$f(x,y,z) = 3y^2z \left( 3+\frac{7x+5}{1+y^2} \right)$

有时,需要 \left. 或 \right. 进行匹配而不显示本身。

例如：
```
$\left.  \frac{{\rm d}u}{{\rm d}x} \right| _{x=0}$
```

显示：
$\left.  \frac{{\rm d}u}{{\rm d}x} \right| _{x=0}$

## 4．分数

例如：

```$\frac{1}{3}$```   显示：$\frac{1}{3}$


```$1 \over 3$```     显示：   $1 \over 3$

## 5  开方

例如：
```
$\sqrt{2}$

$\sqrt[n]{3}$
```

显示：

$\sqrt{2}$

$\sqrt[n]{3}$

## 6．省略号

数学公式中常见的省略号有两种:

 \ldots 表示与文本底线对齐的省略号;

 \cdots 表示与文本中线对齐的省略号。

例如：
```
$f(x_1,x_2,\ldots,x_n) = x_1^2 + x_2^2 + \cdots + x_n^2$

```
显示：

$f(x_1,x_2,\ldots,x_n) = x_1^2 + x_2^2 + \cdots + x_n^2$

## 矢量

例如：
```
$\vec{a} \cdot \vec{b}=0$
```
显示：

$\vec{a} \cdot \vec{b}=0$

## 8．积分

例如：
```
$\int_0^1 x^2 {\rm d}x$
```
显示：

$\int_0^1 x^2 {\rm d}x$

## 9．极限运算

例如：
```
$\lim_{n \rightarrow +\infty} \frac{1}{n(n+1)}$
```

显示：

$\lim_{n \rightarrow +\infty} \frac{1}{n(n+1)}$

## 10．累加、累乘运算

例如：
```
$\sum_{i=0}^n \frac{1}{i^2}　和　\prod_{i=0}^n \frac{1}{i^2}$
```
显示：

$\sum_{i=0}^n \frac{1}{i^2}　和　\prod_{i=0}^n \frac{1}{i^2}$

## 11．希腊字母

例如：
```
 \alpha　\beta　\gamma　\Gamma　\delta　\Delta　\epsilon　
 \varepsilon　　\zeta　\eta　\theta　\Theta　\vartheta
 \iota　\kappa　\lambda　\Lambda　\mu　\nu　
 \xi　\Xi　\pi　\Pi　\varpi　\rho　
 \varrho　\sigma　\Sigma　\varsigma　\tau　\upsilon　\Upsilon
 \phi　\Phi　\varphi　　\chi　X　\psi　\Psi　\omega　\Omega
```

显示：

$\alpha　\beta　\gamma　\Gamma　\delta　\Delta　\epsilon$

$\varepsilon　\zeta　\eta　\theta　\Theta　\vartheta$

$\iota　\kappa　\lambda　\Lambda　\mu　\nu$

$\xi　\Xi　\pi　\Pi　\varpi　　\rho$

$\varrho　\sigma　\Sigma　\varsigma　\tau　\upsilon　\Upsilon$

$\phi　\Phi　\varphi　\chi　\psi　\Psi　\omega　\Omega$

## 12．其它特殊字符

#### 关系运算符：

```$\pm$```  $\pm$

```$\times$``` $\times$

```$\div$```  $\div$

```$\mid$```  $\mid$

```$\nmid$```  $\nmid$

```$\cdot$```  $\cdot$

```$\circ$```  $\circ$

```$\ast$```  $\ast$

```$\bigodot$```  $\bigodot$

```$\bigoplus$```  $\bigoplus$

```$\leq$```  $\leq$

```$\geq$```  $\geq$

```$\neq$```  $\neq$

```$\approx$```  $\approx$

```$\equiv$```  $\equiv$

```$\sum$```  $\sum$

```$\prod$```  $\prod$

```$\coprod$```  $\coprod$

#### 集合运算符：

```$\emptyset$```  $\emptyset$

```$\in$```  $\in$

```$\notin$```  $\notin$

```$\subset$```  $\subset$

```$\supset$```  $\supset$

```$\subseteq$```  $\subseteq$

```$\supseteq$```  $\supseteq$

```$\bigcap$```  $\bigcap$

```$\bigcup$```  $\bigcup$

```$\bigvee$```  $\bigvee$

```$\bigwedge$```  $\bigwedge$

```$\biguplus$```  $\biguplus$

```$\bigsqcup$```  $\bigsqcup$

#### 对数运算符：

```$\log$```  $\log$

```$\lg$```  $\lg$

```$\ln$```  $\ln$

#### 三角运算符：

```$\bot$```  $\bot$

```$\angle$```  $\angle$

```$30^\circ$```  $30^\circ$

```$\sin$```  $\sin$

```$\cos$```  $\cos$

```$\tan$```  $\tan$

```$\cot$```  $\cot$

```$\sec$```  $\sec$

```$\csc$```  $\csc$

#### 微积分运算符：

```$\prime$```  $\prime$

```$\int$```  $\int$

```$\iint$```  $\iint$    

```$\iiint$```  $\iiint$

```$\iiiint$```  $\iiiint$

```$\oint$```  $\oint$

```$\lim$```  $\lim$

```$\infty$```  $\infty$

```$\nabla$```  $\nabla$

#### 逻辑运算符：

```$\because$```  $\because$

```$\therefore$```  $\therefore$

```$\forall$```  $\forall$

```$\exists$```  $\exists$

```$\not=$```  $\not=$

```$\not>$```  $\not>$

```$\not\subset>$```  $\not\subset$

#### 戴帽符号：

```$\hat{y}$```  $\hat{y}$

```$\check{y}$```  $\check{y}$

```$\breve{y}$```  $\breve{y}$

####连线符号：

```$\overline{a+b+c+d}$```  $\overline{a+b+c+d}$

```$\underline{a+b+c+d}$```  $\underline{a+b+c+d}$

```$\overbrace{a+\underbrace{b+c}_{1.0}+d}^{2.0}$```     $\overbrace{a+\underbrace{b+c}_{1.0}+d}^{2.0}$

#### 箭头符号：

```$\uparrow$```  $\uparrow$

```$\downarrow$```  $\downarrow$

```$\Uparrow$```  $\Uparrow$

```$\Downarrow$```  $\Downarrow$

```$\rightarrow$```  $\rightarrow$

```$\leftarrow$```  $\leftarrow$

```$\Rightarrow$```  $\Rightarrow$

```$\Leftarrow$```  $\Leftarrow$

```$\longrightarrow$```  $\longrightarrow$

```$\longleftarrow$```  $\longleftarrow$

```$\Longrightarrow$```  $\Longrightarrow$

```$\Longleftarrow$```  $\Longleftarrow$

#### 输出字符

空格　#　$　%　&　_　{　}　

用命令：　

```  ```   空  格

```$\#```   $\#$

```$\$$```   $\$$

```$\%$```   $\%$

```$\&$```   $\&$

```$\_$```   $\_$

```$\{$```   $\{$

```$\}$```  $\}$

#### 13．字体转换

要对公式的某一部分字符进行字体转换，可以用```{\rm ```需转换的部分字符}命令，其中,```\rm```可以参照下表选择合适的字体。一般情况下，公式默认为意大利体。

罗马体: ```$\rm ABC$```  $\rm ABC$

意大利体: ```$\it ABC$```  $\it ABC$

黑体: ```$\bf 123$```  $\bf 123$

花体: ```$\cal ABC$```  $\cal ABC$

等线体: ```$\sf ABC$```  $\sf ABC$

数学斜体: ```$\mit ABC$```  $\mit ABC$

打字机字体: ```$\tt ABC$```  $\tt ABC$　
