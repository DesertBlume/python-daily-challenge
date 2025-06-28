#!/usr/bin/python3

# Unicorn class

from creature_class import Creature

class unicorn(Creature):

    def heal(self, heal):
        self.heal = heal
        print(f"I am healing! {self.name}'s HP is {self.heal + self.hp} points now!")
        return self.hp
        return hp 

