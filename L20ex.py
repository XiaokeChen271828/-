import numpy as np
import scipy.special as special
from scipy.integrate import quad

f0=lambda x,y:x+y
print f0(2,3)

print 'Ex1'
f=lambda x,y,z:(x+y)/z

x=np.array([1.,2.,3.,4.,5.])
x2=np.array([6.,7.,8.,9.,10.])
x3=np.array([len(x)*20])

print x3
print f(x,x2,x3)

print ''
print 'Ex2'
f2=lambda x,y:x+y
print f2(x,x2)

print ''
print 'Ex3'
f3=lambda x3:2*np.sin(3*np.pi*x3/7)
g3=lambda x,y:np.exp(x+y)
h3=lambda x,y,z:np.sqrt(x+y+z)

a3=np.array([0.4,0.5,0.6])
b3=np.array([5,6,7])
c3=np.array([10,11,12])
print f3(a3)
print g3(a3,b3)
print h3(a3,b3,c3)

print ''
print 'Ex4'
f4=lambda y:np.exp(-2*y)
g4=lambda x:2*np.sin(x**2)
h4=lambda a,x:np.exp(-a*x)
i4=lambda a,x,b:a*np.sin(x**b)
a4=np.arange(0,1000,0.01)
print 'a:',np.sum(f4(a4)*0.01)
b4=np.arange(0,np.pi,0.01)
print 'b:',np.sum(g4(b4)*0.01)
c4=np.arange(0,1000,0.01)
print 'c:',np.sum(h4(4,c4)*0.01)
d4=np.arange(0,np.pi,0.01)
print 'd:',np.sum(i4(2,d4,3)*0.01)

print ''
print 'Ex5'
def mygauss(x,sigma,u):
    up=-(x-u)**2/2/sigma**2
    down=1/sigma/np.sqrt(2*np.pi)
    return np.exp(up)/down
print quad(f4,-1,1,args=())
