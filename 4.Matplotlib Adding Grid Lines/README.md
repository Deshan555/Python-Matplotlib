# Matplotlib Adding Grid Lines

## Add Grid Lines to a Plot

With Pyplot, you can use the `grid()` function to add grid lines to the plot.

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

plt.grid()

plt.show()

```
![output](https://github.com/Deshan555/Python-Matplotlib/blob/main/Screenshots/Chapter_04/Figure_1.png)

## Specify Which Grid Lines to Display

You can use the `axis` parameter in the `grid()` function to specify which grid lines to display.

Legal values are: `'x'`, `'y'`, and 'both'. Default value is 'both'.

Display only grid lines for the y-axis: [example_2.py]()

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

plt.grid(axis = 'x')

plt.show()

```
![output](https://github.com/Deshan555/Python-Matplotlib/blob/main/Screenshots/Chapter_04/Figure_2.png)

Display only grid lines for the y-axis: : [example_3.py]()

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

plt.grid(axis = 'y')

plt.show()

```
![output](https://github.com/Deshan555/Python-Matplotlib/blob/main/Screenshots/Chapter_04/Figure_3.png)

## Set Line Properties for the Grid

You can also set the line properties of the grid, like this: grid(color = 'color', linestyle = 'linestyle', linewidth = number).

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

plt.grid(color = 'blue', ls = '--', linewidth = 1)

plt.show()

```
![output](https://github.com/Deshan555/Python-Matplotlib/blob/main/Screenshots/Chapter_04/Figure_4.png)
