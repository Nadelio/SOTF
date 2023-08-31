#Top of the script to you :>

#imports
import random
import sys
import time
import clear_screen
import save_manager
import input_utils
import inventory
#probability
hit_chance = ""

#player input
player = ""

#player inventory
inventory = inventory.Inventory()

#player and enemy data
player_hp = 10
armor = 0
mob_dmg = 0
mob_hp = 0
mob_armor = 0
player_dmg = 2
weapon_dmg = 0


#crafting data
handle_craft = 0
gspear_craft = 0
wshield_craft = 0
mspear_craft = 0
mshield_craft = 0


#inventory command
def invcheck():
    clear_screen.main()
    for item in inventory.items:
        print(item)
    choose_poi()


#main menu/startup "move" command
def choose_poi():
    clear_screen.main()
    equipment()
    player = input('Type "city" to go to the City\nType "forest" to go to the Forest\nType "inv" to check your inventory\nType "craft" to craft an item\n')
    
    match player:
        case "city":
            enter_city()
        case "forest":
            enter_forest
        case "inv":
            invcheck()
        case "inventory":
            invcheck()
        case "craft":
            crafting()
        case "stop":
            sys.exit()


#runs when entering the city
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
        inventory.add_item("Stone")
        print("Stone added to inventory")
    elif(hit_chance == 2):
        inventory.add_item("Glass")
        print("Glass added to inventory")
    elif(hit_chance == 3):
        inventory.add_item("Metal Scrap")
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
        inventory.add_item("Wood")
        print("Wood added to inventory")
    elif(hit_chance == 2):
        inventory.add_item("Stick")
        print("Stick added to inventory")
    elif(hit_chance == 3):
        inventory.add_item("Vines")
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
    global mob_hp
    global mob_dmg
    global mob_armor
    mob_hp = random.randrange(4)+1
    mob_dmg = random.randrange(1)+1
    mob_armor = random.randrange(1)

#enemy probability to spawn code/fight start code
def mob_spawn():
    player = input("An enemy has appeared!\nDo you want to fight it?\n")
    if(player.lower().strip() in ["y", "yes"]):
        print("Fight started!")
        rand_mob_stats()
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
                inventory.clear()
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


#crafting code (pain in the ass to write)
def crafting():
    clear_screen.main()
    if(inventory.is_empty()):
        pass
    else:
        global handle_craft
        global gspear_craft
        global wshield_craft
        global mspear_craft
        global mshield_craft
        save_manager.save_data()
        print("Recipes:\nRope - Vines\nHandle - 2 sticks\nGlass Spear - Handle, Rope, Glass\nWooden Shield - Wood, Handle\nMetal Spear - Handle, Rope, Metal Scrap\nMetal Shield - Metal Scrap, Handle\n")
        player = input("What would you like to craft?\n1 - Rope\n2 - Handle\n3 - Glass Spear\n4 - Wooden Shield\n5 - Metal Spear\n6- Metal Shield\n")
        if(player == "1"): pass
            # if(inventory.contains_item("vines")):
            #     inventory.remove_item("vines")
            #     inventory.add_item("rope")
            #     print("Rope added to inventory")
        if(player == "2"): pass
            # if(inventory.contains_item("stick", 2)):
            #     handle_craft += 2
            # if(handle_craft == 2):
            #     inventory.remove_item("stick", 2)
            #     inventory.add_item("handle")
            #     print("Handle added to inventory")
            #     handle_craft = 0
        if(player == "3"): pass
            # if(inventory.contains_item("glass")):
            #     gspear_craft += 1
            # if(inventory.contains_item("rope")):
            #     gspear_craft += 1
            # if(inventory.contains_item("handle")):
            #     gspear_craft += 1
            # if(gspear_craft == 3):
            #     inventory.remove_item("glass")
            #     inventory.remove_item("handle")
            #     inventory.remove_item("rope")
            #     inventory.add_item("glass spear")
            #     print("Glass Spear added to inventory")
            #     gspear_craft = 0
        if(player == "4"):  pass
            # if(inventory.contains_item("wood")):
            #     wshield_craft += 1
            # if(inventory.contains_item("handle")):
            #     wshield_craft += 1
            # if(wshield_craft == 2):
            #     inventory.remove_item("wood")
            #     inventory.remove_item("handle")
            #     inventory.add_item("wooden shield")
            #     print("Wooden Shield added to inventory")
            #     wshield_craft = 0
        if(player == "5"): pass
            # if(inventory.contains_item("rope")):
            #     mspear_craft += 1
            # if(inventory.contains_item("handle")):
            #     mspear_craft += 1
            # if(inventory.contains_item("metal scrap")):
            #     mspear_craft += 1
            # if(mspear_craft == 3):
            #     inventory.remove_item("rope")
            #     inventory.remove_item("handle")
            #     inventory.remove_item("metal scrap")
            #     inventory.add_item("metal spear")
            #     inventory.remove("glass spear")
            #     print("Metal Spear added to inventory")
            #     mspear_craft = 0
        if(player == "6"): pass
            # if(inventory.contains_item("metal scrap")):
            #     mshield_craft += 1
            # if(inventory.contains_item("handle")):
            #     mshield_craft += 1
            # if(mshield_craft == 2):
            #     inventory.remove_item("handle")
            #     inventory.remove_item("metal scrap")
            #     inventory.add_item("metal shield")
            #     inventory.remove_item("wood shield")
            #     print("Metal Shield added to inventory")
            #     mshield_craft = 0
    equipment()
    choose_poi()


#dev console commands (password protect)
def dev_console():
    clear_screen.main()
    equipment()
    player = input("Correct password.\nCommands enabled\nType 'add' to add an item to the inventory\nType 'stat' to print player statistics like damage or armor\nType 'clear' to clear inventory\nType 'back' to go back to run menu\n")
    if(player == "add"):
        player = input("DEV_ADD_CMD\n")
        inventory.add_item(player)
        dev_console()
    elif(player == "clear"):
        inventory.clear()
        dev_console()
    elif(player == "stat"):
        print("Player Health: ",player_hp)
        print("Player Damage: ",player_dmg)
        print("Armor: ", armor)
        print("Weapon Damage: ", weapon_dmg)
        print("Inventory: ", inventory.items)
        dev_console()
    elif(player == "back"):
        run()


#equipment code
def equipment():
    global weapon_dmg
    global armor
    
    #armor and shields
    if(inventory.contains_item("metal shield")):
        armor = 2
    elif(inventory.contains_item("wood shield")):
        armor = 1
    else:
        armor = 0



    #weapons
    if(inventory.contains_item("metal spear")):
        weapon_dmg = 2
    elif(inventory.contains_item("wood spear")):
        weapon_dmg = 1
    else:
        weapon_dmg = 0

    #a place for equipment in the future (ex: fishing rod, pickaxe, axe, etc)





#startup code
def run():
    player = input('Type "inv" (or "inventory") to check your inventory\nType "move" to choose a place to go\nType "craft" to open the crafting options\nType "stop" to stop the program\n')
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
