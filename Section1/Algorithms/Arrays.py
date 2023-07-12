
""" Arrays in Python
Learnt this concep from:
https://www.freecodecamp.org/news/python-array-tutorial-define-index-methods/

Both Arrays and lists store elements in contiguos memory locations but the difference bet them is that an Array can only take elements of the same data type while a list can contain elements of different data types.

Working with arrays in python requires us to import an external modul named `array`
"""


from array import array

"""
The general syntax to create an array:
    var_name = array(typecode, [elements])
"""

"""typecode :
    'i' - signed int
    'H' - unsigned short
    'd' - floating num
"""


elements = array('i', [-1,2,3,4,5,6])

elements.remove(5)

print(elements)