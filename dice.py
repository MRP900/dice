# Hot dice rolling action with classes and inheritance
from random import randint

class Dice:
    def __init__(self, sides=6):
        self.sides = sides
        self.rolls_list = []
    
    def roll(self, rolls=1):
        results = [randint(1, self.sides) for x in range(0, rolls)]
        self.rolls_list = results
        return results

    def display_rolls(self):
        rollCount = 0

        if self.rolls_list:
            for i in self.rolls_list:
                rollCount += 1
                print(f"{rollCount}: {i}")
        else:
            print("This dice hasn't been rolled.")

        
class D20(Dice):
    def __init__(self, sides=20):
        self.sides = sides

        
if __name__ == "__main__":
    
    diceA = Dice()
    print("--Dice A--")
    diceA.roll(25)
    diceA.display_rolls();
    
    print("--Dice B--")
    diceB = D20()
    diceB.roll(25)
    diceB.display_rolls()

    print("--Dice C--")
    diceC = Dice()
    diceC.display_rolls()
