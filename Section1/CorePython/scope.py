'''
L -> E -> G -> B ✅
B -> E -> G -> L ❌

Local, Enclosing, Global, Built-in.
    Local - Variables defined inside a functon.
    Global - Variables defined at the top level of a module.
    Built-in - Variables that are pre-defined in python.
'''

x = 'global x'

def scope():
    global z
    z = 'global z'
    y = 'local y'
    # print(x) ==> it throws an error ❌❌❌
    print(y)
    print(z)

# Without calling the scope function, { Z } remains local.
scope()

print(x)
# print(y) ==> it throws an error ❌❌❌
print(z)