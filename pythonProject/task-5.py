import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
class Planets(object):
    def __init__(self,r,color,size):
        self.r = r
        self.color = color
        self.size = size
shuixing,jingxing,diqiu,huoxing,muxing,tuxing  = Planets(2,'black',10),Planets(3,'pink',10),Planets(4,'blue',25),Planets(5,'orange',15),Planets(6,'brown',35),Planets(7,'yellow',30)
fig,ax = plt.subplots()
r_list=[2,3,4,5,6,7]
o_list=[13,9,7,6,5,4]
t_range=np.arange(0,1+0.00005,0.00005)
x_l_list=[]
y_l_list=[]
for i in range(len(r_list)):
    x_l_list.append(r_list[i]*np.cos(o_list[i]*np.pi*t_range))
    y_l_list.append(r_list[i]*np.sin(o_list[i]*np.pi*t_range))
l1 = ax.plot(x_l_list[0],y_l_list[0],'black',linewidth=0.5)#行星轨道开始
l2 = ax.plot(x_l_list[1],y_l_list[1],'black',linewidth=0.5)
l3,= ax.plot(x_l_list[2],y_l_list[2],'black',linewidth=0.5)
l4, = ax.plot(x_l_list[3],y_l_list[3],'black',linewidth=0.5)
l5,= ax.plot(x_l_list[4],y_l_list[4],'black',linewidth=0.5)
l6, = ax.plot(x_l_list[5],y_l_list[5],'black',linewidth=0.5)#行星轨道完成    
l1, = ax.plot([],[],marker='o',color=shuixing.color,markersize=shuixing.size)#行星写入开始
l2, = ax.plot([],[], marker='o', color=jingxing.color,markersize=jingxing.size)
l3,= ax.plot([],[],marker='o',color=diqiu.color,markersize=diqiu.size)
l4, = ax.plot([],[],marker='o',color=huoxing.color,markersize=huoxing.size)
l5,= ax.plot([],[],marker='o',color=muxing.color,markersize=muxing.size)
l6, = ax.plot([],[],marker='o',color=tuxing.color,markersize=tuxing.size)#行星写入完毕
ax.plot([0],[0],color='red',marker='o',markersize=50)
def init():
    ax.set_xlim(-10,10)
    ax.set_ylim(-10,10)
    return l1,l2,l3,l4,l5,l6
def update(frame):
    l1.set_data(shuixing.r*np.cos(frame*1.2), shuixing.r*np.sin(frame*1.2))
    l2.set_data(jingxing.r*np.cos(frame), jingxing.r*np.sin(frame))
    l3.set_data(diqiu.r*np.cos(frame*0.9), diqiu.r*np.sin(frame*0.9))
    l4.set_data(huoxing.r*np.cos(frame*0.85), huoxing.r*np.sin(frame*0.85))
    l5.set_data(muxing.r*np.cos(frame*0.5), muxing.r*np.sin(frame*0.5))
    l6.set_data(tuxing.r*np.cos(frame*0.45), tuxing.r*np.sin(frame*0.45))
    return l1,l2
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 4*np.pi, 200),  init_func=init, blit=False)
ani.save('stars.gif', writer='Pillow', fps=30)
plt.show()