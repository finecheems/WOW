import numpy as np
import paddle as paddle
import matplotlib.pyplot as plt
from paddle import nn
from paddle.metric import Accuracy
from paddle.vision.transforms import Compose, Normalize
transform = Compose([Normalize(mean=[127.5],std=[127.5],data_format='CHW')])
# 使用transform对数据集做归一化
print('下载并加载训练数据')
train_dataset = paddle.vision.datasets.MNIST(mode='train', transform=transform)
test_dataset = paddle.vision.datasets.MNIST(mode='test', transform=transform)
print('加载完成')
class MYCONV(nn.Layer):
    def __init__(self, in_chanel, out_chanel, kernel_size=(3, 3), stride=(1, 1), padding="SAME"):
        super(MYCONV, self).__init__()
        self.conv = nn.Conv2D(in_chanel, out_chanel, kernel_size, stride, padding)
        self.bn = nn.BatchNorm(out_chanel)
        self.relu = nn.ReLU()
    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x)
        x = self.relu(x)
        return x
class Mnist(nn.Layer):
    def __init__(self):
        super(Mnist, self).__init__()
        self.conv1 = MYCONV(1, 16, kernel_size=(3, 3), stride=(1, 1), padding="SAME")
        self.conv2 = MYCONV(16, 32, kernel_size=(3, 3), stride=(1, 1), padding="SAME")
        self.avgpool1 = nn.AvgPool2D(kernel_size=2, stride=2, padding=0)
        self.conv3 = MYCONV(32, 64, kernel_size=(3, 3), stride=(1, 1), padding="SAME")
        self.conv4 = MYCONV(64, 32, kernel_size=(3, 3), stride=(1, 1), padding="SAME")

        self.gap = nn.AdaptiveAvgPool2D(1)
        self.flatten = nn.Flatten()
        self.linear_1 = nn.Linear(32, 16)

        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.2)
        self.linear_2 = nn.Linear(16, 10)
    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.avgpool1(x)
        x = self.conv3(x)
        x = self.conv4(x)
        x = self.gap(x)
        x = self.flatten(x)
        x = self.linear_1(x)
        x = self.relu(x)
        x = self.linear_2(x)
        return x
# 用Model封装模型
model = paddle.Model(Mnist())
# 定义损失函数
optim = paddle.optimizer.Adam(learning_rate=0.001, parameters=model.parameters())
# 配置模型
model.prepare(optim, paddle.nn.CrossEntropyLoss(), Accuracy())
# 训练保存并验证模型
model.fit(train_dataset, test_dataset, epochs=2, batch_size=64, save_dir='multilayer_perceptron', verbose=1)
test_data0, test_label_0 = test_dataset[1][0],test_dataset[1][1]
test_data0 = test_data0.reshape([28,28])
plt.figure(figsize=(2,2))
#展示测试集中的第一个图片
print(plt.imshow(test_data0, cmap=plt.cm.binary))
print('test datag 的标签为: ' + str(test_label_0))#模型预测
result = model.predict(test_dataset, batch_size=1)#打印模型预测的结果
print('test_data 预测的数值为: %d'% np.argsort(result[0][1])[0][-1])