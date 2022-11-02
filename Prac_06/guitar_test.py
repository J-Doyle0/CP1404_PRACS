"""
guitar test
Estimate: 70 minutes
Actual:   85
"""
from Prac_06.guitar import Guitar

CURRENT_YEAR = 2017


def run_tests():
    """Tests for Guitar class."""

    guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    other_guitar = Guitar("Another Guitar", 2013, 764.4)
    print(f"{guitar.name} get_age() - Expected 100. Got {guitar.get_age()}")
    print(f"{other_guitar.name} get_age() - Expected 9. Got {other_guitar.get_age()}")
    print('')
    print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
    print(f"{other_guitar.name} is_vintage() - Expected False. Got {other_guitar.is_vintage()}")


run_tests()
