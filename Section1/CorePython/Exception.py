# try:
#     f = open('Calc.py')
#     var = bad_var
# except FileNotFoundError:
#     print('sorry. This file does not exist')
# except Exception:
#     print('sorry. something went wrong')
# 


#_____{BUILTIN ERROR}_____

# try:
#     f = open('Calc.py')
#     var = bad_var
# except FileNotFoundError as NOTFOUND:
#     print(NOTFOUND)
# except Exception as UNKNOWNERROR:
#     print(UNKNOWNERROR)

# With the "else-block" ==> [if the code in the try-block does not throw an error, the program runs the code in the else-block]
# try:
#     f = open('Calc.py')
# except FileNotFoundError as NOTFOUND:
#     print(NOTFOUND)
# except Exception as UNKNOWNERROR:
#     print(UNKNOWNERROR)
# else:
#     print(f.read())
#     f.close()
#     print(f.closed)

# With the "finally-block" ==> [irrespective of what happens[error or noError] in the try-block the program runs the code in the finally-block]

try:
    f = open('./Calc.py')
except FileNotFoundError as NOTFOUND:
    print(NOTFOUND)
except Exception as UNKNOWNERROR:
    print(UNKNOWNERROR)
else:
    print(f.read())
    f.close()
    print(f.closed)
finally:
    print('I will run irrespective of what happens up there hahaha!!😂😂😂😂😂😂')
