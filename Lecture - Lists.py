#Name: Coach Mack
#Class: 6th Hour
#Assignment: Lecture - Lists


#This is a list. In essence, it's a variable that has multiple values inside that
#you can pull from any of them without needing to make multiple variables for each
#piece of data. This is useful for cases where you have a lot of the same type of
#"thing", such as names in this example.
santasList = ["CJ", "Evan", "Elijah", "Seeley", "AJ", "Jax", "Logan", "Kyle",
              "The Other Logan", "Ryan", "Colin"]

#This is the append function. This allows you to tack on a new value or "object"
#to the end of the list.
#This one specifically has an input() function so you can add your own name.
santasList.append(input())
#This is the remove function. It removes any instance of the value.
santasList.remove("AJ")
#This is the insert function. It works like the append function but you can
#place the object anywhere inside of the list, not just at the end.
santasList.insert(4, "Joe")

#To print the list. You simply name the variable followed by [] with the
#number inside being its "index" location.
#Note that all indexes START AT ZERO. Not one. :)
print(f"{santasList[0]} is NAUGHTY!")
print(f"{santasList[2]} is NAUGHTY!")
print(f"{santasList[4]} is NAUGHTY!")
print(f"{santasList[7]} is NAUGHTY!")
print(f"{santasList[10]} is NAUGHTY!")

#This is a number list. You can place any kind of object in a list,
#not just strings.
numList = [3, 5, 1, 3]
print(numList)

#You can sort the list from lowest to highest. When you sort a list,
#it permanently changes the order of the list so keep that in mind.
numList.sort()
print(numList)
#You can also sort the list from highest to lowest using the
#reverse=True modifier.
numList.sort(reverse=True)
print(numList)
#You can do math with the numbers in a list. Simply call their index location.
#Reminder: START AT ZERO.
sum = numList[0] + numList[1] + numList[2]
print(sum)

#You can also list different types of objects in the same list.
mixList = ["Joe", True, 7]
#You can also put an input() function inside of an index location call
#to print out whichever part of the list you want.
print(mixList[int(input())])
