
import matplotlib.pyplot as plt

import numpy as np

dot_sizes = np.array([20, 50, 100, 200, 500, 1000, 60, 90, 10, 300, 600, 800, 75])

Xpoints = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 16])

Ypoints = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

plt.scatter(Xpoints, Ypoints, color = 'blue', s = dot_sizes)

plt.show()