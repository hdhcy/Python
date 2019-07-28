import numpy as np

A=np.array([1,1,1])
B=np.array([2,2,2])

C=np.vstack((A,B))
print(np.vstack((A,B)))#vertical stack 进行上下合并

print(A.shape,C.shape)

D=np.hstack((A,B))#horizontal stack 进行左右合并

print(D)
print(A.shape,D.shape)

print(A[np.newaxis,:].shape)#对矩阵A的行上面加上一个维度
print(A[:,np.newaxis].shape)#对矩阵A的列上面加上维度

E=np.array([1,1,1])[:,np.newaxis]
F=np.array([2,2,2])[:,np.newaxis]

G=np.vstack((E,F))
H=np.hstack((E,F))

print(G)
print(H)

I=np.concatenate((E,F,F,E),axis=0)#对于多个矩阵进行上下合并
J=np.concatenate((E,F,F,E),axis=1)#对于多个矩阵进行左右合并
print(I)
print(J)