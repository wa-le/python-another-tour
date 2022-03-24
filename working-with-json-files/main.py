
# Note - When you already have a json file filled with data you then just have to update the file
# If you don't have any already filled json file, you then have to create one and write to it
# Use Exception to create a new json file and write to it, so user does not get errors while trying to update -
# a non-existing json file


import json

add_info = True
while add_info:
    the_website = input("type_here: ")
    the_email_username = input("type_here: ")
    the_password = input("type_here: ")

    add_data = {
        the_website: {
            "email": the_email_username,
            "password": the_password,
        }
    }

    # read from json file
    try:
        with open("info_data.json", "r") as d_file:
            data = json.load(d_file)
    except FileNotFoundError:
        with open("info_data.json", "w") as file:
            json.dump(add_data, file, indent=4)
    else:
        data.update(add_data)
        with open("info_data.json", "w") as file:
            json.dump(data, file, indent=4)

    keep_adding = input("Do you want to add more info? (Y or N): ")
    if keep_adding.upper() == "N":
        add_info = False
    elif keep_adding.upper() == "T":
        add_info = True

