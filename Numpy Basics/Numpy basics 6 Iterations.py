import numpy as np

# 1D
np1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(np1)

for x in np1:
    print(x)

print(f'Now for 2D')

# 2D
np2 = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
print(f'{np2}')

print(f'Rows only')
for x in np2:
    # Print rows
    print(x)
print(f'All elements')
for x in np2:
    for y in x:
        print(y)

print(f'Now for 3D')

# 3D
np3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(f'{np3}')

print(f'All elements')
for x in np3:
    for y in x:
        for z in y:
            print(z)

# Use np.nditer()

print(f'Now we use np.nditer')
for x in np.nditer(np3):
    print(x)