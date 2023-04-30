import numpy

# List vs Numpy arrays

a = numpy.array([2, 4, 6, 8, 10, 12, 14, 16])
print(a)
print(a / 2)

b = [2, 4, 6, 9, 10, 12, 14, 16]
print(b)
print(b / 2)
# Notice that a{The numpy array} was divided by 2, and all its elements were actually divided by two. but b{The python list} threw an error when the division operation was performed on it.
