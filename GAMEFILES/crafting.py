import inventory

recipes_blueprints = {("metal spear"):("rope","handle","metal scrap")}

inv = inventory.Inventory()
inv.add_item("rope")
inv.add_item("handle")
inv.add_item("metal scrap")

if(inv.contains_item(recipes_blueprints["metal spear"])):
    inv.add_item("metal spear")
    print(inv)
else:
    print("Error")