# The io module in Python provides facilities for working with streams of data. One of the classes in this module is StringIO, which provides an
#in -memory file-like object that can be used to read from or write to a string buffer.

# The StringIO class is useful in situations where you want to treat a string as a file-like object, for example, when you want to read from or 
# write to a string as if it were a file.

# To use StringIO, you need to import it from the io module using the from statement, like so:

from io import StringIO

# Once you have imported StringIO, you can create an instance of the class and use it to read from or write to a string buffer, like this:

File_one = StringIO()
File_one.write('Hello World')
File_one.seek(0)
print(File_one.read())

# In this example, we create an instance of StringIO called s, then we write the string 'Hello, world!' to the buffer using the write method. 
# Next, we move the cursor to the beginning of the buffer using the seek method, and then we read the contents of the buffer using the read method
# and print it to the console. The output of the program is 'Hello, world!'.

File_two = StringIO()
File_two.write('This is so so amazing')
File_two.seek(0)
print(File_two.read())

# IT WAS A GREAT EXPERIENCE LEARNING ABOUT THE {io} MODULE