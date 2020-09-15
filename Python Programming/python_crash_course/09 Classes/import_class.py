# import car_class

from car_class import Car
from electric_car2 import *
"""
import Car
from Car import Battery,Car2
from Car import *
"""

my_new_car = Car('audi', 'a8', 2020)
print(my_new_car.car_description())
my_new_car.odometer_read()
my_new_car.update_odometer(100)
my_new_car.odometer_read()

my_electric_car = Car2(2018,'model s','tesla')
print(my_electric_car.get_description())