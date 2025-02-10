#Name: Coach Mack
#Class: 6th Hour
#Assigment: Scenario 6
import random

#After an extended leave, the team lead for the RPG developer is back, and he wants to continue the project.
#He wants to prototype the character creation model but first needs something that rolls stats for the characters.
#He wants you to make a function that rolls 4 six-sided dice (d6), sorts them from highest to lowest, and then adds the
#highest 3 together. He then wants you to add that result to a list outside the function. He wants you to run that function
#5 more times (six times total) and print all six stats.

statblock = []

def dice_roll():
    for i in range(6):
        roll = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
        roll.sort(reverse=True)
        stat = roll[0] + roll[1] + roll[2]
        statblock.append(stat)

#Once that is done, to ensure that the average of the statblock is fair (somewhere roughly between 12-13), he wants you
#to plug it into a calculator (Scenario 7) and print the average.
dice_roll()
print(statblock)