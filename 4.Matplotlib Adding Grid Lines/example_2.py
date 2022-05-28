
import matplotlib.pyplot as plt

import numpy as np

Xpoints = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])

Ypoints = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font_style_01 = {'family':'serif', 'color':'blue', 'size':12}

font_style_02 = {'family':'serif', 'color':'darkred', 'size':10}

plt.plot(Xpoints, Ypoints)

plt.xlabel("KM", fontdict = font_style_02) # add lable for X axies add properties

plt.ylabel("Speed Per KM", fontdict = font_style_02) # add lable for Y axies add properties

plt.title("Speed Test For Rocket", fontdict = font_style_01, loc = 'left') # add title for plot add properties

plt.grid(axis = 'x')

plt.show()