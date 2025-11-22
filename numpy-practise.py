import numpy as np

a = np.array([1,2,3])

b = np.array([[1,2,3],[4,5,6]])
#print(b)
# number of dimention
#print(a.ndim)
#print(b.shape)
#print(a.dtype)

#accessing and changing elements
c = np.array([[1,2,3],[4,5,6],[7,8,9]])
#print(c)
#print(c.shape)

#print(c[:,1:2])

c[1,2] = 99
print(c)