import numpy as np

def lu_factor(A):

    if len(A) != len(A[0]):
        print('Matrix is not a square!')

    n = len(A)
    r = np.arange(0,n)

    #This constructs the pivot vector
    #argmax returns the maximum row indices
    for k in range(n-1):
        max_row_index = np.argmax(abs(A[k:n,k])) + k
        r[[k,max_row_index]] = r[[max_row_index,k]]
        A[[k,max_row_index]] = A[[max_row_index,k]]

        for i in range(k+1,n):
            A[i,k] = A[i,k]/A[k,k]
            for j in range(k+1,n):
                A[i,j] -= A[i,k]*A[k,j]

    return [A,r]

y = np.array([2,7,5,6,20,10,4,3,0])
x = y.reshape(3,3)
print(lu_factor(x))
