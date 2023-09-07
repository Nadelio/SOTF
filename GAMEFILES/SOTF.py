#Top of the script to you :>

#imports
import random
import sys
import time
from crafting import crafting_attempt
import clear_screen
import save_manager
import input_utils
import inventory
import enemy_construct
#probability
hit_chance = ""


#player input
player = ""

#player inventory
inv = inventory.Inventory()

#player and enemy data
player_hp = 10
armor = 0
mob_dmg = 0
mob_hp = 0
mob_armor = 0
player_dmg = 2
weapon_dmg = 0

#poi mob value
poi_value = 0

#inventory command
def invcheck():
    clear_screen.main()
    for item in inv.items:
        print(item)
    choose_poi()


#main menu/startup "move" command
def choose_poi():
    clear_screen.main()
    equipment()
    player = input('Type "city" to go to the City\nType "forest" to go to the Forest\nType "catacombs" to go to the Catacombs\nType "inv" to check your inventory\nType "craft" to craft an item\n').lower().strip()
    
    match player:
        case "city":
            search_city()
        case "forest":
            search_forest()
        case "catacombs":
            search_catacombs()
        case "inv":
            invcheck()
        case "inventory":
            invcheck()
        case "craft":
            crafting()
        case "stop":
            sys.exit()


#runs when searching city
def search_city():
    global poi_value
    poi_value = 1
    clear_screen.main()
    hit_chance = random.randrange(3)
    if(hit_chance == 1):
        inv.add_item("Stone")
        print("Stone added to inventory")
    elif(hit_chance == 2):
        inv.add_item("Glass")
        print("Glass added to inventory")
    elif(hit_chance == 3):
        inv.add_item("Metal Scrap")
        print("Metal scrap added to inventory")
    else:
        print("Nothing found")
    hit_chance = random.randrange(2)
    if(hit_chance >= 1):
        mob_spawn()
    else:
        print("No enemies")
        choose_poi()


#runs when searching forest
def search_forest():
    global poi_value 
    poi_value = 2
    clear_screen.main()
    hit_chance = random.randrange(3)
    if(hit_chance == 1):
        inv.add_item("Wood")
        print("Wood added to inventory")
    elif(hit_chance == 2):
        inv.add_item("Stick")
        print("Stick added to inventory")
    elif(hit_chance == 3):
        inv.add_item("Vines")
        print("Vines added to inventory")
    else:
        print("Nothing found")
    hit_chance = random.randrange(2)
    if(hit_chance >= 1):
        mob_spawn()
    else:
        print("No enemies")
        choose_poi()

#runs when searching catacombs
def search_catacombs():
    global poi_value
    poi_value = 3
    clear_screen.main()
    hit_chance = random.randrange(3)
    match hit_chance:
        case 1:
            inv.add_item("Stone")
            print("Stone added to inventory")
        case 2:
            inv.add_item("Vines")
            print("Vines added to inventory")
        case _:
            print("Nothing found")
    hit_chance = random.randrange(2)
    if(hit_chance >= 1):
        mob_spawn()
    else:
        print("No enemies")
        choose_poi()


#enemy probability to spawn code/fight start code
def mob_spawn():
    global poi_value
    player = input("An enemy has appeared!\nDo you want to fight it?\n")
    if(input_utils.yes_no(player) == True):
        print("Fight started!")
        mob = enemy_construct.main(poi_value)
        fighting()
    elif(input_utils.yes_no(player) == False):
        hit_chance = random.randrange(1)
        if(hit_chance == 1):
            print("You escaped!")
            choose_poi()
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
        hit_chance = random.randrange(4)
        if(hit_chance >= 3):
            print("You've been hit!")
            player_hp = player_hp - (mob_dmg - armor)
            print("Player health: ",player_hp)
            player_atk()
        if(player_hp == 0):
            player = input("You died! Wanna try again?\n")
            if(input_utils.yes_no(player) == True):
                player_hp = 10
                inv.clear()
                run()
            else:
                sys.exit()
        if(mob_hp <= 0):
            print("You won the fight!")
            player_hp = 10
            choose_poi()


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
        hit_chance = random.randrange(2)
        if(hit_chance == 1 or hit_chance == 2):
            print("You fled!")
            player_hp = 10
            mob_hp = 5
            choose_poi()
        else:
            print("You failed to escape!")


#crafting code
def crafting():
    clear_screen.main()
    if(inv.is_empty()):
        pass
    else:
        save_manager.save_data()
        print("Recipes:\nRope - Vines\nHandle - 2 sticks\nGlass Spear - Handle, Rope, Glass\nWooden Shield - Wood, Handle\nMetal Spear - Handle, Rope, Metal Scrap\nMetal Shield - Metal Scrap, Handle\n")
        player = input("What would you like to craft?\n1 - Rope\n2 - Handle\n3 - Glass Spear\n4 - Wooden Shield\n5 - Metal Spear\n6- Metal Shield\n")
        if(player == "1"):
            crafting_attempt("Rope")
            # 1 vine = 1 rope
        if(player == "2"):
            crafting_attempt("Handle")
            # 2 stick = 1 handle
        if(player == "3"): 
            crafting_attempt("Glass Spear")
            # 1 handle, 1 rope, 1 glass = 1 glass spear
        if(player == "4"):
            crafting_attempt("Wooden Shield")
            # 1 wood, 1 handle = 1 wooden shield
        if(player == "5"):
            crafting_attempt("Metal Spear")
            # 1 handlem 1 rope, 1 metal scrap = 1 metal spear
        if(player == "6"):
            crafting_attempt("Metal Shield")
            # 1 metal scrap, 1 handle = 1 metal shield
    equipment()
    choose_poi()


#dev console commands (password protect)
def dev_console():
    global poi_value
    clear_screen.main()
    equipment()
    player = input("Correct password.\nCommands enabled\nType 'add' to add an item to the inventory\nType 'stat' to print player statistics like damage or armor\nType 'clear' to clear inventory\nType 'mob' to spawn a mob and choose which mob\nType 'back' to go back to run menu\n")
    if(player == "add"):
        player = input("DEV_ADD_CMD\n")
        inv.add_item(player)
        dev_console()
    elif(player == "clear"):
        inv.clear()
        dev_console()
    elif(player == "stat"):
        print(f'Player Health: {player_hp}\nPlayer Damage: {player_dmg}\nPlayer Armor: {armor}\nWeapon Damage: {weapon_dmg}\n Inventory: {inv.items}')
        dev_console()
    elif(player == "mob"):
        player = input("Set POI: ")
        poi_value = player
        mob = enemy_construct.main(poi_value)
        print(f'Mob Health: {mob_hp}\nMob Damage: {mob_dmg}\nMob Armor: {mob_armor}')
        dev_console()
    elif(player == "back"):
        run()


#equipment code
def equipment():
    global weapon_dmg
    global armor
    
    #armor and shields
    if("Metal Shield" in inv.items):
        armor = 2
    elif("Wood Shield" in inv.items):
        armor = 1
    else:
        armor = 0



    #weapons
    if("Metal Spear" in inv.items):
        weapon_dmg = 2
    elif("Glass Spear" in inv.items):
        weapon_dmg = 1
    else:
        weapon_dmg = 0

    #a place for equipment in the future (ex: fishing rod, pickaxe, axe, etc)





#startup code
def run():
    player = input('Type "inv" (or "inventory") to check your inventory\nType "move" to choose a place to go\nType "craft" to open the crafting options\nType "stop" to stop the program\n')
    match player:
        case "move":
            choose_poi()
        case "inv":
            invcheck()
        case "inventory":
            invcheck()
        case "craft":
            crafting()
        case "stop":
            sys.exit()
        case "dev":
            player = input("Dev Console Started\nPlease enter password: ")
            if(player == "nadelio" or player == "pyrolyzed"):
                dev_console()


#startup
print("Welcome to Survival of the Fittest")
time.sleep(1)
print("This is a game made by Downward Spiral Studios")
time.sleep(1)
print(" ")
print(" ")
run()
