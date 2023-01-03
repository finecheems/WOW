#coding=utf-8
from collections import Counter
from unicodedata import name
scores_0 = []
names_0 = []
rank = []
txt = []
o =1
with open("D:\成绩单.txt",'r',encoding='utf-8') as fp:
    t = fp.readlines()
    for x_0 in t:
        x_1 = x_0.rstrip("\n")
        x_2 = x_1.split("\t")
        a = int(x_2[1])
        b = int(x_2[2])
        c = int(x_2[3])
        d = a+b+c
        del x_2[1:3]
        names_0.append(x_2[0])
        scores_0.append(d)
        x_2.pop()
        x_2.append(str(d))
        x_2_str = ' 总分：'.join(x_2)
zipped_0 = list(zip(scores_0,names_0))
zipped_1 = sorted(zipped_0,reverse=True)
zipped_2 = [tuple(reversed(k)) for k in zipped_1]
dic = dict(zipped_2)
names_1 = dic.keys()
scores_1 = sorted(scores_0,reverse=True)
current_scores = 0
current_index = 0
i =0
mat = 104
for name,score in zip(names_1,scores_1):
    if i<262:
        if score == current_scores:
            txt.append(f'名字：{name}\t成绩:{score}\t并列排名:{current_index}\n')
            i+=1
        elif scores_1[i] == scores_1[i+1]:
            current_index+=1
            txt.append(f'名字：{name}\t成绩:{score}\t并列排名:{current_index}\n')
            i+=1
        else:
            current_index += 1
            txt.append(f'名字：{name}\t成绩:{score}\t排名:{current_index}\n')
            i+=1
        current_scores = score
        rank.append(current_index)
    else:
        current_index+=1
        txt.append(f'名字：{name}\t成绩:{score}\t排名:{current_index}')
        rank.append(mat)
with open("D:\总成绩排名.txt",'a+',encoding='utf-8') as test:
        test.truncate(0)
txt_1 = open("D:\总成绩排名.txt",'a',encoding='utf-8')
for items in txt:
    txt_1.write(items)
o+=1
dic_0 = dict(zip(names_1,rank))
while True:
    keyboard_input= input("\n三国成绩查询,请输入武将姓名或输入退出以离开系统\n")
    if keyboard_input == '退出':
        break
    else:
        print('总分：'+str(dic[keyboard_input]))
        print('排名：'+str(dic_0[keyboard_input]))