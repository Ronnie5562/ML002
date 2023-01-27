#li = [9, 1, 8, 2, 7, 3, 6, 4, 5]

# If you want to create a new list containing the sorted version of the original list, use the sorted() function.
#s_li = sorted(li)

# But if you want to sort the original version of the  list, use the .sort() method on the list.
#li.sort()

# To sort the list in a reversed manner, add the keyword argument -[reverse=True] to the .sort() method. i.e => li.sort(reverse=True). or to the sorted() function. i.e => x = sorted(original_list, reverse=True)

#print('Sorted Variable:\t', li)

# DIFFERENCE BETWEEN the .sort() method and the sorted() function.
# __________________________________________________________________________________
#|_________________.sort()________________ |_____________sorted()___________________|
#| It returns None                         | It returns a new list                  |
#| It is peculiar to only list             | It can be used on tuples and dictionary|
