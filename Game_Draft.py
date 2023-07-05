#imports
import random
import sys
import time
import cls
from Save import *

#probability
hit_chance = ""


#player input
player = ""


#player and enemy data
player_hp = 10
armor = 0
mob_dmg = 1
mob_hp = 5
mob_armor = 0
player_dmg = 1
weapon_dmg = 0


#crafting data
handle_craft = 0
gspear_craft = 0
wshield_craft = 0
mspear_craft = 0
mshield_craft = 0


#inventory command
def invcheck():
    cls.cls()
    for item in inv:
        print(item)


#main menu/startup "move" command
def choose_poi():
    while True:
        cls.cls()
        equipment()
        player = input('Type "city" to go to the City\nType "forest" to go to the Forest\nType "inv" to check your inventory\nType "craft" to craft an item\nType "save" to save your progress\nType "stop" to close the program\n')
        if(player == "city"):
            enter_city()
        if(player == "forest"):
            enter_forest()
        if(player == "inv"):
            invcheck()
        if(player == "craft"):
            crafting()
        if(player == "stop"): 
            break 
        if(player == "save"):
            save_func()


#runs when entering the city
def enter_city():
    cls.cls()
    print("Entered City")
    player = input("Do you want to search the city?\n")
    if(player.lower().strip() in ["y", "yes"]):
        search_city()


#runs when entering the forest
def enter_forest():
    cls.cls()
    print("Entered Forest")
    player = input("Do you want to search the forest?\n")
    if(player.lower().strip() in ["y", "yes"]):
        search_forest()


#runs when searching city
def search_city():
    cls.cls()
    hit_chance = random.randrange(5)
    if(hit_chance == 1):
        inv.append("stone")
        print("Stone added to inventory")
    elif(hit_chance == 2):
        inv.append("glass")
        print("Glass added to inventory")
    elif(hit_chance == 3):
        inv.append("metal scrap")
        print("Metal scrap added to inventory")
    else:
        print("Nothing found")
    hit_chance = random.randrange(3)
    if(hit_chance >= 1):
        mob_spawn()
    else:
        print("No enemies")


#runs when searching forest
def search_forest():
    cls.cls()
    hit_chance = random.randrange(5)
    if(hit_chance == 1):
        inv.append("wood")
        print("Wood added to inventory")
    elif(hit_chance == 2):
        inv.append("stick")
        print("Stick added to inventory")
    elif(hit_chance == 3):
        inv.append("vines")
        print("Vines added to inventory")
    else:
        print("Nothing found")
    hit_chance = random.randrange(3)
    if(hit_chance >= 1):
        mob_spawn()
    else:
        print("No enemies")



#enemy probability to spawn code/fight start code
def mob_spawn():
    player = input("An enemy has appeared!\nDo you want to fight it?\n")
    if(player.lower().strip() in ["y", "yes"]):
        print("Fight started!")
        fighting()
    elif(player.lower().strip() in ["n", "no"]):
        hit_chance = random.randrange(2)
        if(hit_chance == 1):
            print("You escaped!")
        else:
            print("You failed to escape")
            print("Fight started!")
            fighting()


#fighting code  
def fighting():
    equipment()
    global player_hp
    global armor
    global mob_dmg
    global mob_hp
    global weapon_dmg
    while(player_hp > 0 or mob_hp > 0):
        player_hp = player_hp
        hit_chance = random.randrange(8)
        if(hit_chance >= 6):
            print("You've been hit!")
            player_hp = player_hp - (mob_dmg - armor)
            print("Player health: ",player_hp)
            player_atk()
        if(player_hp == 0):
            player = input("You died! Wanna try again?\n")
            if(player.lower().strip() in ["y", "yes"]):
                player_hp = 10
                mob_hp = 5
                inv.clear()
                run()
            else:
                sys.exit()
        if(mob_hp <= 0):
            print("You won the fight!")
            mob_hp = 5
            player_hp = 10


#player attack code/player flee code
def player_atk():
    equipment()
    global mob_hp
    global mob_armor
    global player_dmg
    global player_hp
    global weapon_dmg
    player = input('Type "atk" to attack.\nType "run" to run\n')
    if(player == "atk"):
        hit_chance = random.randrange(3)
        if(hit_chance > mob_armor):
            mob_hp = mob_hp - (player_dmg + weapon_dmg)
            print("Enemy health: ",mob_hp)
        else:
            print("Attack failed!")
            fighting()
    elif(player == "run"):
        hit_chance = random.randrange(3)
        if(hit_chance == 1 or hit_chance == 2):
            print("You fled!")
            player_hp = 10
            mob_hp = 5
        else:
            print("You failed to escape!")


#crafting code (pain in the ass to write)
def crafting():
    cls.cls()
    global handle_craft
    global gspear_craft
    global wshield_craft
    global mspear_craft
    global mshield_craft
    print("Recipes:\nRope - Vines\nHandle - 2 sticks\nGlass Spear - Handle, Rope, Glass\nWooden Shield - Wood, Handle\nMetal Spear - Handle, Rope, Metal Scrap\nMetal Shield - Metal Scrap, Handle\n")
    player = input("What would you like to craft?\n1 - Rope\n2 - Handle\n3 - Glass Spear\n4 - Wooden Shield\n5 - Metal Spear\n6- Metal Shield\n")
    if(player == "1"):
        if("vines" in inv):
            inv.remove("vines")
            inv.append("rope")
            print("Rope added to inventory")
    if(player == "2"):
        if("stick" in inv):
            handle_craft += 1
        if("stick" in inv):
            handle_craft += 1
        if(handle_craft == 2):
            inv.remove("stick")
            inv.remove("stick")
            inv.append("handle")
            print("Handle added to inventory")
            handle_craft = 0
    if(player == "3"):
        if("glass" in inv):
            gspear_craft += 1
        if("rope" in inv):
            gspear_craft += 1
        if("handle" in inv):
            gspear_craft += 1
        if(gspear_craft == 3):
            inv.remove("glass")
            inv.remove("rope")
            inv.remove("handle")
            inv.append("glass spear")
            print("Glass Spear added to inventory")
            gspear_craft = 0
    if(player == "4"):
        if("wood" in inv):
            wshield_craft += 1
        if("handle" in inv):
            wshield_craft += 1
        if(wshield_craft == 2):
            inv.remove("wood")
            inv.remove("handle")
            inv.append("wooden shield")
            print("Wooden Shield added to inventory")
            wshield_craft = 0
    if(player == "5"):
        if("rope" in inv):
            mspear_craft += 1
        if("handle" in inv):
            mspear_craft += 1
        if("metal scrap" in inv):
            mspear_craft += 1
        if(mspear_craft == 3):
            inv.remove("rope")
            inv.remove("handle")
            inv.remove("metal scrap")
            inv.append("metal spear")
            if("glass spear" in inv and mspear_craft == 3):
                inv.remove("glass spear")
            print("Metal Spear added to inventory")
            mspear_craft = 0
    if(player == "6"):
        if("metal scrap" in inv):
            mshield_craft += 1
        if("handle" in inv):
            mshield_craft += 1
        if(mshield_craft == 2):
            inv.remove("handle")
            inv.remove("metal scrap")
            inv.append("metal shield")
            if("wood shield" in inv and mshield_craft == 2):
                inv.remove("wood shield")
            print("Metal Shield added to inventory")
            mshield_craft = 0
    equipment()
    save_func()


#dev console commands (password protect)
def dev_console():
    cls.cls()
    equipment()
    player = input("Correct password.\nCommands enabled\nType 'add' to add an item to the inventory\nType 'stat' to print player statistics like damage or armor\nType 'clear' to clear inventory\nType 'back' to go back to run menu\n")
    if(player == "add"):
        player = input("DEV_ADD_CMD\n")
        inv.append(player)
        save_func()
        dev_console()
    elif(player == "clear"):
        inv.clear()
        dev_console()
    elif(player == "stat"):
        print("Player Health: ",player_hp)
        print("Player Damage: ",player_dmg)
        print("Armor: ", armor)
        print("Weapon Damage: ", weapon_dmg)
        print("Inventory: ", inv)
        dev_console()
    elif(player == "back"):
        run()


#equipment code
def equipment():
    global weapon_dmg
    global armor
    if("metal shield" in inv):
        armor = 2
    elif("wood shield" in inv):
        armor = 1
    else:
        armor = 0




    if("metal spear" in inv):
        weapon_dmg = 2
    elif("glass spear" in inv):
        weapon_dmg = 1
    else:
        weapon_dmg = 0


#put saving function here vvvv
def save_func():
    file_builder = open("Save.py", "w+") #instantiates the file
    file_builder.write("inv = [") #this is my ghetto solution to writing lists into .py files
    for x in inv:
        file_builder.write("'")
        file_builder.write(x)
        file_builder.write("', ")
    file_builder.write("]\n") #this is the end of ghetto solution to writing lists into .py files
    #file_builder.write("player_hp = " + str(player_hp)) #adds variable player_hp into Save.py (FOR FUTURE REFRENCE)
    file_builder.close() #closes the file_builder so it doesn't run infinitely


#startup code
def run():
    player = input('Type "inv" to check your inventory\nType "move" to choose a place to go\nType "craft" to open the crafting options\nType "stop" to stop the program\n')
    if(player == "inv"):
        invcheck()
    elif(player == "move"):
        choose_poi()
    elif(player == "craft"):
        crafting()
    elif(player == "stop"): 
        sys.exit()
    elif(player =="dev"):
        player = input("Dev Console Started\nPlease enter password: ")
        if(player == "nadelio"):
            dev_console()


#startup
print("Welcome to Survival of the Fittest")
time.sleep(1)
print("This is a game made by Downward Spiral Studios")
time.sleep(1)
print(" ")
print(" ")
run()