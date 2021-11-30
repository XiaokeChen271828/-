# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 21:56:19 2021

@author: xiaoke
"""

import numpy as np
from scipy.fftpack import fft2,ifft2
from scipy.integrate import quad,dblquad
import matplotlib.pyplot as plt
import scipy

"""
def H(fx,fy,z,k):
    jug=4*np.pi*(fx**2+fy**2)<k**2
    jug1=np.array(jug,dtype=np.int)
    h=jug1*(np.cos(z*np.sqrt(k**2-4*np.pi*(fx**2+fy**2)))+1j*np.sin(z*np.sqrt(k**2-4*np.pi*(fx**2+fy**2))))
    return (np.sqrt(((np.real(h))**2+(np.imag(h))**2)))
"""
def light(x0,y0,kx,ky):
    r=np.cos(kx*x+ky*y)
    i=np.sin(kx*x+ky*y)
    return r+1j*i

def hole(x,y,r):
    jug=(x**2+y**2)<r**2
    jug1=np.array(jug,dtype=np.int)
    return jug1


def kernelc(x,y,x0,y0,z,k):
    r=np.sqrt((x-x0)**2+(y-y0)**2+z**2)
    kc=z*np.cos(k*r)/(r**2)
    return kc

def kernels(x,y,x0,y0,z,k):
    r=np.sqrt((x-x0)**2+(y-y0)**2+z**2)
    ks=z*np.sin(k*r)/(r**2)
    return ks

"光束孔径"
r=5
N=1000
x0=y0=np.arange(-10,10,0.5)
dx0=x0[1]-x0[0]
dy0=y0[1]-y0[0]
y,x=np.ogrid[-10:10:100j,-10:10:10j]

def ref(x,y):
    x0=y0=np.arange(-10,10,0.09)
    dx0=x0[1]-x0[0]
    dy0=y0[1]-y0[0]
    my_sum=0
    for i in x0:
        for j in y0:
            my_sum+=hole(i,j,5)*kernelc(i,j,x,y,2,100)*dx0*dy0
    return my_sum



    

z=ref(x,y)

extent = [np.min(x),np.max(x),np.min(y),np.max(y)]
 
plt.imshow(z,extent=extent,cmap="gray")
plt.colorbar()
plt.show()
