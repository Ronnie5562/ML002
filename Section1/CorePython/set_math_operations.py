# Sets are an unordered collection of unique elements in Python, and they support several mathematical operations that can be used to manipulate and
# compare sets. Here are some of the common mathematical operations that can be performed on sets in Python:

# Union: The union of two sets A and B is a new set that contains all the elements that are in either A or B or both. The union of sets A and B can
# be calculated using the | operator or the union() method.

# Intersection: The intersection of two sets A and B is a new set that contains all the elements that are in both A and B. The intersection of sets
# A and B can be calculated using the & operator or the intersection() method.

# Difference: The difference of two sets A and B is a new set that contains all the elements that are in A but not in B. The difference of sets A
# and B can be calculated using the - operator or the difference() method.

# Symmetric Difference: The symmetric difference of two sets A and B is a new set that contains all the elements that are in either A or B, but not
# in both. The symmetric difference of sets A and B can be calculated using the ^ operator or the symmetric_difference() method.

# Here is an example of how these operations can be used:

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# union of sets
union_set = set1 | set2
print(union_set)  # {1, 2, 3, 4, 5, 6, 7}

# intersection of sets
intersection_set = set1 & set2
print(intersection_set)  # {3, 4, 5}

# difference of sets
difference_set = set1 - set2
print(difference_set)  # {1, 2}

# symmetric difference of sets
symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)  # {1, 2, 6, 7}


# In addition to these operations, sets also support other mathematical operations such as subset, superset, and disjoint operations, which can be
# used to test the relationship between two sets. Overall, the mathematical operations on sets in Python make it easy to perform set operations
# efficiently and effectively.
