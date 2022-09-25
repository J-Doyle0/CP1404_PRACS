MINIMUM_LENGTH = 8
password = input("Password: ")
while len(password) < MINIMUM_LENGTH:
    print(f"Password doesn't meet requirements (minimum {MINIMUM_LENGTH} letters)")
    password = input("Password: ")
for char in range(0, len(password)):
    print("*", end="")
