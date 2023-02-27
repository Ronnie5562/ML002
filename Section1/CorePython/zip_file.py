# Zipping and Unzipping Files:
#To perform zip and unzip operations, Python contains one in -bulit module zip file.
#This module contains a class: ZipFile

#To create Zip file:
#We have to create ZipFile class object with name of the zip file, mode and constant ZIP_DEFLATED. This constant represents we are creating zip file.

from zipfile import *

f = ZipFile("files.zip", 'w', ZIP_DEFLATED)

# Once we create ZipFile object,we can add files by using write() method.

f.write('test.py')
# The zipfile in this directory was created with the code above. It contains a copy of test.py which is also a file in this directory.
f.close()
print('The zipfile (files.zip) was successfully created!!!!!')