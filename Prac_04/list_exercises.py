"""Write a program that prompts the user for 5 numbers and then stores each of these in a list called numbers.
The program should then output information about these numbers, as in the output below.
Note that you can use the functions min, max, sum and len, and you can use the append method to add a number to a list."""


NUMBER_OF_NUMBERS = 5
numbers = []
for i in range(NUMBER_OF_NUMBERS):
    number = int(input("Number: "))
    numbers.append(number)
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers)/len(numbers)}")


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
name = input("What is your user name? ")
if name in usernames:
    print("Access granted")
else:
    print("Access denied")
