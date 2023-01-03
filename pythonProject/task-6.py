import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.animation as animation
class People(object):
    def __init__(self):
        self.x=np.random.normal()
        self.y=np.random.normal()
        self.color='g'
    def get_loc(self):
        return self.x,self.y
    def get_color(self):
        return self.color
    def set_color(self,color):
        self.color=color
    def move(self):
        random=np.random.random()
        if random<0.25:
            self.x+=1
        elif 0.25<=random<0.5:
            self.x-=1
        elif 0.5<=random<0.75:
            self.y+=1
        else:
            self.y-=1
        if self.x>10.0:
            self.x -= 1.1
        elif self.x<-8.0:
            self.x += 1.1
        if self.y>8.0:
            self.y -= 1.1
        elif self.y<-8.0:
            self.y += 1.1
fig  = plt.figure(figsize=(10,10))
plt.xlim((-10,10))
plt.ylim((-10,10))
all_people=[]
for i in range(100):
    public=People()
    all_people.append(public)
sick_people=[]
scat = plt.scatter([x.get_loc()[0] for x in all_people],[x.get_loc()[1] for x in all_people],c=[x.get_color() for x in all_people])
def dis(a,b):
    d = math.sqrt((a.x-b.x)**2 + (a.y - b.y)**2)
    return d
def infect():
    all_people[int(len(all_people))-1].set_color('r')
    sick_people.append(all_people[int(len(all_people))-1])
def animate(i):
        print(i)
        for j in all_people:
            j.move()
        l_2 =[]
        if i>10:
            if len(sick_people)<2:
                infect()
            else:
                for j in sick_people:
                    for a in all_people:
                        if j.color==a.color:
                            continue
                        elif dis(j,a)<0.4:
                            a.set_color('red')
                            l_2.append(a)
                for j in l_2:
                    sick_people.append(j)
        scat.set_offsets([[x.get_loc()[0],x.get_loc()[1]] for x in all_people])
        scat.set_color([x.get_color() for x in all_people])
anim = animation.FuncAnimation(fig, animate, frames=100, interval=100, blit=False)
anim.save('1.gif',writer='imagemagick')
