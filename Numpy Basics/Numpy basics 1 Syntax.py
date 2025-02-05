import numpy as np

#Basic Array creation

np1 = np.array([0,1,2,3,4,5,6])
print(np1)
print(np1.shape)

#Range
np2 = np.arange(10)
print(np2)

#Step (from, to, step)
np3 = np.arange(0,10,2)
print(np3)

#Zeros
np4 = np.zeros(10)
print(np4)

#Multidimentional Zeros((Dimensions, Items in dimensions))
np5 = np.zeros((2,10))
print(np5)

#Full ((item quantity),value)
np6 = np.full((10),6)
print(np6)

#Multidimensional Full ((dimensions,item quantity),value)
np7 = np.full((2,10),6)
print(np7)

#Convert Python lists to np array
list1 = [1,2,3,4,5]
np8 = np.array(list1)
print(np8)

#Iterates the same way as python lists from 0 to n
print(np8[0])
print(list1[0])
