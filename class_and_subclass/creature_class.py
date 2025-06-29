#!/usr/bin/python3

# Fantasy Creature Class

class Creature:
    def __init__(self, name, hp):
        is_alive = True
        self.is_alive = is_alive
        self.name = name
        self.hp = hp
        if self.hp = 0:
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
{self.name} has died! it's HP is {self.hp}
                  """)
        else:
                  print(f"""
{self.name} has taken {amount} points of damage.
{self.name}'s HP is {self.hp} points.
                         """)
        return self.hp
