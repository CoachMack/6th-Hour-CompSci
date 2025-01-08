#Name: Coach Mack
#Class: 6th Hour
#Assignment: Lecture - Refresher

import random

x = random.randint(1,5)
y = random.randint(1,100)
z = 0
numList = [7, 5, 400, 3]

if x == 1:
    print("X is 1")
elif x == 2:
    print("X is 2")
elif x == 3:
    print("X is 3")
elif x == 4:
    print("X is 4")
else:
    print("X is 5")


print(y)
if y < 80 and y > 20:
    print("These are the middleground grades.")
elif y <= 20:
    print("These are the low grades.")
elif y >= 80:
    print("These are the high grades.")

while z < 5:
    z += 1
    print(z)

for i in range(1,6):
    print(i)

for j in numList:
    print(j)

lower = 2
upper = 1000
for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
