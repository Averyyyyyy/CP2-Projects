# Classes and objects notes

# Notes
# A method is a function that is specific to a class


# A class is just a blue print for creating an object
# init method is allways the first one
class pokemon:
    def __init__(self, name, species, hp, dmg):
        self.name = name
        self.species = species
        self.hp = hp
        self.dmg = dmg

def __str__(self):
    return f"name: {self.name}\nspecise: {self.specise}\nhealth: {self.hp}\nattack: {self.dmg}"

def battle(self, opponent):
    while self.hp > 0 and opponent.hp > 0:
        opponent.hp -= self.dmg
        print(f"{self.name} attacked {opponent.name} for {self.dmg} and {opponent.name} now has {opponent.hp}")
        if opponent.hp > 0:
            self.hp -= opponent.dmg
            print(f"{opponent.name} attacked {self.name} for {opponent.dmg} and {self.name} now has {self.hp}")
        else:
            print(f"{opponent.name} has been knowcked out. {self.name} won the battle!")


# Every instince of a class is an object
# So bob and fluffy are objects
bob = pokemon("Mr.bob", "Charizard", 300, 95)   #object
fluffy = pokemon("Fluffy", "Arcanine", 1000, 110)    #object


print(bob.name)
print(fluffy.species)

bob.battle(fluffy)