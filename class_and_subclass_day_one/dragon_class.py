#!/usr/bin/python3

# Dragon Class

#from day_one import creature_class
from creature_class import Creature

class Dragon(Creature):
    pass    


    def breathe_fire(self):
        print("DIE IN THE INFURNO")

    
    def status(self):
        return print(f"The Mighty! {self.name} has {self.hp}HP!")


