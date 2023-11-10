"""File to define Fish class."""


class Fish:
    """A class to define a fish."""
    age: int
    
    def __init__(self, age_init: int = 0):
        """Constructor."""
        self.age = age_init
        return None
    
    def one_day(self):
        """Increases age by 1."""
        self.age += 1
        return None