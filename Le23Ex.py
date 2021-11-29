import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma,factorial

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
c=np.loadtxt('Le23Ex1.txt',unpack=True)
count,bins,ignored=plt.hist(c,9,normed =False)
plt.show()
count,bins,ignored=plt.hist(c,9,normed =True)
c_mean=np.sum(c)/len(c)
c_standard=np.sqrt(np.sum((c-c_mean)**2)/(len(c)-1)/len(c))
print (c_mean,c_standard)
x=np.arange(10,40,0.01)
y=mypossion(x,c_mean)
plt.plot(x,y)
plt.grid(True)
plt.show()
Sm=0
ndf=10



c2=[]
for i in c:
    c2.append(i/3)
    c2.append(i/3)
    c2.append(i/3)
c2=np.array(c2)
count,bins,ignored=plt.hist(c2,15,normed=False)
plt.show()



print ('Ex2')
v=np.array([600., 609., 619., 628., 637., 647., 656., 665., 674., 684., 693., 702., 712., 721., 730., 740., 749., 758., 768., 777., 786., 796.,
805., 814., 823., 833., 842., 851., 861., 870.
])
r=np.array([6050., 6241., 6432., 6623., 6813., 7004., 7195., 7386., 7577., 7768.,7959., 8107., 8135., 8163., 8191., 8219., 8247., 8271.,
8343., 8467.,8643., 8872., 9152., 9484., 9868., 10305., 10793., 11333., 11926., 12570.])
sigma_r=np.sqrt(r)
plt.errorbar(v,r,sigma_r,fmt='o')

A=np.sum(v/sigma_r**2)
B=np.sum(1/sigma_r**2)
C=np.sum(r/sigma_r**2)
D=np.sum(v**2/sigma_r**2)
E=np.sum(v*r/sigma_r**2)
F=np.sum(r**2/sigma_r**2)
a=(E*B-C*A)/(D*B-A**2)
b=(D*C-E*A)/(D*B-A**2)
sigma_a=np.sqrt(B/(D*B-A**2))
sigma_b=np.sqrt(D/(D*B-A**2))
b_plat=C/B
sigma_bplat=np.sqrt(1/np.sum(1/sigma_r**2))

a_sigmarange=[-sigma_a,0,+sigma_a]
b_sigmarange=[-sigma_b,0,+sigma_b]
x=np.arange(min(v),max(v),0.01)
v1,v2,v3,r1,r2,r3,sigma_r1,sigma_r2,sigma_r3=[],[],[],[],[],[],[],[],[]
for i in range(0,len(v)):
    if r[i]<=8000:
        v1.append(v[i])
        r1.append(r[i])
        sigma_r1.append(sigma_r[i])
    elif r[i]>=8500:
        v3.append(v[i])
        r3.append(r[i])
        sigma_r3.append(sigma_r[i])
    else:
        v2.append(v[i])
        r2.append(r[i])
        sigma_r2.append(sigma_r[i])
        
v1=np.array(v1)
v2=np.array(v2)
v3=np.array(v3)
r1=np.array(r1)
r2=np.array(r2)
r3=np.array(r3)
sigma_r1=np.array(sigma_r1)
sigma_r2=np.array(sigma_r2)
sigma_r3=np.array(sigma_r3)


A1=np.sum(v1/sigma_r1**2)
B1=np.sum(1/sigma_r1**2)
C1=np.sum(r1/sigma_r1**2)
D1=np.sum(v1**2/sigma_r1**2)
E1=np.sum(v1*r1/sigma_r1**2)
F1=np.sum(r1**2/sigma_r1**2)
a1=(E1*B1-C1*A1)/(D1*B1-A1**2)
b1=(D1*C1-E1*A1)/(D1*B1-A1**2)
x1=np.arange(min(v),max(v1),0.01)
plt.plot(x1,a1*x1+b1)

A3=np.sum(v3/sigma_r3**2)
B3=np.sum(1/sigma_r3**2)
C3=np.sum(r3/sigma_r3**2)
D3=np.sum(v3**2/sigma_r3**2)
E3=np.sum(v3*r3/sigma_r3**2)
F3=np.sum(r3**2/sigma_r3**2)
a3=(E3*B3-C3*A3)/(D3*B3-A3**2)
b3=(D3*C3-E3*A3)/(D3*B3-A3**2)
x3=np.arange(min(v3),max(v),0.01)
plt.plot(x3,a3*x3+b3)

A2=np.sum(v2/sigma_r2**2)
B2=np.sum(1/sigma_r2**2)
C2=np.sum(r2/sigma_r2**2)
D2=np.sum(v2**2/sigma_r2**2)
E2=np.sum(v2*r2/sigma_r2**2)
F2=np.sum(r2**2/sigma_r2**2)
a2=(E2*B2-C2*A2)/(D2*B2-A2**2)
b2=(D2*C2-E2*A2)/(D2*B2-A2**2)
x2=np.arange(700,800.01)
plt.plot(x2,a2*x2+b2)

print ('threshold voltage =',(b_plat-b1)/a1,'v')
print ('slope =',a2,'counts/v')
plt.grid(True)
plt.show()
