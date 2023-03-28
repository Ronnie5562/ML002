# Let's work without regex for now!!!
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
      if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
         return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
#The goal here is to get all the phone numbers in the text above without using regex

for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')

# NOW, LET'S WORK WITH REGEXES 🥳🥳🥳🥳🥳
import re
pattern = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
chunk = pattern.search('Call me at 415-555-1011 tomorrow.')
print(f'Phone number found: {chunk.group(0)}')

MO = re.compile(r'Batman|Tina Fey')
MO2 = re.compile(r'Bat(wo)*man')
obj1 = MO.search('Batman and Tina Fey')
print(obj1.group())
print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _')
obj2 = MO.search('Tina Fey and Batman reside in Gotham city')
print(obj2.group())
print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _')
obj3 = MO2.search('The adventure of Batman')
print(obj3.group())