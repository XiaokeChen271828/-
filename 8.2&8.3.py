import matplotlib.pyplot as plt
import os
import sys

lib=[]
file=open('pythonscore.txt','r',encoding='ANSI')
s=file.readline()
while s!='':
    if s!='\n':
        lib.append(s)
    s=file.readline()
file.close()

num=[0,0,0,0,0]
grade=[]
lib.remove(lib[0])

for i in lib:
    i=i.split()
    grade.append(int(i[2]))

for i in grade:
    if i>89:
        num[0]+=1
    elif i>79:
        num[1]+=1
    elif i>69:
        num[2]+=1
    elif i>59:
        num[3]+=1
    else:
        num[4]+=1



labels=['>90','>80','>70','>60','fail']
plt.pie(num,labels=labels)
plt.grid()
plt.show()
plt.close()

plt.bar(labels,num)
plt.grid()
plt.xlabel('range')
plt.ylabel('number')
plt.show()
plt.close()





