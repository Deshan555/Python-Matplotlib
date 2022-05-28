import matplotlib.pyplot as plt

import numpy as np

style = {'family':'serif', 'color':'blue', 'size':9}

Xpoints = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])

Ypoints = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.subplot(2, 1, 1)

plt.title('Plot Number 01', loc = 'left', fontdict = style)

plt.plot(Xpoints, Ypoints)

Xpoints = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])

Ypoints = np.array([240, 220, 260, 270, 480, 290, 330, 310, 320, 350])

plt.subplot(2, 1, 2)

plt.title('Plot Number 02', loc = 'left', fontdict = style)

plt.plot(Xpoints, Ypoints)

plt.suptitle("That Is Super Title (Suptitle)")

plt.show()