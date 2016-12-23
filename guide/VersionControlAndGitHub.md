## Version Control、GIT and Github

## Why version Control?
 
 * **Keep copies of multiple states of files**   
  By committing you record a state of the file to which you can go back any time.
 * **Create alternative states**  
 Imagine you just want to try out something, but you realize you have to modify multiple files. You're not sure whether it works or is worth it. With version control you can just create a **branch** where you can experiment or develop new features without changing the main or other branches.
 * **Collaborate in teams**   
 Nobody wants to send code via e-mail or share via Dropbox. If two people work on a file at the same time it's unclear how to merge the code. Version control lets you keep your code in a shared central location and has dedicated ways to merge and deal with conflicts. 
 * **Keep your work safe**  
 Your hard drive breaks. Your computer is stolen. But your code is safe because you store it not only on your computer but also on a remote server. 
 * **Share**  
 You developed something awesome and want to share it. But not only do you want to make it available, you're also happy about contributions from others! 



### Types of Version Control: Central Repository

![Version Control with Central Repository](./img/vc-centralized.png)

 * Everybody needs to write to one server
 * All operations (history, commit, branches) require server connection
 * The traditional model: CVS, SVN, etc. 
 * Pros: 
   * Simple
 * Cons: 
   * Complex for larger and community projects
        * Who is allowed to write? 
        * How do you apply changes that someone outside your team made? 
        


### Types of Version Control: Distributed Version Control


![Distribute Version Control](./img/vc-distributed.png)

 * Everybody has a full history of the repository locally
 * No dedicated server - every node is equal.
   * In practice: often server is used for one "official" copy of code.
    But: server by convention only, no technical difference.
 * Pros: 
    * No access issues
        * Make a copy and hack away
        * Ask if partner wants to accept your changes
    * Everything is local
        * Fast!
        * No internet connection required
        * Commit often model (once per feature) - don't sync all the time.
 * Cons:
    * Extra effort to distinguish between committing and pushing/pulling (synchronizing). 

### Implementations

 * Centralized
    * CVS
    * SVN
    * Team Foundation Server 
    * ...
 * Distributed
    * git
    * Mercurial
    * ...
 * We will be using git in this lecture. 
 
### git

 * Created by Linus Torvalds, 2005
 * Meaning: British English slang roughly equivalent to "unpleasant person". 
 * git – the stupid content tracker.

*I'm an egotistical bastard, and I name all my projects after myself. First 'Linux', now 'git'. -- Linus Torvalds*

### Why git?

 * Popular (~50% of open source projects)
 * Truly distributed
 * Very fast
 * Everything is local
 * Free
 * Safe against corruptions
 * GitHub!
 
### git model 
 
A git repository is essentially a large graph.

![git sketch](./img/git_user_server_interaction.jpg)

### GitHub

GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.

This tutorial teaches you GitHub essentials like repositories, branches, commits, and Pull Requests. You’ll create your own Hello World repository and learn GitHub’s Pull Request workflow, a popular way to create and review code.

https://guides.github.com/activities/hello-world/

### Git Client

* **GitHub Desktop** 
  [Download here](https://desktop.github.com/)
  
* **EGit In Eclipse** 
  If you have installed Eclipse, EGit is ready for you
  
 

We strongly recommend that you use version control for your projects. 
## Reference:

* Maximilian Koegel,Jonas Helming. EGit Toturial http://eclipsesource.com/blogs/tutorials/egit-tutorial/    2015.02

* Scott Chacon，Ben Straub. Pro Git. https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control

* 廖雪峰. Git教程  http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000

* 知乎：怎样使用GitHub. http://www.zhihu.com/question/20070065