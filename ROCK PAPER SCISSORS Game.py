# INF 120 - Fall 2022
# Project 9
# Rock, Papers, Scissors, Lizard, Spock
# PALDEN TAMANG
# 1st November,2022

#importing random module
import random

#creating a menu for the game
print()
print("Let\'s play rock, paper, scissors, Lizard and Spock!\n")
print("Make your selection from list below.\n\n")
print("R-Rock\n\n""P-Paper\n\n""S-Scissors\n\n""L-Lizard\n\n""V-Spock\n\n")


#preparing the game with choices for user and using random module to make choice for the computer

selection = {'R': 'Rock','P' : 'Paper','S' : 'Scissors','L' : 'Lizard','V' : 'Spock'}
choices = {0 : 'R', 1 : 'P' , 2: 'S', 3 : 'L', 4 : 'V'}
list = ['R', 'P', 'S', 'L', 'V']
random_number = random.randrange(0,5)


#asking for input from user and the computer

computer_selection = choices[random.randrange(0, 5)]
user_selection = input("Enter a selection: ").upper()
while user_selection not in list:
    print('Invalid selection')
    user_selection = input("Enter a valid selection: ").upper()
#counting the user and computer win
user_won = 0
computer_won = 0
condition = True

#checking for invalid selection
while condition == True:

    if user_selection not in list:
        print('You made an invalid selection.')


    # setting the game rules using if condition

    else:
        if user_selection == 'R' and computer_selection == 'R':
            outcome = 'Tie!'
        
        elif user_selection == 'R' and computer_selection == 'P':
            outcome = 'You lost!'
            computer_won += 1
        
        elif user_selection == 'R' and computer_selection == 'S':
            outcome = 'You won!'
            user_won += 1
        
        elif user_selection == 'R' and computer_selection == 'L':
            outcome = 'You won!'
            user_won += 1
        
        elif user_selection == 'R' and computer_selection == 'V':
            outcome = 'You lost!'
            computer_won += 1
        
        elif user_selection == 'P' and computer_selection == 'R':
            outcome = 'You won!'
            user_won += 1
        
        elif user_selection == 'P' and computer_selection == 'P':
            outcome = 'Tie!'
        
        elif user_selection == 'P' and computer_selection == 'S':
            outcome = 'You lost!'
            computer_won += 1
        
        elif user_selection == 'P' and computer_selection == 'L':
            outcome = 'You lost!'
            computer_won += 1
        
        elif user_selection == 'P' and computer_selection == 'V':
            outcome = 'You won!'
            user_won += 1
        
        elif user_selection == 'S' and computer_selection == 'R':
            outcome = 'You lost!'
            computer_won += 1
        
        elif user_selection == 'S' and computer_selection == 'P':
            outcome = 'You won!'
            user_won += 1
        
        elif user_selection == 'S' and computer_selection == 'S':
            outcome = 'Tie!'
        
        elif user_selection == 'S' and computer_selection == 'L':
            outcome = 'You won!'
            user_won += 1
        
        elif user_selection == 'S' and computer_selection == 'V':
            outcome = 'You lost!'
            computer_won += 1
        
        elif user_selection == 'L' and computer_selection == 'R':
            outcome = 'You lost!'
            computer_won += 1
        
        elif user_selection == 'L' and computer_selection == 'P':
            outcome = 'You won!'
            user_won += 1
        
        elif user_selection == 'L' and computer_selection == 'S':
            outcome = 'You lost!'
            computer_won += 1
        
        elif user_selection == 'L' and computer_selection == 'L':
            outcome = 'Tie!'
        
        elif user_selection == 'L' and computer_selection == 'V':
            outcome = 'You won!'
            user_won += 1
        
        elif user_selection == 'V' and computer_selection == 'R':
            outcome = 'You won!'
            user_won += 1
        
        elif user_selection == 'V' and computer_selection == 'P':
            outcome = 'You lost!'
            computer_won += 1
        
        elif user_selection == 'V' and computer_selection == 'S':
            outcome = 'You won!'
            user_won += 1
        
        elif user_selection == 'V' and computer_selection == 'L':
            outcome = 'You lost!'
            computer_won += 1
        
        elif user_selection == 'V' and computer_selection == 'V':
            outcome = 'Tie!'
        
        else:
            outcome = 'You made an invalid selection!'



        #printing the outcomes
        
        print(f'You selected {selection[user_selection]} and I selected {selection[computer_selection]}.')
        print(outcome)

        #Asking the user if they want to play again or not
        play_again = input("Do you want to play again? (y for yes and n for no)").upper()
        if play_again == 'Y':
            user_selection = input("Enter a selection: ").upper()
            computer_selection = choices[random.randrange(0, 5)]      
        elif play_again == 'N':
            condition = False
        else:
            print('Invalid selection, so the game force shut down.')
            condition = False
            
#printing the message according to the number of rounds won by either user or computer
if user_won > computer_won:
    print(f'Congratulations!! You won {user_won} times whereas Computer won just {computer_won} times.  :D')
elif computer_won > user_won:
    print(f'Unfortunately, Computer won {computer_won} times and you only won {user_won} times.  :(')
else:
    print(f'It is a draw. You won {user_won} times which is the same as computer.')
    


