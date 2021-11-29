import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import os
import sys

#噪音处理函数
def moving_average(interval, window_size):
    window = np.ones(int(window_size)) / float(window_size)
    return np.convolve(interval, window, 'same')  # numpy的卷积函数

lib=[]
#文件名入口
filename="7.10.test_noise1"
file=open(filename+".txt")
nfile=open(filename+"detail.txt",'w')

s=file.readline()
while s!='':
    if s!='\n':
        lib.append(s)
    s=file.readline()

file.close()


for j in range(0,15):
    nfile.write(lib[j])
    print(lib[j])
print("实验细节已保存到同目录下（原文件名+detail）")
f_inf=lib[10].replace(',',' ')
f_inf=f_inf.split()
f0=1/2*10**(7)
nfile.close()
data1=[]
data2=[]

print(lib[15])
print(lib[16])
for i in range(15,len(lib)):
    lib[i]=lib[i].replace(',',' ')
    lib[i]=lib[i].split()
    #print(lib[i][0])
    #print(lib[i][1])
    data1.append(float(lib[i][0]))
    data2.append(float(lib[i][1]))
data2_clear=moving_average(interval=data2,window_size=200)
#平均值降噪处理，缩短或增加window_size可以调节精度
data2_fft=fft(data2)
N=len(data2_fft)
print("0频分量在相空间的标度为：",data2_fft[0])

#a_line为筛选振幅的基线，振幅大于a_line的频率部分均会打印在屏幕上,如果输出过多请适当调节a_line（未给出相位信息）
#请记录采样频率f0，通过改变f的大小可以得到相应f的幅度占比(默认为0)

f=0
a_line=0
a_chosen=[]
f_chosen=[]
f_low=0
f_high=20000
if(f0==0):
    print("如想计算相应频率对应的振幅，请在代码中改变f0和f")
else:
    n=int(f*N/f0)
    A=abs(data2_fft[n])/N
    print("目标频率",f,"的振幅为",A)
#and i*f0/N>f_low and i*f0/N<f_high
fft_test=data2_fft
for i in range(0,N):
    if(abs(fft_test[i])>=a_line and i*f0/N>f_low and i*f0/N<f_high):
        a_chosen.append(abs(fft_test[i])/N)
        f_chosen.append(i*f0/N)
        #print("振幅（单位为采样器单位）：",abs(fft_test[i])," 频率（单位与采样频率相同）：",i*f0/N)

#a_chosen.remove(abs(data2_fft[0]))
data2_fft_amplitude=[]  
for i in data2_fft:
    data2_fft_amplitude.append(abs(i))

bins=20

plt.plot(data2)
plt.plot(data2_clear)
plt.grid()
plt.show()

plt.plot(data2_fft_amplitude)
plt.show()

plt.hist(a_chosen,bins,density=1)
plt.title("Amplithde histogram(chosen data)")
plt.show()

plt.hist(f_chosen,bins,density=1)
plt.title("freqence")
plt.show()

#f_chosen.remove(0)
plt.plot(f_chosen,a_chosen)
plt.title("data2 f-A")
plt.grid()
plt.xlabel("f/Hz")
plt.ylabel("A/V")
plt.show()

