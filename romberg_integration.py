import numpy as np

def f(x):
    return x*np.exp(np.negative(x**2))

#use n = 1,2,4,8 for the number of trapezoids
def trap(f,n):
    # x is a partition of [0,1] into n intervals
    x = np.linspace(0,1,n+1)
    # initialize t with the first term
    t = (1/2) * f(0)
    # update t with sum of subsequent terms up to n
    for i in x:
        if i > 0 and i < 1:
            t += f(i)
    # add 1/2 of final term and multiply by h
    t += (1/2) * f(1)
    t *= 1/n
    return t

#first iteration of romberg integration
def rom1(f,h):
    n = 1/h
    n = int(n)
    #we use the general formula on R_0 which is the trapezoid rule
    return 1/3 * (4*trap(f,n)-trap(f,int(1/2 * n)))

#second iteration of romberg
def rom2(f,h):
    return 1/15 * (16 * rom1(f,h)-rom1(f,2*h))

#third iteration of romberg
def rom3(f,h):
    return 1/63 * (64 * rom2(f,h)-rom2(f,2*h))

print(rom3(f,0.125))
