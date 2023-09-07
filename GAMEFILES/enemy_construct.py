import random

#mob type holder
Mobtypes = ["Zombie", "Skeleton", "Bandit", "Animal"]


#default mob class
class Mob:
    def __init__(self, mob_tag, health, damage, defense):
        self.mob_tag = mob_tag
        self.health = health
        self.damage = damage
        self.defense = defense


#mob classes
class Zombie(Mob):
    def __init__(self):
        super().__init__(mob_tag = Mobtypes[0])
        super().__init__(health = random.randrange(4)+1)
        super().__init__(damage = random.randrange(1)+1)
        super().__init__(defense = 0)

class Animal(Mob):
    def __init__(self):
        super().__init__(mob_tag = Mobtypes[3])
        super().__init__(health = random.randrange(2)+1)
        super().__init__(damage = 1)
        super().__init__(defense = 0)

class Bandit(Mob):
    def __init__(self):
        super().__init__(mob_tag = Mobtypes[2])
        super().__init__(health = random.randrange(1)+4)
        super().__init__(damage = random.randrange(2)+1)
        super().__init__(defense = 1)

class Skeleton:
    def __init__(self):
        super().__init__(mob_tag = Mobtypes[1])
        super().__init__(health = random.randrange(1)+1)
        super().__init__(damage = random.randrange(1)+1)
        super().__init__(defense = 0)


#main
def main(poi): 
    mob_spawn = poi
    match mob_spawn:
        case 1:#city
            mob = Zombie(Mobtypes[0], random.randrange(4)+1, random.randrange(1)+1, 0)
            print(f'Enemy type: {mob.mob_tag}')
            return mob

        case 2:#forest
            mob = Animal(Mobtypes[3], random.randrange(2)+1, 1, 0)
            print(f'Enemy type: {mob.mob_tag}')
            return mob
        case 3:#catacombs #
            mob = Skeleton(Mobtypes[1], random.randrange(1)+1, random.randrange(1)+1, 0)
            print(f'Enemy type: {mob.mob_tag}')
            return mob
        case 4:#UNUSED
            mob = Bandit(Mobtypes[2], random.randrange(1)+4, random.randrange(2)+1, 1)
            print(f'Enemy type: {mob.mob_tag}')
            return mob
        case _:#error
            mob = Mob("Default Mob", 1, 1, 0)
            print(f'Enemy type: {mob.mob_tag}')
            return mob


if __name__ == "__main__":
    main()
