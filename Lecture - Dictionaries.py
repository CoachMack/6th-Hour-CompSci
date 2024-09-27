#Name: Coach Mack
#Class: 6th Hour
#Assignment: Lecture - Dictionaries

#Always start with a hello world to make sure your IDE works!
print("Hello World!")

#This is a dictionary. Think of it as a "list of lists".
#This is a way to organize your data in a more functional way
#than making a bunch of lists or a bunch of variables depending
#on what you are trying to do.

#Each dictionary has two parts: a key and a value.
#Think of the key as a kind of "variable" that you
#can sort stuff into, and the values are simply what
#those variables equal.
carDict = {
    "brand" : "Nissan",
    "model" : "Rogue",
    "year" : [2022,2023,2024]
}

#You can print the entire dictionary, one key of a dictionary, or one value within that key.
print(carDict)
print(carDict["model"])
#You can print one value within a key by doing something like this line below.
print(carDict["year"][0])

#You can also add other keys and values to a dictionary this way.
#NOTE: Doing it this way will overwrite the original value.
#For example, if you were to change the key in the line below to "model"
#it would REPLACE the value "Rogue" to "black".
carDict["color"] = "black"
print(carDict)

#This is the update function. This is a safer way to add things
#to a dictionary as you can explicitly state the values without
#overriding them.
carDict.update({"wheels": 4})
print(carDict)

#This is a quick way to print out only the keys within the dictionary.
carDictKeys = carDict.keys()
print(carDictKeys)

#This is a quick way to print out only the values within the dictionary.
carDictValues = carDict.values()
print(carDictValues)

#The "pop" function is what is used to remove a key and its values
#inside a dictionary.
carDict.pop("wheels")
print(carDict)

#This is how you can completely remove ALL data from a dictionary.
#It's a quick and dirty way to remove junk data to make room for new data.
carDict.clear()
print(carDict)

#You can also nest dictionaries. You can place a dictionary inside another
#dictionary for added organization. Nesting is an important skill to
#learn in computer science as it opens up a lot of other opportunities
#for more complex and functional code.
fifthHour = {
    "student1": {
        "Name" : "CJ",
        "Grade" : 12,
        "esports" : False,
    },
    "student2": {
        "Name" : "Colin",
        "Grade" : 12,
        "esports" : True,
    }
}

#This is how you print out the dictionary of one key within another dictionary.
print(fifthHour["student1"])

#This is how you print out a specific value within a nested dictionary.
print(fifthHour["student2"]["esports"])

#This is how you print out multiple values within the same line,
#even if it is from different dictionaries.
print(fifthHour["student1"]["Name"],fifthHour["student2"]["Name"])