from matplotlib import pyplot as plt
import math

import numpy as np

#Our function of interest (the derivative of the given function)
def f(x):
    return 1/x-np.cos(x)


#Bisection method first
def bisection(a,b,num_iter):
    c = (a + b)/2
    #x acts as counter, and increments each step
    x = 0
    while x < num_iter:
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        c = (a + b)/2
        x += 1
    return c

#False position
def falseposition(a,b,num_iter):
    c = b - f(b) * (b-a)/(f(b)-f(a))
    #x acts as counter, and increments each step
    x = 0
    while x < num_iter:
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        c =  b - f(b) * (b-a)/(f(b)-f(a))
        x += 1
    return c

#First derivative
def f(x):
    return 1/x-np.cos(x)


#second derivative
def g(x):
    return -1/(x)**2 + np.sin(x)

#Let c be the initial approximation
def newton(c,num_iter):
    #iteration function
    for i in range(num_iter):
        c = c - f(c)/g(c)
    return c


#Secant method
def secant(a,b,num_iter):
	for i in range(num_iter):
		c = b - (f(b)*(b-a))/(f(b)-f(a))
		a = b
		b = c
	return b


x = np.linspace(0,6,6)

bs = np.zeros(6)
fp = np.zeros(6)
nm = np.zeros(6)
sec = np.zeros(6)

for i in range(6):
    bs[i] = np.log(abs(4.917185925287132-bisection(4,6,i)))
    print(bs[i])

for i in range(6):
    fp[i] = np.log(abs(4.917185925287132-falseposition(4,6,i)))

for i in range(6):
    sec[i] = np.log(abs(4.917185925287132-secant(6,4,i)))

for i in range(6):
    nm[i] = np.log(abs(4.917185925287132-newton(4,i)))


plt.plot(x,bs,label='Bisection')
plt.plot(x,fp,label='False Position')
plt.plot(x,sec,label='Secant')
plt.plot(x,nm,label='Newton\'s Method')
plt.legend()
plt.show()
