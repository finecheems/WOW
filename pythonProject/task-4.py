#coding=utf-8
import time
class Pet(object):
    def __init__(self,name):
        self.name = name 
        self.live = 100
        self.lastMeal = time.time()
        self.bornTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    def die(self):
        now_time = time.time()
        time_leg = now_time-MyPet.lastMeal
        MyPet.live-=(time_leg*4)
        if MyPet.live<=0:
            print('对不起，由于太长时间没有喂食，您的宠物{}已经饿死了...'.format(MyPet.name))
        else:
            print('距离上次喂食已经过去{}秒\n生命值:{}'.format(time_leg,MyPet.live))
def main_0():
    return input('\n请给你的宠物起个名字\n')
MyPet = Pet(main_0())
while True:
    if MyPet.live<=0:
        break
    else:    
        def main_1():
            return input('"主人您好,你想对我做什么"\n1.问名字 2.喂食 3.问生日 4.打招呼 5.说“我爱你” 6.让我唱歌\n')
        order = int(main_1())
        if order == 1:
            print('"你叫什么名字鸭?"\n"我叫{}\n"'.format(MyPet.name))
            MyPet.die()
        elif order == 2:
            MyPet.live = 100
            MyPet.lastMeal = time.time()
            print('"给你好吃的!"\n"谢谢主人,{}吃饱了"\n'.format(MyPet.name))
            MyPet.die()
        elif order == 3:
            print('"你的生日是什么时候鸭?"\n"我的生日是{}"\n'.format(MyPet.bornTime))
            MyPet.die()
        elif order == 4:
            print('"你好,{}"\n"主人和我说话了,{}好开心"\n'.format(MyPet.name,MyPet.name))
            MyPet.die()
        elif order == 5:
            print('"我爱你"\n"不要呀,{}还小呀"\n'.format(MyPet.name))
            MyPet.die()
        elif order ==6:
            print('"{},给我唱首歌吧"\n"叮叮当,叮叮当,铃儿响叮当"\n'.format(MyPet.name))
            MyPet.die()
        else:
            print('"主人在说什么鸭,{}的大脑过载了"\n'.format(MyPet.name))
            MyPet.die()