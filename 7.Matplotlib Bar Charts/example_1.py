
import matplotlib.pyplot as plt

import numpy as np

Xpoints = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G'])

Ypoints = np.array([45, 32, 67, 54, 78, 54, 54])

plt.bar(Xpoints, Ypoints)

plt.show()