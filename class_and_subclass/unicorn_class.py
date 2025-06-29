#!/usr/bin/python3

# Unicorn class

from creature_class import Creature

class Unicorn(Creature):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        max_hp = self.hp + 5
        self.max_hp = max_hp  

    def heal(self, heal):
        self.hp += heal
        if self.hp >= self.max_hp:
            self.hp = self.max_hp
            print(f"""
{self.name} is full of life! it can't heal anymore! It's sitting at {self.hp} HP points!
                  """)
        else:
                  print(f"""
I am healing! {self.name}'s HP is {self.hp} points now!
                        """)
        return self.hp

