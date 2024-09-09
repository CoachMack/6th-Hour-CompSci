#BE SURE TO ADD NAME, CLASS, AND ASSIGNMENT TO THE TOP
#Name:
#Class:
#Assignment:

#print Hello World!
print("Hello World!")

#if you forget to add int() to an input, it will treat your number like a word instead
a = input("Enter a number: ")
b = input("Enter another number: ")
print(a + b)

#this is how it should be done
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
print(x + y)

#putting numbers in lists in quotation marks does the same thing, only put quotations for words
numList = ["1","2","3","4","5"]
numList2 = [1,2,3,4,5]

print(numList[0]+numList[1])
print(numList2[0]+numList2[1])


#You can also add numbers between lists. Lists can interact with each other!
firstNumList = [3, 4, 7]
secondNumList = [12, 9, 10]
sum = firstNumList[1] + secondNumList[2]
print(sum)

