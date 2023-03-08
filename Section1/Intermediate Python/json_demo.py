import json
people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "615-505-2193",
            "emails": null,
            "has_license": true
        }
    ]
}
'''
# To load a JSON sting into a python object, use: json.loads()
data = json.loads(people_string)

print(data)
print('_________________________________________')

# To dump a python object into a JSON string, we use json.dumps()
# To indent the print-out, you can add the indent keyword argument and to sort the keys in the dictionary, pass this also ==> {sort_keys = True}
new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)



# Loading a json file into a python code.
# Check the code in states.json file before going through the following code. 

with open('states.json', encoding='UTF-8') as file:
    states_list = json.load(file)

# Now, I want to pass the content of the states.json file into another file without the states code
for state in states_list['states']:
    del state['area_codes']

with open('new_states.json', 'w', encoding='UTF-8') as new_file:
    new_data = json.dump(states_list, new_file, indent=2)

# The new_states.json file you see in this directory was created with the file above.

#                                                                       using the {io} module

from io import StringIO

First_io_file = StringIO()
with open('states.json', encoding='UTF-8') as io_File_writer:
    file_data = json.load(io_File_writer)
    re_data = json.dumps(file_data, indent=2)
    First_io_file.write(re_data)

print('______________________________')
First_io_file.seek(0)
print(First_io_file.read())

a = (10 + 5j)
print(a.real)
print(a.imag)