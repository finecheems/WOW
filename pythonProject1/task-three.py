class Student():
    def __init__(self,name,sum_score,chinese_score,math_score,english_score,quan_score):
        self.name = name
        self.chinese_score = chinese_score
        self.math_score = math_score
        self.english_score = english_score
        self.sum_score = sum_score
        self.quan_score =quan_score
    def registration(self):
        print(f'{self.name} {self.sum_score}')
welcome = int(input("进入三国学院成绩排序系统，请输入总人数"))
if welcome > 0:
    print("请依次输入学生的姓名，语、数、英成绩，并以空格分割")
shuru = []
name = []
score = []
chinese_score = []
math_score = []
english_score = []
quan_score = []
students = []
#得到初始数据
for i in range(welcome):
     shuru.append(list(map(str,input().rstrip().split())))
#得到名字
for l in shuru:
    name.append(l[0])
    l.pop(0)
#得到语文、数学、英语和总成绩
for i in shuru:
    middle =0
    chinese_score.append(int(i[0]))
    math_score.append(int(i[1]))
    english_score.append(int(i[2]))
    for st in i :
        middle+=int(st)
    score.append(middle)
#得到加权成绩
for i in range(welcome):
    quan_score.append((score[i]*1)+(chinese_score[i]*0.5)+(math_score[i]*0.3)+(english_score[i]*0.2))
for i in range(welcome):
    students.append(Student(name[i],score[i],chinese_score[i],math_score[i],english_score[i],quan_score[i]))
for self in students:
    for i in range(welcome - 1):
        for j in range(welcome - i - 1):
            if students[j].quan_score < students[j + 1].quan_score:
                students[j], students[j + 1] = students[j + 1], students[j]
        continue
for student in students:
    student.registration()