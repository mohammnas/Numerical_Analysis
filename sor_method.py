import numpy as np
from matplotlib import pyplot as plt

#This is the determinant of T_SOR
def det(w):
    return (w-8)/((4-w)*(w-2))

#These are our points for the relaxation factor
omega = np.arange(0.1,2,0.1)
spec_radius = np.zeros(19)

for i in range(18):
    spec_radius[i]=det(omega[i])

plt.plot(omega,spec_radius)
plt.show()
