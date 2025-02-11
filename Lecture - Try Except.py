#Name: Coach Mack
#Class: 6th Hour
#Assignment: Lecture - Try Except
from xmlrpc.client import Boolean

#This is a Try Except catch. It initially tries to do one piece of code and in the case of an error,
#it does whatever code set under the except. This allows for the code to continue on when there is an
#error which can help with debugging.
try:
    print(x)
except:
    print("Hello World!")

#You can define which exceptions to check for. In this example, this is a divide by zero error so
#it prints the second except because the first except is looking for a name error.
try:
    print(100/0)
except NameError:
    print("X is not defined!")
except:
    print("Something else went wrong!")

#There is also finally which does whatever code is under it regardless of if an exception is caught
#or not. Think of it like an else statement but it just does that part of the code no matter what.
try:
    print(y)
except:
    print("Something went wrong")
finally:
    print("Try Except is over")

#You can also raise exceptions that will throw a big red error and end the code anyway but you can
#customize what the error says to help with debugging.
i = -1

if i < 0:
    raise Exception("Sorry, no numbers below zero.")

#This is an example of checking if the type of a variable is what you are looking for or not.
k = "Lemon"

if not type(k) is str:
    raise Exception("Boolean only.")
else:
    print(k)
