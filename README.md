
# Python Matplotlib

## What is Matplotlib?

* Matplotlib is a low level graph plotting library in python that serves as a visualization utility.

* Matplotlib was created by John D. Hunter.

* Matplotlib is open source and we can use it freely.

* Matplotlib is mostly written in python, a few segments are written in C, Objective-C and Javascript for Platform compatibility.


## Table Of Content

- [Matplotlib Pyplot](https://linktodocumentation)

- [Matplotlib Plotting](https://linktodocumentation)

- [Matplotlib Markers](https://linktodocumentation)

- [Matplotlib Line](https://linktodocumentation)

- [Matplotlib Labels](https://linktodocumentation)

- [Matplotlib Grid](https://linktodocumentation)

- [Matplotlib Subplot](https://linktodocumentation)

- [Matplotlib Scatter](https://linktodocumentation)

- [Matplotlib Bars](https://linktodocumentation)

- [Matplotlib Histograms](https://linktodocumentation)

- [Matplotlib Pie Charts](https://linktodocumentation)



## Installation of Matplotlib

If you have Python and PIP already installed on a system, then installation of Matplotlib is very easy.

Install it using this command:

```bash
pip install matplotlib
```

## Import Matplotlib

Once Matplotlib is installed, import it in your applications by adding the import module statement:

```bash
import matplotlib
```

Now Matplotlib is imported and ready to use:

## Checking Matplotlib Version

The version string is stored under __version__ attribute.

```bash
import matplotlib

print(matplotlib.__version__)
```

## About Common Errors

I received the same error and I'm also in Python 3.6.0 

`[AttributeError: 'version_info' object has no attribute '__version__']`

If you want to dig a little more, you can type this in your console and detect which package is using this dependency.

```bash
pip show pyparsing
```
In my case the output was something like this, indicating that packaging:

```bash
Name: pyparsing
Version: 2.4.7
Summary: Python parsing module
License: MIT License
Location:
Requires:
Required-by: packaging
```

To fix it, you can go with the suggestion from PaulMcG

```bash

pip install pyparsing==2.4.7

```

