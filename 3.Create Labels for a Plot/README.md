# Matplotlib Labels and Title

## Create Labels for a Plot

With Pyplot, you can use the `xlabel()` and `ylabel()` functions to set a label for the x- and y-axis.

[**Example Code ➡️ example_1.py**](https://github.com/Deshan555/Python-Matplotlib/blob/main/3.Create%20Labels%20for%20a%20Plot/example_1.py)

```javascript

import matplotlib.pyplot as plt

import numpy as np

Xpoints = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])

Ypoints = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(Xpoints, Ypoints)

plt.xlabel("KM") # add lable for X axies

plt.ylabel("Speed Per KM") # add lable for Y axies

plt.show()

```
![Excepted Output](https://github.com/Deshan555/Python-Matplotlib/blob/main/Screenshots/Chapter_03/Figure_1.png)

## Create a Title for a Plot

With Pyplot, you can use the `title()` function to set a title for the plot.

[**Example Code ➡️ example_2.py**](https://github.com/Deshan555/Python-Matplotlib/blob/main/3.Create%20Labels%20for%20a%20Plot/example_2.py)

```javascript

import matplotlib.pyplot as plt

import numpy as np

Xpoints = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])

Ypoints = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(Xpoints, Ypoints)

plt.xlabel("KM") # add lable for X axies

plt.ylabel("Speed Per KM") # add lable for Y axies

plt.title("Speed Test For Rocket") # add title for plot 

plt.show()

```
![Excepted Output](https://github.com/Deshan555/Python-Matplotlib/blob/main/Screenshots/Chapter_03/Figure_2.png)

## Set Font Properties for Title and Labels

You can use the fontdict parameter in `xlabel()`, `ylabel()`, and `title()` to set font properties for the title and labels.

[**Example Code ➡️ example_3.py**](https://github.com/Deshan555/Python-Matplotlib/blob/main/3.Create%20Labels%20for%20a%20Plot/example_3.py)

```javascript

import matplotlib.pyplot as plt

import numpy as np

Xpoints = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])

Ypoints = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font_style_01 = {'family':'serif', 'color':'blue', 'size':20}

font_style_02 = {'family':'serif', 'color':'darkred', 'size':15}

plt.plot(Xpoints, Ypoints)

plt.xlabel("KM", fontdict = font_style_02) # add lable for X axies add properties

plt.ylabel("Speed Per KM", fontdict = font_style_02) # add lable for Y axies add properties

plt.title("Speed Test For Rocket", fontdict = font_style_01) # add title for plot add properties

plt.show()

```
![Excepted Output](https://github.com/Deshan555/Python-Matplotlib/blob/main/Screenshots/Chapter_03/Figure_3.png)

## Position the Title
You can use the loc parameter in `title()` to position the title.

Legal values are: **'left'**, **'right'**, and **'center'**. Default value is 'center'.

[**Example Code ➡️ example_4.py**](https://github.com/Deshan555/Python-Matplotlib/blob/main/3.Create%20Labels%20for%20a%20Plot/example_4.py)

```javascript

import matplotlib.pyplot as plt

import numpy as np

Xpoints = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])

Ypoints = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font_style_01 = {'family':'serif', 'color':'blue', 'size':12}

font_style_02 = {'family':'serif', 'color':'darkred', 'size':10}

plt.plot(Xpoints, Ypoints)

plt.xlabel("KM", fontdict = font_style_02) # add lable for X axies add properties

plt.ylabel("Speed Per KM", fontdict = font_style_02) # add lable for Y axies add properties

plt.title("Speed Test For Rocket", fontdict = font_style_01, loc = 'left') # add title for plot add properties

plt.show()

```
![Excepted Output](https://github.com/Deshan555/Python-Matplotlib/blob/main/Screenshots/Chapter_03/Figure_4.png)
