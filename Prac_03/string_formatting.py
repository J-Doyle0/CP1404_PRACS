"""CP1404 - Practical 3 - String formatting"""

name = "Gibson L-5 CES"
year = 1922
cost = 16035.4

# 1
print(f"{year} {name} for about ${cost:,.0f}!")

# 2
for i in range(0, 151, 50):
    print(f"{i:3}")
