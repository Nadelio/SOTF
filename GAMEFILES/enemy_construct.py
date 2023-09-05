import random
from constructor_test import Mob


#mob type holder
Mobtypes = ["zombie", "skeleton", "bandit", "animal"]


#mob classes
class Zombie:
    def __init__(self):
        self.mob_tag = "Zombie"
        self.health = random.randrange(4)+1
        self.attack = random.randrange(1)+1
        self.defense = 0

class Animal:
    def __init__(self):
        self.mob_tag = "Animal"
        self.health = random.randrange(2)+1
        self.attack = 1
        self.defense = 0

class Bandit:
    def __init__(self):
        self.mob_tag = "Bandit"
        self.health = random.randrange(1)+4
        self.attack = random.randrange(2)+1
        self.defense = 1

class Skeleton:
    def __init__(self):
        self.mob_tag = "Skeleton"
        self.health = random.randrange(1)+1
        self.attack = random.randrange(1)+1
        self.defense = 0


#main
def main():
    from SOTF import poi_value
    mob_spawn = poi_value
    match mob_spawn:
        case 1:#city
            mob = Zombie()
            print(mob.mob_tag)
        case 2:#forest
            mob = Animal()
        case 3:#catacombs
            mob = Bandit()
        case 4:#catacombs
            mob = Skeleton()
        case _:#error
            mob = Mob()
            print(mob.health)


if __name__ == "__main__":
    main()