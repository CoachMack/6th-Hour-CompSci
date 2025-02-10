#Name: Coach Mack
#Class: 6th Hour
#Assignment: HW18
import random

#1. Import the "random" library and create a def function that prints "Hello World!"
def hello_world():
    print("Hello World!")
#2. Create a list called beanBag and add at least 5 different colored beans to the list as strings.
beanBag = ["blue", "red", "green", "yellow", "black"]
#3. Create a def function that pulls a random bean out of the beanBag list, prints which bean you pulled, and then removes it from the list.
def bean_pull():
    if not beanBag:
        print("Bean Bag is empty!")
        exit()
    else:
        hand = random.choice(beanBag)
        print(hand)
        beanBag.remove(hand)
        repeat_bean()
#4. Create a def function that asks if you want to pull another bean out of the bag and, if yes, repeats the #3 def function
def repeat_bean():
    userInput = input("Would you like to pull another? Y/N ")
    if userInput == "Y" or userInput == "y":
        bean_pull()
    elif userInput == "N" or userInput == "n":
        exit()
    else:
        print("Invalid input")
        repeat_bean()
#5. Call the #3 function at the bottom.
hello_world()
bean_pull()