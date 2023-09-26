"""Defines the Car class.

Author: Francesco Benedetto
Version: 05/02/23

This work complies with the JMU Honor Code.
"""


class Car:
    """Information about a car trying to park in the garage.

    Attributes:
        _plate (str): The car's license plate (Ex: "ABC 123").
        _dimensions (tuple): The car's length, width, and height.
        _arrival (datetime): When the car entered the garage.
    """

    def __init__(self, plate, dimensions, arrival):
        self._plate = plate
        self._dimensions = dimensions
        self._arrival = arrival

    def get_plate(self):
        return self._plate

    def get_dimensions(self):
        return self._dimensions

    def get_arrival(self):
        return self._arrival

    def __str__(self):
        dimensions_str = "x".join(str(dimension) for dimension in self._dimensions)
        return f"Car: {self._plate}, {dimensions_str}, {self._arrival}"
