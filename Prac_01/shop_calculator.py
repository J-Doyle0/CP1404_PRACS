"""
CP1404 - Practical 1
shop calculator
"""

TOTAL = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for items in range(number_of_items):
    price_of_item = float(input("Price of item: $"))
    total_cost = TOTAL + price_of_item
    TOTAL = total_cost
if TOTAL > 100:
    TOTAL = TOTAL - (TOTAL * 0.10)  # 10%
print(f"Total price for {number_of_items} items is ${TOTAL:.2f}")
