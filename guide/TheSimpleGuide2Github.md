## 建立本地项目git仓库并和远程Github仓库同步方法简介

**1** 本地安装git、远程建立github账户

**2** 配置Git本地用户名和email(和github账户一致）

**NOTE**: 所有git命名都必须是在本地所在目录下打开的终端中执行

```bash
>git config --global user.name  yourname
>git config --global user.email youremail
```

**3** 对本地项目所在目录用git进行版本控制

```bash
>git init
```

**4** 提交本地工作内容变化提交到git仓库

工作内容变化提交到暂存区

```bash
>git add .
```

存入暂存区修改内容提交至本地仓库
```bash
>git commit -m “your desc of the commit"
```

**5** 在github账户中建立一个和本地项目所在目录名 **一样** 的仓库

注意:是 **空** 仓库，不要有README.md

**6** 将远程github仓库加为本地git项目的远程源

```bash
>git remote add origin https://github.com/your-username/your-reponame.git     
```

**7** `首次`推送本地仓库到远程github仓库 

```bash
>git push -u origin master
```

**8** 本地仓库工作内容变化更新、同步到远程github

8.1 工作内容变化提交到暂存区

```bash
>git add .
```

8.2 存入暂存区修改内容提交至本地仓库

```bash
>git commit -m “your desc of the commit"
```

8.3 同步本地仓库内容远程github仓库

```bash
>git push
```

1，7工作完成后，仓库本地内容更新，推送到远程的工作就是8

9 持久化远程github账号:

本地全局存储持久化远程github账号，解决每次链接到github远程仓库都必须输入用户名和密码登陆的问题


Windows下
```bash
>git config --global credential.helper wincred
```

Linux:
```
$git config --global credential.helper 'store --file ~/.mygit-credentials'
```

### 参考：

**[1]** How to get started with GIT and work with GIT Remote Repo http://www3.ntu.edu.sg/home/ehchua/programming/howto/Git_HowTo.html

**[2]** Git Version Control in VS Code：   https://code.visualstudio.com/docs/editor/versioncontrol

  * 借助Visual Studio Code中，可不使用终端命令，在GUI下更方便地进行版本控制工作。
