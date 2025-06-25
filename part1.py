class Character:
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.strength = 1
        self.defence = 1

    def getStats(self):
        return "".join([self.name, "\n", "♥:", str(self.health), "\n", "💪:", str(self.strength), "\n", "⛊:", str(self.defence)])

# Main code starts here
p1 = Character(input("Enter p1 name: "))
print(p1.getStats())
print("")

p2 = Character(input("Enter p2 name: "))
print(p2.getStats())
