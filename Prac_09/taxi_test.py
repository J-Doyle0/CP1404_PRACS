"""taxi test"""
from Prac_09.taxi import Taxi


def run_tests():
    """Test for taxi.py"""
    my_taxi = Taxi('Prius 1', 100)
    my_taxi.drive(40)
    print(my_taxi, f"current fare ${my_taxi.get_fare()}")
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi, f"current fare ${my_taxi.get_fare()}")


run_tests()
