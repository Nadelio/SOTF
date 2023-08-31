import inventory
recipes_blueprints = {("metal spear"):("rope","handle","metal scrap")} # finish adding the rest of the recipes please

attempt = 0 

inv = inventory.Inventory()
'''
inv.add_item("rope")
inv.add_item("rope")
inv.add_item("handle")
inv.add_item("metal scrap")
'''
#^^^test code

def crafting_attempt(input):
    for required_item in recipes_blueprints[input]:
        if inv.contains_item(required_item):
            attempt += 1
            inv.remove_item(required_item)
        #print(attempt)

    #print(len(recipes_blueprints[input]))
    if attempt == len(recipes_blueprints[input]):
        attempt = 0
        inv.add_item(input)
        #for item in inv.items:
        #    print(item)