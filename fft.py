import numpy as np
from scipy.fftpack import fft,ifft
from scipy.integrate import quad
import matplotlib.pyplot as plt
import scipy
import cmath


def rectanglar(x,a):
    if np.abs(x)<a:
        return 1
    else:
        return 0


x=np.arange(-2,2,0.01)


"取样频率，取样点"
N=len(x)
dx=x[1]-x[0]
fa=1.0/dx
print(N,fa,dx)

y=[]
x_f=[]
for i in x:
    x_f.append(np.exp(-i**2))
y2=fft(x_f)
x_t=ifft(y2)
plt.plot(x,x_t)
plt.show()
plt.close()

y_f=y2[range(int(N/2))]/N
x_f=np.arange(N)
x_f2=x_f[range(int(N/2))]


plt.plot(x_f2,np.abs(y_f))
plt.show()

