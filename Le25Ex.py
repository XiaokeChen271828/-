import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma,factorial
from scipy.integrate import quad
from scipy.optimize import curve_fit


def mypossion(x,u):
    return np.power(u,x)*np.exp(-u)/factorial(x)
def mygauss(x,u,sigma):
    up=-(x-u)**2/2/sigma
    return np.exp(up)/np.sqrt(2*np.pi*sigma)
def chi2(x,k):
    if x>0 :
        return np.power(x,k/2-1)*np.exp(-x/2)/2**(k/2)/gamma(k/2)
    else:
        return 0

print ('Ex1')
v=np.array([600.,609.,628.,637.,647.,656.])
r=np.array([6112,6181,6321,6785,6539,7015,7276])

v2=605
v3=650
boolv=np.logical_and(np.array(v)>=v2,np.array(v)<v3)
print (boolv)


print ('Ex2')
s=np.loadtxt(fname='L25Ex2.txt',unpack=True)
count,bins,ignored=plt.hist(s,20,density=True,stacked=True,alpha=0.3,color='b')
bin_width=bins[1]-bins[0]
err=np.sqrt(count/len(s)/bin_width)
x=bins[1:]-bin_width/2
plt.errorbar(x,count,err,fmt='o')

pinit=(110,90)
params,covar=curve_fit(mygauss,x,count,sigma=err,p0=pinit,absolute_sigma=True)
print (params)
print (covar)
fitted_y=mygauss(x,*params)
plt.plot(x,fitted_y,label='fit',color='b')
plt.show()

Sm=np.sum(((count-fitted_y)/err)**2)
ndf=20-3
k=ndf
p=quad(lambda x,k:chi2(x,k),Sm,np.inf,args=(k))
print (Sm,ndf,Sm/ndf)



