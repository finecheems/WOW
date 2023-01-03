import numpy as np
import paddle as paddle
from paddle.vision.transforms import Compose, Normalize
import paddle.fluid as fluid
from PIL import Image
import matplotlib.pyplot as plt
from paddle.metric import Accuracy
import os
from paddle.fluid.dygraph import Linear
print("本教程基于Paddle的版本号为："+paddle.__version__)
transform = Compose([Normalize(mean=[127.5],std=[127.5],data_format='CHW')])
# 使用transform对数据集做归一化
print('下载并加载训练数据')
train_dataset = paddle.vision.datasets.MNIST(mode='train', transform=transform)
test_dataset = paddle.vision.datasets.MNIST(mode='test', transform=transform)
print('加载完成')
train_data0, train_label_0 = train_dataset[0][0],train_dataset[0][1]
train_data0 = train_data0.reshape([28,28])
plt.figure(figsize=(2,2))
print(plt.imshow(train_data0, cmap=plt.cm.binary))
print('train_data0 的标签为: ' + str(train_label_0))
print(train_data0)
class Mnist(paddle.nn.Layer):
    def __init__(self,in_features,classes_num):
        super(Mnist, self).__init__()
        self.flatten = paddle.nn.Flatten()
        self.fc1 = paddle.nn.Linear(in_features=in_features, out_features=1024)
        self.relu1 = paddle.nn.Sigmoid()
        self.fc2 = paddle.nn.Linear(in_features=1024, out_features=512)
        self.relu2 = paddle.nn.Sigmoid()
        self.fc3 = paddle.nn.Linear(in_features=512, out_features=256)
        self.relu3 = paddle.nn.Sigmoid()
        self.fc4 = paddle.nn.Linear(in_features=256, out_features=128)
        self.relu4 = paddle.nn.Sigmoid()
        self.fc5 = paddle.nn.Linear(in_features=128, out_features=64)
        self.relu5 = paddle.nn.Sigmoid()
        self.fc6 = paddle.nn.Linear(in_features=64, out_features=32)
        self.relu6 = paddle.nn.Sigmoid()
        self.fc7 = paddle.nn.Linear(in_features=32, out_features=classes_num)
        # 请同学们在这里填写代码，别忘了是7层网络
    def forward(self, x):
        x = self.flatten(x)
        x = self.fc1(x)
        x = self.relu1(x)
        x = self.fc2(x)
        x = self.relu2(x)
        x = self.fc3(x)
        x = self.relu3(x)
        x = self.fc4(x)
        x = self.relu4(x)
        x = self.fc5(x)
        x = self.relu5(x)
        x = self.fc6(x)
        x = self.relu6(x)
        x = self.fc7(x)
        return x
# 请同学们在这里填写代码
# 用Model封装模型
model = paddle.Model(Mnist(in_features=28*28,classes_num=10))
# 定义损失函数
optim = paddle.optimizer.Adam(learning_rate=0.001, parameters=model.parameters())
# 配置模型
model.prepare(optim, paddle.nn.CrossEntropyLoss(), Accuracy())
# 训练保存并验证模型
model.fit(train_dataset, test_dataset, epochs=2, batch_size=64, save_dir='multilayer_perceptron', verbose=1)
# 训练保存并验证模型
model.fit(train_dataset,test_dataset,epochs=2,batch_size=64,save_dir='multilayer_perceptron',verbose=1)
# 获取测试集的第一个图片
test_data0, test_label_0 = test_dataset[1][0],test_dataset[1][1]
test_data0 = test_data0.reshape([28,28])
print('test_data0 的标签为: ' + str(test_label_0))
#模型预测
result = model.predict(test_dataset, batch_size=1)
#打印模型预测的结果
print('test_data0 预测的数值为：%d' % np.argsort(result[0][1])[0][-1])