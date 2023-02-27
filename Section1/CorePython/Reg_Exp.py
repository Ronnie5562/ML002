# Regular expressions, also known as regex or regexp, are powerful tools for pattern matching and text manipulation. In Python, regular expressions are implemented 
# through the built-in re module.

# A regular expression is a sequence of characters that defines a search pattern. The re module provides a variety of functions for working with regular expressions,
# including search(), match(), findall(), sub(), and split(). These functions allow you to search for patterns within strings, replace substrings, and split strings 
#based on patterns.

# Here are some basic examples of regular expressions in Python:

# re.search(pattern, string) searches the string for the first occurrence of the pattern and returns a match object if found

import re

text = "The quick brown fox jumps over the lazy dog"
pattern = "quick"

match = re.search(pattern, text)

if match:
    print("Pattern found!")
else:
    print("Pattern not found.")

text2 = 'The boy is very innovative. We call him starboy'
pattern = 'boy'

match2 = re.search(pattern, text2)
print(match2)

# re.findall(pattern, string) searches the string for all occurrences of the pattern and returns a list of matching strings.


text = "The quick brown fox jumps over the lazy dog"
pattern = "[aeiou]"

matches = re.findall(pattern, text)

print(matches)

more_text = "I really don't know what to type here sha!!"
more_pattern = "[acegikmo]"

result = re.findall(more_pattern, more_text)

print(result)
# re.sub(pattern, replacement, string) replaces all occurrences of the pattern in the string with the replacement string.

import re

text = "The quick brown fox jumps over the lazy dog"
pattern = "brown"
replacement = "red"

new_text = re.sub(pattern, replacement, text)

print(new_text)



# These are just a few examples of what you can do with regular expressions in Python. Regular expressions are a powerful tool for working with text data, and learning 
# how to use them can be very beneficial for data cleaning, text processing, and more.


# using .compile()

compile_text = 'This text is a text that was texted to text him about a text that was texted on text day'
compile_pattern = 'text'

Text_filter = re.compile(compile_text, )