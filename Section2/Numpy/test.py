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
#print(help(np.arange))
#print(help(np.zeros))

LN1 = np.linspace(1, 35, dtype=complex, num=5)
print(LN1)

lp = np.eye(10, dtype=complex)

print(lp)

stuff = np.zeros(shape=(2,3), dtype=int)
print(stuff)
print(stuff.ndim)
print(stuff.size)
print(stuff.shape)
print(stuff.dtype)
print(stuff.itemsize)

New_Stuff = np.array([[10, 20, 30], [40, 50, 60]])
print(New_Stuff)
print(New_Stuff.shape)

new_Array = np.arange(1, 41, 2)

print(new_Array.reshape((5,4)))
new_Array.resize((6, 8))
print(new_Array)
