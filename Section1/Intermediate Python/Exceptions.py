class TooYoungException(Exception):
    def __init__(self, message):
        self.message = message


class TooOldException(Exception):
    def __init__(self, message):
        self.message = message


Age = int(input("Enter your age: "))
if Age < 18:
    raise TooYoungException("You are too young to get married")
elif Age > 60:
    raise TooOldException("You are too old to get married")
else:
    print("You are eligible to get married")
