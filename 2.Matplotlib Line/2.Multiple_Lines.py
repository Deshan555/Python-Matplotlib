# Draw two lines by specifiyng the x- and y-point values for both lines:

import matplotlib.pyplot as plot

import numpy as np

x1 = np.array([0, 1, 2, 3])

y1 = np.array([3, 8, 1, 10])

x2 = np.array([0, 1, 2, 3])

y2 = np.array([6, 2, 7, 11])

plot.plot(x1, y1, x2, y2)

plot.show()