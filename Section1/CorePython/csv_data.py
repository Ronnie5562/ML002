import csv

# The normal way

# with open('data.csv', 'r', encoding='UTF-8') as csv_file:
#     csv_reader = csv.reader(csv_file)

#     with open('new_data.csv', 'w', encoding='UTF-8') as new_file:
#         csv_writer = csv.writer(new_file, delimiter='-')

#         for line in csv_reader:
#             csv_writer.writerow(line)

# Using DictReader and DictWriter

with open('data.csv', 'r', encoding='UTF-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_data.csv', 'w', encoding='UTF-8') as new_file:
        fieldnames = ['first_name', 'last_name', 'email']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\n')

        for line in csv_reader:
            csv_writer.writerow(line)