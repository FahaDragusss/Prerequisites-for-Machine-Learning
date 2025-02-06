import numpy as np

# np.sort()
np1 = np.array([6,8,5,7,2,3,4,1])
print(np1)
print(np.sort(np1))

# Alphabetical
np2 = np.array(['Melissa','Fedosev','Marie','Anna','Zagreus','Trisha','Meliodus','Sarah','Xavier','Anton','Elijah'])
print(np2)
print(np.sort(np2))

# Boolean T/F
np3 = np.array([True,False,True,False])
print(np2)
print(np.sort(np2))

# Sorting is essentially returning a copy

print(f'Sorting is a copy, so original is unchanged')
print(np1)
print(np.sort(np1))
print(f'Original NP1 {np1}')

# Sorting 2D
np4 = np.array([[5,4,2,3,1],[10,7,9,8,6]])
print(np4)
print(np.sort(np4))

