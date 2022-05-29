
import matplotlib.pyplot as plt

import numpy as np

Ypoints = np.array([35, 25, 25, 15])

My_Lables = ['Apples', 'Bananas', 'Cherries', 'Dates']

My_explode = [0.2, 0, 0, 0]

plt.pie(Ypoints, labels = My_Lables, explode = My_explode, shadow = True)

plt.show()