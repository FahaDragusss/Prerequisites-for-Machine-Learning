import numpy as np

# Filtering numpy Arrays with Boolean Index Lists

np1 = np.array([1,2,3,4,5,6,7,8,9,10])

x = [True, True, False, False, False, False, False, False, False, False]

print(np1)
print(np1[x])

'''
# Filtering Even from Odd
filtered = []
for thing in np1:
    if thing % 2 == 0: # We can change logic 
        filtered.append(True)
    else:
        filtered.append(False)

print(f'Filteration in play')
print(np1)
print(filtered)
print(np1[filtered])
'''

# Shortcut
filtered = np1 % 2 == 0 #Change logic for situation
print(np1)
print(filtered)
print(np1[filtered])






