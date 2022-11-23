"""silver service taxi test"""

from Prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    taxi = SilverServiceTaxi("Hummer", 200, 4)
    print(taxi)
    taxi = SilverServiceTaxi("taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(f"${taxi.get_fare()}")


main()
