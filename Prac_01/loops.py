"""
CP1404 - Practical 1
Loops
"""


for i in range(1, 21, 2):
    print(i, end=' ')
print()


for i in range(0, 110, 10):
    print(i, end=' ')
print()


for i in range(20, 0, -1):
    print(i, end=' ')
print()


stars = int(input("How many stars?: "))
for i in range(0, stars, 1):
    print("*", end='')
print()


stars = int(input("How many stars?: "))
for i in range(0, stars + 1, 1):
    print("*" * i)
print()


