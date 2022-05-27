
# Matplotlib Plotting

## Plotting x and y points

- The plot() function is used to draw points (markers) in a diagram.

- By default, the plot() function draws a line from point to point.

- The function takes parameters for specifying points in the diagram.

- Parameter 1 is an array containing the points on the x-axis.

- Parameter 2 is an array containing the points on the y-axis.

- If we need to plot a line from (1, 3) to (8, 10), we have to pass two arrays [1, 8] and [3, 10] to the plot function.

**Example**

Draw a line in a diagram from position (1, 3) to position (8, 10):

```bash
import matplotlib.pyplot as plt

import numpy as np

xpoints = np.array([1, 8])

ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)

plt.show()

```
![Output](https://github.com/Deshan555/Python-Matplotlib/blob/main/1.Matplotlib%20Pyplot/Figure_1.png)

## Marker reference

Matplotlib supports multiple categories of markers which are selected using the marker parameter of plot commands:

- [Unfilled markers](https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html#unfilled-markers)

- [Filled markers](https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html#filled-markers)

- [Markers created from TeX symbols](https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html#markers-created-from-tex-symbols)

- [Markers created from Paths](https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html#markers-created-from-paths)

For a list of all markers see also the **matplotlib.markers** documentation.

For example usages see Marker examples.

```bash

import matplotlib.pyplot as plt

from matplotlib.lines import Line2D


text_style = dict(horizontalalignment='right', verticalalignment='center',
                  fontsize=12, fontfamily='monospace')

marker_style = dict(linestyle=':', color='0.8', markersize=10,
                    markerfacecolor="tab:blue", markeredgecolor="tab:blue")


def format_axes(ax):

    ax.margins(0.2)

    ax.set_axis_off()

    ax.invert_yaxis()


def split_list(a_list):

    i_half = len(a_list) // 2

    return a_list[:i_half], a_list[i_half:]

```

## Unfilled markers

Unfilled markers are single-colored.

```bash

fig, axs = plt.subplots(ncols=2)

fig.suptitle('Un-filled markers', fontsize=14)

# Filter out filled markers and marker settings that do nothing.
unfilled_markers = [m for m, func in Line2D.markers.items()
                    if func != 'nothing' and m not in Line2D.filled_markers]

for ax, markers in zip(axs, split_list(unfilled_markers)):

    for y, marker in enumerate(markers):
        
        ax.text(-0.5, y, repr(marker), **text_style)
        
        ax.plot([y] * 3, marker=marker, **marker_style)
    
    format_axes(ax)

plt.show()

```
![Expected Output: ](https://matplotlib.org/stable/_images/sphx_glr_marker_reference_001.png)

[**Use that Marker Referance ➡️ marker_reference.py**](https://github.com/Deshan555/Python-Matplotlib/blob/main/1.Matplotlib%20Pyplot/marker_reference.py)


## Multiple Points

You can plot as many points as you like, just make sure you have the same number of points in both axis.

Example : ``

```bash

import matplotlib.pyplot as plot

import numpy

xpoint = numpy.array([1, 2, 6, 8])

ypoint = numpy.array([3, 8, 1, 10])

plot.plot(xpoint, ypoint)

plot.show()

```

**Output**

![Expected Output: ](https://github.com/Deshan555/Python-Matplotlib/blob/main/1.Matplotlib%20Pyplot/Figure_3.png)

## Default X-Points

If we do not specify the points in the x-axis, they will get the default values 0, 1, 2, 3, (etc. depending on the length of the y-points.

So, if we take the same example as above, and leave out the x-points, the diagram will look like this:

```bash

import matplotlib.pyplot as plt

import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)

plt.show()

```

**Output**

![Expected Output: ](https://github.com/Deshan555/Python-Matplotlib/blob/main/1.Matplotlib%20Pyplot/Figure_2.png)
