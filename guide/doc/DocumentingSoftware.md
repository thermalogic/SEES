
#  Documenting Software

## Why write docs

https://www.writethedocs.org/guide/writing/beginners-guide-to-docs/

## You will be using your code in 6 months

Code that you wrote 6 months ago is often `indistinguishable` from code that someone else has written.

If only I had written down why I had done this. Life would be so much simpler. Documentation allows you to transfer the why behind code. Much in the same way code comments explain the why, and not the how, documentation serves the same purpose.

### You want your code to be better

It’s really easy to have an idea in your head that sounds perfect, but the act of putting words to paper requires `a distillation of thought` that may not be so easy.

Writing documentation improves the design of your code. Talking through your API and design decisions on paper allows you to `think about them in a more formalized way`. A nice side effect is that it allows people to contribute code that follows your original intentions as well.


## Documenting Tools:

**Version controlled plain text**

As programmers we live in a world of `plain text`. Our documentation tooling should be no exception. We want tools that turn plain text into pretty HTML. We also have some of the best tooling available for tracking changes to files. 

There are a number of tools to build and maintain documentation. 

### Sphinx

[Sphinx](http://sphinx-doc.org/) is the most well-known documentation tool for Python. It uses files in the [reStructuredText](http://docutils.sourceforge.net/rst.html) markup format to create **HTML websites** and **PDF documents**. Running Sphinx could look like this:

```bash
>sphinx-build html
```
The strengths of Sphinx are that you can construct cross-references within your documentation easily, and that the Python syntax highlighting is one of the best. Finally, Sphinx runs **doctests** in your code.

### Mkdocs

[Mkdocs](http://www.mkdocs.org/) is a very young Python project for writing documentation which is undergoing rapid development. It uses **Markdown** as a markup language. [Markdown](http://daringfireball.net/projects/markdown/basics) is almost ridiculously simple (see an [interactive tutorial](http://markdowntutorial.com)). With Mkdocs you can compile a static HTML website from a folder with Markdown files. There are many templates to choose from and you can create your own easily. A very cool feature is that you can run a local documentation server with 

```bash
>mkdocs serve
```
and the local website is automatically updated as you edit the Markdown documents.

### Public Code Repositories

 [Github](https://github.com/) and [Bitbucket](https://bitbucket.org/) have their own mechanisms to display pages with documentation. These include rendering of ReST and Markdown documents (e.g. README files) and simple Wiki sites. 

### Readthedocs

[Readthedocs](https://readthedocs.org/) is a website hosting documentation for many programming projects. It can handle both the **Sphinx** and **Mkdocs** formats (ReST and Markdown, respectively). The nice thing about it is that you can connect Readthedocs to your Github or Bitbucket repository, so that every time you push new code to the repository, the documentation gets updated as well.

### Gitbook

If you want to publish your documentation as an e-book, [Gitbook](https://www.gitbook.com/) is the tool of choice. It uses Markdown files plus a file with the table of contents to build your book as HTML, PDF, EPUB and MOBY. Gitbook provides its own editor, so you can write a book without knowing anything about e-books, about git or about programming. 

Gitbook is a great way to publish free technical documentation and training material.

