# """Pattern 1"""

# print("Pattern 1")
# n = int(input("Enter the number of rows: "))
# for i in range(1, n + 1):
#     print("*" * n)

# """Pattern 2"""

# print("Pattern 2")
# n = int(input("Enter the number of rows: "))
# for i in range(1, n + 1):
#     for j in range(n):
#         print(i, end="")
#     print()

# """Pattern 3"""

# print("Pattern 3")
# n = int(input("Enter the number of rows: "))
# for i in range(n):
#     for j in range(1, n + 1):
#         print(j, end="")
#     print()

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
