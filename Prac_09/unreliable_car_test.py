"""unreliable car test"""

from Prac_09.unreliable_car import UnreliableCar


def main():
    """Test some UnreliableCars."""

    reliable_car = UnreliableCar("ol' reliable", 100, 85)
    unreliable_car = UnreliableCar("old & unreliable", 100, 15)

    for i in range(1, 10):
        print(f"\nAttempting to drive {i}km:")
        print(f"{reliable_car.name:12} drove {reliable_car.drive(i):2}km")
        print(f"{unreliable_car.name:12} drove {unreliable_car.drive(i):2}km")
    print('')
    print(reliable_car)
    print(unreliable_car)


main()
