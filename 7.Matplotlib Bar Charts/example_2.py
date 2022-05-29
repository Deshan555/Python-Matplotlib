# The bar() function takes arguments that describes the layout of the bars.

import matplotlib.pyplot as plt

import numpy as np

Xpoints = ["Apples", "Bananas", "Oranges"]

Ypoints = [400, 600, 566]

plt.bar(Xpoints, Ypoints)

plt.show()