"""__Numpy Array Functions__
1. Array() ==>  It creates an Array from lists or tuples.
"""

import numpy as np
#  1. Array():
# To get info about the numpy array() function, run ==> print(help(np.array))

li1 = np.array([1,2,3,4,])
li2 = np.array([1,2,3,4,2.5,3.7])
li3 = np.array([1,2,3,4,2.5,3.7,'d'])
print(li1)
print(li2)
print(li3)

# Run the code above and carefully observe the data type of the elements in each array. What can you say about this?
# Basically, the type is determined as the minimum type required to hold the objects in the sequence.

