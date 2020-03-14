import numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate
import scipy as sci
from scipy.interpolate import BarycentricInterpolator


#This function returns an array containing n Chebyshev points
def cheb_points(n):
    theta_i = np.zeros(n+1)
    for i in range(n+1):
        theta_i[i]= ((np.pi)/n)*i
    cheb = np.zeros(n+1)
    #Below is the array containing n chebyshev points
    for i in range(n+1):
        cheb[i] = np.negative(np.cos(theta_i[i]))
    return cheb

#Now we will interpolate a function f at the chebyshev points
def interpolate(f,n):
    #First we the interpolating polynomial
    x = cheb_points(n)
    #y contains our function's values at the chebyshev points
    y = f(x)
    #Below we get an interpolating polynomial that runs through points in y
    p = BarycentricInterpolator(x, y)
    xnew = np.linspace(-1,1,1000)
    ynew = p(xnew)

    #Below we plotted on (-2,2) using values from our interpolating polynomial
    plt.plot(xnew,ynew)
    return y

def f(x):
    return np.abs(x)

def g(x):
    return np.sign(x)

interpolate(f,4)
interpolate(f,8)
interpolate(f,16)
plt.legend()
plt.show()


interpolate(g,4)
plt.legend('first')
interpolate(g,8)
plt.legend('second')
interpolate(g,16)
plt.legend('last')
plt.show()
