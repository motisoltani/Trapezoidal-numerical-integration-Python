'''
Numerical Integration 
Trapezoidal Method

language: Python

Motahare Soltani
soltani.wse@gmail.com

'''

import numpy as np

def trapz(f,a,b,N=50):
    x = np.linspace(a,b,N+1) 
    y = f(x)
    y_right = y[1:] 
    y_left = y[:-1] 
    dx = (b - a)/N
    T = (dx/2) * np.sum(y_right + y_left)
    return T

    
print(trapz(lambda x : 3*x**2,0,1,10000))
print(trapz(np.sin,0,np.pi/2,1000))