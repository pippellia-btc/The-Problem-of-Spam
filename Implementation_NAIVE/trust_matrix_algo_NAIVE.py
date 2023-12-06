import numpy as np
import scipy as sp
from matplotlib import pyplot as plt
import time

# B is the belief matrix (bij = 1 if ni follows nj, 0 otherwise)
# n is the number of iterations
# gamma is the trust decay factor

def trust_matrix(B, n = 5, gamma = 0.5):

    # Initialization
    
    # the trust matrix T at the beginning
    T = np.minimum(1, np.identity(B.shape[0]) + B)

    # the list of indexes already counted, as a matrix
    index_matrix = -T

    # the previous power of B
    B_prev_pow = B

    # Loop
    for i in range(n-1): #(j = 2, ... n)

        # compute B^j and eliminate all the redundant indices
        B_new_pow = np.maximum(0, np.minimum(1,B_prev_pow @ B) + index_matrix)
        
        # get all the new nonzero indices
        index_matrix = index_matrix - B_new_pow
        
        # add the new matrix to the Trust matrix T
        T = T + gamma**(i+1) * B_new_pow

        # update the previous power of B
        B_prev_pow = B_new_pow

    return T
