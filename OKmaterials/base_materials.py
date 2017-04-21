# OKmaterials.py

import json


with open("worth_dic.json", "r") as f:
    try:
        item_value = json.load(f)
    except ValueError:
        item_value = {}

drop_rate = {"obsidian": 0.055, "thorny_twig": 0.1, "bone": 0.21, "jute_string": 0.25, "egg": 0.35,
             "wool": 0.5, "milk": 0.7, "diamond": 0.05, "citrin": 0.06, "jade": 0.08, "jasper": 0.12, "pearl": 0.036,
             "small_copper_ore": 0.2, "stone_splinter": 0.15, "savannah_rock": 0.6, "small_iron_ore": 0.7,
             "savannah_grass": 0.7, "earthworm": 0.17, "bug": 0.15, "green_worm": 0.1, "copper_ore": 0.33,
             "iron_ore": 0.67, "gold_doubloon": 0.037, "silver_doubloon": 0.296, "bronze_doubloon": 0.667}

# TODO what if the used materials are crafted not found
# Use 1 / materials value
# TODO what if material takes timer not drop_rate, like corn or violet berries
# for harvesting: drop_rate = 1 / (time in h * 60 / 5 - 2 / amount you get from harvesting)
# but harvesting stuff should be nerfed so / 10
# for animals: drop_drop = 1 / (time in h * 60 / 5 - 1) * ensured_drop from pure drop_rate
# might use new_eggs and stuff but also nerfed
# for mining thing: drop_rate = 1 / (time in h * 60 / 5 - used_energy / amount you get + used material ensured_drop)
# TODO what if energy is needed to craft. one energy ensured_drop == one_energy (should be)
# energy drop_rate is 0.25 and is included in description
# TODO pure drop_rate can not be items value because of ensured_drop problem
# solved by applied worth() to basic materials as well
# TODO base always mining stuff on energy use
# done for stone and clay
# TODO wood stuff. could be similar to clay and stone
# is similar to clay and stone. is EXACTLY like clay and stone
# TODO items not crafted OR dropped, like cirtni un klits sulas un garsvielas
# TODO make so can enter items name and script will pull value from drop_rates.py
# replaced that with dictionary and made input work
# TODO for drop rates could take into account mine timer, like for water
# TODO crafted amount and timer could be out side of the loop, somehow
# TODO add coconuts and collection items
# TODO what about items that are not materials?
# TODO what to do with materials you can only buy?
# 1 ruby = 25 shells
# 1 ruby drop_rate = 2.5
# 1 shell drop_rate = 0.1
# TODO if drop_rate > 1
# if > 1 takes drop_rate as ensured_dorp
# TODO items that ask for other crafted items
# TODO make so need to write in material want to check and it spits out worth
# DONE asks for material and checks if it's in item_value dic
# TODO make so appends item_value with calculated items worth
# DONE as part of worth_dic.json
# TODO make it so item_value is writen to a file so can be saved outside of loop
# DONE saves in worth_dic.json and new script reads that and assigns to item_value which is a dic
# TODO what to do with items that take time?
# DONE 5min = 4 cents
# TODO food is not being taken into account yet. shells are taken weirdly into account
# TODO for now skipping items you can only buy with money

"""for crafting recipe - read crafting.JSON, split reward at, remove ones where
need to know how many of what thing is used to create the item
value should represent how hard it is to obtain the item
is it worth taking note of experience? probably not, cause it's not balanced well
base item value could be bound to how often they are used in different things
should also take into account how often something can be gotten. not only timer for crafting.
should also note how many items the recipe crafts
how many energies would it take to ensure material drop

basic materials don't take into account if another material besides energy is used to obtain it"""

# energy value from previous calculations for rubies project. based on energies price in real money
# one energy is worth 4 cents, thusly the worth of item will be in cents
# 5min = 4 cents
one_energy = 4

# calculates the worth of items
gained_worth = []


def worth(item, additional_worth):
    material_amount = float(input("Gained material amount: "))
    if item in drop_rate:
        material_drop_rate = drop_rate[item]
    else:
        material_drop_rate = 1
    if material_drop_rate >= 1:
        ensured_drop = material_drop_rate
    else:
        ensured_drop = 1 / material_drop_rate
    raw_timer = float(input("Timer in min (0 if none): "))
    used_energy = float(input("Energy used: "))
    print("-----------------")
    timer = raw_timer / 1.25
    items_worth = ((ensured_drop * (used_energy * one_energy)) / material_amount) + timer + additional_worth
    with open("worth_dic.json", "w") as g:
        item_value[item] = items_worth
        json.dump(item_value, g)
    print("Items worth:", items_worth)


def additional_items():
    # needs value to add to worth of used items
    additional_total = []
    additional_amount = int(input("How many different additional items are needed?: "))
    for i in range(additional_amount):
        add_item = str(input("Additional item: "))
        add_item_amount = int(input("How many of these items are used?: "))
        for n in range(add_item_amount):
            additional_total.append(item_value[add_item])
    additional_worth = sum(float(x) for x in additional_total)
    worth(item, additional_worth)


item = str(input("Item you want to calculate worth for: "))
if item in item_value:
    print("Items worth:", item_value[item])
else:
    needs_others = str(input("Are additional items needed? Y/N: "))
    if needs_others == "Y":
        additional_items()
    else:
        worth(item, 0)
