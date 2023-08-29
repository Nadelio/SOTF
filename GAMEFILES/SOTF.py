#Top of the script to you :>

#imports
import random
import sys
import time
import clear_screen
import json

#probability
hit_chance = ""


#player input
player = ""

#player inventory
inv = []

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
    for item in inv:
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
    if(player.lower().strip() in ["y", "yes"]):
        search_city()
    if(player.lower().strip() in ["n", "no"]):
        choose_poi()


#runs when entering the forest
def enter_forest():
    clear_screen.main()
    print("Entered Forest")
    player = input("Do you want to search the forest?\n")
    if(player.lower().strip() in ["y", "yes"]):
        search_forest()
    if(player.lower().strip() in ["n", "no"]):
        choose_poi()


#runs when searching city
def search_city():
    clear_screen.main()
    hit_chance = random.randrange(3)
    if(hit_chance == 1):
        save()
        inv.append("stone")
        close_save()
        print("Stone added to inventory")
    elif(hit_chance == 2):
        save()
        inv.append("glass")
        close_save()
        print("Glass added to inventory")
    elif(hit_chance == 3):
        save()
        inv.append("metal scrap")
        close_save()
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
        save()
        inv.append("wood")
        close_save()
        print("Wood added to inventory")
    elif(hit_chance == 2):
        save()
        inv.append("stick")
        close_save()
        print("Stick added to inventory")
    elif(hit_chance == 3):
        save()
        inv.append("vines")
        close_save()
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
                save()
                inv.clear()
                close_save()
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
    if(inv == []):
        pass
    else:
        global handle_craft
        global gspear_craft
        global wshield_craft
        global mspear_craft
        global mshield_craft
        save()
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
        close_save()
    equipment()
    choose_poi()


#dev console commands (password protect)
def dev_console():
    clear_screen.main()
    equipment()
    player = input("Correct password.\nCommands enabled\nType 'add' to add an item to the inventory\nType 'stat' to print player statistics like damage or armor\nType 'clear' to clear inventory\nType 'back' to go back to run menu\n")
    if(player == "add"):
        player = input("DEV_ADD_CMD\n")
        save()
        inv.append(player)
        close_save()
        dev_console()
    elif(player == "clear"):
        save()
        inv.clear()
        close_save()
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
    
    #armor and shields
    if("metal shield" in inv):
        armor = 2
    elif("wood shield" in inv):
        armor = 1
    else:
        armor = 0



    #weapons
    if("metal spear" in inv):
        weapon_dmg = 2
    elif("glass spear" in inv):
        weapon_dmg = 1
    else:
        weapon_dmg = 0

    #a place for equipment in the future (ex: fishing rod, pickaxe, axe, etc)


#save functions
def save():
    filename = 'Save.json'
    with open(filename, 'r') as f:
        data = json.load(f)
        inv = data #<--- replace 'inv' value

def close_save():
    with open('Save.json', 'w') as f:
        json.dump(inv, f, indent=4)


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
