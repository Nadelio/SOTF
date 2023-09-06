import inventory
recipes_blueprints = {
    "Metal Spear":["Rope","Handle","Metal Scrap"], 
    "Rope":["Vines"], 
    "Handle":["Stick","Stick"], 
    "Glass Spear":["Handle","Rope","Glass"], 
    "Wooden Shield":["Wood","Handle"], 
    "Metal Shield":["Metal scrap", "Handle"], 
    #add next recipe here "<item_name>":["<material_1>","<material_2>", etc...]
    }

# I'd like to add some new items, bones, gems, stone brick
# Stone Bricks can be crafted with 2 stones or in the catacombs
# Bones are collected from catacombs
# Gems are also collected from catacombs

# If y'all have any more ideas for items or recipes I can use these items in add them as a comment here or send a message in #sotf-collaborators

inv = inventory.Inventory()


def crafting_attempt(input):
    attempt = 0
    for required_item in recipes_blueprints[input]:
        if inv.contains_item(required_item):
            attempt += 1
            inv.remove_item(required_item)
        #print(attempt)

    #print(len(recipes_blueprints[input]))
    
    if attempt == len(recipes_blueprints[input]):
        attempt = 0
        inv.add_item(input)
        print(f"Successful crafted {input}")
        # return True
        #for item in inv.items:
        #    print(item)
    # else:
    #     return False