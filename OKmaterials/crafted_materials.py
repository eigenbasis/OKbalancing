# Crafted_worth.py
import json

with open("worth_dic.json", "r") as f:
    item_value = json.load(f)

gained_worth = []

# basic function should be to just add values of the used materials
# TODO there are things that take 1h to craft which is also placeholder value if no time is needed
# Fixed by move to minute use
# TODO gold brick and gold dublouns
# for now pretend one try takes one energy, could include quest / key needed


def worth(timer, crafted_amount):
    material_name = str(raw_input("Used material: "))
    material_amount = float(raw_input("Used material amount: "))
    material_worth = item_value[material_name]
    print("-----------------")
    worth_value = ((material_worth * material_amount) + timer) / crafted_amount
    gained_worth.append(worth_value)


def item_worth():
    # depending on item amount call worth() for each item
    # item = str(raw_input("Item you want to calculate worth for: "))
    needed_material_amount = int(raw_input("Needed material amount: "))
    # 5min == 4 cents
    # 1min == 1.25 cents
    has_timer = str(raw_input("Does crafting take time? Y/N: "))
    if has_timer == "Y" or has_timer == "y":
        raw_timer = float(raw_input("Craft timer (in minutes): "))
        timer = raw_timer / 1.25
    else:
        timer = 0
    crafted_amount = float(raw_input("Crafted amount: "))
    print("-----------------")
    for i in range(needed_material_amount):
        worth(timer, crafted_amount)
    items_worth = sum(float(x) for x in gained_worth)
    item_value[item] = items_worth
    with open("worth_dic.json", "w") as g:
        item_value[item] = items_worth
        json.dump(item_value, g)
    print(item, "worth: ", items_worth)
    # sum worth() string to get final worth

item = str(raw_input("Item you want to calculate worth for: "))
if item in item_value:
    print(item, "worth: ", item_value[item])
else:
    item_worth()
