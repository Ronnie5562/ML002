# To get a file object we can use the built in [open('the_path_of_the_file')] command.
# f = open('File_objects.py', 'r')

# print(f.name)
# print(f.mode)

# f.close()

#      HOW TO OPEN A FILE USING CONTEXT MANAGER
# To read the content in a file
# with open("main.py", "r") as f:
#     f_contents = f.read()
# print(f_contents)

# To read the content in a file line by line
# with open("main.py", "r") as f:
#     f_contents = f.readlines()
# print(f_contents)

# To loop through the content of a particular file.
# with open('main.py') as T:
#     for line in T:
#         print(line, end='')

# To read a particular number of words in a file.
# with open('main.py', 'r') as p:
#     #it's 100 words in this case
#     p_content = p.read(100)
#     print(p_content)

# NOTE: .seek(int) takes us back to the word with the index of the argument - (int). i.e seek(0) takes us back to the beginning of the file.

# To write into files
# with open('test_1.txt', 'w') as W:
#     W.write('YELLO')
#     W.seek(0)
#     W.write('H')

# To copy the content in a file and paste it in another file.
# with open('test_1.txt', 'r') as RF:
#     with open('test_cp.txt', 'w') as RFC:
#         for line in RF:
#             RFC.write(line)

# To make copies of images
# Notice the 'b' beside the 'r' and 'w' - it represents bytes. To work with pictures, we have to work on it from the byte level.
# with open('library_eggshell.webp', 'rb') as PB:
#     with open('image_copy.pdf', 'wb') as PBCP:
#         for bytes in PB:
#             PBCP.write(bytes)
