#Name: Coach Mack
#Class: 5th Hour
#Assignment: HW11

#A common exercise in computer science is "FizzBuzz". The rules of
#the game are simple. Count from 1 to 100 but with every number that
#is divisible by 3 you say "Fizz" instead of the number,
#every number divisible by 5 you say "Buzz" instead,
#and if it's divisible by both you say "FizzBuzz".

#Create a while loop that follows the rules of the game.
#(HINT: Look back to HW6 on how to see if a number is divisible by another)

#THIS IS THE BAD METHOD

i = 1
while i <= 100:
    if i % 3 == 0 and not i % 5 == 0:
        print("Fizz")
    if i % 5 == 0 and not i % 3 == 0:
        print("Buzz")
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    if not i % 3 == 0 and not i % 5 == 0:
        print(i)
    i += 1

#This is the good method

i = 1

while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i += 1


#This is the "true ending" method
i = 1

while i <= 1000:
    output = ""
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    if i % 7 == 0:
        output += "Fazz"
    if output == "":
        output = i
    print(output)
    i += 1