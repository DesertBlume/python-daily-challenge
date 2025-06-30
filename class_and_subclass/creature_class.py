#!/usr/bin/python3

# Fantasy Creature Class

import random
class Creature:
    def __init__(self, name, hp):
        is_alive = True
        self.is_alive = is_alive
        self.name = name
        self.hp = hp
        max_hp = self.hp
        self.max_hp = max_hp
        if self.hp == 0:
            self.is_alive = False


    def __str__(self) -> str:
        return f"""{self.name}"""

    def status(self):
        print(f"""
{self.name} has {self.hp} HP
              """)


    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
            print(f"""
{self.name} has died!
                  """)
        else:
                  print(f"""
{self.name} has taken {amount} points of damage.
{self.name}'s HP is {self.hp} points.
                         """)
        return self.hp

    def fight(self, target):
        amount = random.randint(1, 5)
        print(f"""
{self.name} has attacked {target}
              """)
        target.take_damage(amount)
        if target.hp <= 0:
            print(f"{self.name} has slain {target}")
        return self.hp



    def rest(self):
        self.hp += random.randint(1, 3)
        if self.hp >= self.max_hp:
            self.hp = self.max_hp
            print(f" {self.name} healed up to the max! HP is at {self.hp} points!")
        else:
            print(f" {self.name} healed to {self.hp} HP points!")
        return self.hp







