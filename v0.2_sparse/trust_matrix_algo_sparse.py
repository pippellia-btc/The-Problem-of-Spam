# we expect this method to be the best when the density of 1s p < 0.05
# Use trust_matrix_dense if p > 0.1

# B should be a scipy.sparse.csr_matrix

# note that (B^j)* = (B^(j-1) @ B)* = (B^(j-1)*  @ B)*

def trust_matrix_sparse(B, n = 5, gamma = 0.5):

    # the list of indexes already counted, as a matrix
    index_matrix =  sp.sparse.identity(B.shape[0], dtype='bool', format='csr') + B
    
    # the trust matrix T at the beginning
    T = index_matrix.astype(np.float32)

    # the current power of B , with star *
    B_pow_star = B

    # Loop
    for i in range(n-1):

        # compute B^j (j = 2, ... n), which becomes the current power of B
        B_pow = B_pow_star @ B

        # eliminate all the redundant indices
        B_pow_star = B_pow - B_pow.multiply(index_matrix)
        
        # include all the new indices in the index_matrix
        index_matrix = index_matrix + B_pow_star
        
        # add the new matrix, multiplied by gamma^(j-1) to the Trust matrix T
        T = T + gamma**(i+1) * B_pow_star

    return T
