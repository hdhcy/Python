import numpy as np

a=np.array([
    [1,1],
    [0,1]
])
b=np.arange(4).reshape((2,2))

c=a-b
d=a+b
e=a*b
f=a**2
g=10*np.sin(a)
f=10*np.tan(a)
h=b<3#b中小于3的元素
i=b==3#b中等于3的元素
j=a*b#逐个相乘
k=np.dot(a,b)#矩阵的乘法
l=a.dot(b)#另外一种矩阵乘法形式

x=np.random.random((2,4))#默认在0-1的范围内
print(x)
print(x.sum(),x.min(),x.max())
print(np.sum(x),np.min(x),np.max(x))
print(np.sum(x,axis=1))#分别对行求和
print(np.sum(x,axis=0))#分别对列求和
print(np.max(x,axis=1))#对于每一行找到最大值
print(np.max(x,axis=0))#对于每一列找到最大值
