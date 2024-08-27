santasList = ["CJ", "Evan", "Elijah", "Seeley", "AJ", "Jax", "Logan", "Kyle", "The Other Logan", "Ryan", "Colin"]
#santasList.append(input())
santasList.remove("AJ")
santasList.insert(4, "Joe")
print(f"{santasList[0]} is NAUGHTY!")
print(f"{santasList[2]} is NAUGHTY!")
print(f"{santasList[4]} is NAUGHTY!")
print(f"{santasList[7]} is NAUGHTY!")
print(f"{santasList[10]} is NAUGHTY!")


numList = [3, 5, 1, 3]
print(numList)
numList.sort()
print(numList)
numList.sort(reverse=True)
print(numList)
sum = numList[0] + numList[1] + numList[2]
print(sum)


mixList = ["Joe", True, 7]
print(mixList[int(input())])
