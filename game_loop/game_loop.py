#!/usr/bin/python3

# Program name: Game loop
# Program purpose: to practice loops
# Author: Hmoad Hajali
# Date & version: june 29th 2025 version 0.1.0
# Start time: 10:05 am 
# End time: end
from class_and_subclass.player_class import Player
import random
hp = 10
name = input(" Welcome adventurer! what is your name? ")

fighter = Player(name, hp)
while True and fighter.hp > 0:
    fight_dice = random.randint(1, 5)
    rest_dice = random.randint(1, 3)
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
        print(f" You fight and take some damage")
        fighter.fight()
        print(f"{fighter.name}'s HP is now {fighter.hp}")
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
    
if fighter.hp <= 0:
    print(f" {fighter.name} died. what a fool!")
else:
    print(f" {fighter.name}, thank you for playing. see you next time mohahahahahaha")




