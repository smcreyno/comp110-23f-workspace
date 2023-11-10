"""File to define Bear class."""


class Bear:
    """A class to represent bear."""
    age: int
    hunger_score: int
    
    def __init__(self, age_init: int = 0, hunger_score_init: int = 0):
        """Constructor."""
        self.age = age_init
        self.hunger_score = hunger_score_init
        return None
    
    def one_day(self):
        """Increases value of age by 1."""
        self.hunger_score -= 1
        self.age += 1
        return None
    
    def eat(self, num_fish: int):
        """Bears gotta eat."""
        self.hunger_score += num_fish
        return None