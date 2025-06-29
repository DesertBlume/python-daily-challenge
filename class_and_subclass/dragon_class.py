#!/usr/bin/python3

# Dragon Class

#from day_one import creature_class
from creature_class import Creature

class Dragon(Creature):
    


    def breathe_fire(self):
        print("""
DIE IN THE INFURNO!""")

    
    def status(self):
        print(f"""
The Mighty! {self.name} has {self.hp} HP!
              """)

    
    def attack(self, target, damage_amount):
        print (f"""
{self.name} attacked {target}!""")
        target.take_damage(damage_amount)
        return target.hp

