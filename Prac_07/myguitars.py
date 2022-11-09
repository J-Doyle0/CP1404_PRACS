from Prac_06.guitar import Guitar

FILENAME = 'guitars.csv'


def main():
    guitars = get_guitars()
    for guitar in guitars:
        print(guitar)
    guitars.sort()
    add_guitars(guitars)
    guitars.sort()
    write_guitars(guitars)


def write_guitars(guitars):
    out_file = open(FILENAME, 'w')
    for guitar in guitars:
        out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")
    out_file.close()


def add_guitars(guitars):
    """add new guitar to guitars"""
    print("Add new guitars")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(guitar, "added.")
        name = input("Name: ")
    return


def get_guitars():
    """read guitar file and saves as list of objects"""
    guitars = []
    in_file = open(FILENAME, 'r')
    for line in in_file:
        guitar = line.strip().split(',')
        name = guitar[0]
        year = int(guitar[1])
        cost = float(guitar[2])
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
    in_file.close()
    return guitars


main()
