---
title: Installing and Using Quarto
---

Unless you plan to generate your problem set solutions on the SCF, you'll need to [install Quarto](https://quarto.org/docs/get-started/).

Once installed, you should be able to run commands such as `quarto render FILE` and `quarto preview FILE` from the command line.

To render to PDF, you'll need a LaTeX engine installed. A good minimal solution if don't already have LaTeX installed (e.g., via MicTeX in Windows or MacTeX on MacOS) is to install `tinytex`: `quarto install tinytex`.

Quarto also runs from the Windows Command shell or PowerShell. We'll add details/troubleshooting tips here (or in the [lab 1](../labs/lab1.html)  materials) as needed.

`quarto convert` converts back and forth between the Jupyter notebook (.ipynb) and Quarto Markdown (.qmd) formats.

By default, quarto uses Jupyter to process code chunks. This works well generally, but you can't have different chunks that use different languages in the same document (e.g., some chunks in Python and some in bash or R). In that case, you can use the R-based `knitr` package to do the processing. To do so, add `engine: knitr` to the YAML metadata at the top of the file (if you happen to have an `execute` stanza, you'll need to have `engine: knitr` nested within that stanza). For the `knitr` engine, you'll need to have R installed on your computer, with the `rmarkdown` R package installed. And if you have Python chunks, you'll also need the `reticulate` R package.

For Python chunks when using the default `jupyter` engine, if you want all output from multiple commands in a chunk to be printed (without explicitly using `print()`), you can add the following syntax to the YAML metadata at the top of the file. (Note that, unfortunately, the output will be printed out below the code chunk rather than interspersed with the code, as that is how Jupyter notebooks chunks work.)

```
ipynb-shell-interactivity: all
```

