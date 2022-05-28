
# compare plots

import matplotlib.pyplot as plt

import numpy as np

colors_map = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

#day one, the age and speed of 13 cars:

Xpoints = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 16])

Ypoints = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

# 'viridis' mean name of available pre build color map

plt.scatter(Xpoints, Ypoints, c = colors_map, cmap='nipy_spectral')

plt.xlabel("Age")

plt.ylabel("Speed")

plt.colorbar()

plt.show()

