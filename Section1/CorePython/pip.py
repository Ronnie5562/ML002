# pip help - Run this on your terminal to get the full descripton of all the pip commands.
# Run pip list -o to check for oudated packages.
# Run pip install -U (The package name without the Parentheses) to update a package.
# Run pip install -r (file name) to install a list of packages inside a particular file.

# Unrelated -- SOME OTHER STUFFS
# Understanging __name__ and __main__


print("hello")
if __name__ == "__main__":
    print("The code is executed as a program")
else:
    print("The code executed as a module from some other program")

# Explanation of the code above
# If the program is executed as an individual program the value of __name__ is __main__.
# But if the program is executed as a module from some other program then the value of __name__ is the name of the file itself.add()

# When we run the code here, it prints out {The code is executed as a program} but if we import it into another program like we did in {Reload_module.py} it will print out {The code executed as a module from some other program}. The shows that the value of __name__ varies depending on where we are executing the program.
