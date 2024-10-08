#Name:
#Class: 6th Hour
#Assignment: HW7

#1. Print Hello World!
print("Hello World!")
#2. Create three different boolean variables named wifi, login, and admin.
watermelon = True
lewis = True
GTAVI = True
#3. Create a separate integer variable that denotes the number of times
#someone with admin credentials has logged in.
jeffery = 7
#4. Create a nested if statement that checks to see if wifi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one they are "missing".

if watermelon == True: #Create an if statement that checks to see if watermelon is true
    if lewis == True: #Create an if statment that checks to see if lewis is true
        if GTAVI == True: #Create an if statement that checks to see if GTAVI is released
            print("Welcome Rockstar!") #Create Welcome message
            jeffery += 1 #Increase jeffery by one
            print(jeffery) #Print jeffery
        else: #Error message for GTA6
            print("GTA VI is not released yet!")
    else: #Error message for Lewis
        print("Lewis got benched!")
else: #Error message for Watermelon
    print("No watermelon in the bowl.")
