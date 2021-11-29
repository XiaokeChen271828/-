import math

print 'Midterm'
print ''

print 'every value with uncertainty'
def get_a(M,m):
    a=9.8*(M-m)/(M+m)
    return a;
def get_sigma_a(M,sigma_M,m,sigma_m):
    square=(2*m*9.8*sigma_M/(M+m)**2)**2+(2*M*9.8*sigma_m/(M+m)**2)**2
    return math.sqrt(square)

M=[100.1,99.9,100.0,100.0,100.1,100.0,100.0,100.1,100.1,99.9]
m=[50.1,50.0,50.1,50.0,50.1,50.0,49.8,50.0,50.0,49.9]
sigma_M=0.1
sigma_m=0.1
a=[]
sigma_a=[]
for i in range(0,10):
    r=get_a(M[i],m[i])
    sigma_r=get_sigma_a(M[i],sigma_M,m[i],sigma_m)
    a.append(r)
    sigma_a.append(sigma_r)
    print round(r,5),'+/-',round(sigma_r,5),'m/s^2'

print ''
print 'Best value with uncertainty'
sigma_sum=0
a_best=0
sigma_a_best=0
for i in range (0,10):
    sigma_sum+=1/sigma_a[i]**2
sigma_a_best=math.sqrt(1/sigma_sum)
for j in range (0,10):
    a_best+=a[i]/sigma_a[i]**2/sigma_sum

print round(a_best,5),'+/-',round(sigma_a_best,5),'m/s^2'
    
    
