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

DATA_FILE = 'phonebook.json'

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


def print_contacts(found_contact):
    if found_contact:
        for contact in found_contact:
            contact_index = return_index(contact, phonebook)
            print(f'Index: {contact_index}, {contact}')
    else:
        print("Cannot find a contact.")


def return_index(contact, phonebook):
    return phonebook.index(contact)+1


def delete_contact(index, phonebook):
    try:
        print(phonebook.pop(int(index)-1))
    except (TypeError, IndexError):
        print("Wrong format of index or no contacts are found.")
    return phonebook


def load_jsonfile(filename=DATA_FILE, encoding='utf-8'):
    try:
        with open(filename, encoding) as phonebook:
            data = json.load(phonebook)
    except FileNotFoundError:
        print("The file doesn't exist.")
    return data


def add_contact_to_json(contact):
    data = load_jsonfile()
    data.append(contact)
    return data


def update_contact(index, firstname, lastname, fullname, number, city):
    try:
        phonebook[int(index)-1] = create_contact(firstname, lastname, fullname, number, city)
    except (TypeError, IndexError):
        print("Wrong format of index or no contacts are found.")
    return phonebook


def dump_into_jsonfile(filename=DATA_FILE, flag='w', encoding='utf-8'):
    try:
        with open(filename, flag, encoding) as phonebook:
            json.dump(filename, phonebook, indent=4)
    except FileNotFoundError:
        print("The file doesn't exist.")
    else:
        print('The the phonebook was updated.')


if __name__ == '__main__':

    search_actions = {'sn': 'firstname', 'sl': 'lastname', 'sf': 'fullname', 'snm': 'number', 'sc': 'city'}

    while True:
        phonebook = load_jsonfile('phonebook.json')
        user_choice = input(f'"cc" - create new contact,\n"sn" - search by firstname,\n"sl" - search by lastname,'
                            f'\n"sf" - search by fullname,\n"snm" - search by number,\n"sc" - search by city,'
                            f'\n"d" - delete record,\n"u" - update record,\n"pr" - print phonebook'
                            f'\n"q" - quit application\nYour choice: ')
        if user_choice == 'cc':
            firstname, lastname, fullname, number, city, = [input(f'Enter {elem}: ').title().strip() for elem in
                                                            search_actions.values()]
            new_contact = create_contact(firstname, lastname, fullname, number, city)
            dump_into_jsonfile(add_contact_to_json(new_contact))
        elif user_choice in search_actions:
            user_input = input(f"Enter {search_actions[user_choice]}: ").title().strip()
            found_contact = search_by_key(search_actions[user_choice], user_input)
            print_contacts(found_contact)
        elif user_choice in ('d', 'u'):
            action = {'d': 'delete', 'u': 'update'}
            user_input = input(f"Enter number of a contact you want to {action[user_choice]}: ").title().strip()
            found_contact = search_by_key('number', user_input)
            print_contacts(found_contact)
            if found_contact:
                index = input(f'Please choose index of a contact you want to {action[user_choice]}: ')
                if user_choice == 'd':
                    dump_into_jsonfile(delete_contact(index, phonebook))
                elif user_choice == 'u':
                    firstname, lastname, fullname, number, city, = [input(f'Enter {elem}: ').title().strip() for elem in
                                                                    search_actions.values()]
                    dump_into_jsonfile(update_contact(index, firstname, lastname, fullname, number, city))
        elif user_choice == "q":
            break
        else:
            print("Wrong input. Try again.")
    print(phonebook)
