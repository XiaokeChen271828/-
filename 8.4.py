import wordcloud as wc
import matplotlib.pyplot as plt

print('使用第七周第四题的英文短文')
file=open('engpaper02.txt','r',encoding='UTF-8')
text=file.read()
file.close()

meaningless  ='\".,:-?$0123456789'
for i in meaningless:
    text=text.replace(i,' ')

lib=text.split()
txt=''
for i in lib:
    txt+=i+' by '



file.close()
w=wc.WordCloud()
w=wc.WordCloud(width=1200)
w=wc.WordCloud(height=800)
w.generate(txt)
w.to_file('8.4.png')
print('done')
