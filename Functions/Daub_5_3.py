import numpy as np
def Daub_5_3(N):
    if ((N > 1)&((N % 2) == 0)):
        Na = N + 3
        Nd = N + 1
        
        V = np.zeros((N//2,Na))
        W = np.zeros((N//2,Nd))
        
        alpha = [-1/8, 1/4, 3/4, 1/4, -1/8]
        beta = [-1/2, 1, -1/2]
        N_alpha = len(alpha)
        N_beta = len(beta)
        
        for idx in range(N//2):
            V[idx,(2*idx):(2*idx+N_alpha)] = alpha
            W[idx,(2*idx):(2*idx+N_beta )] = beta
        
        # Even symmetry.
        V[:,3] = V[:,3] + V[:,1]
        V[:,4] = V[:,4] + V[:,0]
        V[:,-3] = V[:,-3] + V[:,-1]
        
        W[:,-3] = W[:,-3] + W[:,-1]
    else:
        print('USER ERROR: Length (N) is incorrect!!!')
    return V[:,2:-1], W[:,0:-1]