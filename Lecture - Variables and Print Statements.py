#Name: Coach Mack
#Class: 6th Hour
#Assignment: Lecture - Varibles and Print Statements


#These are variables. They are simply a thing we can assign a value to.
#These variables can be anything and can have any value from numbers to words
#(known as strings in programming) to booleans (true/false values).

#Get ingredients
bread = 2
peanutButter = 1
jelly = float(0.5)

#Utensils and Plates
knife = 2
jars = 2
plate = 1

#These are print statements. This is how we print out anything
#we want so that the user can see what we want when we want
#without them needing to peek into the code.

#Prep work
print("Step 1: Put the plate on the table.")
print("Step 2: Open the jars of Peanut Butter and Jelly.")
print("Step 3: Take the bread out and put on the plate.")

#Make the PB and J
print("Use the knife to spread the peanut butter on one piece of bread.")
print("Use the knife to spread the jelly on the other piece of bread.")
print("Put the two pieces of bread together.")

#Plate the food
print("Then set it on the plate.")
ingredientTotal = bread + peanutButter + jelly

#To print multiple things, you can place a comma between them to
#print them all in the same line. Just remember that printing a string
#(something within "") will print what you type out exactly. To print
#a variable, just type the name of the variable without quotation marks.
print("The total of the ingredients is: ", ingredientTotal)