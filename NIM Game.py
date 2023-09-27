# INF 120 - Fall 2022
# Project 10
# The Nim Game
# PALDEN TAMANG
# 15 Nov,2022


#importing the random module
import random

sticks = 13

#displaying the "board"
for i in range(sticks):
    print('|', end = ' ')
print(f"{sticks} sticks remaining")

#setting the maximum number of pickable sticks
maximum_pickable_sticks = 4

who_starts = random.randrange(1, 3)

#setting the condition for the game
while sticks > 0:
    
    #swapping between users
    
    if who_starts == 1:
        who_starts = 2
    elif who_starts == 2:
        who_starts = 1
    if sticks < maximum_pickable_sticks:
        maximum_pickable_sticks = sticks 
    if who_starts == 1:
        print(f"You may pick up between 1 and {maximum_pickable_sticks} sticks")
        pick = int(input("How many sticks do you want to pick up?\n"))
        
        #validating the picks
        
        while pick > maximum_pickable_sticks or pick > sticks:
            print("invalid number of sticks picked")
            pick = int(input("you must pick again\n"))
        sticks = sticks - pick
        for i in range(sticks):
            print('|', end = ' ')
        if sticks != 0:
            print(f"\t{sticks} sticks remaining")
    else:
        if maximum_pickable_sticks >= sticks:
            pick = sticks
        else:
            #using random module to find a random number for computer

            pick = random.randrange(1, maximum_pickable_sticks + 1)
        sticks = sticks - pick
        for i in range(sticks):
            print('|', end = ' ')
        if sticks != 0:
            print(f"\t{sticks} sticks remaining")
if who_starts == 1:
    print("Human player won.")
else:
    print('Computer Won')
