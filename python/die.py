from random import randint

class Die():

    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        print(randint(1,self.sides))