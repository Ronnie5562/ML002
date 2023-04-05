"""__Numpy Array Functions__
1. Array() ==>  It creates an Array from lists or tuples.
2. Arange() ==> It creates an Array of evenly spaced values within a given interval.
3. Zeros() ==> It creates an Array filled with zeros.
4. Empty() ==> It creates a new uninitialized array.
"""

import numpy as np
#  1. Array():
# To get info about the numpy array() function, run ==> print(help(np.array))

LI1 = np.array([1,2,3,4,])
LI2 = np.array([1,2,3,4,2.5,3.7])
LI3 = np.array([1,2,3,4,2.5,3.7,'d'])
print('1. array() function')
print(LI1)
print('______')
print(LI2)
print('______')
print(LI3)
print('______')
print()

# Run the code above and carefully observe the data type of the elements in each array. What can you say about this?
# Basically, the type is determined as the minimum type required to hold the objects in the sequence.


#  2. Arange():
# To get info about the numpy arrange() function, run ==> print(help(np.arange))
# SYNTAX ==> np.arange([start,] stop [,step], dtype=None)
# It is kind of similar to the actual range() function in python.

AR1 = np.arange(1,10)
AR2 = np.arange(2,20,2)
AR3 = np.arange(2, 20, dtype="complex")
print('2. arange() function')
print(AR1)
print('______')
print(AR2)
print('______')
print(AR3)
print('______')
print()

#  3. Zeros():
# To get info about the numpy zeros() function, run ==> print(help(np.zeros))
# SYNTAX ==> np.zeros(shape, dtype=float,order='c')

AZ1 = np.zeros(5)
AZ2 = np.zeros((2,4), dtype=int)
AZ3 = np.zeros((2,3,4), dtype=int)
print('3. zeros() function')
print(AZ1)
print('______')
print(AZ2)
print('______')
print(AZ3)
print('______')
print()

#  4. ones():
# It has the same working principle as the zeros() function.

AZ1 = np.ones(5)
AZ2 = np.ones((2, 4), dtype=int)
AZ3 = np.ones((2, 3, 4), dtype=int)
print('4. ones() function')
print(AZ1)
print('______')
print(AZ2)
print('______')
print(AZ3)
print('______') 
print()

# We also have another function that works like zeros() and ones() - empty(). This function creates a new uninitialized array. I nstaed of filling the array with either zeros or ones, it fills them with random values.
# You can also check out the full() function.