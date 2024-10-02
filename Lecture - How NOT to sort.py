#Name: Coach Mack
#Class: 6th Hour
#Assignment: Lecture - How NOT to sort


#So this is the result of a story. Back in college, I was in a mobile applications
#class. In this class, I was given a personal project to work on. This project was
#of your own choosing so I, as a big Dungeons & Dragons fan, made a D&D project I
#called the "Book of Kaati". It was meant to be a repository and character creation
#tool that existed long before VTTs or D&D Beyond was ever really a thing.
#HOWEVER, I sucked at coding then. This is my attempt to recreate the code to use
#as a cautionary tale of what NOT to do when it comes to more complex problems.
#You can't solve every problem with a million print statements.

import random

roll1 = random.randint(1,6)
roll2 = random.randint(1,6)
roll3 = random.randint(1,6)
roll4 = random.randint(1,6)
resultroll1 = 0

print(f"{roll1}, {roll2}, {roll3}, {roll4}")

if roll1 >= roll2 and roll3 >= roll4:
    resultroll1 = roll1 + roll3
    if roll2 >= roll4:
        resultroll1 = resultroll1 + roll2
        print(resultroll1)
    elif roll4 > roll2:
        resultroll1 = resultroll1 + roll4
        print(resultroll1)
elif roll1 < roll2 and roll3 >= roll4:
    resultroll1 = roll2 + roll3
    if roll1 >= roll4:
        resultroll1 = resultroll1 + roll1
        print(resultroll1)
    elif roll4 > roll1:
        resultroll1 = resultroll1 + roll4
        print(resultroll1)
elif roll1 >= roll2 and roll3 < roll4:
    resultroll1 = roll1 + roll4
    if roll2 >= roll3:
        resultroll1 = resultroll1 + roll2
        print(resultroll1)
    elif roll3 > roll2:
        resultroll1 = resultroll1 + roll3
        print(resultroll1)
elif roll1 < roll2 and roll3 < roll4:
    resultroll1 = roll2 + roll4
    if roll1 >= roll3:
        resultroll1 = resultroll1 + roll1
        print(resultroll1)
    elif roll3 > roll1:
        resultroll1 = resultroll1 + roll3
        print(resultroll1)



#Here's what you're SUPPOSED to do in this context.

stat1 = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]

print(stat1)
stat1.sort(reverse=True)
print(stat1[0]+stat1[1]+stat1[2])
