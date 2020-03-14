import numpy as np

#First derivative
def f(x):
    return 2*x + 1


#second derivative
def g(x):
    return -1/(x)**2 + np.sin(x)

#Let c be the initial approximation
def newton(c,num_iter):
    #iteration function
    for i in range(num_iter):
        c = c - f(c)/g(c)
    return c

print(newton(4,3))

#Secant method
def secant(a,b,num_iter):
	for i in range(num_iter):
		c = b - (f(b)*(b-a))/(f(b)-f(a))
		a = b
		b = c
	return b

for i in range(3):
    print(secant(-2,0,i))
