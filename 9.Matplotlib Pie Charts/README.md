
# Matplotlib Pie Charts

## Creating Pie Charts

With Pyplot, you can use the `pie()` function to draw pie charts

**Example**

```javascript
import matplotlib.pyplot as plt

import numpy as np

Ypoints = np.array([35, 25, 25, 15])

plt.pie(Ypoints)

plt.show() 

```

**Result**

![appshots](https://github.com/Deshan555/Python-Matplotlib/blob/main/Screenshots/Chapter_09/Figure_1.png)


## Labels

Add `labels` to the pie chart with the label parameter.

The `label` parameter must be an array with one label for each wedge

```javascript

import matplotlib.pyplot as plt

import numpy as np

Ypoints = np.array([35, 25, 25, 15])

My_Lables = ['Apples', 'Bananas', 'Cherries', 'Dates']

plt.pie(Ypoints, labels = My_Lables)

plt.show()

```

**Result**

![appshots](https://github.com/Deshan555/Python-Matplotlib/blob/main/Screenshots/Chapter_09/Figure_2.png)

## Explode

Maybe you want one of the wedges to stand out? The `explode` parameter allows you to do that.

The `explode` parameter, if specified, and not None, must be an array with one value for each wedge.

Each value represents how far from the center each wedge is displayed:

for add show to explode use `shadow = True` parameter 

```javascript

import matplotlib.pyplot as plt

import numpy as np

Ypoints = np.array([35, 25, 25, 15])

My_Lables = ['Apples', 'Bananas', 'Cherries', 'Dates']

My_explode = [0.2, 0, 0, 0]

plt.pie(Ypoints, labels = My_Lables, explode = My_explode, shadow = True)

plt.show()

```
**Result**

![appshots](https://github.com/Deshan555/Python-Matplotlib/blob/main/Screenshots/Chapter_09/Figure_3.png)

## Legend

To add a list of explanation for each wedge, use the `legend()` function:

```javascript
import matplotlib.pyplot as plt

import numpy as np

Ypoints = np.array([35, 25, 25, 15])

My_Lables = ['Apples', 'Bananas', 'Cherries', 'Dates']

plt.pie(Ypoints, labels = My_Lables, startangle = 90)

plt.legend()

plt.show()

```

**Result**

![appshots](https://github.com/Deshan555/Python-Matplotlib/blob/main/Screenshots/Chapter_09/Figure_4.png)
