import inventory
recipes_blueprints = {("metal spear"):("rope","handle","metal scrap")}

attempt = 0

inv = inventory.Inventory()
inv.add_item("rope")
inv.add_item("rope")
inv.add_item("handle")
inv.add_item("metal scrap")
def crafting_attempt():
    for required_item in recipes_blueprints["metal spear"]:
        if inv.contains_item(required_item):
            attempt += 1
            inv.remove_item(required_item)
        print(attempt)

    print(len(recipes_blueprints["metal spear"]))
    if attempt == len(recipes_blueprints["metal spear"]):
        attempt = 0
        inv.add_item("metal_spear")
        for item in inv.items:
            print(item)