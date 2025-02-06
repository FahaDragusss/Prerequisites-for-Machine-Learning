import numpy as np

# Copy vs View
#-------------
#Copy is a copy of the array
#A view is a copy of the array but is conencted to the original

np1 = np.array([0,1,2,3,4,5])
np3 = np.array([0,1,2,3,4,5])

#Create a view
print(f'Create a view')

np2 = np1.view()

print(f'Original NP1 {np1}')
print(f'Original NP2 {np2}')

np1[0] = 41

print(f'Changed NP1 {np1}')
print(f'Original NP2 {np2}')

#When we change the original in view we also change the 'copy'

#Create a copy
print(f'Create a Copy')

np4 = np3.copy()
print(f'Original NP3 {np3}')
print(f'Original NP4 {np4}')

np3[0] = 41

print(f'Changed NP3 {np3}')
print(f'Original NP4 {np4}')

#Chaging the Original doesnt effect the copy when the copy is made with the copy funtion.