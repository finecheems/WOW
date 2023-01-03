import matplotlib.pyplot as plt
import numpy as np
factor_names = ['性别','长度','直径','高度','总重量','皮重','内脏重量','克重','年龄']
factor_num = len(factor_names)
datafile = "AbaloneAgePrediction.txt"
data_0 = np.genfromtxt(datafile,dtype = str,delimiter =',')
for i in range(len(data_0)):
    data_1=data_0[i]
    if data_1[0]=='M' or data_1[0]=='F':
        data_1[0] = 0
    else:
        data_1[0] = 1
    for o in range(1,8):
        data_1[0] = int(data_1[0])
        data_1[o] = float(data_1[o])
        data_1[8] = int(data_1[8])
data_0 = np.array(data_0)
b = []
for  data_1 in data_0:
    a = []
    for i in range(9):
        if i==0 or i ==8:
            a.append(int(data_1[i]))
        else:
            i_1 = float(data_1[i])
            a.append(i_1)
    b.append(a)
data_0 = np.array(b)
def load_data():
    ratio = 0.8
    offset = int(data_0.shape[0]*ratio)
    training_data = data_0[:offset]
    maximums,minimums,avgs = training_data.max(axis=0),training_data.min(axis=0),training_data.sum(axis=0) / training_data.shape[0]
    for i in range(factor_num):
        data_0[:,i] = (data_0[:,i]-avgs[i])/(maximums[i]-minimums[i])
    training_data = data_0[:offset]
    test_data = data_0[offset:]
    return training_data,test_data
class Network(object):
    def __init__(self,num_of_weights) :
        np.random.seed(0)
        self.w = np.random.randn(num_of_weights,1)
        self.b = 0.
    def forward(self,x):
        z = np.dot(x,self.w) + self.b
        return z
    def loss(self,z,y):
        error = z-y
        cost = error*error
        cost = np.mean(cost)
        return cost
    def gradient(self,x,y):
        z =  self.forward(x)
        gradient_w = (z-y)*x
        gradient_w = np.mean(gradient_w,axis=0)
        gradient_w = gradient_w[:,np.newaxis]
        gradient_b = (z-y)
        gradient_b = np.mean(gradient_b)
        return gradient_w,gradient_b
    def update(self,gradient_w,gradient_b,eta = 0.01):
        self.w = self.w-eta*gradient_w
        self.b = self.b-eta*gradient_b
    def train(self,x,y,iterations = 100,eta=0.01):
        losses = []
        for i in range(iterations):
            z = self.forward(x)
            L =self.loss(z,y)
            gradient_w,gradient_b = self.gradient(x,y)
            self.update(gradient_w,gradient_b,eta)
            losses.append(L)
            if (i+1)%10==0:
                print('iter{},loss{}'.format(i,L))
        return losses
if __name__=="__main__":
    train_data,test_data = load_data()
    x = train_data[:, :-1]
    y = train_data[:, -1:]
    net = Network(8)
    num_iterations = 10000
    losses = net.train(x,y,iterations=num_iterations,eta=0.01)
    plot_x = np.arange(num_iterations)
    plot_y = np.array(losses)
    plt.plot(plot_x,plot_y)
    plt.show()