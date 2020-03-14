import numpy as np
from scipy import linalg


#The following computes the roots in decimal form
d = np.sqrt(70)
e1 = 35 + 2*d
e2 = 35 -2*d
f = np.sqrt(e1/63)
g = np.sqrt(e2/63)
gn = np.negative(g)
fn = np.negative(f)

#arrays which will be our matrix's rows
ones = np.ones(5)
roots = ([fn,gn,0,g,f])
roots_2 = np.float_power(roots,2)
roots_3 = np.float_power(roots,3)
roots_4 = np.float_power(roots,4)

#A is a matrix containing as rows the roots
A = np.array([ones,roots,roots_2,roots_3,roots_4])
b = np.array([[2],[0],[2/3],[0],[2/5]])
weights = linalg.solve(A,b)

#the function for part c)
def f(x):
    return pow(x,8)+42*pow(x,7)

#the function for part d)
def g(x):
    return pow(x,11)+pow(x,10)

#computes the integral using gaussian quadrature
def integrate(f,a,b):
    integral = 0
    for i in range(5):
        integral += a[i] * f(b[i])
    print(integral)

integrate(f,weights,roots)
integrate(g,weights,roots)

print(roots)
