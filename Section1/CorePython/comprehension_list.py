#               Example 1

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# my_list = [n for n in nums]

#               Example 2

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# my_list = []
# for n in nums:
#     if n % 2 == 0:
#         my_list.append(n)

# list comprehension method
#          ||
#         VVVV

# my_list = [n for n in nums if n % 2 == 0]

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

#              dictionary Comprehensions

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


# dictinary comprehension method
#          ||
#         VVVV

# names = ['Jude', 'jane', 'clark', 'peter']
# surnames = ['wayne', 'john', 'superman', 'Oyonda']

# my_dict = {name: surname for name, surname in zip(names, surnames) if name != 'peter'}

#                   set Comprehensions
# nums = [1, 1, 2, 3, 4, 5, 6, 7, 4, 3, 2, 6, 5, 5, 4, 2, 3]

# my_set = set()

# for n in nums:
#     my_set.add(n)
# print(my_set)

# set comprehension method
#          ||
#         VVVV
# nums = [1, 1, 2, 3, 4, 5, 6, 7, 4, 3, 2, 6, 5, 5, 4, 2, 3]

# my_set = {n for n in nums}

# print(my_set)

#               Generator Expressions

# Checkout how generator Expressions work normally.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# def gen_Exp(data):
#     for n in data:
#         yield n * n


# my_gen = gen_Exp(nums)

# print(list(my_gen))


#           Print Output:
#           [1, 4, 9, 16, 25, 36, 49, 64, 81]
#           Variables:
#           -{
#               my_gen: -{
#                   py/object: "builtins.generator"
#               },
#               nums: -[
#                   1,
#                   2,
#                   3,
#                   4,
#                   5,
#                   6,
#                   7,
#                   8,
#                   9
#               ]
#           }


# Checkout how generator Expressions works using Comprehension.

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# gen_comp = (n * n for n in nums)


# print(list(gen_comp))


#             Print Output:
#             [1, 4, 9, 16, 25, 36, 49, 64, 81]
#             Variables:
#             -{
#                 gen_comp: -{
#                     py/object: "builtins.generator"
#                 },
#                 nums: -[
#                     1,
#                     2,
#                     3,
#                     4,
#                     5,
#                     6,
#                     7,
#                     8,
#                     9
#                 ]
#             }
#             0 ms
