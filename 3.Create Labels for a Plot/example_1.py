
import matplotlib.pyplot as plt

import numpy as np

Xpoints = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])

Ypoints = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(Xpoints, Ypoints)

plt.xlabel("KM") # add lable for X axies

plt.ylabel("Speed Per KM") # add lable for Y axies

plt.show()