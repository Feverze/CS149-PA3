"""Defines the Space class.

Author: Francesco Benedetto
Version: 05/02/23

This work complies with the JMU Honor Code.
"""


class Space:
    """An individual parking space in the garage.

    Attributes:
        _label (str): The label for the space (Ex: "A 0").
        _dimensions (tuple): The space's length, width, and height.
        _car (Car): The car currently parked in this space.
    """

    def __init__(self, label, dimensions, car=None):
        self._label = label
        self._dimensions = dimensions
        self._car = car

    def get_label(self):
        return self._label

    def get_dimensions(self):
        return self._dimensions

    def get_car(self):
        return self._car

    def set_car(self, car):
        self._car = car

    def is_occupied(self):
        return self._car is not None

    def can_park(self, car):
        car_length, car_width, car_height = car.get_dimensions()
        space_length, space_width, space_height = self._dimensions
        if car_length <= space_length:
            if car_width + 4 <= space_width:
                if car_height + 1 <= space_height:
                    return True
        return False

    def __str__(self):
        dimensions_str = f"{self._dimensions[0]}x{self._dimensions[1]}x{self._dimensions[2]}"
        if self._car is not None:
            car_str = str(self._car.get_plate())
            return f"Space: {self._label}, {dimensions_str}, {car_str}"
        else:
            return f"Space: {self._label}, {dimensions_str}, not occupied"
