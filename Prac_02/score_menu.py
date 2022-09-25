"""CP1404 - Practical 2 - SCORE MENU"""


MENU = """R - Results
S - Stars
Q - Quit"""


def main():
    """score menu"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "R":
            score = get_valid_score()
            print(f"A score of {score} is {determine_result(score)}.")
        elif choice == "S":
            score = get_valid_score()
            display_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Goodbye")


def get_valid_score():
    """get a valid score"""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def display_stars(score):
    """display stars based on score"""
    for i in range(0, int(score)):
        print("*", end="")
    print()
    return


def determine_result(score):
    """determines result from score"""
    if score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()
