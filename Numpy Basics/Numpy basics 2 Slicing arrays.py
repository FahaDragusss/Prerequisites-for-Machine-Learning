import numpy as np

#Slicing Numpy Arrays
np1 = np.array([1,2,3,4,5,6,7,8,9])

#Returning 2,3,4,5 
print(np1[1:5]) #Works differently that python eventhough the last element is 4th 
#in the list our syntax logic is that we slice till 5th but 5th isnt included lets
# see how it works if we want to print the last 3 elements

#Returning Last 3 elements
print(np1[6:10]) #Even though there isnt a item at the 10 position but slicing till
#10th means not the 10th item

print(np1[6:]) #Returning the last 3 elements

#Negative slices
#7 , 8
print(np1[-3:-1]) #till -1 not also -1
print(np1[-3:]) #As python reads from left to right once we are at -3rd item we move 
# in towards the right and print the list until the whole listis printed

#Steps
print(np1[1:5]) #2-5
print(np1[1:5:2]) #2-5 in 2 steps
print(np1[::2]) #Steps of 2 the whole list

#Slice a 2-d array
np2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

#Pull out a single item
print(np2[1,2]) #Pull out 8

#Slice a 2d array [which dimensions,what from the selected dimensions]
print(np2[0:1,1:3])
print(np2[0:2,1:3]) #Both syntax works as the logic we made
print(np2[0:,1:3])