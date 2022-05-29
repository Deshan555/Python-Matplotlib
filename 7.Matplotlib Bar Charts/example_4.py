import matplotlib.pyplot as plt

import numpy as np

x = np.array(["A", "B", "C", "D"])

y = np.array([3, 8, 1, 10])

plt.bar(x, y, width = 0.1) # you can use width keyword for change the width of the bar

plt.show()