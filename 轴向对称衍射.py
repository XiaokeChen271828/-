# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 00:49:29 2021

@author: 12879
"""

import numpy as np
from scipy.fftpack import fft2,ifft2
from scipy.integrate import quad,dblquad
import matplotlib.pyplot as plt
import scipy

k0=2*np.pi/0.6

def hole(r,radius):
    jug=np.abs(r)<radius
    jug1=np.array(jug,dtype=np.int)
    return jug1

def kernelc(r,r0,z,k):
    delt_r=np.sqrt((r-r0)**2+z**2)
    return z*r0*np.cos(k*delt_r)/delt_r**2

def kernels(r,r0,z,k):
    delt_r=np.sqrt((r-r0)**2+z**2)
    return z*r0*np.sin(k*delt_r)/delt_r**2

"源点为r0,场点为r"
r=np.arange(-100,100,0.1)
A=[]
for i in r:
    I1=quad(lambda r0:hole(r0,20)*kernels(i,r0,100,k0),-40,40)
    A.append(abs(I1[0]))


plt.plot(r,A)