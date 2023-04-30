"""_summary_
    The else in a python loop acts like a Nobreak statement.
    it runs the code you put in it if there was break in the loop above it.
"""

NAMES = ["Richard", "Sharon", "benita", "Ronald", "Iremide"]
NAMES2 = ["Jay Jay", 1]

for name in NAMES:
    if type(name) == str:
        print(name)
    else:
        break
else:
    print("All names are of type string")

# Notice that the code in the else block ran.
# Now, change the the iterable in the code above to { NAME2 } and see the reaction of the code.
