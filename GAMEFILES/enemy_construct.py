import random
from constructor_test import Mob
from SOTF import poi_value

#mob type holder
Mobtypes = ["zombie", "skeleton", "bandit", "animal"]

#mob classes
class Zombie:
    def __init__(self):
        self.health = random.randrange(4)+1
        self.attack = random.randrange(1)+1
        self.defense = 0

class Animal:
    def __init__(self):
        self.health = random.randrange(2)+1
        self.attack = 1
        self.defense = 0

class Bandit:
    def __init__(self):
        self.health = random.randrange(1)+4
        self.attack = random.randrange(2)+1
        self.defense = 1

class Skeleton:
    def __init__(self):
        self.health = random.randrange(1)+1
        self.attack = random.randrange(1)+1
        self.defense = 0


#main
def main():
    mob_spawn = poi_value
    match mob_spawn:
        case 1:#city
            mob = Zombie()
        case 2:#forest
            mob = Animal()
        case 3:#catacombs
            mob = Bandit()
        case 4:#catacombs
            mob = Skeleton()
        case _:#error
            mob = Mob()


if __name__ == "__main__":
    main()