with open("case.txt", "r", encoding="UTF-8") as f:
    readfile = f.readline()

    print(readfile)
    f.seek(10)
    print("The current cursor positon: ", f.tell())
    f.seek(20)
    print("The current cursor positon: ", f.tell())
    f.seek(30)
    print("The current cursor positon: ", f.tell())
    f.seek(40)
    print("The current cursor positon: ", f.tell())
    f.seek(50)
    print("The current cursor positon: ", f.tell())
    f.seek(60)
    print("The current cursor positon: ", f.tell())


# {  How to check a particular file exists or not ?  }
# We can use os library to get information about files in our computer.
# os module has path sub module, which contains isFile() function to check whether a particular file exists or not ?
# os.path.isfile(fname)

# Q. Write a program to check whether the given file exists or not . If it is available then print its content?

import os
import sys

fname = input("Enter the name of the file: ")

if os.path.isfile(fname):
    print(f"File exists: {fname}")
    f = open(fname, "r", encoding="UTF-8")
else:
    print(f"File does not exists: {fname}")
    sys.exit(0)  # ===> To exit system without executing rest of the program
print("The content of the file is: ")
data = f.read()
print(data)
