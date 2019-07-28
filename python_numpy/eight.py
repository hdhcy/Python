import numpy as np

a=np.arange(4)

print(a)

#这样的赋值，把a,b,c,d都指向同一个空间地址，b,c,d都会跟着a来发生变化,同时b,c,d的改变也会引起a的改变
b=a
c=a
d=b
a[0]=11
print(a)
print(d)

print(b is a)

b[0]=13
print(a)

b=a.copy()#deep copy b对a进行深度的copy,创建一个新的空间，b和a的改变都不会影响到对方

print(a)
print(b)

a[0]=22
print(a)
print(b)