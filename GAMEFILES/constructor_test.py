import random

class Mob:
    def __init__(self):
        self.mob_tag = "Mob Template"
        self.health = random.randrange(1) + 1
        self.damage = random.randrange(1) + 1
        self.defense = random.randrange(1)
        
        

def main():
    mob = Mob()
    print(mob.damage)
    print(mob.defense)
    print(mob.health)
    
if __name__ == "__main__":
    main()