#Name:
#Class: 6th Hour
#Assignment: Scenario 3
import random

#Scenario 3:
#Now that the game development team has a dictionary for enemies
#(see Scenario 1) and the dictionary for the party is fixed
#(see Scenario 2), they want to start making a full prototype for the
#combat system. The team lead is a big Dungeons & Dragons fan and
#wants to make the combat similar to that. Because of this, the
#dictionaries need to be reworked slightly to be like that.

#Each enemy and party member in both dictionaries needs:
# - health points (somewhere between 6 and 25)
# - an attack modifier (somewhere between 3 and 7)
# - a damage roll (a number that varies based on weapon/spell)
# - and an Armor Class (somewhere between 10 and 17).

#To make things easier, here is a reference list for party damage rolls.
#(Feel free to use similar numbers for your enemy dictionary.)

# - Lae'Zel uses a greatsword: 2d6 + 3
# - Shadowheart uses a mace: 1d6 + 2
# - Gale uses the firebolt spell: 1d10
# - Astarion uses a shortbow: 1d6 + 4

#Step 1: Bring over Party Dictionary

#Step 2: Bring over Enemy Dictionary

#Step 3: Make sure every party and enemy has health points (fixed)

#Step 4: Make sure every party and enemy has an attack modifier (fixed)

#Step 5: Make sure every party and enemy has an an armor class (AC) (fixed)

#Step 6: Make sure every party and enemy has an damage roll (random)


#Party Dictionary Goes Here
partyDict = {
    "LaeZel" : {
        "Race" : "Githyanki",
        "Class" : "Fighter",
        "Background" : "Soldier",
        "Health" : 12,
        "AC" : 17,
        "AtkMod": 5,
        "Damage" : random.randint(1,6) + random.randint(1,6) + 3
    },
    "Shadowheart" : {
        "Race" : "Half-Elf",
        "Class" : "Cleric",
        "Background" : "Acolyte",
        "Health" : 10,
        "AC" : 14,
        "AtkMod": 3,
        "Damage" : random.randint(1,6) + 3,
    },
    "Gale" : {
        "Race" : "Human",
        "Class" : "Wizard",
        "Background" : "Sage",
        "Health" : 8,
        "AC" : 14,
        "AtkMod": 5,
        "Damage" : random.randint(1,10),
    },
    "Astarion" : {
        "Race" : "High Elf",
        "Class" : "Rogue",
        "Background" : "Charlatan",
        "Health" : 10,
        "AC" : 14,
        "AtkMod": 5,
        "Damage" : random.randint(1,6) + 4,
    }
}


#Enemy Dictionary Goes Here
enemyDict = {
    "Goblin" : {
        "Health" : 6,
        "AC" : 12,
        "AtkMod": 5,
        "Damage" : random.randint(1,6) + 4,
    },
    "Orc": {
        "Health" : 14,
        "AC" : 14,
        "AtkMod": 5,
        "Damage" : random.randint(1,6) + 4,
    },
    "Troll": {
        "Health" : 22,
        "AC" : 13,
        "AtkMod": 5,
        "Damage" : random.randint(1,6) + 4,
    },
    "Dragon": {
        "Health" : 56,
        "AC" : 17,
        "AtkMod": 5,
        "Damage" : random.randint(1,6) + 4,
    },
    "Mindflayer": {
        "Health" : 110,
        "AC" : 16,
        "AtkMod": 5,
        "Damage" : random.randint(1,6) + 4,
    }
}


#Once both dictionaries are updated, create a combat
#prototype that has a party member attack first, then an enemy
#attacks back right after.

#To determine if a creature hits another creature, you roll a
#20-sided die (d20) and add the attack modifier to the roll.
#If that number is the same as or higher than the enemy's Armor Class
#(AC), the attack hits and you roll for damage. If it is lower, the
#attack misses. If an enemy or party member hits zero (0) health
#points, they die.

#Step 7: Roll the attack roll for party member (d20 + Attack Modifier)

#Step 8: Check to see if the party member hits the enemy

#Step 9: Roll damage if it hits and subtract from enemy health

#Step 10: Check to see if the enemy is still alive

#Step 11: If the enemy is alive, repeat steps 7 through 10 but with the enemy attacking










#Combat Code Goes Here

#What variables do we need?
# - Enemy AC
# - D20 Roll
# - Enemy's Health
# - Party Attack Mod
# - Party Damage Roll

#if D20 + Party Attack Mod is greater than Enemy AC
if random.randint(1,20) + partyDict["Shadowheart"]["AtkMod"] >= enemyDict["Goblin"]["AC"]:
#   We hit! Deal Damage (subtract Party Damage Roll from HP)
    enemyDict["Goblin"]["Health"] -= partyDict["Shadowheart"]["Damage"]
    #Check to see if enemy is dead
    if enemyDict["Goblin"]["Health"] <= 0:
        print("Gobbo was hit! Gobbo is dead!")
        exit()
    #else, go to enemy turn
    else:
        print("Gobbo was hit! Gobbo is still alive!")
#else, we miss
else:
    print("Shadowheart Missed!")

if random.randint(1,20) + enemyDict["Goblin"]["AtkMod"] >= partyDict["Shadowheart"]["AC"]:
    partyDict["Shadowheart"]["Health"] -= enemyDict["Goblin"]["Damage"]
    if partyDict["Shadowheart"]["Health"] <= 0:
        print("Gobbo hit! Shadowheart is down!")
        exit()
    else:
        print("Gobbo hit! Shadowheart is alive!")
else:
    print("No one hit!")