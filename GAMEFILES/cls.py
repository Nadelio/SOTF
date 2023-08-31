import os
import time


def cls():
    time.sleep(1)
    os.system('cls' if os.name=='nt' else 'clear')
    print("Welcome to Survival of the Fittest")
    print("This is a game made by Downward Spiral Studios")
    print("")
    print("")
if __name__ == '__main__':
    cls()
