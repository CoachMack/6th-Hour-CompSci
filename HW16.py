#Name: Coach Mack
#Class: 6th Hour
#Assignment: HW16
import random

#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".

def lazy_rps():
    playerHand = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors. "))
    enemyHand = random.randint(1,3)

    if playerHand == 1 and enemyHand == 3:
        print("You Win!")
    elif playerHand == 1 and enemyHand == 2:
        print("You lose!")
    elif playerHand == 2 and enemyHand == 1:
        print("You Win!")
    elif playerHand == 2 and enemyHand == 3:
        print("You lose!")
    elif playerHand == 3 and enemyHand == 2:
        print("You Win!")
    elif playerHand == 3 and enemyHand == 1:
        print("You lose!")
    elif playerHand == enemyHand:
        print("Tie!")

    repeat_game()

def cool_rps():
    playerHand = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors. "))
    enemyHand = random.randint(1, 3)

    if playerHand == enemyHand:
        print("Tie!")
    elif (playerHand == 1 and enemyHand == 3) or (playerHand == 2 and enemyHand == 1) or (playerHand == 3 and enemyHand == 2):
        print("You win!")
    else:
        print("You lose!")

    repeat_game()
#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.

def repeat_game():
    userInput = input("Would you like to play again? Y/N ")
    if userInput == "Y" or userInput == "y":
        cool_rps()
    elif userInput == "N" or userInput == "n":
        exit()
    else:
        print("Invalid input")
        repeat_game()

cool_rps()
