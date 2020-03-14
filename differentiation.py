import numpy as np

h = [1,0.5,0.25,0.125,0.0625,0.03125]

def f(x):
    return np.log(x)

def fp(f,x,h):
        z = f(x+(2*h))-f(x-h)
        return z/(3*h)

print(h)

for i in h:
    print(fp(f,2,i))

print('\n')

print('error')
for i in h:
    e = 1/2 - fp(f,2,i)
    print(e)

print('\n')

print('e/h')
for i in h:
     e = 1/2 - fp(f,2,i)
     print(e/i)

print('\n')

print('e/h^2')
for i in h:
     e = 1/2 - fp(f,2,i)
     print(e/(i**2))

print('\n')


for i in h:
    e = 1/2 - fp(f,2,i)
    print(e/(i**3))
