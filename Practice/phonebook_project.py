phonebook_dictionary = {}

def use_phonebook():
    """
    It means that the user adds a person with name name and phone numbernumber to the phone book. If there exists a user with such number already,then your manager has to add the new number to the existing ones
    """
    given_input = ""
    while given_input != "exit":
        print("What do you want to do with the phonebook?")
        given_input = input("> ")

        words = given_input.split()

        if words[0] == "add" and len(words) == 3:
            phone_number = words[1]
            contact_name = words[2]

            add_item(phone_number, contact_name)
            for item in phonebook_dictionary:
                print(item)

        elif words[0] == "del" and len(words) == 2:
            contact_name = words[1]
            delete_item(contact_name)

        elif words[0] == "find" and len(words) == 2:
            contact_name = words[1]
            find_item(contact_name)

        else:
            print("The sentence is invalid. Please try again")

def add_item(phone_number, contact_name):
    """
    It means that the user adds a person with name name and phone numbernumber to the phone book. If there exists a user with such number already,then your manager has to add the new number to the existing ones
    """
    phonebook_dictionary[contact_name] = phone_number


def delete_item(contact_name):
    """
    It means that the manager should erase a person with name name fromthe phone book. If there is no such person, then it should just ignore thequery
    """
    if contact_name in phonebook_dictionary:
        phonebook_dictionary.pop(contact_name)
    else:
        print("Name not found!")

def find_item(contact_name):
    """
    It means that the user looks for a person with name name. The managershould reply with the appropriate phone number, or with string “not found”(without quotes) if there is no such person in the book. In case of multiplephone numbers for the same person, return the shortest one(You can justcompare the numbers like integers). Also, case matters. E.g. mom is notthe same as Mom.
    """
    if contact_name in phonebook_dictionary:
        print(phonebook_dictionary[contact_name])
    else:
        print("Name not found!")

use_phonebook()