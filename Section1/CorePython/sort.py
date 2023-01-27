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
# The sorted() function can work on a dictionary, but it will only return the keys and not the values.

#                     USING A KEY TO SORT OUT DATA

class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def __repr__(self):
        return f'({self.name}, {self.age}, {self.position}, ${self.salary})'


E1 = Employee('Ronald', 17, 'Machine Learning Engineer', 100000)
E2 = Employee('Henry', 26, 'Front-end Engineer', 70000)
E3 = Employee('James', 30, 'Machine Learning Engineer', 500000)
E4 = Employee('Frank', 22, 'Back-end Engineer', 110000)

Employees_list = [E1, E2, E3, E4]


def Esort(Employee):
    return Employee.name


Sorted_list = sorted(Employees_list, key=Esort)

print(Sorted_list)
