# The difference this time is that the matrix B is boolean.
# This means that the matrix product is no more O(N^2.8) using the Strassen Algorithm
# but (on average), it is O(N^2) ---> extraordinary improvement!

# This however, doensn't work well when the density of 1s is below 0.1 O(N^3). Use v0.2_sparse instead.

# the sum is replaced by the '|' (element-wise OR) operator
# the subtraction '- index_matrix' is replaced by the  '& ~index_matrix' operator (AND NOT)

def trust_matrix_dense(B, n = 5, gamma = 0.5):

    # the list of indexes already counted, as a matrix
    index_matrix = ~(np.identity(B.shape[0], dtype = bool) | B)
    
    # the trust matrix T at the beginning
    T = (~index_matrix).astype(float)

    # the current power of B
    B_pow = B

    # Loop
    for i in range(n-1):

        # compute B^j (j = 2, ... n), which becomes the current power of B
        B_pow = B_pow @ B

        # eliminate all the redundant indices
        B_pow_star =  B_pow & index_matrix
        
        # include all the new indices in the index_matrix
        index_matrix = index_matrix ^ B_pow_star
        
        # add the new matrix, multiplied by gamma^(j-1) to the Trust matrix T
        T = T + gamma**(i+1) * B_pow_star

    return T
