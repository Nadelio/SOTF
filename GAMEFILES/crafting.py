import inventory
recipes_blueprints = {
    "metal spear":["rope","handle","metal scrap"], 
    "rope":["vines"], 
    "handle":["stick","stick"], 
    "glass spear":["handle","rope","glass"], 
    "wooden shield":["wood","handle"], 
    "metal shield":["metal scrap", "handle"], 
    #add next recipe here "<item_name>":["<material_1>","<material_2>", etc...]
    }



inv = inventory.Inventory()
'''
inv.add_item("rope")
inv.add_item("rope")
inv.add_item("handle")
inv.add_item("metal scrap")
'''
#^^^test code

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