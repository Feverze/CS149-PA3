"""Defines the DukesParking class.

Author: Francesco
Version: 05/02/23

This work complies with the JMU Honor Code.
"""
from car import Car
from garage import Garage
import math
import datetime


class DukesParking:
    """Simulation of cars arriving/departing and making payments.

    Attributes:
        _garage_data (list): Lines of the garage file.
        _events_data (list): Lines of the events file.
    """

    def __init__(self, garage_file, events_file):
        with open(garage_file) as f:
            self._garage_data = f.readlines()
        with open(events_file) as f:
            self._events_data = f.readlines()

    def run(self):
        garage = Garage(self._garage_data)
        for x in self._events_data:
            info = x.split(',')
            event_time = datetime.datetime.strptime(info[0], '%Y-%m-%d %H:%M:%S')
            gate = info[1]
            plate_number = info[2]
            dim_str = info[3]
            dim_list = dim_str.split('x')
            L = int(dim_list[0])
            W = int(dim_list[1])
            H = int(dim_list[2])
            dimension = (L, W, H)
            if gate == "Arrive":
                car = Car(plate_number, dimension, event_time)
                print(f'ARRIVAL {car}')
                space = garage.assign_space(car)
                if space:
                    print(f"PARK_IN {space}")
                else:
                    print("NO SPACES AVAILABLE")
            elif gate == "Depart":
                car = garage.remove_car(plate_number)
                print(f'EXITING {car}')
                fee = self.payment(car.get_arrival(), event_time)
                print(f'PAYMENT ${fee:.2f}')
        impounded = garage.impound_cars(now=event_time)
        for car in impounded:
            print(f"IMPOUND {car}")
            
    @staticmethod
    def payment(arrive, depart, hourly_rate=1, daily_limit=20):
        stay_time = depart - arrive
        total_hours = stay_time.total_seconds() / 3600
        if total_hours <= 24:
            total_price = min(total_hours * hourly_rate, daily_limit)
        else:
            full_days = int(total_hours // 24)
            remaining_hours = int(total_hours % 24)
            daily_fee = min(daily_limit, hourly_rate * 24)
            hourly_fee = remaining_hours * hourly_rate
            total_price = full_days * daily_fee + hourly_fee
        return math.ceil(total_price)
