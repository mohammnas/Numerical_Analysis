import numpy as np
from matplotlib import pyplot as plt


#   Each array represents the number of parts [-1,1] is
#   broken into
whole = np.linspace(-1,1,2)
half = np.linspace(-1,1,3)
quarter = np.linspace(-1,1,5)
eights = np.linspace(-1,1,9)

#   This array contains the points the interpolate
#   will be evaluated at.
x_axis = np.linspace(-1,1,100)

def f(x):
    return np.sqrt(1-x**2)

y1 = f(whole)
y2 = f(half)
y3 = f(quarter)
y4 = f(eights)

#We now interpolate all of the points linearly
two_points = np.interp(x_axis,whole,y1)
three_points = np.interp(x_axis,half,y2)
five_points = np.interp(x_axis,quarter,y3)
nine_points = np.interp(x_axis,eights,y4)

plt.plot(x_axis,two_points)
plt.plot(x_axis,three_points)
plt.plot(x_axis,five_points)
plt.plot(x_axis,nine_points)
plt.show()
