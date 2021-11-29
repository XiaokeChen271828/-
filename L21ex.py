import numpy as np
from scipy.special import gamma
from scipy.integrate import quad
import matplotlib.pyplot as plt

def myChi2(x,k):
    return x**(k/2-1)*np.exp(-x/2)/(2**(k/2)*gamma(k/2))
def pvalue(s,k):
    i=quad(myChi2,s,np.inf,args=(k))
    return i[0]

Sm=2.078
k=4
Sm2=6.7
k2=9
m=4

I=quad(myChi2,Sm,np.inf,args=(k))
I2=quad(lambda x2,k2:myChi2(x2,k2),Sm2,np.inf,args=(k2))
print I
print I2


K=np.array([1.,2.,3.,4.,5.,6.,7.,8.,9.])
sm=np.arange(0,20,1)
y=[]
for i in sm:
    y.append(pvalue(i,2))
print y
y=np.array(y)        
print y
