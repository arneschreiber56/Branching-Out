import json


def load_users():
    """
    Load and return users from the json file.
    :return: json.load(file)
    """
    with open("users.json", "r") as file:
        return json.load(file)


def filter_users_by_name(users, name):
    """
    Filter and return all users whose name matches the given string.
    The comparison is case-insensitive. Gets user data from load_users().
    :param
        users (list): List of user dictionaries.
        name (str): The name to filter users by.
    :return:
        filtered users (list): Filtered list of matching user dictionaries.
    """
    return [
        user for user in users if user["name"].lower() == name.lower()
    ]


def filter_by_age(users, age):
    """
    Filter and return all users whose age matches the given integer.
    Gets user data from load_users(). Only exact integer matches are returned.
    :param
        users (list): List of user dictionaries.
        age (int): The age value used to filter users.
    :return:
        filtered users (list): Filtered list of matching user dictionaries.
    """
    return [user for user in users if user["age"] == age]


def filter_by_email(users, email):
    """
    Filter and return all users whose email matches the given string.
    The comparison is case-insensitive. Gets user data from load_users().
    :param
        users (list): List of user dictionaries.
        email (str): The email string to filter users by.
    :return:
        filtered users (list): Filtered list of matching user dictionaries.
    """
    return [
        user for user in users if user["email"].lower() == email.lower()
    ]

def main():
    # loading users list only one time should be enough
    users = load_users()
    while True:
        filter_option = input(
            "What would you like to filter by? "
            "(You can filter by 'name', 'email'  and 'age' or quit with 'q'): "
        ).strip().lower()
        if not filter_option:
            print("Please enter a valid option.")
            continue
        if filter_option == "q":
            print("Thank you and goodbye!")
            break
        if filter_option == "age":
            age_to_search = input(
                "Enter the age as integer to filter user: ").strip()
            if age_to_search.isdigit():
                age_to_search_int = int(age_to_search)
                results = filter_by_age(users, age_to_search_int)
            else:
                print("Please enter a valid age as integer.")
                continue
        elif filter_option == "name":
            name_to_search = input("Enter a name to filter users: ").strip()
            results = filter_users_by_name(users, name_to_search)
        elif filter_option == "email":
            email_to_search = input("Enter a email to filter users: ").strip()
            results = filter_by_email(users, email_to_search)
        else:
            print("Please enter a valid option.")
            continue
        if results:
            for user in results:
                print(user)
        else:
            print("Sorry, no users matching the given criteria.")

if __name__ == "__main__":
    main()