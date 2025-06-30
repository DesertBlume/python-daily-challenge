#!/usr/bin/python3

# Program name: Goblin SubClass
# Program purpose: This is the code for the Goblin SubClass
# Author: Hmoad Hajali
# Date & version: June 30th 2025
# Start time: 8:37AM
# End time: end

from class_and_subclass.creature_class import Creature
import random
class Goblin(Creature):

    def fight(self, target):
        amount = random.randint(1, 3)
        print(f"""
{self.name} has attacked {target}
              """)
        target.take_damage(amount)
        if target.hp <= 0:
            print(f"{self.name} has slain {target}")
        return self.hp


        
