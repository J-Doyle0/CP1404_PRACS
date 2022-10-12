import random


MINIMUM = 1
MAXIMUM = 45
NUMBER_OF_NUMBERS = 6

quick_list = []
quick_picks = int(input("How many quick picks do you want? "))
# rows = [pick for pick in range(quick_picks)]
for picks in range(quick_picks):
    for i in range(NUMBER_OF_NUMBERS):
        number = random.randint(MINIMUM, MAXIMUM)
        while number in quick_list:
            number = random.randint(MINIMUM, MAXIMUM)
        quick_list.append(number)
        quick_list = sorted(quick_list)
    print(*quick_list)
    quick_list.clear()
