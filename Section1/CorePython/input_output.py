# with open('./test_1.txt', 'r', encoding='UTF-8') as file:
#     # print(list(file))
#     for x in range(10):
#         content = file.readline()
#         print(content)


# def append_after(filename="", search_string="", new_string=""):
#     lines = []
#     with open(filename, 'r', encoding='UTF-8') as file:
#         lines.extend(file.readlines())
#         for index, line in enumerate(lines):
#             if search_string in line:
#                 lines.insert(index + 1, new_string)
#     with open(filename, 'w', encoding='UTF-8') as file:
#         file.writelines(lines)


def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r', encoding='UTF-8') as file:
        lines = file.readlines()

    new_lines = [line + new_string if search_string in line else line for line in lines]

    with open(filename, 'w', encoding='UTF-8') as file:
        file.writelines(new_lines)


append_after('test_1.txt', "c", "python is cool\n")