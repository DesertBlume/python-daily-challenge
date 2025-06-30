#!/usr/bin/python3

# Program name: Game loop
# Program purpose: to practice loops
# Author: Hmoad Hajali
# Date & version: june 29th 2025 version 0.1.0
# Start time: 10:05 am 
# End time: end
from class_and_subclass.player_class import Player
from class_and_subclass.goblin_class import Goblin
import random
turn = 1
hp = 10
name = input(" Welcome adventurer! what is your name? ")
goblin = Goblin("Gorak the Goblin", 50)
fighter = Player(name, hp)
while True and fighter.hp > 0:
    untype_choice = input(f"""
1. Fight!
2. Rest!
3. Check status
4. Quit!
""")
    try:
        choice = int(untype_choice)
    except ValueError:
        print(" type cast failed input 1 2 3")
        continue
    if choice == 1:
        if goblin.hp > 0:
            if turn == 1:
                print(f"{fighter.name} gets the first hit on {goblin.name}!")
                fighter.fight(goblin)

                if goblin.hp > 0:
                    goblin.fight(fighter)
            else:
                print(f"{goblin.name} gets the first hit on {fighter.name}!")
                goblin.fight(fighter)
                if fighter.hp <= 0:
                    pass
                else:
                    fighter.fight(goblin)

        else:
            print(f"{goblin.name} is dead. There is no thing for you to fight!")
    elif choice == 2:
        print(f" Sometimes you just have to take a break")
        fighter.rest()
    elif choice == 3:
        fighter.status()
    elif choice == 4:
        print(f" I hope you had a good time {fighter.name}")
        break
    else:
        print(" pick one of the numbers in the options please")

    if turn == 1:
        turn = 2
    else:
        turn = 1
    
if fighter.hp <= 0:
    print(f" {fighter.name} died. what a fool!")
else:
    print(f" {fighter.name}, thank you for playing. see you next time mohahahahahaha")




