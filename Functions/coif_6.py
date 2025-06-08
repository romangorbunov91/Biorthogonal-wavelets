import numpy as np
def coif_6(N):
    alpha = [( 1 - np.sqrt(7))/(16*np.sqrt(2)),
             ( 5 + np.sqrt(7))/(16*np.sqrt(2)),
             (14+2*np.sqrt(7))/(16*np.sqrt(2)),
             (14-2*np.sqrt(7))/(16*np.sqrt(2)),
             ( 1 - np.sqrt(7))/(16*np.sqrt(2)),
             (-3 + np.sqrt(7))/(16*np.sqrt(2))]
    
    beta =  [ alpha[5],
             -alpha[4],
              alpha[3],
             -alpha[2],
              alpha[1],
             -alpha[0]]
    
    N_alpha = len(alpha)
    N_beta = len(beta)
    
    if ((N >= max(N_alpha, N_beta))&((N % 2) == 0)):

        V = np.zeros((N//2, N))
        W = np.zeros((N//2, N))

        V[1,:N_alpha] = alpha
        W[1,:N_beta] = beta
        
        # Rotate left by 2.
        V[0,:] = np.roll(V[1,:], -2)
        W[0,:] = np.roll(W[1,:], -2)
        
        for idx in range(2,N//2):
            # Rotate right by 2.
            V[idx,:] = np.roll(V[idx-1,:], 2)
            W[idx,:] = np.roll(W[idx-1,:], 2)
  
    else:
        print('USER ERROR: Length (N) is incorrect!!!')
    return V, W