"""__Numpy Array Functions__
1. Array() ==>  It creates an Array from lists or tuples.
2. Arange() ==> It creates an Array of evenly spaced values within a given interval.
"""

import numpy as np
#  1. Array():
# To get info about the numpy array() function, run ==> print(help(np.array))

LI1 = np.array([1,2,3,4,])
LI2 = np.array([1,2,3,4,2.5,3.7])
LI3 = np.array([1,2,3,4,2.5,3.7,'d'])
print('array() function')
print(LI1)
print(LI2)
print(LI3)
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
print('arange() function')
print(AR1)
print(AR2)
print(AR3)
print()