#               Example 1

#nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#my_list = [n for n in nums]

#               Example 2

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#my_list = []
# for n in nums:
#     if n % 2 == 0:
#         my_list.append(n)

# list comprehension method
#          ||
#         VVVV

#my_list = [n for n in nums if n % 2 == 0]

#               Example 3

# my_list = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter, num))
# print(my_list)

# list comprehension method
#          ||
#         VVVV

# my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
# print(my_list)

#               Example 4

#           The Zip Function

# zip() - The zip function combines two different arrays in a single zip object, Then you have to typecast the result into a tuple.
#               Syntax

# name = ['Jude', 'jane', 'clark']
# surname = ['wayne', 'john', 'superman']

# result = zip(name, surname)

# print(tuple(result))


#   Making a dictinary from the zip function
# names = ['Jude', 'jane', 'clark']
# surnames = ['wayne', 'john', 'superman']

# my_dict = {}
# for name, surname in zip(names, surnames):
#     my_dict[name] = surname
# print(my_dict)


# list comprehension method
#          ||
#         VVVV

