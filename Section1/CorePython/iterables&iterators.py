# Do you know that an iterator is different from an iterable.
# In Python, an iterable is an object that can be iterated (looped) upon. Examples of iterables include lists, tuples, sets, dictionaries, strings, file objects, and
# generators.

# An iterator, on the other hand, is an object that produces the next value in a sequence when the next() function is called on it. In other words, an iterator is an
# object that implements the __next__() method, which returns the next value in the sequence or raises the StopIteration exception if there are no more values.

nums = [1, 2, 3, 4]

array = nums.__iter__()
print(next(array))
print(next(array))
print(next(array))


# To create an iterator from an iterable, you can call the iter() function on the iterable. The iter() function returns an iterator object that can be used to iterate
# over the elements of the iterable.

# For example, consider the following code:

my_list = [1, 2, 3, 4, 5]
my_iterator = iter(my_list)

print(next(my_iterator))  # Output: 1
print(next(my_iterator))  # Output: 2
print(next(my_iterator))  # Output: 3


# In the code above, my_list is an iterable, and my_iterator is an iterator that is created by calling the iter() function on my_list. The next() function is called on
# my_iterator to get the next value in the sequence.

# Note that if we try to call next() on the iterator after all the elements have been exhausted, it will raise the StopIteration exception.


class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


nem = MyRange(1, 10)

for x in nem:
    print(x)
print("______________________________________________________")


def my_range(start, end):

    current = start
    while start < end:
        yield current
        current += 1


Mrange = my_range(1, 10)
print(Mrange)

for element in Mrange:
    print(element)
