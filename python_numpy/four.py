import numpy as np

A=np.arange(14,2,-1).reshape((3,4))

print(np.argmin(A))#返回最小值的索引
print(np.argmax(A))#返回最大值的索引
print(np.mean(A))#计算平均值
print(A.mean())#计算平均值的另外一种写法
print(np.average(A))#和mean一样计算平均值
print(np.median(A))#返回中位数
print(np.cumsum(A))#逐步累积，例如第三个数等于前三个数的值的和
print(np.diff(A))#每一行的相邻的数的差值，对比原先矩阵，少了一列
print(np.nonzero(A))#用两个数组表示非零元素的位置，第一个数组表示行数，第二个数组表示列数
print(np.sort(A))#对原始矩阵进行逐行排序
print(np.transpose(A))#反向矩阵，行变成列，列变成行
print(A.T)#反向矩阵的另外一种写法
print((A.T).dot(A))#矩阵的乘法运算
print(np.clip(A,5,9))#截取矩阵，小于5的数都等于5，大于9的数都等于9
print(np.mean(A,axis=0))#对于列进行计算平均值
print(np.mean(A,axis=1))#对于行进行计算平均值

print(A)