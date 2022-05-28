
import matplotlib.pyplot as plt

import numpy as np

dot_sizes = np.array([20, 50, 100, 200, 500, 1000, 60, 90, 10, 300, 600, 800, 75])

colors_map = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

Xpoints = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 16])

Ypoints = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

# You can adjust the transparency of the dots with the alpha argument.

plt.scatter(Xpoints, Ypoints, c = colors_map, cmap='nipy_spectral' , s = dot_sizes, alpha = 0.5)

plt.title("Alfa Arguement Test")

plt.colorbar()

plt.show()