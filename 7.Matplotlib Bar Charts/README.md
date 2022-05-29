# Matplotlib Bars

## Creating Bars

With Pyplot, you can use the `bar()` function to draw bar graphs

**Example**

```javascript

import matplotlib.pyplot as plt

import numpy as np

Xpoints = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G'])

Ypoints = np.array([45, 32, 67, 54, 78, 54, 54])

plt.bar(Xpoints, Ypoints)

plt.show()

```

**Result**

![app screenshot](https://github.com/Deshan555/Python-Matplotlib/blob/main/Screenshots/Chapter_07/Figure_1.png)

The `bar()` function takes arguments that describes the layout of the bars.

The categories and their values represented by the first and second argument as arrays.

```javascript

# The bar() function takes arguments that describes the layout of the bars.

import matplotlib.pyplot as plt

import numpy as np

Xpoints = ["Apples", "Bananas", "Oranges"]

Ypoints = [400, 600, 566]

plt.bar(Xpoints, Ypoints)

plt.show()

```

**Result**

![app screenshot](https://github.com/Deshan555/Python-Matplotlib/blob/main/Screenshots/Chapter_07/Figure_2.png)

## Horizontal Bars

If you want the bars to be displayed horizontally instead of vertically, use the `barh()` function:

```javascript

import matplotlib.pyplot as plt

import numpy as np

Xpoints = ["Apples", "Bananas", "Oranges"]

Ypoints = [400, 600, 566]

plt.barh(Xpoints, Ypoints, color = 'gray') # you can add bar colors using 'color' or 'c' keyword

plt.show()

```

**Result**

![app screenshot](https://github.com/Deshan555/Python-Matplotlib/blob/main/Screenshots/Chapter_07/Figure_4.png)

## Bar Width

The `bar()` takes the keyword argument width to set the `width` of the bars:

**Example**

```javascript
import matplotlib.pyplot as plt

import numpy as np

x = np.array(["A", "B", "C", "D"])

y = np.array([3, 8, 1, 10])

plt.bar(x, y, width = 0.1) # you can use width keyword for change the width of the bar

plt.show()

```

**Result**

![app screenshot](https://github.com/Deshan555/Python-Matplotlib/blob/main/Screenshots/Chapter_07/Figure_5.png)

## Bar Height

The `barh()` takes the keyword argument height to set the `height` of the bars:

**Example**

```javascript
# The bar() function takes arguments that describes the layout of the bars.

import matplotlib.pyplot as plt

import numpy as np

Xpoints = ["Apples", "Bananas", "Oranges"]

Ypoints = [400, 600, 566]

plt.barh(Xpoints, Ypoints, color = 'gray', height = 0.5) 

# you can add bar colors using 'color' or 'c' keyword

# you can change height of the bar using 'height' key word

plt.show()

```

**Result**

![app screenshot](https://github.com/Deshan555/Python-Matplotlib/blob/main/Screenshots/Chapter_07/Figure_4.png)

## Bar Color

The `bar()` and `barh()` takes the keyword argument color to set the color of the bars

**Example**


```javascript

import matplotlib.pyplot as plt

import numpy as np

Xpoints = ["Apples", "Bananas", "Oranges"]

Ypoints = [400, 600, 566]

plt.barh(Xpoints, Ypoints, color = 'gray') # you can add bar colors using 'color' or 'c' keyword

plt.show()

```

**Result**

![app screenshot](https://github.com/Deshan555/Python-Matplotlib/blob/main/Screenshots/Chapter_07/Figure_4.png)
