
from Prac_06.guitar import Guitar
FILENAME = 'guitars.csv'


def main():
    guitars = get_guitars()
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def get_guitars():
    """read guitar file and saves as list of objects"""
    guitars = []
    in_file = open('guitars.csv', 'r')
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
