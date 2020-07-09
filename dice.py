#!/usr/bin/env python
# Hot dice rolling action with classes and inheritance
from random import randint

class Dice:
    def __init__(self, sides=6):
        self.sides = sides
        self.rolls_list = []
    
    def roll(self, rolls=1):
        self.rolls_list = [randint(1, self.sides) for x in range(0, rolls)]

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
        self.rolls_list = []
        
        messages = {
            1 : "CRITICAL FAILURE",
            20 : "CRITICAL SUCCESS"
        }
        
        # Override parent class method
        def display_rolls(self):
            rollCount = 0
            if self.rolls_list:
                for i in self.rolls_list:                  
                    rollCount += 1
                    if i in messages.keys():
                        print(f"{rollCount}: {i} - {messages[i]}")
                    else:
                        print(f"{rollCount}: {i}")
            else:
                print("This dice hasn't been rolled.")

        
if __name__ == "__main__":
    
    diceA = Dice()
    print("\n--Dice A--")
    diceA.roll(25)
    diceA.display_rolls();
    
    print("\n--Dice B--")
    diceB = D20()
    diceB.roll(25)
    diceB.display_rolls()

    print("\n--Dice C--")
    diceC = Dice()
    diceC.display_rolls()

    print("\n--Dice D--")
    diceD = Dice(4)
    diceD.roll(5)
    diceD.display_rolls()
