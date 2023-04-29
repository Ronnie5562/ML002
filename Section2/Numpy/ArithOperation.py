import numpy as np

"""_summary_
We can perform Addition, Subtraction, Multiplication and Division on Numpy arrays.
We perform those operations in two ways.
    ==> (1) Using Scalars
        (2) Using Arrays[matrix]
"""
# ONE DIMENSIONAL ARRAY

A1 = np.arange(1, 11)
ADD_A1 = A1 + 2
MUL_A1 = A1 * 10
SUB_A1 = A1 - 1
DIV1_A1 = 3 / A1
DIV2_A1 = A1 / 5
SQR_A1 = A1 ** 2

# Notice that the elements in ADD_A1 are higher than their respective value in A1 by 2.
print(A1, " ==> ", ADD_A1)
print(A1, " ==> ", MUL_A1)
print(A1, " ==> ", SUB_A1)
print(A1, " ==> ", DIV1_A1)
print(A1, " ==> ", DIV2_A1)
print(A1, " ==> ", SQR_A1)

print()
print('______________________________________________________________________')

# TWO DIMENSIONAL ARRAY
B1 = np.array([
    [1,2,3,4],
    [5,6,7,8]
])

ADD_B1 = B1 + 2
MUL_B1 = B1 * 10
SUB_B1 = B1 - 1
DIV1_B1 = 3 / B1
DIV2_B1 = B1 / 5
SQR_B1 = B1 ** 2

# Notice that the elements in ADD_B1 are higher than their respective value in B1 by 2.
print(B1, " ==> ", ADD_B1)
print(B1, " ==> ", MUL_B1)
print(B1, " ==> ", SUB_B1)
print(B1, " ==> ", DIV1_B1)
print(B1, " ==> ", DIV2_B1)
print(B1, " ==> ", SQR_B1)


"""_summary_
To perform arithmetic operations on array, we can also use the built-in methods
a + b ==> np.add(a, b)
a - b ==> np.subtract(a, b)
a * b ==> np.multiply(a, b)
a / b ==> np.divide(a, b)
a % b ==> np.mod(a, b)
a ** b ==> np.power(a, b)
"""