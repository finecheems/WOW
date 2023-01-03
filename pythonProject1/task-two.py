#coding = utf-8
import numpy as np
def main():
    list = []
    n = int(input("请输入矩阵的阶数"))
    shuliang = n*n
    m = input("请输入{}个数字以生成矩阵,请以空格分割".format(shuliang))
    m_2 = m.rstrip().split()
    for item in m_2:
        list.append(int(item))
    origal_matrix = np.reshape(np.array(list), (n, n))
    print(origal_matrix)
    input("此为生成的矩阵，请按任意键继续")
    Transpose_matrix = origal_matrix.T
    Cw90_matrix = np.rot90(origal_matrix,k = 3)
    print(Transpose_matrix)
    print(Cw90_matrix)
    input("上述分别为原矩阵的转置矩阵和顺时针旋转90度后得到的矩阵，请按任意键退出程序")
main()
