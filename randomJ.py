import random

for i in range(3):
    print(random.random())

for i in range(3):
    print(random.randint(10,20))

members = ['John','Mary','Bob','Josh']

leader = random.choice(members)

print(leader)

class Dice:
    def roll(self):
        tupl = []
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second

snakieDie = Dice()

print(snakieDie.roll())