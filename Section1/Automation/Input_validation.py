import random

color = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
a = random.choices(color, weights=[2, 10, 2, 10, 2, 10, 40], k=2)

print(a)
