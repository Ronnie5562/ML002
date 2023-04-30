import numpy as np

Row_Matrix = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])


Two_Dim_Matrix = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])


Three_Dim_Matrix = np.array(
    [
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [
                9,
                10,
                11,
                12,
            ],
        ],
        [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]],
    ]
)


#   INDEXING IN NUMPY

print("_____________________{ INDEXING }________________________")
print()

print(Row_Matrix.ndim, "Dimensional Matrix")
X = Row_Matrix[4]
Y = Row_Matrix[-1]
print(X * Y)


print(Two_Dim_Matrix.ndim, "Dimensional Matrix")
X = Two_Dim_Matrix[0][-1]
Y = Two_Dim_Matrix[1][0]
print(X * Y)


print(Three_Dim_Matrix.ndim, "Dimensional Matrix")
X = Three_Dim_Matrix[0][1][3]
Y = Three_Dim_Matrix[1][-2][-4]
print(X * Y)

print("_________________________________________________________")


#   SLICING IN NUMPY

print("_____________________{ SLICING }________________________")
print()

print(Row_Matrix.ndim, "Dimensional Matrix")
#   SYNTAX ==> array_name[start:stop:step]
X = Row_Matrix[2:6]
Y = Row_Matrix[3::2]
print(X)
print("______________________")
print(Y)
print()


print(Two_Dim_Matrix.ndim, "Dimensional Matrix")
#   SYNTAX ==> array_name[start:stop:step, start:stop:step]
X = Two_Dim_Matrix[1:, 1:]
Y = Two_Dim_Matrix[:, -3::-1]
print(X)
print("______________________")
print(Y)
print()


print(Three_Dim_Matrix.ndim, "Dimensional Matrix")
#   SYNTAX ==> array_name[start:stop:step, start:stop:step, start:stop:step]
X = Three_Dim_Matrix[:, :, -1:]
Y = Three_Dim_Matrix[:, 1:, ::2]
print(X)
print("______________________")
print(Y)

print("_________________________________________________________")
