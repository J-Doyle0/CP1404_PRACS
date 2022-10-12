import random


MINIMUM = 1
MAXIMUM = 45
NUMBER_OF_NUMBERS = 6

numbers = []
quick_picks = int(input("How many quick picks do you want? "))
for picks in range(quick_picks):
    for i in range(NUMBER_OF_NUMBERS):
        number = random.randint(MINIMUM, MAXIMUM)
        while number in numbers:
            number = random.randint(MINIMUM, MAXIMUM)
        numbers.append(number)
        numbers = sorted(numbers)
    print(*numbers)
    numbers.clear()
