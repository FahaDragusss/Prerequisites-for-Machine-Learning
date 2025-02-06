import numpy as np

# Search
np1 = np.array([1,2,3,4,5,6,7,8,9,10])

x = np.where(np1==3) #Look in np1 and return the index tuple
print(np1)
print(x)
print(x[0])

# more than one 3
np2 = np.array([1,2,3,4,5,6,7,8,9,10,3])

y = np.where(np2==3)
print(np2)
print(y)
print(f'Printing the location of the 3 {y[0]}')
print(f'Printing all the 3 {np2[y[0]]}')

# Return the even items
print(f'Returning the even numbers')
z = np.where(np1 % 2 == 0)
print(np1)
print(f'Indexes{z[0]}')
print(np1[z[0]])

# Returning the Odd items
print(f'Returning the odd numbers')
h = np.where(np1 % 2 == 1)
print(np1)
print(f'Indexes{h[0]}')
print(np1[h[0]])


