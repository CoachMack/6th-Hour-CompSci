#Name:
#Class: 6th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead
#has asked you to create a nested dictionary containing five enemy
#creatures (and their properties) for combat testing. Additionally,
#the testers are asking for a way to input changes to the enemy's
#damage values for balancing, as well as having it print those changes to
#confirm they went through.

#It is up to you to decide what properties
#are important and the theme of the game.

#UPDATE: The testers have run into some bugs with your code. Some of the
#code seems to not work correctly. For example, one of the testers changed
#the damage for an enemy to 30 per attack, but when they attacked the player
#character, the health went from 100 to 10030 instead of the intended 70.
#Your team lead has asked you to fix the bug and make sure your enemy damage
#can be subtracted properly while testing.
#(HINT: The player's health is stored as an integer.)

#Make an enemy dictionary containing 5 enemies
enemyDict = {
    "goblin" : {
        "Health" : 6,
        "AC" : 10,
        "Damage" : 4
    },
    "mimic": {
        "Health" : 17,
        "AC" : 13,
        "Damage" : 10
    },
    "orc": {
        "Health" : 22,
        "AC" : 14,
        "Damage" : 17
    },
    "dragon": {
        "Health" : 78,
        "AC" : 16,
        "Damage" : 25
    },
    "mindflayer": {
        "Health" : 101,
        "AC" : 17,
        "Damage" : 33
    },
}

#Allow user input to change damage value of enemies
enemyDict["goblin"]["Damage"] = int(input("Change the damage for Goblin: "))
enemyDict["mimic"]["Damage"] = int(input("Change the damage for Mimic: "))
enemyDict["orc"]["Damage"] = int(input("Change the damage for Orc: "))
enemyDict["dragon"]["Damage"] = int(input("Change the damage for Dragon: "))
enemyDict["mindflayer"]["Damage"] = int(input("Change the damage for Mindflayer: "))

#Print the changes to confirm they went through
print("The new damage for Goblin is:", enemyDict["goblin"]["Damage"])
print("The new damage for Mimic is:", enemyDict["mimic"]["Damage"])
print("The new damage for Orc is:", enemyDict["orc"]["Damage"])
print("The new damage for Dragon is:", enemyDict["dragon"]["Damage"])
print("The new damage for Mindflayer is:", enemyDict["mindflayer"]["Damage"])