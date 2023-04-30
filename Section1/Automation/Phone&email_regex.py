"""_summary_
    ==> Project: Phone Number and Email Address Extractor from a copied text {text in clipboard}
"""
import re
import pyperclip

number_pattern = re.compile(
    r"""(
    (\d{3}|\(\d{3}\)) #Area code
    (\s|-|\.)?        #seperator
    (\d{3})           #First three digits after the area code
    (\s|-|\.)?         #seperator
    (\d{4})           # The last four digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
)""",
    re.VERBOSE,
)
email_pattern = re.compile(
    r"""(
    [a-zA-Z0-9._%+-]+   #Username
    @                  # @ symbol
    [a-zA-Z0-9.-]+      #domain name
    (\.[a-zA-Z]{2,4})  # dot-something
)""",
    re.VERBOSE,
)
"""_ABOUT EMAILS_
    The username part of the email address ➊ is one or more characters that can be any of the following: lowercase and uppercase letters, numbers, a dot, an underscore, a percent sign, a plus sign, or a hyphen. You can put all of these into a character class: [a-zA-Z0-9._%+-].

    The domain and username are separated by an @ symbol ➋. The domain name ➌ has a slightly less permissive character class with only letters, numbers, periods, and hyphens: [a-zA-Z0-9.-]. And last will be the “dot-com” part (technically known as the top-level domain), which can really be dot-anything. This is between two and four characters.

    The format for email addresses has a lot of weird rules. This regular expression won't match every possible valid email address, but it'll match almost any typical email address you'll encounter.
"""

text = pyperclip.paste()
Matches = []

for number_group in number_pattern.findall(text):
    number = "-".join([number_group[1], number_group[3], number_group[5]])
    if number_group[8] != "":
        number += " x" + number_group[8]
    Matches.append(number)

for email_group in email_pattern.findall(text):
    Matches.append(email_group[0])

for data in Matches:
    print(data)


"""re.DOTALL is a flag in Python's re module that changes the behavior of the dot(.) metacharacter. Normally, the dot matches any character except a newline. However, when re.DOTALL is used, the dot will also match newline characters.

Here's an example to demonstrate how re.DOTALL works:
import re

text = "Hello\nworld"
pattern = r".*"
match = re.search(pattern, text)

print(match.group())  # Output: "Hello"

In the above code, the regular expression .* matches all characters in the input string up to the first newline character. Therefore, the matched string is "Hello". If we want the dot to match newline characters as well, we can use re.DOTALL as follows:
import re

text = "Hello\nworld"
pattern = r".*"
match = re.search(pattern, text, flags=re.DOTALL)

print(match.group())  # Output: "Hello\nworld"
In this example, we pass the re.DOTALL flag to re.search() function, which causes the dot to match newline characters as well. Therefore, the matched string is "Hello\nworld".
"""
