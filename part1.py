import random

class Character:
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.strength = 1
        self.defence = 1

    def getStats(self):
        return "".join([self.name, "\n", "♥:", str(self.health), "\n", "💪:", str(self.strength), "\n", "⛊:", str(self.defence)])

    def takeDamage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(self.name + " took " + str(damage) + " damage. Health is now " + str(self.health))

    def isAlive(self):
        return self.health > 0

    def attack(self):
        attackVal = random.randint(0, 20) + self.strength
        print(self.name + " does " + str(attackVal) + " damage!")
        return attackVal


# Main code starts here
#p1 = Character(input("Enter p1 name: "))
p1 = Character("Amy")
print(p1.getStats())
print("")

#p2 = Character(input("Enter p2 name: "))
p2 = Character("Adam")
print(p2.getStats())

p1.takeDamage(2)

p1.attack()




