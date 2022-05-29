

import matplotlib.pyplot as plt

import numpy as np

Ypoints = np.array([35, 25, 25, 15])

My_Lables = ['Apples', 'Bananas', 'Cherries', 'Dates']

plt.pie(Ypoints, labels = My_Lables, startangle = 90)

plt.legend()

plt.show()