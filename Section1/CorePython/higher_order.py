#filter() function:
# We can use filter() function to filter values from the given sequence based on some condition.
#
# filter(function, sequence)
#
# where function argument is responsible to perform conditional check and the sequence can be list or tuple or string.


# Q. Program to filter only even numbers from the list by using filter() function?

# without lambda Function:
def isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False
    
l=[0,5,10,15,20,25,30] 
l1=list(filter(isEven,l)) 
print(l1) #[0,10,20,30]

#with lambda Function:
l=[0,5,10,15,20,25,30] 
l1=list(filter(lambda x:x%2==0,l)) 
print(l1) #[0,10,20,30] 
l2=list(filter(lambda x:x%2!=0,l)) 
print(l2) #[5,15,25]


# map() function:
# For every element present in the given sequence, apply some functionality and generate
# new element with the required modification. For this requirement we should go for
# map() function.
# Eg: For every element present in the list perform double and generate new list of doubles.
# Syntax:
# map(function, sequence)
# The function can be applied on each element of sequence and generates new sequence


numbers = [1,2,3,4,5,6,7,8]

new_numbers = list(map(lambda x : x * x, numbers))

print(new_numbers)

# Python code to join each family members' name with the family surname
family_members = ['johnson', 'mira', 'anabel', 'faith', 'jude', 'gabriel']
family_surname = 'Elon'

names_with_surname = list(map(lambda name: f'{family_surname} {name}', family_members))

print(names_with_surname)

#We can apply map() function on multiple lists also.But make sure all list should have same length.
#Syntax: 
# map(lambda x, y: x*y, l1, l2))
#     x is from l1 and y is from l2
#     Eg:

l1= [1, 2, 3, 4]
l2= [2, 3, 4, 5]
l3 = list(map(lambda x, y: x*y, l1, l2))
print(l3)  # [2, 6, 12, 20]


list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
list3 = [11, 12, 13, 14, 15]

mul_list = list(map(lambda x, y, z: x * y * z, list1, list2, list3))

print(mul_list)
