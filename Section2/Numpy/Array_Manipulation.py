"""___Array Manipulation___
We can manipulate numpy arrays in different ways one of which is performing arith,etic operations on it.
In this module, I am going to be learning about other ways in which a numpy array can be manipulated.
(1) Reshape: We can reshape an array in two ways:
    ==> [A] By using the reshape() function
    ==> [B] By using the resize() function
(2) Flatten: We can Flatten an array in two ways:
    ==> [A] By using the flatten() function
    ==> [B] By using the ravel() function
(2) Transpose: We can Transpose an array in two ways:
    ==> [A] By using the transpose() function
    ==> [B] By using the swapaxes() function
"""
import numpy as np

# A1. Reshape:

Array_1 = np.arange(10)
Reshaped_Array_1_Order_C = np.reshape(Array_1, (2, 5))
print(Reshaped_Array_1_Order_C)

Reshaped_Array_1_Order_F = np.reshape(Array_1, (2,5), order='F') # The default order is 'C' which is a row implementation of data, while F is a columnn implementation. Check out the difference between Reshaped_Array_1 and Reshaped_Array_1_Order_F.
print(Reshaped_Array_1_Order_C)

# You can also use:
x = Array_1.reshape((2,5))
print(x)

# A2. Resize:

Array_2 = np.arange(0, 41, 2)
Resized_Array_2 = np.resize(Array_2, (10,10))
print(Resized_Array_2)

# You can also use:
Array_2.resize((5,10)) # This does not return anything. It resizes the opriginal array directly.


# B1. Flatten:
Array_3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
Array_3_flatten = Array_3.flatten(order='F') # The default order of this operation is 'C'
print(Array_3_flatten)

# B2. Ravel:

Array_3_flatten_ravel = Array_3.ravel()
print(Array_3_flatten_ravel)

# C1. Transpose: it changes the axes of a matrix - e.g (2,5) becomes (5,2), (2,3,4) ==> (4,3,2).

Array_4 = np.arange(1,11).reshape(5,2)
Array_4_transposed = Array_4.transpose( )
print(Array_4_transposed)

# C2.  