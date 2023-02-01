#THE OS MODULE
#The os module allows ud to interact with the undelying operating system in several different ways.

import os
#To print the current directory
#print(os.getcwd) #[get current working directory]

#To change directory
# os.chdir('The path')

#To list the files and folders in a directory
# os.listdir()

#To make a new directory
# os.mkdir('name of the directory')

#To make a directory with a content inside, use:
# os.makedirs('directory_name/sub_directory_name')

#To delete a directory
# os.rmdir('name of the directory')

#To delete a directory with the contents inside, use:
# os.removedirs('directory_name/sub_directory_name')

# To rename a directory
# os.rename('old_name', 'new_name')

# To print out all the information about a file
#print(os.stat(os.getcwd()))

    # To get the last time a file was modified
#from datetime import datetime

#mod_time = os.stat(os.getcwd()).st_mtime
#print(datetime.fromtimestamp(mod_time))

#To print out all the sub_directories and files at all levels inside a particular directory

# for dirpath, dirnames, filenames in os.walk(os.getcwd()):
#     print(dirpath)
#     print(dirnames)
#     print(filenames)
#     print()


# print(os.path.isdir('/Section1/CorePython/'))

#To change the format of a new file

# with open(name_of_file_to_be_changed, 'rb') as Fp:
#     with open(name_of_file_to_be_created.The_new_format, 'wb') as Cp:
#         for bytes in Fp:
#             Cp.write(bytes)