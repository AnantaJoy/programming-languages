# Car class 
class Car():
    def __init__(self, brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer = 10
    def car_description(self):
        long_name = self.brand+" "+self.model+" "+str(self.year)
        return long_name.title()

    def odometer_read(self):
        print("My car has "+ str(self.odometer)+" miles.")
    def update_odometer(self,milage):
        if milage>=self.odometer:
            self.odometer = milage
        else:
            print("You can't roll back odometer back")
    def increment_odometer(self,miles):
        self.odometer += miles

my_car = Car('audi','a8',2020)
brother_car = Car('toyota','GT-86',2019)
friend_car = Car('BMW','m3','2018')
print(my_car.car_description())
print(brother_car.car_description())
print(friend_car.car_description())

# modify attibute value
my_car.odometer = 100
my_car.odometer_read()

# modify attibute value
my_car.update_odometer(30)
my_car.odometer_read()

# increment odometer value
my_car.increment_odometer(200)
my_car.odometer_read()