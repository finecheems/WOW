# coding=utf-8
from typing import Mapping
from unittest import result


names = ['哆啦A梦', '野比大雄', '源静香', '骨川小夫', '刚田武', '出木杉英才', '哆啦美']
scores = [76,4,98,92,59,100,87]
s_n=zip(scores,names)
d_s=dict(s_n)#成绩对应名字
def maopao(x):
    for i in range(len(scores)-1):
        for j in range(len(scores) -i -1):
            if x[j]>x[j+1]:
                x[j],x[j+1]=x[j+1],x[j]
        continue
    return x
x=maopao(scores)
new_names=[]
for n in x:
    new_names.append(d_s[n])
mapping=zip(new_names,x)
dic_mapping=dict(mapping)
print(dic_mapping)
