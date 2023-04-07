import numpy as np

A = np.array([
    [3, 7],
    [2, 3]
], subok=True)

B = np.array([
    [3, 4],
    [2, -1]
], subok=True)

C = A * B
print(C)

#print(help(np.array))
print(help(np.arange))
#print(help(np.zeros))