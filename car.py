class Car():
    """ This  is a car class that will display the make, model, color """
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
        self.gas = 100
    def __str__(self):
        return "{}, {}, {}".format(self.make, self.model, self.color)

    def drive(self):
        self.gas -= 10
        print(self.gas)
    
    def fill_tank(self):
        self.gas = 100
        print('Car is now filled')

    def check_gas(self):
        print(f"Gas handle: {self.gas}")

car1 = Car("Mercedes", "C Class", "White")

# print(car1)

car1.drive() # equal to 90
car1.drive() # equal to 80
car1.fill_tank()
car1.check_gas()
