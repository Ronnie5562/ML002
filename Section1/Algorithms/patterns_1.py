"""Pattern 1"""

print("Pattern 1")
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    print("*" * n)

"""Pattern 2"""

print("Pattern 2")
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    for j in range(n):
        print(i, end="")
    print()

"""Pattern 3"""

print("Pattern 3")
n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(1, n + 1):
        print(j, end="")
    print()

"""Pattern 4"""

print("Pattern 4")
n = int(input("Enter the number of rows: "))
for letter in range(1, n + 1):
    for j in range(n):
        print(chr(64 + letter), end="")
    print()

"""Pattern 5"""

print("Pattern 5")
n = int(input("Enter the number of rows: "))
for letter in range(n):
    for j in range(1, n + 1):
        print(chr(64 + j), end="")
    print()

"""Pattern 6"""

print("Pattern 6")
n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n):
        print(n - i, end="")
    print()

"""Pattern 7"""

print("Pattern 7")
n = int(input("Enter the number of rows: "))
for letter in range(1, n + 1):
    for j in range(n):
        print(chr(65 + n - letter), end="")
    print()

"""Pattern 8"""

print("Pattern 8")
n = int(input("Enter the number of rows: "))
for i in range(n):
    for letter in range(1, n + 1):
        print(chr(65 + n - letter), end="")
    print()

"""Pattern 9"""
print("Pattern 9")
n = int(input("Enter the number of rows: "))
for j in range(1, n + 1):
    print("*" * j)
print()