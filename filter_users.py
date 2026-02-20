import json


def filter_users_by_name(name):
    """
    Filter and print all users whose name matches the given string.

    The comparison is case-insensitive. Loads user data from 'users.json'
    and prints each matching user dictionary to the console.
    :param
        name (str): The name to filter users by.
    :return: None
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if
                      user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_by_age(age):
    """
    Filter and print all users whose age matches the given integer.

    Loads user data from 'users.json' and prints each matching user
    dictionary to the console. Only exact integer matches are returned.
    :param
        age (int): The age value used to filter users.
    :return: None
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["age"] == age]

    for user in filtered_users:
        print(user)

if __name__ == "__main__":
    filter_option = input(
        "What would you like to filter by? "
        "(Currently, only 'name'  and 'age' is supported): "
    ).strip().lower()

    if filter_option == "age":
        age_to_search = input("Enter the age as integer to filter user: ").strip()
        if age_to_search.isdigit():
            age_to_search_int = int(age_to_search)
            filter_by_age(age_to_search_int)
        else:
            print("Please enter a valid age as integer.")
    elif filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    else:
        print("Filtering by that option is not yet supported.")