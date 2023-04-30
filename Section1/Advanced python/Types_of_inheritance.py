# Types of inheritance
# 1. Single inheritance
# it involves a single parent class and a single child class and just one level of inheritance.


class Parent:
    def m1(self):
        print("Parent Method")


class Child(Parent):
    def m2(self):
        print("Child Method")


# 2. multi level inheritance
# it involves multiple level of inheritance.


class Parent:
    def m1(self):
        print("Parent Method")


# Notice that all the classess below are direct sub classess of Parent(the above class) i.e they both directly inherit from Parent Class.
class Child(Parent):
    def m2(self):
        print("Child Method")


class SubChild(Parent):
    def m3(self):
        print("Sub Child Method")


# 3. Hierarchical inheritance
# It involves one parent but multiple childs at the same level.


class Parent:
    def m1(self):
        print("Parent Method")


class Child(Parent):
    def m2(self):
        print("Child Method")


class SubChild(Child):
    def m3(self):
        print("Sub Child Method")


# 4. Multiple inheritance
# It involves multiple parents but a single child.
# An instance whereby we have a subclass inherinting from two parent classess that both contain one or more same method, an Ambiguity problem
# is introduced - Some people also refer to it as Diamond Access problem. In that case, the method in the first listed class is used.
# i.e class Example(parent1, parent2) in this example, if parent1 and parent2 both have a particular method, the method in parent1 will be the
# chosen one.


class first_Parent:
    def m1(self):
        print("first_Parent")


class second_Parent:
    def m1(self):
        print("second_Parent")


class Child(first_Parent, second_Parent):
    def m3(self):
        print("Child Method")


# 5. Hybrid inheritance ==> It involves the use of two or more of the above at the same time.
# 6. Cyclic inheritance
# It involves a class inheriting from itself.
# E.g ==> class A(A) - in this case, the class A is inheriting from class A (itself)
# Note Cyclic inheritance is not accepted in any programming language.
#  Another example
# class A(B):
#     def m1(self):
#         print('Hello')


# class B(A):
#     def m2(self):
#         print('Holla')
