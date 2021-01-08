class Hole():
    def __init__(self, par, distance, color):
        self.par = par
        self.distance = distance
        self.color = color
        
    def __str__(self):
        return "{}, {}, {}".format(self.par, self.distance, self.color)

    def drive(self):
        self.distance -= 293
        print(f'Remaining distance {self.distance}')
    

    def second_shot(self):
        self.distance -= 100
        print(f'Remaining distance {self.distance}')

   

hole3 = Hole(5, 489, "White")

print(hole3)
hole3.drive()
hole3.second_shot()
