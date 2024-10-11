#Name:
#Class: 6th Hour
#Assignment: Scenario 3

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



#Enemy Dictionary Goes Here



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
