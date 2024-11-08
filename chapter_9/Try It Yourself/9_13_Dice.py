#9-13 Dice
from random import randint
class Dice():
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_dice(self):
        print(randint(1,self.sides))
        
dice_6 = Dice(6)
print("Dice 6 sides:")
for value in range(10):
    dice_6.roll_dice()
    
dice_10 = Dice(10)
print("Dice 10 sides:")
for value in range(10):
    dice_10.roll_dice()

dice_20 = Dice(20)
print("Dice 20 sides:")
for value in range(10):
    dice_20.roll_dice()