import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma,factorial
from scipy.integrate import quad

def mypossion(x,u):
    return np.power(u,x)*np.exp(-u)/factorial(x)
def mygauss(x,u,sigma):
    up=-(x-u)**2/2/sigma**2
    return np.exp(up)/np.sqrt(2*np.pi)/sigma
def chi2(x,k):
    if x>0 :
        return np.power(x,k/2-1)*np.exp(-x/2)/2**(k/2)/gamma(k/2)
    else:
        return 0
def A(x,sigmaf):
    return np.sum(x/sigmaf**2)
def C(f,sigmaf):
    return np.sum(f/sigmaf**2)
def D(x,sigmaf):
    return np.sum(x**2/sigmaf**2)
def E(x,f,sigmaf):
    return np.sum(x*f/sigmaf**2)
def F(f,sigmaf):
    return np.sum(f**2/sigmaf**2)
def a(A,B,C,D,E,F):
    return (E*B-C*A)/(D*B-A**2)
def b(A,B,C,D,E,F):
    return (D*C-E*A)/(D*B-A**2)
def sigmaa(A,B,C,D,E,F):
    return np.sqrt(B/(D*B-A**2))
def sigmab(A,B,C,D,E,F):
    return np.sqrt(D/(D*B-A**2))

sigmaK=1.0
tWna=2.3
vna=np.array([4.2,8.3,10.4,12.5,14.6,16.7,18.8,20.8,22.9,25.,27.1,29.2,31.3,33.3,35.4,37.5,39.6,41.7,43.8,45.8,47.9,50.])
Kna=np.array([1.0,2.0,3.2,2.7,5.1,4.1,6.1,5.9,8.2,7.8,10.3,8.5,10.2,11.4,13.,13.7,12.9,14.8,16.1,15.7,17.1,19.4])
tWpt=6.4
vpt=np.array([16.7,18.8,20.8,22.9,25.,27.1,29.2,31.3,33.3,35.4,37.5,39.6,41.7,43.8,45.8,47.9,50.])
Kpt=np.array([1.9,1.9,1.3,5.,2.8,4.6,3.,4.9,8.,7.3,9.1,10.4,8.6,11.9,13.7,14.,13.1])
tWag=4.7
vag=np.array([10.4,12.5,14.6,16.7,18.8,20.8,22.9,25.,27.1,29.2,31.3,33.3,35.4,37.5,39.6,41.7,43.8,45.8,47.9,50.])
Kag=np.array([1.5,0.3,2.4,2.6,3.1,3.2,5.4,3.9,7.5,7.,8.5,6.9,9.4,10.5,12.7,13.7,13.6,14.6,15.1,15.])
tWk=2.2
vk=np.array([6.2,8.3,10.4,12.5,14.6,16.7,18.8,20.8,22.9,25.,27.1,29.2,31.3,33.3,35.4,37.5,39.6,41.7,43.8,45.8,47.9,50.])
Kk=np.array([0.9,0.8,1.6,2.5,3.7,5.9,4.3,6.8,9.1,8.8,8.7,10.2,9.4,10.7,13.1,12.1,14.3,15.8,15.2,15.8,17.6,18.8])
tWcs=1.9
vcs=np.array([2.1,4.2,6.2,8.3,10.4,12.5,14.6,16.7,18.8,20.8,22.9,25.,27.1,29.2,31.3,33.3,35.4,37.5,39.6,41.7,43.8,45.8,47.9,50.])
Kcs=np.array([0.3,0.4,0.4,2.6,3.,3.3,4.1,5.7,7.2,5.7,6.5,8.8,8.,10.6,10.4,12.1,11.7,13.7,15.9,16.5,15.6,18.1,18.2,18.7])

print ('a of part 1')
print ('Na')
Ana=np.sum(vna)
Bna=len(Kna)
Cna=C(Kna,sigmaK)
Dna=D(vna,sigmaK)
Ena=E(vna,Kna,sigmaK)
Fna=F(Kna,sigmaK)
ana=a(Ana,Bna,Cna,Dna,Ena,Fna)
bna=b(Ana,Bna,Cna,Dna,Ena,Fna)
sigmaana=sigmaa(Ana,Bna,Cna,Dna,Ena,Fna)
sigmabna=sigmab(Ana,Bna,Cna,Dna,Ena,Fna)
Smna=np.sum(((Kna-ana*vna-bna)/sigmaK)**2)
pna=quad(lambda x,k:chi2(x,k),Smna,np.inf,args=len(vna)-2)[0]
plt.errorbar(vna,Kna,sigmaK,fmt='o')
x=np.arange(0,50,0.01)
plt.plot(x,ana*x+bna)
plt.grid(True)
plt.xlabel('10^14Hz')
plt.ylabel('eV')
plt.title('Data of Sodium')
plt.show()
plt.close()
print ('Wna=',-bna,'+/-',sigmabna)
print ('hna=(',ana,'+/-',sigmaana,')*10^(-14) eV*s')
print ('ndf=',len(Kna)-2)
print ('Sm=',Smna,'/p vaule of fitting sodium',pna)

print ('Pt')
Apt=np.sum(vpt)
Bpt=len(Kpt)
Cpt=C(Kpt,sigmaK)
Dpt=D(vpt,sigmaK)
Ept=E(vpt,Kpt,sigmaK)
Fpt=F(Kpt,sigmaK)
apt=a(Apt,Bpt,Cpt,Dpt,Ept,Fpt)
bpt=b(Apt,Bpt,Cpt,Dpt,Ept,Fpt)
sigmaapt=sigmaa(Apt,Bpt,Cpt,Dpt,Ept,Fpt)
sigmabpt=sigmab(Apt,Bpt,Cpt,Dpt,Ept,Fpt)
Smpt=np.sum(((Kpt-apt*vpt-bpt)/sigmaK)**2)
ppt=quad(lambda x,k:chi2(x,k),Smpt,np.inf,args=len(vpt)-2)[0]
plt.errorbar(vpt,Kpt,sigmaK,fmt='o')
x2=np.arange(15,50,0.01)
plt.plot(x2,apt*x2+bpt)
plt.grid(True)
plt.xlabel('10^14Hz')
plt.ylabel('eV')
plt.title('Data of Platinum')
plt.show()
plt.close()
print ('Wpt=',-bpt,'+/-',sigmabpt)
print ('hpt=(',apt,'+/-',sigmaapt,')*10^(-14) eV*s')
print ('ndf=',len(Kpt)-2)
print ('Sm=',Smpt,'/p vaule of fitting of Platinum',ppt)

print ('Ag')
Aag=np.sum(vag)
Bag=len(Kag)
Cag=C(Kag,sigmaK)
Dag=D(vag,sigmaK)
Eag=E(vag,Kag,sigmaK)
Fag=F(Kag,sigmaK)
aag=a(Aag,Bag,Cag,Dag,Eag,Fag)
bag=b(Aag,Bag,Cag,Dag,Eag,Fag)
sigmaaag=sigmaa(Aag,Bag,Cag,Dag,Eag,Fag)
sigmabag=sigmab(Aag,Bag,Cag,Dag,Eag,Fag)
Smag=np.sum(((Kag-aag*vag-bag)/sigmaK)**2)
pag=quad(lambda x,k:chi2(x,k),Smag,np.inf,args=len(vag)-2)[0]
plt.errorbar(vag,Kag,sigmaK,fmt='o')
x3=np.arange(10,50,0.01)
plt.plot(x3,aag*x3+bag)
plt.grid(True)
plt.xlabel('10^14Hz')
plt.ylabel('eV')
plt.title('Data of Silver')
plt.show()
plt.close()
print ('Wag=',-bag,'+/-',sigmabag)
print ('hag=(',aag,'+/-',sigmaaag,')*10^(-14) eV*s')
print ('ndf=',len(Kag)-2)
print ('Sm=',Smag,'/p vaule of fitting of silver',pag)

print ('K')
Ak=np.sum(vk)
Bk=len(Kk)
Ck=C(Kk,sigmaK)
Dk=D(vk,sigmaK)
Ek=E(vk,Kk,sigmaK)
Fk=F(Kk,sigmaK)
ak=a(Ak,Bk,Ck,Dk,Ek,Fk)
bk=b(Ak,Bk,Ck,Dk,Ek,Fk)
sigmaak=sigmaa(Ak,Bk,Ck,Dk,Ek,Fk)
sigmabk=sigmab(Ak,Bk,Ck,Dk,Ek,Fk)
Smk=np.sum(((Kk-ak*vk-bk)/sigmaK)**2)
pk=quad(lambda x,k:chi2(x,k),Smk,np.inf,args=len(vk)-2)[0]
plt.errorbar(vk,Kk,sigmaK,fmt='o')
x4=np.arange(5,50,0.01)
plt.plot(x4,ak*x4+bk)
plt.grid(True)
plt.xlabel('10^14Hz')
plt.ylabel('eV')
plt.title('Data of Potassium')
plt.show()
plt.close()
print ('Wk=',-bk,'+/-',sigmabk)
print ('hk=(',ak,'+/-',sigmaak,')*10^(-14) eV*s')
print ('ndf=',len(Kk)-2)
print ('Sm=',Smk,'/p vaule of fitting of potassium',pk)

print ('Cs')
Acs=np.sum(vcs)
Bcs=len(Kcs)
Ccs=C(Kcs,sigmaK)
Dcs=D(vcs,sigmaK)
Ecs=E(vcs,Kcs,sigmaK)
Fcs=F(Kcs,sigmaK)
acs=a(Acs,Bcs,Ccs,Dcs,Ecs,Fcs)
bcs=b(Acs,Bcs,Ccs,Dcs,Ecs,Fcs)
sigmaacs=sigmaa(Acs,Bcs,Ccs,Dcs,Ecs,Fcs)
sigmabcs=sigmab(Acs,Bcs,Ccs,Dcs,Ecs,Fcs)
Smcs=np.sum(((Kcs-acs*vcs-bcs)/sigmaK)**2)
pcs=quad(lambda x,k:chi2(x,k),Smcs,np.inf,args=len(vcs)-2)[0]
plt.errorbar(vcs,Kcs,sigmaK,fmt='o')
x5=np.arange(0,50,0.01)
plt.plot(x5,acs*x5+bcs)
plt.grid(True)
plt.xlabel('10^14Hz')
plt.ylabel('eV')
plt.title('Data of Cesium')
plt.show()
plt.close()
print ('Wcs=',-bcs,'+/-',sigmabcs)
print ('hcs=(',acs,'+/-',sigmaacs,')*10^(-14) eV*s')
print ('ndf=',len(Kcs)-2)
print ('Sm=',Smcs,'/p vaule of fitting of cesium',pcs)

print ('')
print ('b of part 1')
print ('W of Na')
Wna=-bna
fna=abs((Wna-tWna)/sigmabna)
gpna=2*quad(lambda x,u,sigma:mygauss(x,u,sigma),tWna+fna*sigmabna,+np.inf,args=(tWna,sigmabna))[0]
print ('consider Wtrue, we have f value:',fna,'and p value:',gpna)
print ('W of Pt')
Wpt=-bpt
fpt=abs((Wpt-tWpt)/sigmabpt)
gppt=2*quad(lambda x,u,sigma:mygauss(x,u,sigma),tWpt+fpt*sigmabpt,+np.inf,args=(tWpt,sigmabpt))[0]
print ('consider Wtrue, we have f value:',fpt,'and p value:',gppt)
print ('W of Ag')
Wag=-bag
fag=abs((Wag-tWag)/sigmabag)
gpag=2*quad(lambda x,u,sigma:mygauss(x,u,sigma),tWag+fag*sigmabag,+np.inf,args=(tWag,sigmabag))[0]
print ('consider Wtrue, we have f value:',fag,'and p value:',gpag)
print ('W of K')
Wk=-bk
fk=abs((Wk-tWk)/sigmabk)
gpk=2*quad(lambda x,u,sigma:mygauss(x,u,sigma),tWk+fk*sigmabk,+np.inf,args=(tWk,sigmabk))[0]
print ('consider Wtrue, we have f value:',fk,'and p value:',gpk)
print ('W of Cs')
Wcs=-bcs
fcs=abs((Wcs-tWcs)/sigmabcs)
gpcs=2*quad(lambda x,u,sigma:mygauss(x,u,sigma),tWcs+fcs*sigmabcs,np.inf,args=(tWcs,sigmabcs))[0]
print ('consider Wtrue, we have f value:',fcs,'and p value:',gpcs)

print ('')
print ('part 2')
h_true=0.4135667696
h=np.array([ana,apt,aag,ak,acs])
h_sigma=np.array([sigmaana,sigmaapt,sigmaaag,sigmaak,sigmaacs])
h_best=np.sum(h/h_sigma**2)/np.sum(1/h_sigma**2)
h_bestsigma=np.sqrt(1/np.sum(1/h_sigma**2))
print ('the true value of h is:',h_true,'*10^(-14)eV*s')
print ('experiment h value:(',h_best,'+/-',h_bestsigma,')*10^(-14)eV*s')
hf=abs((h_best-h_true)/h_bestsigma)
h_pvalue=2*quad(lambda x,u,sigma:mygauss(x,u,sigma),h_true+hf*h_bestsigma,np.inf,args=(h_true,h_bestsigma))[0]
print ('the f value is:',hf,'the p value is:',h_pvalue) 

