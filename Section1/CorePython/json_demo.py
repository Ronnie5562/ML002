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