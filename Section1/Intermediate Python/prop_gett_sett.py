# In Python, @ property is a decorator that allows us to define a method that can be accessed as an attribute. It is often used in object-oriented
#  programming to provide a controlled access to class properties. By using the @ property decorator, we can define getter and setter methods that
#  are called when we access or assign a value to a property.

# A getter method is used to retrieve the value of a property. We can define a getter method using the @ property decorator. When we access the
#  property, the getter method is called automatically, and the value is returned.

# A setter method is used to set the value of a property. We can define a setter method using the @ <property_name > .setter decorator. When we 
# assign a value to the property, the setter method is called automatically, and the value is set.

# A deleter method is used to delete a property. We can define a deleter method using the @ <property_name > .deleter decorator. When we delete 
# the property, the deleter method is called automatically, and the property is removed.

# The @ property decorator is useful for encapsulating class properties, controlling access to them, and adding validation checks. It is also 
# useful for providing a simple and intuitive interface for interacting with the properties. Overall, the @ property decorator is a powerful tool
# for writing robust, maintainable, and easy-to-use code.


# import random
# class Employee:

#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#         self.email = f'{first}_{last}{random.randint(100, 999)}@email.com'

#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)


# emp_1 = Employee('john', 'smith')

# emp_1.first = 'Jim'

# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.fullname())

#The ouput of the code above:
    # Jim
    # john_smith835@email.com
    # Jim smith
# Note that even though the first attribute of emp_1 was changed to 'Jim', the email address still includes the original value of 'john' since it
# was generated when the object was first created.


# To solve this problem, we have to turn the email attribute into a method but we will add a decorator(@property) that will make the method act
# like an attribute.

import random


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property    
    def email(self):
        return f'{self.first}_{self.last}{random.randint(100, 999)}@email.com'
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('john', 'smith')

emp_1.first = 'Jim'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())
