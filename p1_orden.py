import numpy as np
from numpy.core.fromnumeric import shape

def merge(A,B):
    n = min(A.size, B.size)
    T = np.zeros(A.size + B.size)
    j = 0
    k = 0
    i= 0
    while(j != A.size-1 and k != B.size-1):
        if A[j] < B[k]:
            T[i] = A[j]
            j += 1
        else:
            T[i] = B[k]
            k += 1

    if j == A.size - 1:
        for l in range(n, B.size - j):
            T[i] = B[l]
            i += 1
    else:
        for l in range(n, A.size - k):
            T[i] = A[l]
            i += 1
    return T

A = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
B = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
C = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])

F = merge(A,B)
F = merge(F,C)

print(F)