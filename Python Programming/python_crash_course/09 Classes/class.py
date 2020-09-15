class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title()+" is now sitting")
    def roll_over(self):
        print(self.name.title()+" rolled over!")
    
animal = Dog('Shelly',8)
animal2 = Dog('Jelly',7)
# calling a instance
print(animal.name)
print(animal.age)

# calling methods
animal.sit()
animal.roll_over()
# animal2 instance and methods
print(animal2.name)
print(animal2.age)
animal2.sit()
animal2.roll_over()