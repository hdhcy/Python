import numpy as np

a=np.array([2,3,4],dtype=np.float)

b=np.array([
    [1,2,3],
    [4,5,6]
])

c=np.zeros((3,3))
d=np.ones((3,4),dtype=np.int16)
e=np.empty((3,4))
f=np.arange(10,20,2)
g=np.arange(12).reshape((3,4))
h=np.linspace(1,10,5)#最后一个参数表示生存几段
i=np.linspace(1,10,6).reshape((2,3))
print(h)