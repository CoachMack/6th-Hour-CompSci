#Name:
#Class: 6th Hour
#Assignment: HW24

import random, time

#1. Copy over your class from HW23 and all the functions inside of it, and alter any functions to use self if applicable.
class Character:
    def __init__(self, health, damage, speed, max_health):
        self.health = health
        self.damage = damage
        self.speed = speed
        self.max_health = max_health

    def poison(self):
        for i in range(10):
            self.health -= random.randint(1,3)
            print(self.health)
            time.sleep(0.4)

    def healing(self):
        self.health += 30
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"Character healed! Current health at: {self.health}")
#2. Create a fourth attribute in the class called max_health that has the same values as health

#3. Copy the warrior and healer objects from HW23, and then make two more character objects with the following attribute values:
#thief (health/max: 50, damage: 30, speed: 40) and mage (health/max: 45, damage:35, speed: 25)
warrior = Character(100, 20, 30, 100)
healer = Character(60, 10, 30, 60)
thief = Character(50,30,40,50)
mage = Character(45,35,25,45)
#4. Randomly choose one of the four character objects to take the damage over time function and call the function to them
partyList = [warrior,healer,thief,mage]

charHit = random.choice(partyList)
charHit.poison()
#5. Determine who lost health by comparing the current health to the max_health and heal that character object by calling your healing function to that object and then print their health afterwards.
charHit.healing()