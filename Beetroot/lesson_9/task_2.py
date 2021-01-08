"""
Extend Phonebook application

Functionality of Phonebook application:

Add new entries
Search by first name
Search by last name
Search by full name
Search by telephone number
Search by city or state
Delete a record for a given telephone number
Update a record for a given telephone number
An option to exit the program
The first argument to the application should be the name of the phonebook. Application should load JSON data,
if it is present in the folder with application, else raise an error. After the user exits, all data should be saved to
loaded JSON.
"""
import json


def create_contact(firstname, lastname, fullname, number, city):
    return {
        'firstname': firstname,
        'lastname': lastname,
        'fullname': fullname,
        'number': number,
        'city': city
    }


def search_by_key(key, value):
    return [element for element in phonebook if element.get(key) == value]


def load_jsonfile(filename='phonebook.json'):
    try:
        with open(filename) as phonebook:
            data = json.load(phonebook)
    except FileNotFoundError:
        print("The file doesn't exist.")
    return data


def dump_into_jsonfile(dictionary):
    data = load_jsonfile()
    data.append(dictionary)
    try:
        with open('phonebook.json', 'w') as phonebook:
            json.dump(data, phonebook, indent=4)
    except FileNotFoundError:
        print("The file doesn't exist.")
    else:
        print('The information was successfully added to the phonebook.')


if __name__ == '__main__':

    # data = load_jsonfile()
    # for item in data:
    #     if item['lastname'] == 'Mamonov':
    #         print(item)

    search_actions = {'sn': ['firstname', search_by_firstname], 'sl': ['lastname', search_by_lastname],
                      'sf': ['fullname', search_by_fullname], 'snm': ['number', search_by_number],
                      'sc': ['city', search_by_city]}
    phonebook_keys = [key[0] for key in search_actions.values()]
    while True:
        phonebook = load_jsonfile('phonebook.json')
        user_choice = input(f'"cc" - create new contact,\n"sn" - search by firstname,\n"sl" - search by lastname,'
                            f'\n"sf" - search by fullname,\n"snm" - search by number,\n"sc" - search by city,'
                            f'\n"d" - delete record,\n"u" - update record,\n"pr" - print phonebook'
                            f'\n"q" - quit application\nYour choice: ')
        if user_choice == 'cc':
            firstname, lastname, fullname, number, city, = [input(f'Enter {elem}: ').title().strip() for elem in
                                                            search_actions]
            new_contact = create_contact(firstname, lastname, fullname, number, city)
            dump_into_jsonfile(new_contact)
        elif user_choice in search_actions:
            user_input = input(f"Enter {search_actions[user_choice][0]}: ").title().strip()
            found_contact = search_by_key(search_actions[user_choice][0], user_input)
            print(found_contact)
        elif user_choice == "q":
            break
    print(phonebook)
