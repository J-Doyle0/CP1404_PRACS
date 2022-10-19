"""
emails
Estimate: 40 minutes
Actual:   120* minutes
"""


def main():
    """email to name"""
    email_to_name = {}
    user_email = input("Email: ")
    while user_email != '':
        user_name = get_name(user_email)
        email_to_name[user_email] = user_name
        user_email = input("Email: ")
    display_dictionary(email_to_name)


def get_name(user_email):
    """gets name from email"""
    user_name = user_email.title().split('@')
    del user_name[1]
    user_name = user_name[0]
    if '.' in user_name[0]:
        user_name = user_name[0].split('.')
        user_name = user_name[0] + ' ' + user_name[1]
    confirm_name = input(f"Is your name {user_name}? (Y/n) ").lower()
    if confirm_name != 'y' or confirm_name != '':
        return user_name
    else:
        user_name = input("Name: ")
        return user_name


def display_dictionary(email_to_name):
    """displays names and emails"""
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


main()
