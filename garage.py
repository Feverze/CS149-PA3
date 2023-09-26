"""Defines the Garage class.

Author: Francesco
Version: 05/02/23

This work complies with the JMU Honor Code.
"""
from space import Space
import datetime


class Garage:
    """Represents a parking garage and assigns cars to spaces.

    Attributes:
        _spaces (list): Parking spaces, sorted by distance from the entrance.
        _cars (dict): Maps license plate strings to assigned parking spaces.
    """

    def __init__(self, data):
        self._spaces = []
        self._cars = {}
        for line in data:
            info = line.strip().split(",")
            label = info[0]
            W = int(info[1])
            L = int(info[2])
            H = int(info[3])
            space = Space(label, (W, L, H))
            self._spaces.append(space)

    def get_capacity(self):
        return len(self._spaces)

    def get_occupied(self):
        return len(self._cars)

    def assign_space(self, car):
        for x in self._spaces:
            fit = x.can_park(car)
            occupied = x.is_occupied()
            if fit and not occupied:
                x.set_car(car)
                self._cars[car.get_plate()] = x
                return x
        return None

    def remove_car(self, plate):
        for x, space in self._cars.items():
            if x == plate:
                car = space.get_car()
                del self._cars[plate]
                space.set_car(None)
                return car

    def impound_cars(self, now):
        week = datetime.timedelta(weeks=1)
        towed = []
        y = dict(self._cars)
        for x in y:
            space = self._cars[x]
            car = space.get_car()
            car_time = now - car.get_arrival()
            if car_time > week:
                towed.append(car)
                self.remove_car(x)
        return towed

    def __str__(self):
        space = self.get_capacity() - self.get_occupied()
        return f"Garage: {space} spaces available"
