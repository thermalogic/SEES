## 建立本地项目的git仓库、和远程Github仓库同步方法简介

**1** 本地安装git、远程建立github账户

**2** 配置Git本地用户名和email(和github账户一致）

```bash
>git config --global user.name  yourname
>git config --global user.email youremail
```

**3** 将本地项目所在目录用git进行版本控制

```bash
>git init
```

**4** 提交本地项目中内容到git

```bash
>git commit -m “first commit"
```

**5** 在github账户中建立一个和本地项目所在目录名 **一样** 的仓库

注意:是 **空** 仓库，不要有README.MD

**6** 将远程github仓库加为本地git项目的远程源

```bash
>git remote add origin https://github.com/your-username/your-reponame.git     
```

**7**  推送本地仓库到github 

```bash
>git push
```

**8** 本地仓库内容更新、同步到远程github

```bash
>git commit -m “desc of the commit"
```

```bash
>git push
```

1，7工作完成后，仓库本地更新和推送到远程的工作就是8

**NOTE：** 这些工作在Visual Studio Code中可以更方便地完成

 ### 参考：

**[1]** How to get started with GIT and work with GIT Remote Repo http://www3.ntu.edu.sg/home/ehchua/programming/howto/Git_HowTo.html

 **[2]** Git Version Control in VS Code：   https://code.visualstudio.com/docs/editor/versioncontrol