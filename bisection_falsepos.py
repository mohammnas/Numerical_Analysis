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

print(bisection(4,6,6))

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


print(falseposition(4,6,6))
