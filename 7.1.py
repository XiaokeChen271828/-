import os
import sys

en=[]
ch=[]
file=open('7.1.txt','r',encoding='UTF-8')
lib=file.readlines()
file.close()

for i in lib:
    i=i.split()
    en.append(i[0])
    ch.append(i[1])

dit={en[i]:ch[i] for i in range(len(en))}

d=[]
for j in dit:
    if len(j)<5:
        d.append(j)                     
for k in d:
    dit.pop(k)
#选取长度小于等于4的单词放入列表，并对列表循环依次弹出字典中相应的字母
for l in dit:
    print (l,dit[l])

