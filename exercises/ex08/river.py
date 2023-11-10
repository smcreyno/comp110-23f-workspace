"""File to define River class."""

__author__ = "730642974"


from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """A class to define a river."""
    day: int
    bears: list[int]
    fish: list[int]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removes animals that age out."""
        new_bears: list[int] = self.bears
        new_fish: list[int] = self.fish
        for elem in self.fish:
            if elem.age > 3:
                new_fish.pop()
        for elem in self.bears:
            if elem.age > 5:
                new_bears.pop()
        self.fish = new_fish
        self.bears = new_bears
        return None

    def bears_eating(self):
        """Bears eat 3 fish if there are more than 5 fish."""
        for bear in self.bears:
            if len(self.fish) > 4:
                bear.eat(3)
                self.remove_fish(3)
        return None
    
    def check_hunger(self):
        """A hungry bear will die."""
        new_bears: list[int] = self.bears
        for bear in self.bears:
            if bear.hunger_score < 0:
                new_bears.pop()
        self.bears = new_bears
        return None
        
    def repopulate_fish(self):
        """Two fish make 4 more fish."""
        n: int = len(self.fish)
        new_fish: int = (n // 2) * 4
        i: int = 0
        while i < new_fish:
            self.fish.append(Bear())
            i += 1
        return None
    
    def repopulate_bears(self):
        """Two bears make one more bear."""
        n: int = len(self.bears)
        new_bears: int = n // 2
        i: int = 0
        while i < new_bears:
            self.bears.append(Bear())
            i += 1
        return None
    
    def view_river(self) -> None:
        """Seeing the river."""
        print(f"~~~ Day {self.day}: ~~~\nFish population: {len(self.fish)}\nBear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
    
    def one_river_week(self):
        """Calls one_river_day() seven times."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
    
    def remove_fish(self, amount: int):
        """Removes amount Fish from the River."""
        i: int = 0
        while i < amount:
            self.fish.pop(0)
            i += 1
        return None
            
