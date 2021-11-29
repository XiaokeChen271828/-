import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative


def f(x):
    if x==0:
        return 1
    else:
        return np.sin(x)/x
    
#d为构造弯矩方程组的非齐次项
def dvalue(a,b,c):
    c1=(f(b)-f(a))/(b-a)
    c2=(f(c)-f(b))/(c-b)
    d=(c2-c1)/(c-a)
    return 6*d
#a,b为区间端点，m，l为区间端点处的弯矩
def S(x,a,b,m,l):
    h=b-a
    part1=(b-x)**3*m/6/h
    part2=(x-a)**3*l/6/h
    part3=(f(a)-h**2*m/6)*(b-x)/h
    part4=(f(b)-h**2*l/6)*(x-a)/h
    return part1+part2+part3+part4

#制造插值节点
a=float(input("请给出插值下界："))
b=float(input("请给出插值上界："))
n=int(input("请给出划分的区间数："))
h=(b-a)/n
f_1_a=derivative(f, a, dx=1e-10,n=1)
f_1_b=derivative(f, b, dx=1e-10,n=1)
f_2_a=derivative(f, a, dx=1e-10,n=2)
f_2_b=derivative(f, b, dx=1e-10,n=2)
x_s=[]
for i in range(0,n+1):
    x_s.append(a+i*h)

#构造方程组变量
h_n=[]
nu=[]
lamda=[]
h1=x_s[1]-x_s[0]
hn=x_s[n]-x_s[n-1]
d0=6*((f(x_s[1])-f(x_s[0]))/h1-f_1_a)/h1
dn=6*(f_1_b-(f(x_s[n])-f(x_s[n-1]))/hn)/hn
d=[d0]
for i in range(1,len(x_s)):
    h_n.append(x_s[i]-x_s[i-1])
for j in range(len(h_n)-1):
    loc1=h_n[j]/(h_n[j]+h_n[j+1])
    nu.append(loc1)
    lamda.append(1-loc1)
for i in range(1,len(x_s)-1):
    d.append(dvalue(x_s[i-1],x_s[i],x_s[i+1]))
print ('插值点：',len(x_s),x_s)
print ('插值区间步长：',len(h_n),h_n)
print('μ参数值：',len(nu),nu)
print('λ参数值',len(lamda),lamda)
d.append(dn)
print('d参数值：',len(d),d)


#追赶法解方程
M=[]
for i in range (n+1):
    M.append(1)
print (M)


#对应区间的样条函数
x_list=[]
y_list=[]
for i in range (len(x_s)-1):
    loc_plot=np.arange(x_s[i],x_s[i+1],0.001)
    loc_yplot=S(loc_plot,x_s[i],x_s[i+1],M[i],M[i+1])
    x_list.append(loc_plot)
    y_list.append(loc_yplot)
    plt.plot(loc_plot,loc_yplot,color='b')

print(x_list)
print(y_list)

x=[]
y=[]
for i in range(1001):
    test=a+(b-a)*i/1000
    x.append(test)
    y.append(f(test))
plt.plot(np.array(x),np.array(y),color='r')
plt.grid()
plt.show()

