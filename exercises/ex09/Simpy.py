"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730642974"


class Simpy:
    """A Simpy class."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Constructor Simpy."""
        self.values = values

    def ones(self, values: list[float]) -> list[float]:
        """Initialize the values of Simpy to the argument passed in."""
        return self.values
    
    def __str__(self) -> str:
        """A Simpy object is converted to a string representation."""
        return f"Simpy({self.values})"
    
    def fill(self, val_fill: float, int_times: int) -> None:
        """Fill a Simpy's values with a number of repeated values."""
        if self.values == "Simpy([])":
            i: int = 0
            while i < int_times:
                self.values.append(val_fill)
                i += 1
        else:
            self.values = []
            i: int = 0
            while i < int_times:
                self.values.append(val_fill)
                i += 1
        return self.values
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in values with a range."""
        assert step != 0.0
        self.values = [start]
        value: float = start
        while value != stop:
            value += step
            if value == stop:
                return self.values
            else:
                self.values.append(value)
        return self.values
    
    def sum(self) -> float:
        """Compute and return the sum of all values."""
        total: float = 0.0
        i: int = 0
        while i < len(self.values):
            total += self.values[i]
            i += 1
        return total
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Using the addition operator in conjunction with Simpy and floats."""
        new: Simpy = Simpy([])
        if type(rhs) is float:
            for item in self.values:
                new.values.append(item + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                val1: float = self.values[i]
                val2: float = rhs.values[i]
                new.values.append(val1 + val2)
                i += 1
        return new
        
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Using the power operator in conjunction with Simpy objects and floats."""
        new: Simpy = Simpy([])
        if type(rhs) is Simpy:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                val1: float = self.values[i]
                val2: float = rhs.values[i]
                new.values.append(val1 ** val2)
                i += 1
        elif type(rhs) is float:
            for item in self.values:
                new.values.append(item ** rhs)
        return new
        
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produce a mask based on the equality of values items with other objects/values."""
        my_list: list[bool] = []
        if type(rhs) is Simpy:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                if self.values[i] == rhs.values[i]:
                    my_list.append(True)
                else:
                    my_list.append(False)
                i += 1
        elif type(rhs) is float:
            for item in self.values:
                if item == rhs:
                    my_list.append(True)
                else:
                    my_list.append(False)
        return my_list
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produce a mask based on the greater than relationships between values."""
        my_list: list[bool] = []
        if type(rhs) is Simpy:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                if self.values[i] > rhs.values[i]:
                    my_list.append(True)
                else:
                    my_list.append(False)
                i += 1
        elif type(rhs) is float:
            for item in self.values:
                if item > rhs:
                    my_list.append(True)
                else:
                    my_list.append(False)
        return my_list
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Adds the ability to use the subscription operator with Simpy objects."""
        if type(rhs) is int:
            i: int = 0
            while i < len(self.values):
                if rhs == i:
                    return self.values[i]
                i += 1
        elif type(rhs) is list:
            new: Simpy = Simpy([])
            idx: int = 0
            while idx < len(self.values):
                if rhs[idx] is True:
                    new.values.append(self.values[idx])
                idx += 1
            return new