#Name: Coach Mack
#Class: 5th Hour
#Assignment: Lecture - While Loops

#This is the "time" library. This is to do cool stuff with time like delays.
#It's not important for the lecture but I used it to show the loops in action.
import time

#This is a while loop. Basically, this is a conditional statement that says
#"while something is true, repeat the code indented below it". This is useful
#for situations like counting that might take a long time to do manually.
i = 0
while i <= 1000:
    print(i)
    time.sleep(0.4)
    i += 1

#Using increments, you can count down as well.
j = 10
while j >= 0:
    print(j)
    time.sleep(1)
    j -= 1
#You can tie an else statement to a loop. Once the loop finishes, it will
#do whatever the else statement says.
else:
    print("Happy Halloween!")

#You can also nest if statements inside of while loops. It'll check to see if
#that condition is met and do it.
k = 1
while k < 6:
    print(k)
    if k == 3:
        #This is the break function. It will end a loop prematurely
        #if the condition is met.
        break
    k += 1
#NOTE: Breaks will end the loop entirely INCLUDING else statements below.
else:
    print("Hello!")

#This function uses a continue function. Continue makes the loop repeat,
#ignoring anything else below it. In this case, it counts from 1 to 6, but
#prints the word "Three" instead of the number 3.
l = 0
while l < 6:
    l += 1
    if l == 3:
        print("Three")
        continue
    print(l)

