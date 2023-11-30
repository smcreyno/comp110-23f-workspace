"""Class writing for QZ04."""

from __future__ import annotations

class ChristmasTreeFarm:
    """A christmas tree farm!"""

    plots: list[int]

    def __init__(self, plots: int, initial_planning: int):
        """Constructor."""
        self.plots = []
        i: int = 0
        while i < initial_planning:
            self.plots.append(1)
            i += 1
        while i < len(self.plots):
            self.plots.append(0)
            i += 1
    
    def plant(self, plot_index: int) -> None:
        """Planting."""
        self.plots[plot_index] = 1

    def growth(self) -> None:
        """Growing."""
        i: int = 0
        while i < len(self.plots):
            if self.plots[i] != 0:
                self.plots[i] += 1
            i += 1
    
    def harvest(self, replant: bool) -> int:
        """Harvesting."""
        i: int = 0
        count: int = 0
        while i < len(self.plots):
            if self.plots[i] > 5:
                if replant is True:
                    self.plots[i] = 1
                else:
                    self.plots[i] = 0
                count += 1
            i += 1
        return count
    
    def __add__(self, rhs: ChristmasTreeFarm) -> ChristmasTreeFarm:
        """Overloading the addition operator."""
        tree: int = 0
        first: int = len(self.plots)
        second: int = len(rhs.plots)
        for plot in self.plots:
            if plot > 0:
                tree += 1
        for plot in self.rhs:
            if plot > 0:
                tree += 1
        return ChristmasTreeFarm(first + second, tree)
    
    def __str__(self) -> str:
        """String."""
        return f"Total Trees: {self.plots}"
    
farm: ChristmasTreeFarm = ChristmasTreeFarm(6,2)
farm.growth
print(farm.growth)