# The bar() function takes arguments that describes the layout of the bars.

import matplotlib.pyplot as plt

import numpy as np

Xpoints = ["Apples", "Bananas", "Oranges"]

Ypoints = [400, 600, 566]

plt.barh(Xpoints, Ypoints, color = 'gray', height = 0.5) 

# you can add bar colors using 'color' or 'c' keyword

# you can change height of the bar using 'height' key word

plt.show()