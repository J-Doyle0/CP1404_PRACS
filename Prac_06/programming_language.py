"""
programming languages
Estimate: 30 minutes
Actual:   43
"""


class ProgrammingLanguage:
    """represent a programming language"""

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """ display representation of language"""
        return f"{self.name}, {self.typing} typing, reflection={self.reflection}, first appeared in {self.year}"

    def is_dynamic(self):
        """determine if language is dynamic"""
        return self.typing == 'Dynamic'
