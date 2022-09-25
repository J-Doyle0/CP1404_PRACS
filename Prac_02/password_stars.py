"""CP1404 - PRACTICAL 2 - PASSWORD STARS"""


MINIMUM_LENGTH = 8


def main():
    password = get_password()
    display_asterisks(password)


def display_asterisks(password):
    """will display password as asterisks"""
    for char in range(0, len(password)):
        print("*", end="")


def get_password():
    """will get valid password"""
    password = input("Password")
    while len(password) < MINIMUM_LENGTH:
        print(f"Password doesn't meet requirements (minimum {MINIMUM_LENGTH} letters)")
        password = input("Password: ")
    return password


main()
