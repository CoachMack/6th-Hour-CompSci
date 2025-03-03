#Name: Coach Mack
#Class: 5th Hour
#Assignment: Mack's Playground

import random

#TODO: Test every option for bugs and document bugs in each game
#TODO: Adjust payouts to be correct

#A roulette wheel layout consisting of a 0, double 0, and 1 through 36

rouletteWheel = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,
            15,16,17,18,19,20,21,22,23,24,25,26,
            27,28,29,30,31,32,33,34,35,36]

greenNums = [0]

blackNums = [2,4,6,8,10,11,13,15,17,20,22,24,26,
             28,29,31,33,35]

redNums = [1,3,5,7,9,12,14,16,18,19,21,23,27,25,
           30,32,34,36]

street1 = [1,2,3]
street4 = [4,5,6]
street7 = [7,8,9]
street10 = [10,11,12]
street13 = [13,14,15]
street16 = [16,17,18]
street19 = [19,20,21]
street22 = [22,23,24]
street25 = [25,26,27]
street28 = [28,29,30]
street31 = [31,32,33]
street34 = [34,35,36]

basket1 = [0,1,2]
basket2 = [0,2,3]

#Potential winning options for outside groupings
manqueLow = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
passeHigh = [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
firstDozen = [1,2,3,4,5,6,7,8,9,10,11,12]
secondDozen = [13,14,15,16,17,18,19,20,21,22,23,24]
thirdDozen = [25,26,27,28,29,30,31,32,33,34,35,36]
firstColumn = [1,4,7,10,13,16,19,22,25,28,31,34]
secondColumn = [2,5,8,11,14,17,20,23,26,29,32,35]
thirdColumn = [3,6,9,12,15,18,21,24,27,30,33,36]
snake = [1,5,9,12,14,16,19,23,27,30,32,34]

#The results to be used as a global
spinResult = 0
spinResultColor = ""

#Wager variable so the user can bet.
playerPot = 100
wagerAmount = 0

print("Welcome to the roulette table! We are about to begin!")
print("Place your bets!")

def wager_call():
    global playerPot, wagerAmount
    print(f"Your current winnings are: {playerPot}")
    try:
        wagerAmount = int(input("How much do you want to bet?"))
        playerPot -= wagerAmount
        in_or_out()
    except ValueError:
        print("Not a valid wager amount. Please try again.")
        wager_call()

def in_or_out():
    inBetNames = ["Single", "Street", "Basket", "First Four"]
    outBetNames = ["Low/High", "Red/Black", "Even/Odd", "Dozen", "Column", "Snake"]
    try:
        userInOrOut = int(input("Do you bet Inside (1) or Outside (2)?"))
        if userInOrOut == 1:
            userInChoice = int(input("Do you want to bet on (Split, Double Street, Corner not implented):\n"
                                     "1. Single\n"
                                     "2. Street\n"
                                     "3. Basket\n"
                                     "4. First Four\n"))
            print(f"You chose: {inBetNames[userInChoice-1]}")
            if userInChoice == 1:
                single_play()
            elif userInChoice == 2:
                street_play()
            elif userInChoice == 3:
                basket_play()
            elif userInChoice == 4:
                first_four_play()
        elif userInOrOut == 2:
            userOutChoice = int(input("Do you want to bet on:\n"
                                     "1. Low/High\n"
                                     "2. Red/Black\n"
                                     "3. Even/Odd\n"
                                     "4. Dozen\n"
                                     "5. Column\n"
                                     "6. Snake\n"))
            print(f"You chose: {outBetNames[userOutChoice-1]}")
            if userOutChoice == 1:
                low_high_play()
            elif userOutChoice == 2:
                red_black_play()
            elif userOutChoice == 3:
                even_odd_play()
            elif userOutChoice == 4:
                dozen_play()
            elif userOutChoice == 5:
                column_play()
            elif userOutChoice == 6:
                snake_play()
    except ValueError:
        print("Not a valid response. Please try again.")
        in_or_out()

def repeat_game():
    userRepeat = input("Would you like to play again? Y/N")
    if userRepeat == "Y" or userRepeat == "y":
        wager_call()
    elif userRepeat == "N" or userRepeat == "n":
        exit()
    else:
        print("Invalid input.")
        repeat_game()

def roulette_spin():
    global spinResult, spinResultColor
    spinResult = random.choice(rouletteWheel)
    if spinResult in greenNums:
        spinResultColor = "Green"
        print(f"{spinResult} {spinResultColor}")
    elif spinResult in blackNums:
        spinResultColor = "Black"
        print(f"{spinResult} {spinResultColor}")
    elif spinResult in redNums:
        spinResultColor = "Red"
        print(f"{spinResult} {spinResultColor}")


def single_play():
    global playerPot, wagerAmount
    try:
        userPick = int(input("Pick your number to bet on (0-36)!"))
        roulette_spin()
        if userPick > 36 or userPick < 0:
            print("Not a valid number. Please try again.")
            single_play()
        else:
            if userPick == spinResult:
                print("You win!")
                wagerAmount *= 35
                playerPot += wagerAmount
            else:
                print("You lose!")
    except ValueError:
        print("Not a valid number. Please try again.")
        single_play()
    repeat_game()

def street_play():
    global playerPot, wagerAmount
    try:
        userPick = int(input("Pick your street to bet on (ex: entering 1 is 1,2,3)!"))
        roulette_spin()
        if userPick > 36 or userPick < 0:
            print("Not a valid number. Please try again.")
            street_play()
        else:
            if userPick in street1 and spinResult in street1:
                print("You win!")
                wagerAmount *= 11
                playerPot += wagerAmount
            elif userPick in street4 and spinResult in street4:
                print("You win!")
                wagerAmount *= 11
                playerPot += wagerAmount
            elif userPick in street7 and spinResult in street7:
                print("You win!")
                wagerAmount *= 11
                playerPot += wagerAmount
            elif userPick in street10 and spinResult in street10:
                print("You win!")
                wagerAmount *= 11
                playerPot += wagerAmount
            elif userPick in street13 and spinResult in street13:
                print("You win!")
                wagerAmount *= 11
                playerPot += wagerAmount
            elif userPick in street16 and spinResult in street16:
                print("You win!")
                wagerAmount *= 11
                playerPot += wagerAmount
            elif userPick in street19 and spinResult in street19:
                print("You win!")
                wagerAmount *= 11
                playerPot += wagerAmount
            elif userPick in street22 and spinResult in street22:
                print("You win!")
                wagerAmount *= 11
                playerPot += wagerAmount
            elif userPick in street25 and spinResult in street25:
                print("You win!")
                wagerAmount *= 11
                playerPot += wagerAmount
            elif userPick in street28 and spinResult in street28:
                print("You win!")
                wagerAmount *= 11
                playerPot += wagerAmount
            elif userPick in street31 and spinResult in street31:
                print("You win!")
                wagerAmount *= 11
                playerPot += wagerAmount
            elif userPick in street34 and spinResult in street34:
                print("You win!")
                wagerAmount *= 11
                playerPot += wagerAmount
            else:
                print("You lose!")
    except ValueError:
        print("Not a valid number. Please try again.")
        basket_play()
    repeat_game()

def basket_play():
    global playerPot, wagerAmount
    try:
        userPick = int(input("Pick 1 for 0-1-2 or 2 for 0-2-3!"))
        if userPick != 1 or userPick != 2:
            roulette_spin()
            if userPick == 1:
                if spinResult == 0 or spinResult == 1 or spinResult == 2:
                    print("You win!")
                    wagerAmount *= 11
                    playerPot += wagerAmount
                else:
                    print("You lose!")
            elif userPick == 2:
                if spinResult == 0 or spinResult == 2 or spinResult == 3:
                    print("You win!")
                    wagerAmount *= 11
                    playerPot += wagerAmount
                else:
                    print("You lose!")
        else:
            print("Not a valid number. Please try again.")
            basket_play()
    except ValueError:
        print("Not a valid number. Please try again.")
        basket_play()
    repeat_game()

def first_four_play():
    global playerPot, wagerAmount
    print("Good Luck!")
    roulette_spin()
    if spinResult == 0 or spinResult == 1 or spinResult == 2 or spinResult == 3:
        print("You win!")
        wagerAmount *= 8
        playerPot += wagerAmount
    else:
        print("You lose!")
    repeat_game()

def low_high_play():
    global playerPot, wagerAmount
    try:
        userPick = int(input("Pick 1 for Low or 2 for High!"))
        if userPick == 1 or userPick == 2:
            roulette_spin()
            if userPick == 1:
                if spinResult in manqueLow:
                    print("You win!")
                    wagerAmount *= 2
                    playerPot += wagerAmount
                else:
                    print("You lose!")
            elif userPick == 2:
                if spinResult in passeHigh:
                    print("You win!")
                    wagerAmount *= 2
                    playerPot += wagerAmount
                else:
                    print("You lose!")
        else:
            print("Not a valid number. Please try again.")
            low_high_play()
    except ValueError:
        print("Not a valid number. Please try again.")
        low_high_play()
    repeat_game()

def red_black_play():
    global playerPot, wagerAmount
    try:
        userPick = int(input("Pick 1 for Red or 2 for Black!"))
        if userPick == 1 or userPick == 2:
            roulette_spin()
            if userPick == 1:
                if spinResult in redNums:
                    print("You win!")
                    wagerAmount *= 2
                    playerPot += wagerAmount
                else:
                    print("You lose!")
            elif userPick == 2:
                if spinResult in blackNums:
                    print("You win!")
                    wagerAmount *= 2
                    playerPot += wagerAmount
                else:
                    print("You lose!")
        else:
            print("Not a valid number. Please try again.")
            red_black_play()
    except ValueError:
        print("Not a valid number. Please try again.")
        red_black_play()
    repeat_game()

def even_odd_play():
    global playerPot, wagerAmount
    try:
        userPick = int(input("Pick 1 for Even or 2 for Odd!"))
        if userPick != 1 or userPick != 2:
            roulette_spin()
            if userPick == 1:
                if spinResult % 2 == 0:
                    print("You win!")
                    wagerAmount *= 2
                    playerPot += wagerAmount
                else:
                    print("You lose!")
            elif userPick == 2:
                if spinResult % 2:
                    print("You win!")
                    wagerAmount *= 2
                    playerPot += wagerAmount
                else:
                    print("You lose!")
        else:
            print("Not a valid number. Please try again.")
            even_odd_play()
    except ValueError:
        print("Not a valid number. Please try again.")
        even_odd_play()
    repeat_game()

def dozen_play():
    global wagerAmount, playerPot
    try:
        userPick = int(input("Pick 1 for First Dozen (1-12),\n"
                             "2 for Second Dozen (13-24),\n"
                             "3 for Third Dozen (35-36)"))

        if userPick == 1 or userPick == 2 or userPick == 3:
            roulette_spin()
            if userPick == 1 and spinResult in firstDozen:
                print("You win!")
                wagerAmount *= 2
                playerPot += wagerAmount
            elif userPick == 2 and spinResult in secondDozen:
                print("You win!")
                wagerAmount *= 2
                playerPot += wagerAmount
            elif userPick == 3 and spinResult in thirdDozen:
                print("You win!")
                wagerAmount *= 2
                playerPot += wagerAmount
            else:
                print("You lose!")
        else:
            print("Not a valid number. Please try again.")
            dozen_play()
    except ValueError:
        print("Not a valid number. Please try again.")
        dozen_play()
    repeat_game()

def column_play():
    global wagerAmount, playerPot
    try:
        userPick = int(input("Pick 1 for First Column (1,4,7...),\n"
                             "2 for Second Column (2,5,8...),\n"
                             "3 for Third Column (3,6,9...)"))
        if userPick == 1 or userPick == 2 or userPick == 3:
            roulette_spin()
            if userPick == 1 and spinResult in firstColumn:
                print("You win!")
                wagerAmount *= 4
                playerPot += wagerAmount
            elif userPick == 2 and spinResult in secondColumn:
                print("You win!")
                wagerAmount *= 4
                playerPot += wagerAmount
            elif userPick == 3 and spinResult in thirdColumn:
                print("You win!")
                wagerAmount *= 4
                playerPot += wagerAmount
            else:
                print("You lose!")
        else:
            print("Not a valid number. Please try again.")
            dozen_play()
    except ValueError:
        print("Not a valid number. Please try again.")
        dozen_play()
    repeat_game()

def snake_play():
    global playerPot, wagerAmount
    print("Good Luck!")
    roulette_spin()
    if spinResult in snake:
        print("You win!")
        wagerAmount *= 2
        playerPot += wagerAmount
    else:
        print("You lose!")
    repeat_game()

wager_call()