# ______The_random_module_____
# To get a random number between 0[inclusive] and 1[exclusive] use:
import random

x = random.randint(1, 5)
print(x)
# y = random.uniform(1, 5)
# import random
# courses = ['Math', 'English', 'CompSci', 'Machine-Learning']
#
# random_course = random.choice(courses)
#
# print(random_course)


x = random.uniform(1, 5)
print(x)

# To get a random whole number between a and b use:
y = random.randint(1, 5)
print(y)

# To get a random choice from a list use: .choice()

greetings = ["Hello", "Hi", "Holla", "Hey", "Howdy", "Wagwan"]
greet_value = random.choice(greetings)
print(f"{greet_value}, Ronald")
# Notice that the console prints different greeting each time the program is run.

# To get a list of random values from another list use: .choices()

# ______________Let's make this a story______________:
# An NGO went to a village to Empower females.
# On getting to the village, they noticed that the men also need Empowerment.
# So, they decided to help the villagers at random but giving more preference to the females.
# The villagers have their names in [names] list. Once your name is chosen, you are given a sum of $60.
names = [
    "Ronald",
    "Richard",
    "Sharon",
    "Benita",
    "Elizabeth",
    "Peter",
    "James",
    "Joshua",
    "Precious",
    "Prof",
]

Chosen = random.choices(names, weights=[1, 1, 2, 2, 2, 1, 1, 1, 2, 1], k=5)
# K: it indicates the number of people that will be picked
# The weight list above represents the probability of a person being chosen.
# The list is in respective to the names list
# Notice that the females have a value of 2 and the males have a value of 1.
# This shows that a female is two times likely to be picked than a male.

print(Chosen)
