# Matplotlib Line

## Line Style

You can use the keyword argument `linestyle`, or shorter `ls`, to change the style of the plotted line:

```javascript

import matplotlib.pyplot as plot

import numpy as number_py

ypoints = number_py.array([3, 8, 1, 10])

# that line help to draw line ploatted line

plot.plot(ypoints, linestyle = 'dotted')

plot.show()

```

for add dashed lines simply use : `plt.plot(ypoints, linestyle = 'dashed')`

```javascript

import matplotlib.pyplot as plot

import numpy as number_py

ypoints = number_py.array([3, 8, 1, 10])

# that line help to draw dashed ploatted line

plot.plot(ypoints, linestyle = 'dashed')

plot.show()

```

```javascript

import matplotlib.pyplot as plt

import numpy as np

ploatted = np.array([3, 8, 1, 10])

plt.plot(ploatted, ls = ':')

plt.show()

```

## Shorter Syntax

The line style can be written in a shorter syntax:

linestyle can be written as `ls`

dotted can be written as `:`

dashed can be written as `--`

## Line Width

You can use the keyword argument linewidth or the shorter `lw` to change the width of the line.

The value is a floating number, in points:

```javascript

import matplotlib.pyplot as plot

import numpy as np

ypoints = np.array([3, 5, 8, 5, 8, 2])

plot.plot(ypoints, linewidth = '20.34', color = 'pink')

plot.show()

```

## Multiple Lines

You can plot as many lines as you like by simply adding more `plt.plot()` functions:


```javascript

import matplotlib.pyplot as plt

import numpy as np

line_1 = np.array([3, 8, 1, 10])

line_2 = np.array([6, 2, 7, 11])

plt.plot(line_1)

plt.plot(line_2)

plt.show()

```

You can also plot many lines by adding the points for the x- and y-axis for each line in the same plt.plot() function.

(In the examples above we only specified the points on the y-axis, meaning that the points on the x-axis got the the default values (0, 1, 2, 3).)

The x- and y- values come in pairs:

```javascript

# Draw two lines by specifiyng the x- and y-point values for both lines:

import matplotlib.pyplot as plot

import numpy as np

x1 = np.array([0, 1, 2, 3])

y1 = np.array([3, 8, 1, 10])

x2 = np.array([0, 1, 2, 3])

y2 = np.array([6, 2, 7, 11])

plot.plot(x1, y1, x2, y2)

plot.show()

```

## Line Color

You can use the keyword argument `color` or the shorter `c` to set the color of the line

```javascript
import matplotlib.pyplot as plt

import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, color = 'blue', ls = '--')

plt.show()
```
