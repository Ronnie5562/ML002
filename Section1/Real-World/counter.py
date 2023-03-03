# Write a python code that takes a list and returns a list of tuples each containing an element of the original list and the number of times it appeared in the original
# list.
from collections import Counter

groceries = ['apple', 'mango', 'orange', 'ginger', 'beef', 'chicken', 'mango', 'apple', 'carrot', 'ginger', 'beef', 'mango', 'grape', 'mango', 'apple', 'carrot', 'ginger', 'rice', 'orange', 'mango', 'mango']

payment_details = Counter(groceries)
print(payment_details.most_common()) # Prints the out in according to the number of times they appear descending order.add()
print(payment_details.most_common(1)) # Prints out the element that appears the most.

