# parent class
# in inheritance parent class must be called before child class 
class Car():
    def __init__(self,year,model,brand):
        self.brand = brand
        self.model = model
        self.year = year
    
    def get_description(self):
        long_name = self.brand+" "+ self.model+" "+str(self.year)
        return long_name.title()
class Battery():
    # set default battery_size value 100
    def __init__(self,battery_size = 100):
        self.battery_size = battery_size
    def battery_descrip(self):
        print("This car has a "+str(self.battery_size)+"-kWh battery")
    
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 90:
            range = 300
        message = "This car can go approximately "+ str(range)
        message += " miles on a full charge."
        print(message)

# child class
# parent class must be defined in child class
class Electric_Car(Car):
    # take information to create a Car instance
    def __init__(self, year,model,brand):
        # super class is a special class in python
        # it creates connection between parent and child class
        # super named after super class and sub class concept 
        super().__init__(year,model,brand)
        self.battery = Battery(90)

# instance of Electric_Car() class and store in my_tesla 
my_tesla = Electric_Car(2016,'model s','tesla')
# print the child class description
print(my_tesla.get_description())
my_tesla.battery.battery_descrip()       
my_tesla.battery.get_range()