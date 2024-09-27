#Name: Coach Mack
#Class: 5th Hour
#Assignment: Conditional Statements

a = 2
b = 2
c = 10
d = 9
e = 6
f = 19
g = 5


#This section is a conditional statment (AKA an "if then" or "if else" statement).
#These are used for giving your code specific directions based on whatever rules you
#set for it. There are three different types of conditional statements.

#if = Check to see if this condition is valid.
#elif = Short for "else if". Check to see if this condition is valid if the first isn't.
#else = If no other condition is valid, do this.

#Often you have conditional statements being compared using logical conditions from mathematics.

#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b

if a > b:
    #YOU MUST INDENT EVERYTHING YOU WANT TO DO WITHIN AN IF STATEMENT
    print("A is greater than B.")
elif a < b:
    #INDENT
    print("A is less than B.")
else:
    #INDENT
    print("A is equal to B.")


#Additonally, you can have one or more conditions on the same line using "and" and "or".

#or = One statement must be true, even if the other is false (both can also be true).
#and = Both conditions must be true.

if d > c or d > e:
    print("D is NOT the smallest number.")

if e < d and e < c:
    print("E is the smallest number.")
else:
    print("Hello World!")



#Often this is where modifier conditions are made. By adding g to f, the new value
#for f becomes G + F. In this case, 24. This is a permanent change that will affect
#later code until it is changed back.

if f < g:
    f = f + g
    print(f)
elif f >= g:
    f = f - g
    print(f)
print(f)

#This is a nested conditional statement. You can nest them inside of each other
#to create more complex pathways and conditions if you need to be more precise.
if f >= 10:
    if f >= 20:
        print("F is greater than 20!")
    else:
        print("F is greater than 10 but less than 20!")
elif f < 10:
    if f >= 5:
        print("F is greater than 5 but less than 10!")
    else:
        print("F is less than 5")