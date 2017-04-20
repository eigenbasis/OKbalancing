# OKmaterials.py

# from worth_dic import item_value
import json


with open("worth_dic.json", "r") as f:
    try:
        item_value = json.load(f)
    except ValueError:
        item_value = {}
# f = open("worth_dic.txt", "w")
drop_rate = {"obsidian": 0.055, "fireoil": 0.09, "thorny_twig": 0.1, "bone": 0.21, "jute_string": 0.25, "egg": 0.35,
             "wool": 0.5, "milk": 0.7, "diamond": 0.05, "citrin": 0.06, "jade": 0.08, "jasper": 0.12, "pearl": 0.12,
             "dark_magic_potion": 0.2, "small_copper_ore": 0.2, "bees_wax": 0.2, "poison": 0.3, "vulcano_rock": 0.4,
             "savannah_rock": 0.6, "aloe_blossom": 0.7, "small_iron_ore": 0.7, "savannah_grass": 0.7, "stone": 0.5,
             "clay": 0.5, "water": 0.34, "flax": 0.007, "corn": 0.02, "violet_berries": 0.03, "wood": 0.5,
             "coal": 0.03, "iron_ore": 0.07, "copper_ore": 0.08, "cactus_flower": 0.004, "limestone": 0.5,
             "earthworm": 0.17, "bug": 0.15, "green_worm": 0.1, "silk_thread": 4.0, "glass": 25.0, "pergament": 20.0,
             "gold_chain": 10.0, "green_powder": 0.5, "blue_powder": 1.0, "violet_powder": 1.5, "moon_apple": 25.0,
             "energy": 0.25, "time_eggs": 0.015, "time_wool": 0.003, "time_milk": 0.002}

# item_value = {}

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
# TODO it' s NOT loading .json RIGHT AT ALL! --> Never leave it completely empty it will fuck shit up ---> the Y continue loop is what breaks it

"""for crafting recipe - read crafting.JSON, split reward at, remove ones where
need to know how many of what thing is used to create the item
value should represent how hard it is to obtain the item
is it worth taking note of experience? probably not, cause it's not balanced well
base item value could be bound to how often they are used in different things
should also take into account how often something can be gotten. not only timer for crafting.
should also note how many items the recipe crafts
how many energies would it take to ensure material drop"""

# energy value from previous calculations for rubies project. based on energies proice in real money.
one_energy = 4

material_amount = 0
timer = 1
crafted_amount = 1
material_drop_rate = 1

# calculates the worth of items
gained_worth = []


def worth(material_amount, timer, crafted_amount, material_drop_rate):
    material_name = str(input("Used material: "))
    material_amount = float(input("Used material amount: "))
    material_drop_rate = drop_rate[material_name]
    if material_drop_rate >= 1:
        ensured_drop = material_drop_rate
    else:
        ensured_drop = 1 / material_drop_rate
    # timer in seconds doesn't work cause value too high compared to other ones. should be in hours
    # but what if it's not full hour?
    # could be in minutes
    timer = float(input("Craft timer: "))
    crafted_amount = float(input("Crafted amount: "))
    print("-----------------")
    worth_value = ((ensured_drop * one_energy) * material_amount * timer) / crafted_amount
    gained_worth.append(worth_value)


def item_worth(material_amount, timer, crafted_amount, material_drop_rate, needed_material_amount, item):
    print("Enter required values for each material separately")
    print("In case of none enter 1")
    # depending on item amount call worth() for each item
    for i in range(needed_material_amount):
        worth(material_amount, timer, crafted_amount, material_drop_rate)
    items_worth = sum(float(x) for x in gained_worth)
    item_value[item] = items_worth
    with open("worth_dic.json", "w") as f:
        item_value[item] = items_worth
        json.dump(item_value, f)
    print("Items worth: ", items_worth)
    # sum worth() string to get final worth


# item_worth(material_amount, timer, crafted_amount, material_drop_rate, needed_material_amount)
cont = "Y"
while cont == "Y":
    item = str(input("Item you want to calculate worth for: "))
    if item in item_value:
        print(item_value[item])
    else:
        needed_material_amount = int(input("Needed material amount: "))
        item_worth(material_amount, timer, crafted_amount, material_drop_rate, needed_material_amount, item)
    print(item_value)
    cont = str(input("Continue? Y/N: "))
    # f.write(item_value)


# f.close()