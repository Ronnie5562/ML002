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
print(match)
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


# using .compile() and .finditer()

compile_text = 'This text is a text that was texted to text him about a text that was texted on text day'


compile_pattern = re.compile('text')
Text_matches = compile_pattern.finditer(compile_text)

print('______________________________________________')
for match in Text_matches:
    print(match)
print('______________________________________________')


text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

# The re.IGNORECASE makes the pattern case-insensitive
pattern = re.compile(r'start', re.IGNORECASE)

matches = pattern.search(sentence)

print(matches)

# code to match all the phone numbers inside the text_to_search variable above.
# check th Reg_Exp.txt file to understand why we are using \d and . in the below.
# The { r } inside the compile method, before the string represents raw string.
num_pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d')
new_match = num_pattern.finditer(text_to_search)

for match in new_match:
    print(match)


# Write a code to parse out all the phone numbers in Reg_Exp_data.txt

with open('Reg_Exp_data.txt', 'r', encoding='UTF-8') as file:
    file_data = file.read()
    # The data_pattern below matches a number that has the format of -[3digits, any char, 3digits, any chat, 4digits]
    data_pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
    # To specify a list of char the {any char} can be, we use a character set - [different_characters]
    data_pattern = re.compile(r'\d\d\d[-]\d\d\d[-]\d\d\d\d')

    Phone_book = data_pattern.finditer(file_data)

    for numbers in Phone_book:
        print(numbers)

with open('Reg_Exp_data.txt', 'r', encoding='UTF-8') as file:
    file_data = file.read()
    name_pattern = re.compile(r'M(r|s|rs)\s[\w]*')
    
    matched_names = name_pattern.finditer(file_data)
 
    for name in matched_names:
        print(name)

# To match all the emails in Reg_Exp_data.txt file.
print('______________________________________________')
with open('Reg_Exp_data.txt', 'r', encoding='UTF-8') as file:
    file_data = file.read()
    name_pattern = re.compile(r'\w+@\w+\.\w+')
    
    matched_names = name_pattern.finditer(file_data)

    for name in matched_names:
        print(name)

# Working with groups [()] in RegExp


with open('./Reg_Exp_data.txt') as file:
    url_pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
    data = file.read()

    urls = url_pattern.finditer(data)

    for url in urls:
        print(url.group())