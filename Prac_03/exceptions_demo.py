"""
CP1404 - Practical 3
Answer the following questions:
1. When will a ValueError occur?
when enter string or float instead of int

2. When will a ZeroDivisionError occur?
when denominator is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    # 3 can't divide by 0
    while denominator == 0:
        print("Can't divide by zero try again")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:  #
    print("Cannot divide by zero!")
print("Finished.")
