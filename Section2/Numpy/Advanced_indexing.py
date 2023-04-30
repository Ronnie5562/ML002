import numpy as np

Row_Matrix = np.arange(1, 10)


Two_Dim_Matrix = np.array(
    [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
)


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
        [[25, 26, 27, 28], [29, 30, 31, 32], [33, 34, 35, 36]],
    ]
)

#   INTEGER INDEXING.

index1 = np.array(
    [3, 6, 8]
)  # 3,6 and 9 indicates the index of the required elements in an array.
INT_A = Row_Matrix[
    index1
]  # Now, A contains the values of Row_Matrix that are in indexes 3,6 and 9. This is the basic concept of Advanced Indexing
print(INT_A)
# We can also index the array repeatedly.
index2 = np.array([1, 3, 4, 3, 4, 1])
INT_B = Row_Matrix[index2]
print(INT_B)
# NOTE: We can also use the regular python list to create the index array.


# Let's say we want to extract Two_Dim_Matrix04 and Two_Dim_Matrix23
index3 = ([0, 2], [4, 3])  # This represents (list of their rows, list of their columns)
INT_C = Two_Dim_Matrix[index3]
print(INT_C)

#   BOOLEAN INDEXING
"""_summary_
Boolean indexing is basically all about using boolean expressions to slice an array.
"""
BOOL_A = Two_Dim_Matrix[Two_Dim_Matrix < 7]
print(BOOL_A)

Two_Dim_Matrix2 = np.array([[1, -2, 65, -31, 5], [61, 12, -32, -9, 10]])

BOOL_B = Two_Dim_Matrix2[Two_Dim_Matrix2 < 0]
print(BOOL_B)
