import random
from constructor_test import Mob #at some point lets move Mob default class here


#mob type holder
Mobtypes = ["Zombie", "Skeleton", "Bandit", "Animal"]


#mob classes
class Zombie:
    def __init__(self):
        self.mob_tag = Mobtypes[0]
        self.health = random.randrange(4)+1
        self.attack = random.randrange(1)+1
        self.defense = 0

class Animal:
    def __init__(self):
        self.mob_tag = Mobtypes[1]
        self.health = random.randrange(2)+1
        self.attack = 1
        self.defense = 0

class Bandit:
    def __init__(self):
        self.mob_tag = Mobtypes[2]
        self.health = random.randrange(1)+4
        self.attack = random.randrange(2)+1
        self.defense = 1

class Skeleton:
    def __init__(self):
        self.mob_tag = Mobtypes[3]
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
            print(f'Enemy type: {mob.mob_tag}')
        case 2:#forest
            mob = Animal()
            print(f'Enemy type: {mob.mob_tag}')
        case 3:#catacombs
            mob = Skeleton()
            print(f'Enemy type: {mob.mob_tag}')
        case 4:#UNUSED
            mob = Bandit()
            print(f'Enemy type: {mob.mob_tag}')
        case _:#error
            mob = Mob()
            print(f'Enemy type: {mob.mob_tag}')


if __name__ == "__main__":
    main()