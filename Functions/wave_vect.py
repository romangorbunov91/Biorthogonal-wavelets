import numpy as np
from Functions.daub_5_3 import daub_5_3
from Functions.daub_9_7 import daub_9_7
from Functions.coif_6 import coif_6
def wave_vect(N,K, wave_type):
    if ((N > 1)&((N % 2) == 0)):
        
        Mtrx = np.empty((K,), dtype=object)
        Mdir = np.empty((K,), dtype=object)
        Mrev = np.empty((K,), dtype=object)
        
        Vdir = np.empty((K,), dtype=object)
        Wdir = np.empty((K,), dtype=object)
        Vrev = np.empty((K,), dtype=object)
        Wrev = np.empty((K,), dtype=object)
        
        for k in range(K):
            Mtrx[k] = np.matrix(np.concatenate(wave_type(N//2**k), axis = 0))
            
            if k == 0:
                Mdir[0] = Mtrx[0].copy()
            else:
                Mdir[k] = np.identity(N)
                Mdir[k][:(N//2**k),:(N//2**k)] = Mtrx[k][:(N//2**k),:(N//2**k)].copy()
                Mdir[k] = Mdir[k] * Mdir[k-1]  
            Mrev[k] = np.linalg.inv(Mdir[k])
            
            Vdir[k] = Mdir[k][:(N//2**(k+1)),:]
            Wdir[k] = Mdir[k][(N//2**(k+1)):(N//2**k),:]
            Vrev[k] = Mrev[k][:,:(N//2**(k+1))].T
            Wrev[k] = Mrev[k][:,(N//2**(k+1)):(N//2**k)].T

        return Vdir, Wdir, Vrev, Wrev
    else:
        print('USER ERROR: Length (N) is incorrect!!!')