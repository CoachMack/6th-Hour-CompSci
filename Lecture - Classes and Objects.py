#Name: Coach Mack
#Class: 5th Hour
#Assignment: Lecture - Classes and Objects


#This is a class. These are used to apply certain attributes to a specific variable, known as an object.
#Python is what is called an "object-oriented" language. It is about taking things and doing things
#with those things. More practical than conceptual.
class Character:
    # Inside a class, you initialize it with an __init__ function, and assign to a variable called "self".
    # Self is the placeholder for objects so it can assign those specific attributes when the class is used.
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed

    #You can put functions inside of a class that allows you to use the functions to specific objects when called.
    def health_10_percent_nerf(self):
        self.health *= (9/10)
    def damage_20_percent_buff(self):
        self.damage *= (12/10)

#This is an object. By assigning a class to a variable, the numbers inside represent the object's
#attributes. In this case, the hulk has 750 health, 30 damage, and 50 speed.
theHulk = Character(750, 30, 50)
lunaSnow = Character(300, 20, 80)
spoodermon = Character(250, 60, 90)

print(f"The Hulk Health: {theHulk.health}")
print(f"Luna Snow Health: {lunaSnow.health}")
print(f"Spoodermon Health: {spoodermon.health}")

#You can use functions inside of a class to change the attributes to an object at will without having
#to change the original values or repeat the code for multiple objects.
theHulk.health_10_percent_nerf()
lunaSnow.damage_20_percent_buff()

print(f"The Hulk New Health: {theHulk.health}")
print(f"Luna Snow New Damage: {lunaSnow.damage}")

#You can also change the attribute directly if you need to and it will apply.
lunaSnow.damage = 25
print(f"Luna Snow New Damage (should be 25 now): {lunaSnow.damage}")

#You can also delete objects if an object needs to be deleted for whatever reason.
del spoodermon

#Just like if functions and def functions, classes can't be left empty so you can add
#pass to prevent errors.
class NPC:
    pass