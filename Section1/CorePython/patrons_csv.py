# This file together with patrons.csv shows how we can automate real-world problems with python.
# Assume you have a patrons list on your website and you need perform some automation on it to automatically remove the name of those patrons who dont want their name to be on your website and also render the list as an HTML unordered list tag.#

# This code extracts the names of the users from the Patrons.csv file and prints it out using the HTML unordered list format.
import csv

new_patrons_list = ""

with open("patrons.csv") as Plist:
    Plist_reader = csv.DictReader(Plist)

    next(Plist_reader)

    new_patrons_list += "\n<ul>"
    for line in Plist_reader:
        if line["FirstName"] == "No Reward":
            break
        Fullname = f"{line['FirstName']} {line['LastName']}"

        new_patrons_list += f"\n\t<li>{Fullname}</li>"

    new_patrons_list += "\n<ul/>"

print(new_patrons_list)
