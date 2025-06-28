#!/usr/bin/python3

# Dragon Class

#from day_one import creature_class
from creature_class import Creature

class Dragon(Creature):
    


    def breathe_fire(self):
        print("DIE IN THE INFURNO")

    
    def status(self):
        print(f"The Mighty! {self.name} has {self.hp} HP!")


