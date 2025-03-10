#Name: Coach Mack
#Class: 6th Hour
#Assignment: Scenario 7

#Import all of Scenario 6 here
from Scenario6 import *

listAverage = 0

def final_average():
    global listAverage
    listAverage = sum(statblock)/len(statblock)#Calculate the sum of the list by the length of the list here
    return listAverage

final_average()

print(listAverage)