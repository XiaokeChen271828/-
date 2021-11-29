meaningless  ='''
the and  of a in on out an not 
from to with through firmly 
am is are but while when who what
this that these we them you
will could would 
as after  by between
say said The before
have has  had
'''

def sortby(x):
    return x[1]


wordsfreq={}
with open('engpaper02.txt','r',encoding='UTF-8') as file:
    punctuation='''\'\".,:-?$0123456789'''
    lines=file.readlines()
    for x in lines:
        x=x.lower()
        for p in punctuation:
            x=x.replace(p,' ')
        y=x.strip()
        y=y.split()
        for word in y:
            if word in wordsfreq:
                wordsfreq[word]+=1
            elif word not in meaningless:
                wordsfreq[word]=1
    wordsfreq=list(wordsfreq.items())
    wordsfreq.sort(key=sortby,reverse=True)
    for x in wordsfreq[:15]:
        print(x[0],'\t',x[1])
