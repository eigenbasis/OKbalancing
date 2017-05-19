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
             "iron_ore": 0.67, "doubloon_gold": 0.037, "doubloon_silver": 0.296, "doubloon_bronze": 0.667,
             "small_fish": 0.5, "sea_shell": 0.15, "pearl": 0.12, "salmon": 0.1, "boot": 0.07, "striped_angelfish": 0.05,
             "shark_mini": 0.26, "royal_violet": 0.05, "old_key_shark": 0.04,
             "sea_cabbage": 0.2, "gold_fish": 0.05, "blue_guppy": 0.1,
             "jellyfish": 0.15, "royal_crab": 0.1, "octopus": 0.06, "doubloon_silver_octopus": 0.05,
             "shark_hammerhead": 0.07, "clownfish": 0.2, "lion_fish": 0.1, "blossom_aloe": 0.7, "blossom_curcuma": 0.7,
             "bees_wax": 0.3, "poison": 0.3,
             "col_butterfly_tricolor": 0.07, "col_butterfly_pear": 0.06, "col_butterfly_fire": 0.07, "col_butterfly_romantic": 0.05,
             "col_butterfly_pink": 0.08, "col_butterfly_blue": 0.08, "col_butterfly_green": 0.07, "col_butterfly_big": 0.06,
             "col_seashell_amber": 0.06, "col_seashell_horn": 0.07, "col_seashell_ pink": 0.06, "col_seashell_star": 0.06,
             "col_seashell_royal": 0.06, "col_seashell_moon": 0.05, "col_seashell_arch": 0.06, "col_seashell_mist": 0.08,
             "col_rock_lapis": 0.06, "col_rock_diorite": 0.08, "col_rock_sphalerite": 0.05, "col_rock_quartz": 0.05,
             "col_rock_sandstone": 0.05, "col_rock_travertine": 0.06, "col_rock_granite": 0.06, "col_rock_serpentine": 0.06,
             "col_feather_thrush": 0.07, "col_feather_eagle": 0.06, "col_feather_parrot": 0.05, "col_feather_pheasant": 0.05,
             "col_feather_hoopoe": 0.06, "col_feather_jay": 0.07, "col_feather_woodpecker": 0.06, "col_feather_crow": 0.07,
             "col_object_spoon": 0.07, "col_object_comb": 0.06, "col_object_sickle": 0.08, "col_object_urn": 0.06,
             "col_object_slingshot": 0.08, "col_object_doll": 0.07, "col_object_wheel": 0.08, "col_object_shaker": 0.07,
             "col_bug_twig": 0.05, "col_bug_grasshopper": 0.07, "col_bug_dragonfly": 0.07, "col_bug_spider": 0.05,
             "col_bug_beetle": 0.06, "col_bug_centipede": 0.07, "col_bug_bumblebee": 0.1, "col_bug_ladybug": 0.09,
             "col_flower_lilly": 0.09, "col_flower_iris": 0.07, "col_flower_calla": 0.06, "col_flower_freesia": 0.06,
             "col_flower_sunflower": 0.07, "col_flower_pansy": 0.06, "col_flower_gerbera": 0.06, "col_flower_strelitzia": 0.2,
             "col_nature_cone": 0.08, "col_nature_nut": 0.08, "col_nature_moss": 0.07, "col_nature_lichen": 0.09,
             "col_nature_bark": 0.15, "col_nature_seeds": 0.1, "col_nature_sorb": 0.09, "col_nature_champignons": 0.12,
             "col_animal_egg": 0.09, "col_animal_fishbone": 0.1, "col_animal_choral": 0.2, "col_animal_shell": 0.25,
             "col_animal_wool": 0.1, "col_animal_horn": 0.09, "col_animal_tooth": 0.15, "col_animal_fossil": 0.2,
             "col_travel_map": 0.09, "col_travel_compass": 0.06, "col_travel_boots": 0.09, "col_travel_sleepingbag": 0.4,
             "col_travel_lighter": 0.06, "col_travel_waterbottle": 0.08, "col_travel_hat": 0.08, "col_travel_medpack": 0.05,
             "col_mask_carnival": 0.04, "col_mask_cannibal": 0.07, "col_mask_game": 0.06, "col_mask_wood": 0.127,
             "col_mask_decorative":0.15 , "col_mask_flower": 0.07, "col_mask_smiling": 0.06, "col_mask_harvest": 0.09}

# TODO what if the used materials are crafted not found
# Use 1 / materials value
# TODO what if material takes timer not drop_rate, like corn or violet berries
# for plants: drop_rate == 1 and main factor is time it takes to ripen
# TODO this kinda breaks because of grapes and truffles
# for animals: TODO include HP
# TODO what if energy is needed to craft. one energy ensured_drop == one_energy (should be)
# energy drop_rate is 0.25 and is included in description
# TODO pure drop_rate can not be items value because of ensured_drop problem
# solved by applied worth() to basic materials as well
# TODO base always mining stuff on energy use
# done for stone and clay
# TODO wood stuff. could be similar to clay and stone
# is similar to clay and stone. is EXACTLY like clay and stone
# TODO items not crafted OR dropped, like klits sulas un garsvielas
# TODO make so can enter items name and script will pull value from drop_rates.py
# replaced that with dictionary and made input work
# TODO for drop rates could take into account mine timer, like for water
# DONE mines takes the unupgraded version
# TODO crafted amount and timer could be out side of the loop, somehow
# DONE
# TODO add coconuts and collection items
# TODO what about items that are not materials?
# TODO what to do with materials you can only buy?
# 1 ruby = 25 shells
# 1 ruby drop_rate = 2.5
# 1 shell drop_rate = 0.1
# TODO if drop_rate > 1
# if > 1 takes drop_rate as ensured_dorp
# TODO items that ask for other crafted items
# seperate scripts for base and crafted materials
# TODO make so need to write in material want to check and it spits out worth
# DONE asks for material and checks if it's in item_value dic
# TODO make so appends item_value with calculated items worth
# DONE as part of worth_dic.json
# TODO make it so item_value is writen to a file so can be saved outside of loop
# DONE saves in worth_dic.json and new script reads that and assigns to item_value which is a dic
# TODO what to do with items that take time?
# DONE 5min = 4 cents
# TODO food is not being taken into account yet
# DONE food = 36.0
# TODO items you can only buy with money
# DONE 1 shell = 0.6
# TODO fishes, don't forget that uses worms and stuff, but also has drop_rate
# DONE
# TODO drops form plants in theory use those plants to gain
# TODO redo things with flax and corn and berries_violet un straw_bundle
# DONE
# TODO animals, based on shell_gain?
# TODO materials you get form animals (for egg chicken is additional item)
# additional items: animal and what you feed with and timer how long grown takes to get hungry
# TODO fishing stuff
# DONE
# TODO collection stuff
# TODO value of recipe dish as an item
# TODO dekori
# TODO stuff you buy only with rubies
# TODO things that need to be built

"""for crafting recipe - read crafting.JSON, split reward at, remove ones where
need to know how many of what thing is used to create the item
value should represent how hard it is to obtain the item
is it worth taking note of experience? probably not, cause it's not balanced well
base item value could be bound to how often they are used in different things
should also take into account how often something can be gotten. not only timer for crafting.
should also note how many items the recipe crafts
how many energies would it take to ensure material drop

basic materials don't take into account if another material besides energy is used to obtain it

1 energy costs 0.4 cents has base value 4
1 ruby costs 4 cents has base value 40

ruby price in store can't be used to calculate worth's cause it's highly unbalanced
need to use price in shells instead

shell value calculated based on 4 base animals - chicken, pig, sheep, cow
average from shells gained for 1 energy spent
food is not taken into account because food and shells are intertwined values
average per energy spent ends up at 6.6125
rounding down to 6 to at least somewhat account for food
1 energy == 6 shells
1 shell == 0.6

when calculating for plants their cost in shells is not used, cause would take changing code and probably
does not effect the value much, because shells are considerably worthless
for plant tress energy used is 1 instead of 2 like for plantation plants
"""

# energy value from previous calculations for rubies project. based on energies price in real money
# one energy is worth 4 cents, thusly the worth of item will be in cents
# 5min = 4 cents
one_energy = 4.0
one_ruby = 40.0
one_shell = 0.6
one_food = 36.0

# calculates the worth of items
gained_worth = []


def worth(item, additional_worth):
    # worth for basic base materials
    print("-----------------")
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
    items_worth = ((ensured_drop * (used_energy * one_energy) + timer) / material_amount) + additional_worth
    with open("worth_dic.json", "w") as g:
        item_value[item] = items_worth
        json.dump(item_value, g)
    print("Items worth:", items_worth)


def additional_items():
    # additional function to worth() if additional items are needed
    # mainly used for mines
    additional_total = []
    additional_amount = int(input("How many different additional items are needed?: "))
    for i in range(additional_amount):
        print("-----------------")
        add_item = str(input("Additional item: "))
        add_item_amount = int(input("How many of these items are used?: "))
        for n in range(add_item_amount):
            additional_total.append(item_value[add_item])
    additional_worth = sum(float(x) for x in additional_total)
    worth(item, additional_worth)


def animals(item):
    # function to calculate worth of animals
    feditem_total = []
    raw_timer = float(input("Timer in min (0 if none): "))
    timer = raw_timer / 1.25
    hp = float(input("Animals HP: "))
    raw_currency = str(input("What do you pay with: "))
    currency = item_value[raw_currency]
    currency_amount = float(input("How much of this currency is paid: "))
    feditem_amount = int(input("How many different items you feed animal with: "))
    for i in range(feditem_amount):
        print("-----------------")
        food_item = str(input("Fed item: "))
        food_item_amount = int(input("How many of these items are used?: "))
        for n in range(food_item_amount):
            feditem_total.append(item_value[food_item])
    fedfood_worth = sum(float(x) for x in feditem_total)
    items_worth = ((one_energy + fedfood_worth + timer) * hp) + (currency * currency_amount)
    with open("worth_dic.json", "w") as g:
        item_value[item] = items_worth
        json.dump(item_value, g)
    print("Items worth:", items_worth)


def plants(item):
    # function to calculate worth of plants
    raw_timer = float(input("Timer in min (0 if none): "))
    timer = raw_timer / 1.25
    material_amount = float(input("Gained amount: "))
    currency_total = []
    dif_currencies = int(input("How many different currencies are used: "))
    for i in range(dif_currencies):
        print("-----------------")
        currency = str(input("What do you pay with: "))
        currency_amount = int(input("How much of this currency is paid: "))
        for n in range(currency_amount):
            currency_total.append(item_value[currency])
    items_worth = (((one_energy * 2) + timer + sum(float(x) for x in currency_total)) / material_amount)
    with open("worth_dic.json", "w") as g:
        item_value[item] = items_worth
        json.dump(item_value, g)
    print("Items worth:", items_worth)


def decor(item):
    # function to calculate worth of animals
    decoritem_total = []
    print("-----------------")
    raw_currency = str(input("What do you pay with: "))
    currency = item_value[raw_currency]
    currency_amount = float(input("How much of this currency is paid: "))
    print("-----------------")
    hp = float(input("Decors HP: "))
    finish_price = []
    print("-----------------")
    builtitem_amount = int(input("How many different items build with: "))
    for i in range(builtitem_amount):
        print("-----------------")
        food_item = str(input("Build item: "))
        food_item_amount = int(input("How many of these items are used?: "))
        for j in range(food_item_amount):
            decoritem_total.append(item_value[food_item])
    print("-----------------")
    finishitem_amount = int(input("How many different items are needed to finish building: "))
    for n in range(finishitem_amount):
        print("-----------------")
        needed_item = str(input("Item needed to finish: "))
        needed_item_amount = int(input("How many of these items are used?: "))
        for m in range(needed_item_amount):
            finish_price.append(item_value[needed_item])
    useditem_worth = sum(float(x) for x in decoritem_total)
    finsih_worth = sum(float(x) for x in finish_price)
    items_worth = ((one_energy * hp) + useditem_worth) + (currency * currency_amount) + finsih_worth
    with open("worth_dic.json", "w") as g:
        item_value[item] = items_worth
        json.dump(item_value, g)
    print("Items worth:", items_worth)

item = str(input("Item you want to calculate worth for: "))
if item in item_value:
    print("Items worth:", item_value[item])
else:
    is_plant = str(input("Is the item a plant? Y/N: "))
    if is_plant == "Y" or is_plant == "y":
        plants(item)
    else:
        is_animal = str(input("Is the item an animal? Y/N: "))
        if is_animal == "Y" or is_animal == "y":
            animals(item)
        else:
            is_decor = str(input("Is the item a decor that needs building? Y/N: "))
            if is_decor == "Y" or is_decor == "y":
                decor(item)
            else:
                needs_others = str(input("Are additional items needed? Y/N: "))
                if needs_others == "Y" or needs_others == "y":
                    additional_items()
                else:
                    worth(item, 0)
