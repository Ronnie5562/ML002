# I learnt this from Amulus Academy.
"""__Numpy Array Functions__
1. Array() ==>  It creates an Array from lists or tuples.
2. Arange() ==> It creates an Array of evenly spaced values within a given interval.
3. Zeros() ==> It creates an Array filled with zeros.
4. ones() ==>  It creates an Array filled with ones.
5. Empty() ==> It creates a new uninitialized array.
6. Linspace() ==> It creates Array filled with evenly spaced values.
7. Eye() ==> Returns array filled with zeros except in the k-th diagonal, whose values are equal to 1.
8. Identity() ==> The identity array is a square array with ones on the principal diagonal.
"""

import numpy as np

#  1. Array():
# To get info about the numpy array() function, run ==> print(help(np.array))

LI1 = np.array(
    [
        1,
        2,
        3,
        4,
    ]
)
LI2 = np.array([1, 2, 3, 4, 2.5, 3.7])
LI3 = np.array([1, 2, 3, 4, 2.5, 3.7, "d"])
print("1. array() function")
print(LI1)
print("______")
print(LI2)
print("______")
print(LI3)
print("______")
print()

# Run the code above and carefully observe the data type of the elements in each array. What can you say about this?
# Basically, the type is determined as the minimum type required to hold the objects in the sequence.


#  2. Arange():
# To get info about the numpy arrange() function, run ==> print(help(np.arange))
# SYNTAX ==> np.arange([start,] stop [,step], dtype=None)
# It is kind of similar to the actual range() function in python.

AR1 = np.arange(1, 10)
AR2 = np.arange(2, 20, 2)
AR3 = np.arange(2, 20, dtype="complex")
print("2. arange() function")
print(AR1)
print("______")
print(AR2)
print("______")
print(AR3)
print("______")
print()

#  3. Zeros():
# To get info about the numpy zeros() function, run ==> print(help(np.zeros))
# SYNTAX ==> np.zeros(shape, dtype=float,order='c')

AZ1 = np.zeros(5)
AZ2 = np.zeros((2, 4), dtype=int)
AZ3 = np.zeros((2, 3, 4), dtype=complex)
print("3. zeros() function")
print(AZ1)
print("______")
print(AZ2)
print("______")
print(AZ3)
print("______")
print()

#  4. ones():
# It has the same working principle as the zeros() function.

AZ1 = np.ones(5)
AZ2 = np.ones((2, 4), dtype=int)
AZ3 = np.ones((2, 3, 4), dtype=int)
print("4. ones() function")
print(AZ1)
print("______")
print(AZ2)
print("______")
print(AZ3)
print("______")
print()

# We also have another function that works like zeros() and ones() - empty(). This function creates a new uninitialized array. I nstaed of filling the array with either zeros or ones, it fills them with random values.
# You can also check out the full() function.

# 6. Linspace():

LIN1 = np.linspace(1, 100, num=5, retstep=True)
LIN2 = np.linspace(2, 45, retstep=True, endpoint=False)
print(LIN1)
print(LIN2)

# 7. Eye():

Matrix1 = np.eye(10)
Matrix2 = np.eye(3, 3, k=1)
Matrix3 = np.eye(3, 3, k=-1)
Matrix4 = np.eye(3, 3, k=-1, dtype=int)
Matrix5 = np.eye(10, 5)

print(Matrix1)
print(Matrix2)
print(Matrix3)
print(Matrix4)
print(Matrix5)

# 8. Identity():
# identity(n, dtype=None)

Identity_Matrix = np.identity(5, dtype=int)
print(Identity_Matrix)

# Numpy Random Module
# rand(): Creates an array of the given shape and populate it with random samples from a uniform distribution over [0,1]

rand = np.random.rand(4, 5)
print(rand)

# randn(): Creates array of specified shape and fils it with random values as per standard normal distribution

randn = np.random.randn(5, 2)
print(randn)

# ranf(): Creates array of specified shape and fils it with random floats in the half open interval [0.0, 1.0]

ranf = np.random.ranf(5)
print(ranf)

# randint(): Creates array of specified shape and fils it with random integers from low to high.
#           If high is not mentioned, then interval will be [0, low]

randint = np.random.randint(low=4, high=10, size=(3, 4))
print(randint)

"""__Numpy Array Attributes__
(1) .ndim - To get the number on dimensions has array posess.
(2) .shape - It returns the (row, column) representation of an array.
(3) .size - It returns the number of elements in the array.
(4) .dtype - It returns the data type of the elements contained in the array.
(5) .itemsize - It returns the size of each element in an array in byte.
"""


A = np.random.randn(10, 5)
print(A)
