# 本地项目Git版本控制并同步到远程Github仓库的简单方法

初始环境：一个没有使用版本控制的本地目录。

<!-- TOC -->

- [本地项目Git版本控制并同步到远程Github仓库的简单方法](#本地项目git版本控制并同步到远程github仓库的简单方法)
  - [1 本地Git和远程Github版本控制的初始化](#1-本地git和远程github版本控制的初始化)
    - [1.1 本地安装Git、远程建立Github账户](#11-本地安装git远程建立github账户)
    - [1.2 配置Git本地用户名和email(和Github账户一致）](#12-配置git本地用户名和email和github账户一致)
  - [2  使用Git对本地项目进行版本控制](#2--使用git对本地项目进行版本控制)
    - [2.1  初始化本地项目的Git版本控制](#21--初始化本地项目的git版本控制)
    - [2.2 提交工作内容到Git仓库](#22-提交工作内容到git仓库)
      - [2.2.1 工作内容提交到缓存区](#221-工作内容提交到缓存区)
      - [2.2.2 存入缓存区的内容提交至本地仓库](#222-存入缓存区的内容提交至本地仓库)
  - [3 本地仓库的远程Github仓库初始化](#3-本地仓库的远程github仓库初始化)
    - [3.1 在Github账户中建立一个和本地项目目录`同名`的空仓库](#31-在github账户中建立一个和本地项目目录同名的空仓库)
    - [3.2 将远程Github仓库加为本Git项目的远程源](#32-将远程github仓库加为本git项目的远程源)
    - [3.3 `首次` 推送本地仓库到远程github仓库](#33-首次-推送本地仓库到远程github仓库)
  - [4 本地仓库工作内容变化更新、同步到远程github](#4-本地仓库工作内容变化更新同步到远程github)
    - [4.1 本地工作内容变化提交到暂存区](#41-本地工作内容变化提交到暂存区)
    - [4.2 存入暂存区内容提交至本地仓库](#42-存入暂存区内容提交至本地仓库)
    - [4.3 本地仓库推送到远程git仓库](#43-本地仓库推送到远程git仓库)
    - [4.4 Git本地和远程仓库操作过程图](#44-git本地和远程仓库操作过程图)
  - [5 持久化远程Github账号](#5-持久化远程github账号)
  - [6 创建分支](#6-创建分支)
    - [6.1 本地新建分支](#61-本地新建分支)
    - [6.2 切换到新分支](#62-切换到新分支)
    - [6.3 新分支发布到远程Git仓库](#63-新分支发布到远程git仓库)
  - [7 删除分支](#7-删除分支)
    - [7.1 删除本地分支](#71-删除本地分支)
    - [7.2 删除远程Git仓库中的分支](#72-删除远程git仓库中的分支)
  - [8 本地仓库使用多个远程仓库](#8-本地仓库使用多个远程仓库)
    - [8.1 添加一个远程仓库](#81-添加一个远程仓库)
    - [8.2 推送本地仓库内容到镜像仓库](#82-推送本地仓库内容到镜像仓库)
  - [9 Git GUI客户端](#9-git-gui客户端)
    - [9.1 Git GUI](#91-git-gui)
    - [9.2 it Version Control in VS Code](#92-it-version-control-in-vs-code)
  - [参考：](#参考)

<!-- /TOC -->

**NOTE**: 所有Git命令都须在用Git进行版本控制项目的目录下，打开的终端中执行

* open the terminal from the project directory, then run the git command.

## 1 本地Git和远程Github版本控制的初始化

对项目工作目录进行本地Git和远程Github版本控制需要做的初始化工作，只需做一次。

### 1.1 本地安装Git、远程建立Github账户

### 1.2 配置Git本地用户名和email(和Github账户一致）

Every git user should first introduce himself to git, by running these two commands:

```bash
>git config --global user.name  yourname
>git config --global user.email youremail
```

## 2  使用Git对本地项目进行版本控制

### 2.1  初始化本地项目的Git版本控制

```bash
>git init
```

### 2.2 提交工作内容到Git仓库

#### 2.2.1 工作内容提交到缓存区

```bash
>git add .
```

注意： add命令后面是：`空格` 加一个 `.`

#### 2.2.2 存入缓存区的内容提交至本地仓库

```bash
>git commit -m “your desc of the commit"
```

## 3 本地仓库的远程Github仓库初始化

### 3.1 在Github账户中建立一个和本地项目目录`同名`的空仓库

新建的Github仓库必须是 **空** 仓库，不能有README.md等任何内容

### 3.2 将远程Github仓库加为本Git项目的远程源

在本地Git仓库所在目录下打开的终端中执行：

```bash
>git remote add origin https://github.com/your-username/your-reponame.git   
```

> `origin`: 用户在Github建立远程仓库时，创建的指向这个远程仓库的`标签（名字）`

### 3.3 `首次` 推送本地仓库到远程github仓库 

在本地Git仓库所在目录下打开的终端中执行：

```bash
>git push -u origin master
```

> master: 在git仓库中创建的第一个branch

## 4 本地仓库工作内容变化更新、同步到远程github

在初始化了本地仓库的远程Github仓库后，本地Git仓库中的本地也 远程内容更新和同步工作如下：

### 4.1 本地工作内容变化提交到暂存区

```bash
>git add .
```

### 4.2 存入暂存区内容提交至本地仓库

```bash
>git commit -m “your desc of the commit"
```

### 4.3 本地仓库推送到远程git仓库

```bash
>git push
```

### 4.4 Git本地和远程仓库操作过程图 

   ![The process of Git](./img/TheProcessGit.jpg)

## 5 持久化远程Github账号

本地全局存储持久化远程Github账号，解决每次链接到github远程仓库都必须输入用户名和密码登陆的问题

Windows下
```bash
>git config --global credential.helper wincred
```
Linux:
```
$git config --global credential.helper 'store --file ~/.mygit-credentials'
```

## 6 创建分支

设创建分支：branch1

### 6.1 本地新建分支 

```bash
>git branch branch1 
```

### 6.2 切换到新分支

```bash
>git checkout branch1
```

### 6.3 新分支发布到远程Git仓库

```bash
>git push origin branch1 
```

## 7 删除分支 

设删除分支：betaBranch1

### 7.1 删除本地分支 

```bash
>git branch -d betaBranch1 
```

### 7.2 删除远程Git仓库中的分支

```bash
git push origin –delete betaBranch1 
```

## 8 本地仓库使用多个远程仓库

### 8.1 添加一个远程仓库

如使用码云(gitee.com)为本地`your-reponame`加一个远程仓库，在其中建立和本地项目目录`同名`的 **空** 仓库，不要有`README.md`等任何内容

使用命令，为本地仓库加这个远程仓库，并为其`命名`，比如`mirror`：

```
git remote add mirror https://gitee.com/your-username/your-reponame.git
```

### 8.2 推送本地仓库内容到镜像仓库

使用以下命令，可以推送(`push`)本地内容到远程镜像仓库的master分支：

```
git push mirror master
```

## 9 Git GUI客户端

### 9.1 Git GUI

在使用git的项目目录中打开终端，执行

```bash
>git gui
```

### 9.2 it Version Control in VS Code

![](./img/vscode-git.jpg)


## 参考：

* [1] [Version Control with Git](https://swcarpentry.github.io/git-novice/)

* [2] [How to get started with GIT and work with GIT Remote Repo](http://www3.ntu.edu.sg/home/ehchua/programming/howto/Git_HowTo.html)

* [3] [it Version Control in VS CodeGit Version Control in VS Code](https://code.visualstudio.com/docs/editor/versioncontrol)

