# Duck Typing Example:

# In this example, we have two classes, Dog and Cat, each with a speak() method. We then define a function animal_speak() that takes an argument
# animal and calls its speak() method. However, instead of checking whether animal is an instance of Dog or Cat, we simply assume that it has a
# speak() method and call it. This is an example of duck typing.


class Dog:
    def speak(self):
        return "Woof!"


class Cat:
    def speak(self):
        return "Meow!"


def animal_speak(animal):
    return animal.speak()


dog = Dog()
cat = Cat()

print(animal_speak(dog))  # Output: Woof!
print(animal_speak(cat))  # Output: Meow!


# In this example, we can see that the animal_speak() function can accept any object that has a speak() method, regardless of its type. This makes
#  the code more flexible and easier to maintain.

# Easier to Ask for Forgiveness than Permission Example:

# In this example, we have a function write_to_file() that writes a string to a file. However, instead of checking whether the user has permission
# to write to the file beforehand, we simply try to write to the file and handle any errors that occur. This is an example of "easier to ask for
#  forgiveness than permission."


def write_to_file(filename, text):
    try:
        with open(filename, "w") as file:
            file.write(text)
            print(f"Successfully wrote '{text}' to file '{filename}'")
    except Exception as e:
        print(f"Error writing to file '{filename}': {e}")


write_to_file("example.txt", "Hello, world!")


# In this example, we can see that the write_to_file() function assumes permission to write to the file and handles any errors that occur. This
# makes the code simpler and more flexible, as it can work in a variety of situations without having to check permissions beforehand. However, it
# is important to handle errors properly to prevent unexpected behavior and security vulnerabilities.
