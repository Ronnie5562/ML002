# Types of inheritance
# 1. Single inheritance
    # it involves a single parent class and a single child class and just one level of inheritance.

class Parent:
    def m1(self):
        print('Parent Method')
class Child(Parent):
    def m2(self):
        print('Child Method')

# 2. multi level inheritance
    # it involves multiple level of inheritance.

class Parent:
    def m1(self):
        print('Parent Method')
class Child(Parent):
    def m2(self):
        print('Child Method')
class SubChild(Child):
    def m3(self):
        print('Sub Child Method')

# 3. Hierarchical inheritance
    # It involves one parent but multiple childs at the same level.

class Parent:
    def m1(self):
        print('Parent Method')
class Child(Parent):
    def m2(self):
        print('Child Method')
class SubChild(Child):
    def m3(self):
        print('Sub Child Method')
        
# 4. Multiple inheritance
# 5. Hybrid inheritance
# 6. Cyclic inheritance
