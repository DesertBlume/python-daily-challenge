#!/usr/bin/python3

# Unicorn class

from creature_class import Creature

class Unicorn(Creature):

    def heal(self, heal):
        self.hp += heal
        print(f"I am healing! {self.name}'s HP is {self.hp} points now!")
        return self.hp

