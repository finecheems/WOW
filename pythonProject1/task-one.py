#coding=utf-8
import random
def du(numbers):
    num_du = numbers.count(max(numbers,key=numbers.count))
    return num_du
#求数度的函数
def circulate(b):
    zhongshus = []
    origal_du = du(b)
    while du(b) == origal_du:
        zhongshu = max(b, key=b.count)
        middle.remove(zhongshu)
        zhongshus.append(zhongshu)
    return zhongshus
#计算众数集的函数
nums = []
i = 0
middle = []
lens = []
while i < 10:
    nums.append(random.randint(0,10))
    i+=1
for p in nums:
    middle.append(p)
num_du = du(nums)
zhongshus = circulate(middle)
print(nums)
for item in zhongshus:
    rax = 0
    list = []
    for i in nums :
        if rax == 0:
            if i == item:
                rax+=1
                list.append(i)
        elif rax == num_du:
            break
        else:
            if i == item:
                rax += 1
            list.append(i)
    lens.append(len(list))
#得到度相同的连续子数组的长度
answer = min(lens)
print(answer)