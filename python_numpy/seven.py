import numpy as np

A=np.arange(12).reshape((3,4))

print(A)

print(np.split(A,2,axis=1))#对原始矩阵A的列分成两块
print(np.split(A,3,axis=0))#对原始矩阵A的行分成三块
#split不能进行不等的分割

print(np.array_split(A,3,axis=1))#可以利用array_split函数进行不等量的分割

print(np.vsplit(A,3))#进行横向分割成三块
print(np.hsplit(A,2))#进行纵向分割成两块
#vsplit和hsplit也不能进行不等的分割