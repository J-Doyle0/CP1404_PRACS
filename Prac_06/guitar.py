"""
guitar
Estimate: 70 minutes
Actual:   85
"""
VINTAGE = 50
CURRENT_YEAR = 2022


class Guitar:
    """represent a guitar class"""

    def __init__(self, name='', year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """displays guitar information"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """get the age of guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """determine if guitar is vintage"""
        return self.get_age() >= VINTAGE
