"""CP1404 - Practical 2 - SCORES"""
import random


def main():
    score = float(input("Enter score: "))
    print(f"A score of {score} is {determine_result(score)}.")
    score = random.randint(0, 100)
    print(f"A random score of {score} is {determine_result(score)}.")


def determine_result(score):
    """determines result from score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()
