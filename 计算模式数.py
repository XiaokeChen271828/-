import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative




k0=2*np.pi/1
ra=1.5**2/1.4**2
b=np.arange(k0*1.4,k0*1.5,0.00001)
kf=np.sqrt((k0*1.5)**2-b**2)
gama=np.sqrt(b**2-1.4**2)

print ("run")
plt.plot(b,np.tan(5*np.sqrt((k0*1.5)**2-b**2)))
plt.plot(b,2*kf*ra*gama/(kf**2-gama**2*ra**2))
plt.show()

rhs=np.tan(5*np.sqrt((k0*1.5)**2-b**2))
lhs=2*kf*ra*gama/(kf**2-gama**2*ra**2)
b_get=[]

for i in range(0,len(b)):
    if rhs[i]==lhs[i]:
        print (b[i])
        
    
    
