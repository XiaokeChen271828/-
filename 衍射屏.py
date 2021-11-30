import numpy as np
from scipy.fftpack import fft,ifft
from scipy.integrate import quad
import matplotlib.pyplot as plt
import scipy
import os
import sys
import cmath

my_i=cmath.sqrt(-1)

def light(x,y,z,kx,ky,kz):
    return cmath.exp(cmath.sqrt(-1)*(kx*x+ky*y+kz*z))

def my_ft_kernel(x,y,kx,ky):
    kernel=np.exp(my_i*(kx*x+ky*y))
    return kernel

def rectanglar(x,a):
    if np.abs(x)<a:
        return 1
    else:
        return 0


def e_int(a):
    I=quad(lambda x:np.exp(-x**2),a,np.inf)
    return I[0]


def my_ft(f,frequency,down,up):
    I1=quad(lambda x:f(x)*2*np.pi*scipy.cos(2*np.pi*frequency*x),down,up)
    I2=quad(lambda x:f(x)*2*np.pi*scipy.sin(2*np.pi*frequency*x),down,up)
    result=I1[0]+my_i*I2[0]

    return result


"""    
def my_ft_e(f,w,down,up):
    I=quad(lambda x:f(x)*my_ft_kernel(x,0,w,0),down,up)
    return I[0]
"""
x=np.arange(-10,10,0.01)
w=np.arange(-10,10,0.01)
f=[]
y=[]
for i in w:
    f.append(my_ft(lambda h:np.exp(-h**2),i,-10,10))

plt.plot(w,np.real(f))
plt.show()           





"""
print(np.inf)
t=np.arange(-10,10,0.01)
test=[]

for i in t:
    test.append(np.sin(i))

fft_test=fft(test)/len(t)
print(fft_test[1]/len(t))

plt.plot(t,test)
plt.show()
plt.close()
plt.plot(t,np.abs(fft_test))
plt.show()
"""
