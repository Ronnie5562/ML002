class Employer:
    def __init__(self, name):
        self.name = name
        self.age = 17
        setattr(self, "position", "AI engineer")

    def change_name(self, new_name):
        self.name = new_name

    def print_name(self):
        print(self.name)


Ronald = Employer("Ronald")
Ronald.change_name("Sharon")
Ronald.print_name()
print(Ronald.__dict__)
print(type(Ronald).__name__ is Ronald.__class__.__name__)
print(Ronald.__class__.__name__)
print(type(Ronald).__name__)
print(Ronald.__class__.__name__)

# Study the code above and tell what you notice - You can definitely run it to see the outcome
