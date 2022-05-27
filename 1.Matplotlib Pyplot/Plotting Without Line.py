# o plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'.

import matplotlib.pyplot as plot 

import numpy

xpoint = numpy.array([1, 8])

ypoint = numpy.array([3, 10])

plot.plot(xpoint, ypoint, 'o')

plot.show()