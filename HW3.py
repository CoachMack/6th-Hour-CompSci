#Name: Coach Mack
#Class: 6th Hour
#Assignment: HW3
#Code Used:


#Objectives:

#Print Hello World!
print("Hello World!")

#Create a list with 5 strings containing 5 different names in it
nameList = ["Logan", "AJ", "Bryan", "Kevin", "Evan"]
print(nameList)
#Append a new name onto the Name List
nameList.append("Steve")
#Print out the 4th name on the list
print(nameList[3])
print(nameList[5])

#Create a list with 4 different integers in it
numList = [7, 9, 23, 4]
#Insert a new integer into the 2nd spot
numList.insert(1,6)
#Print the Integer List
print(numList)
#Sort the list from lowest to highest
numList.sort()
print(numList)
#Add the 1st three numbers on the sorted list together
sum = numList[0] + numList[1] + numList[2]
#Print the sum
print(sum)