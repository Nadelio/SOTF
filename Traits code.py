#Intelligence Specialties - Eletrical, Mechanical, Chemical, Medical
#Physical Specialties - Speed (More actions per move), Agility(Higher dodge), Strength (Melee damage increase)
#Miscellaneous Specialties - Scavenger(More resources gathered), Lucky(Higher probabilities for rarer items, fleeing, and dodging attacks), Crafty(Less materials/more common materials needed to craft rarer/powerful items *does not apply to story or boss items*), Charasmatic(Higher success chance when bargaining and convincing NPC's)

player = ""

elec_stat = 1
mech_stat = 1
chem_stat = 1
med_stat = 1

spd_stat = 0
agl_stat = 1
str_stat = 0

scav_stat = 1
luck_stat = 2
crft_stat = 0
char_stat = 1

def int_spec_choice():
    global elec_stat
    global mech_stat
    global chem_stat
    global med_stat
    
    print('Type "1" for Electrical, "2" for Mecanical, "3" for Chemical, or "4" for Medical\n')
    player = input("Choose an intelligence specialty\nElectrical - Less research points to unlock recipes in the electrical tree, first 3 levels of electrical tree unlocked\nMechanical - Less research points to unlock recipes in the mechanical tree, first 3 levels of mechanical tree unlocked\nChemical - Less research points to unlock recipes in the chemical tree, first 3 levels of chemical tree unlocked\nMedical - Less research points to unlock recipes in the medical tree, first 3 levels of medical tree unlocked\n")
    if(player == "1"):
        elec_stat = 2
    elif(player == "2"):
        mech_stat = 2
    elif(player == "3"):
        chem_stat = 2
    elif(player == "4"):
        med_stat = 2
    else:
        print("Error, please correctly input a choice\n")
        int_spec_choice()
        
def str_spec_choice():
    global spd_stat
    global agl_stat
    global str_stat

    print('Type "1" for Speed, "2" for Agility, or "3" for Strength\n')
    player = input("Choose a physical specialty\nSpeed - More actions per turn, Agility - Higher successful dodge probability, Strength - Melee weapons and fists have a +1 to damage\n")
    if(player == "1"):
        spd_stat = 1
    elif(player == "2"):
        agl_stat = 2
    elif(player == "3"):
        str_stat = 1
    else:
        print("Error, please correctly input a choice\n")
        str_spec_choice()
        
def misc_spec_choice():
    global scav_stat
    global luck_stat
    global crft_stat
    global char_stat

    print('Type "1" for Scavenger, "2" for Lucky, "3" for Crafty, or "4" for Charasmatic\n')
    player = input("Choose a skill specialty\nScavenger - More resources gathered, Lucky - Higher successful probability for rarer items, fleeing, and dodging attacks, Crafty - Less materials/more common materials needed to craft rarer/powerful items *does not apply to story or boss items*, Charasmatic - Higher success chance when bargaining and convincing NPC's\n")
    if(player == "1"):
        scav_stat = 2
    elif(player == "2"):
        luck_stat = 2
    elif(player == "3"):
        crft_stat = 1
    elif(player == "4"):
        char_stat = 2
    else:
        print("Error, please correctly input a choice\n")
        misc_spec_choice()

def stats():
    print(elec_stat, mech_stat, chem_stat, med_stat, spd_stat, agl_stat, str_stat, scav_stat, luck_stat, crft_stat, char_stat)

def runtime():
    stats()
    int_spec_choice()
    str_spec_choice()
    misc_spec_choice()
    stats()

runtime()