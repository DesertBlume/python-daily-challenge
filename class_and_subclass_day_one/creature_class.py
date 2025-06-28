#!/usr/bin/python3

# Fantasy Creature Class

class Creature:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
         

    def __str__(self) -> str:
        return f"{self.name}({self.hp})"

    def status(self):
        return print(f"{self.name} has {self.hp} HP")


    def take_damage(self, amount):
        self.amount = amount
        self.hp = self.hp - self.amount
        return print(f"""
{self.name} has taken {self.amount} points of damage.
{self.name}'s HP is {self.hp} point.
                    """)
 

