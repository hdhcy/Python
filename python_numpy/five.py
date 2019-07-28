import numpy as np

A=np.arange(3,15).reshape((3,4))
print(A)
print(A[2])#输出第二行
print(A[1][1])#输出第一行第一列的数字8
print(A[1,1])#另外一种表达形式

print(A[2:])#输出第二行的所有数
print(A[:1])#输出第一列的所有数
print(A[1,1:2])#输出第一行中下标从1到2的数，左闭右开，即包含下标1不包含下标2

for row in A: #默认迭代矩阵中的行
    print(row)

for column in A.T: #使用矩阵的翻转矩阵，得到行
    print(column)

print(A.flatten())#将矩阵转换成只有一行的数组，矩阵
for item in A.flat:
    print(item)
