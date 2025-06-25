import random

class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.strength = 10
        self.defence = 10
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

class Wizard(Character):
    def __init__(self, name, spell):
        self.name = name
        self.health = 110
        self.strength = 8
        self.defence = 14
        self.spell = spell

    def getStats(self):
        return(super().getStats() + "\n Spell: " + self.spell)

p1 = Wizard("Amy", "Fireball")
print(p1.getStats())
p2 = Character("Adam")
print(p2.getStats())

p1.takeDamage(2)
p1.attack()




