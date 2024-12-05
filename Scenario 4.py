#Name:
#Class: 6th Hour
#Assignment: Scenario 4

#Scenario 4:
#Due to scope creep leading to high development costs, the RPG you were working on has been
#shelved for the time being. You have been transferred to a new team working on a mobile game
#that allows you to dress up a model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.

#Objectives:
#1. Make an input that asks for number of players.
#2. Have each player input a ranking from 1-5.
#3. Find the average of the player rankings and print it.

#Pseudocode:
#Step 1. Establish Variables
players = int(input("Enter number of players: "))
i = 1
ratingSum = 0

if players < 2:
    print("Error, not enough players")
    exit()

#Step 2. Make a loop
while i <= players:
#Step 2a. Ask for a rating number
    rating = int(input("Enter rating from 1 to 5: "))
    #Step 2b. Check if rating number is between 1 and 5
    if rating > 5 or rating < 1:
        print("Error, invalid rating")
    #Step 2c. If rating number is valid, add to total
    else:
        i += 1
        ratingSum += rating

#Step 3. Find and print the average
print("The Average Rating is: ", ratingSum / players)