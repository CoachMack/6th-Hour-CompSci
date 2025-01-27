#Name: Coach Mack
#Class: 6th Hour
#Assignment: Lecture - Monty Hall Problem
import random

def monty_hall_problem():
    prizes = ["goat", "goat", "car"]
    random.shuffle(prizes)
    userDoor = int(input("Do you want to open Door #1, Door #2, or Door #3? "))
    if userDoor == 1:
        if prizes[1] == "goat":
            print("Door #2 is a goat! Do you want to switch to Door #3 or stay with Door #1?")
            userSwitch = int(input("Press 3 to switch or 1 to stay "))
            if userSwitch == 1:
                print(f"You got a {prizes[0]}")
            else:
                print(f"You got a {prizes[2]}")
        else:
            print("Door #3 is a goat! Do you want to switch to Door #2 or stay with Door #1?")
            userSwitch = int(input("Press 2 to switch or 1 to stay "))
            if userSwitch == 1:
                print(f"You got a {prizes[0]}")
            else:
                print(f"You got a {prizes[1]}")
    elif userDoor == 2:
        if prizes[0] == "goat":
            print("Door #1 is a goat! Do you want to switch to Door #3 or stay with Door #2?")
            userSwitch = int(input("Press 3 to switch or 2 to stay "))
            if userSwitch == 2:
                print(f"You got a {prizes[1]}")
            else:
                print(f"You got a {prizes[2]}")
        else:
            print("Door #3 is a goat! Do you want to switch to Door #1 or stay with Door #2?")
            userSwitch = int(input("Press 1 to switch or 2 to stay "))
            if userSwitch == 2:
                print(f"You got a {prizes[1]}")
            else:
                print(f"You got a {prizes[0]}")
    elif userDoor == 3:
        if prizes[0] == "goat":
            print("Door #1 is a goat! Do you want to switch to Door #2 or stay with Door #3?")
            userSwitch = int(input("Press 2 to switch or 3 to stay "))
            if userSwitch == 3:
                print(f"You got a {prizes[2]}")
            else:
                print(f"You got a {prizes[1]}")
        else:
            print("Door #3 is a goat! Do you want to switch to Door #1 or stay with Door #2?")
            userSwitch = int(input("Press 1 to switch or 3 to stay "))
            if userSwitch == 3:
                print(f"You got a {prizes[2]}")
            else:
                print(f"You got a {prizes[0]}")

monty_hall_problem()