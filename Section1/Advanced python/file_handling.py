import datetime

"""_summary_
There are two main branches of storage in computing, these are temporary storage and permanent storage.
        { in python}
    ==> Temporary storage: List, Tuple, Dict e.t.c
        ==> When we store data inside a temporary storage facility, it is usually kept inside the PVM{Python Virtual Machine} as the part of heap. Once the exucution of the code is complete, the data is lost.
    ==> Permanent Storage: Files and database
Types of files:
1. Text file - used to store texual data
2. Binary file - Used to store binary data like pictures, videos, audio e.t.c

    ==> FROM DURGA PYTHON NOTE
    Various properties of File Object:
    Once we opend a file and we got file object,we can get various details related to that file 
    by using its properties.
    name  Name of opened file
    mode  Mode in which the file is opened
    closed  Returns boolean value indicates that file is closed or not
    readable() Retruns boolean value indicates that whether file is readable or not
    writable() Returns boolean value indicates that whether file is writable or not.
"""

if __name__ == "__main__":
    for x in range(3):
        file_name = input("Enter file name:")
        message = input("Enter your log message: ") + " " + str(datetime.datetime.now())
        f = open(
            f"C:\\Users\\HP\\Desktop\\ML002\\Section1\\Advanced python\\inputs\\{file_name}",
            "w",
        )
        f.write(message)
        f.close()
