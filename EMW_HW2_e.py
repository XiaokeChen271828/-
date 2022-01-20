# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 17:09:41 2021

@author: 12879
"""

import numpy as np
import matplotlib.pyplot as plt
import cmath

wp=2*np.pi*10**6
c0=3*10**8
v=2*np.pi*10**3

w=np.arange(1,5*10**9,10**3)


er=[]
ei=[]

for i in w:
    e=1+wp**2/(1j*i*(v+1j*i))
    er.append(np.real(e))
    ei.append(np.abs(np.imag(e)))
    


plt.plot(np.log10(w),np.log(np.abs(er)))
plt.show()
plt.close()

plt.plot(np.log10(w),np.log(np.abs(ei)))
plt.show()
plt.close()