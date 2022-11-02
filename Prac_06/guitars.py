"""
guitars
Estimate: 70 minutes
Actual:   85
"""
from Prac_06.guitar import Guitar


def main():
    """guitar program using Guitar class."""
    guitars = []
    # guitars.append((Guitar("Fender Stratocaster", 2014, 765.4)))
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(guitar, "added.\n")
        name = input("Name: ")
    print("\n... snip ...\n")
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = " (vintage)"
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()
