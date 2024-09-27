#DON'T FORGET TO ADD YOUR NAME, CLASS, AND ASSIGNMENT
#Name: Coach Mack
#Class: 6th Hour
#Assignment: Lecture - Playground Common Mistakes

#print hello world!
print("Hello World!")

#if you forget to add int() to an input, it will treat your number
#like a word instead
a = input("Enter number here: ")
b = input("Enter another number here: ")
print(a+b)

#this is how it should be done
x = int(input("Enter number here: "))
y = int(input("Enter another number here: "))
print(x+y)

#putting numbers in lists in quotation marks does the same thing,
#only put quotations for words
numList = ["1","2","3","4","5"]
numList2 = [1,2,3,4,5]

print(numList[0] + numList[1])
print(numList2[0] + numList2[1])

#You can also add numbers between lists. Variables can interact with each other!
firstNumList = [3, 1, 2]
secondNumList = [10, 6, 20]

print(firstNumList[0]+secondNumList[2])
