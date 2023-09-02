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
import constructor_test
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
    player = input('Type "city" to go to the City\nType "forest" to go to the Forest\nType "inv" to check your inventory\nType "craft" to craft an item\n').lower().strip()
    
    match player:
        case "city":
            enter_city()
        case "forest":
            enter_forest()
        case "inv":
            invcheck()
        case "inventory":
            invcheck()
        case "craft":
            crafting()
        case "stop":
            sys.exit()


#runs when entering the city
# THIS CAN BE REPLACED USING PLAYER ACTIONS I CREATED
def enter_city():
    clear_screen.main()
    print("Entered City")
    player = input("Do you want to search the city?\n")
    
    if (input_utils.yes_no(player)):
        search_city()
    else:
        choose_poi()


#runs when entering the forest
def enter_forest():
    clear_screen.main()
    print("Entered Forest")
    player = input("Do you want to search the forest?\n")
    if (input_utils.yes_no(player)):
        search_forest()
    else:
        choose_poi()


#runs when searching city
def search_city():
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

#randomizes mob stats
def rand_mob_stats():
    mob = constructor_test.Mob()
    return mob

#enemy probability to spawn code/fight start code
def mob_spawn():
    player = input("An enemy has appeared!\nDo you want to fight it?\n")
    if(player.lower().strip() in ["y", "yes"]):
        print("Fight started!")
        mob = rand_mob_stats()
        fighting()
    elif(player.lower().strip() in ["n", "no"]):
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
            crafting_attempt("rope")
            # 1 vine = 1 rope
        if(player == "2"):
            crafting_attempt("handle")
            # 2 stick = 1 handle
        if(player == "3"): 
            crafting_attempt("glass spear")
            # 1 handle, 1 rope, 1 glass = 1 glass spear
        if(player == "4"):
            crafting_attempt("wooden shield")
            # 1 wood, 1 handle = 1 wooden shield
        if(player == "5"):
            crafting_attempt("metal spear")
            # 1 handlem 1 rope, 1 metal scrap = 1 metal spear
        if(player == "6"):
            crafting_attempt("metal shield")
            # 1 metal scrap, 1 handle = 1 metal shield
    equipment()
    choose_poi()


#dev console commands (password protect)
def dev_console():
    clear_screen.main()
    equipment()
    player = input("Correct password.\nCommands enabled\nType 'add' to add an item to the inventory\nType 'stat' to print player statistics like damage or armor\nType 'clear' to clear inventory\nType 'back' to go back to run menu\n")
    if(player == "add"):
        player = input("DEV_ADD_CMD\n")
        inv.add_item(player)
        dev_console()
    elif(player == "clear"):
        inv.clear()
        dev_console()
    elif(player == "stat"):
        print("Player Health: ",player_hp)
        print("Player Damage: ",player_dmg)
        print("Armor: ", armor)
        print("Weapon Damage: ", weapon_dmg)
        print("Inventory: ", inv.items)
        dev_console()
    elif(player == "back"):
        run()


#equipment code
def equipment():
    global weapon_dmg
    global armor
    
    #armor and shields
    if("metal shield" in inv.items):
        armor = 2
    elif("wood shield" in inv.items):
        armor = 1
    else:
        armor = 0



    #weapons
    if("metal spear" in inv.items):
        weapon_dmg = 2
    elif("glass spear" in inv.items):
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
