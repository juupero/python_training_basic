Add number

Delete name

Find name

phonebook_dictionary


def use_phonebook():
    """
    It means that the user adds a person with name name and phone numbernumber to the phone book. If there exists a user with such number already,then your manager has to add the new number to the existing ones
    """
    phonebook_dictionary, given_input = [], ""

    print("What do you want to do with the phonebook?")
    given_input = input("> ")
    given_input_split = given_input.split()
    if given_input_split[0] == "add":
        add_item(given_input)
    elif given_input_split[0] == "del":
        delete_item(given)
    elif given_input_split[0] == "find":
    else:
        print("String started with an invalid word.")

def add_item(item):
    """
    It means that the user adds a person with name name and phone numbernumber to the phone book. If there exists a user with such number already,then your manager has to add the new number to the existing ones
    """
    pass


def delete_item():
    """
    It means that the manager should erase a person with name name fromthe phone book. If there is no such person, then it should just ignore thequery
    """
    pass

def find_item():
    """
    It means that the user looks for a person with name name. The managershould reply with the appropriate phone number, or with string “not found”(without quotes) if there is no such person in the book. In case of multiplephone numbers for the same person, return the shortest one(You can justcompare the numbers like integers). Also, case matters. E.g. mom is notthe same as Mom.
    """
    pass

use_phonebook()