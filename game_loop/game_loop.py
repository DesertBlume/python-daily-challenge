#!/usr/bin/python3

# Program name: Game loop
# Program purpose: to practice loops
# Author: Hmoad Hajali
# Date & version: june 29th 2025 version 0.1.0
# Start time: 10:05 am 
# End time: end

import random
hp = 10
player = input(" Welcome adventurer! what is your name? ")

while True and hp > 0:
    fight_dice = random.randint(1, 5)
    rest_dice = random.randint(1, 3)
    untype_choice = input(f"""
1. Fight!
2. Rest!
3. Quit!
""")
    #try:
     #   choice = int(untype_choice)
    #except ValueError:
     #   print(" input 1 2 3")
    choice = int(untype_choice)
    if choice == 1:
        print(f" You fight and take some damage")
        hp -= fight_dice
        print(fight_dice)
        print(f" {player} took {fight_dice} points in damage {player}'s HP is now {hp}")
    elif choice == 2:
        print(f" Sometimes you just have to take a break")
        hp += rest_dice
        if hp >= 10:
            hp = 10
            print(f" You've healed up to the max! your HP is {hp}")
        else:
            print(f"{player}'s HP healed to {hp} HP points!")
    elif choice == 3:
        print(f" I hope you had a good time {player}")
        break
    else:
        print(" pick one of the numbers in the options please")
    
if hp <= 0:
    print(f" {player} died. what a fool!")
else:
    print(f" {player}, thank you for playing. see you next time mohahahahahaha")




