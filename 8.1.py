import matplotlib.pyplot as plt
import numpy as np

print('使用角度值')
x=np.arange(-360,360,0.1)
A=float(input('请输入振幅：'))
w=float(input('请输入频率：'))
f=float(input('请输入初相位：'))
y1=A*np.sin(2*np.pi*(w*x+f)/360)
plt.plot(x,y1)
y2=A*np.cos(2*np.pi*(w*x+f)/360)
plt.plot(x,y2,)
plt.grid()

print(np.sin((90/360)*2*np.pi))
plt.show()
plt.close()
