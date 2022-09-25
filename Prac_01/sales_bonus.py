"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Sales totals: $"))
while sales > 0:
    if sales >= 1000:
        bonus = 0.15  # 15%
    else:
        bonus = 0.10  # 10%
    total_bonus = sales * bonus
    print(f"Sales of ${sales} will earn you a bonus of ${total_bonus}")
    sales = float(input("Sales totals: $"))
