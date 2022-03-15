import numpy as np
import scipy.fftpack as fp


def gaussian(S,sigma = 1, vmax = .05):
    
    Nu, Nv = S.shape
    
    u = Nu *np.linspace(-vmax, vmax, Nu)
    v = Nv *np.linspace(-vmax, vmax, Nv)
    U, V = np.meshgrid(u, v)
    
    
    G = np.exp(-((np.multiply(U,U) + np.multiply(V,V)) / 2. / (sigma**2)))
    G = fp.fftshift(G) #faz o deslocamento
    
    return G/(sigma**2)
    
    