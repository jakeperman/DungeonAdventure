import loot
import advtools
tools = loot.Loot()
weapon = "weapon"
consumable = "consumable"
junk = "junk"
material = "material"
any_item = "any"
# Dev Tools
# probability simulation for various events
def probsim(tier, runs, ipr=1):
    junkcount = 0
    weaponcount = 0
    materialcount = 0
    consumablecount = 0
    
     # generate simulated loot for testing purposes
    for x in range(0, runs):
        loot = tools.gen_loot(ipr, tier, any_item)
        for i in range(0, len(loot)):
            if loot[i].item_type == junk:
                junkcount += 1
            elif loot[i].item_type == weapon:
                weaponcount += 1
            elif loot[i].item_type == material:
                materialcount += 1
            elif loot[i].item_type == consumable:
                consumablecount += 1
     # print total count of each item and what percentage of the simulated loot pool it was
    print(f"Junk: {junkcount} items. {(junkcount/runs)*100}%\n weapons: {weaponcount} items. {(weaponcount/runs)*100}%\n "
           f"consumable: {consumablecount} items {(consumablecount/runs)*100}%\n material: {materialcount} items. {(materialcount/runs)*100}%")



 # dev commands menu
def dev(inp, player, rooms):
    global removed
    if inp == "/list":
        for rooms in room_list:
            print(f"\n{room_list[room_list.index(rooms)][0].upper()}:")
            for those in room_list[room_list.index(        rooms)][5]:
                print(those.name)
    elif inp == "/sim":
        sim = inp.split("m ")
     # kind = input("\n1) tier sim\n 2) loot sim\n 3) tier + loot sim")
        if sim == "tier":
            for i in range(0, 14):
                tier = random.choices([0, 1, 2, 3], weights=[5, 4, 3, 1.5], k=1)[0]
                print(tier)
        elif sim == "loot":
            # run auto-sim
            a = input("Run Auto Sim? [y/n]")
            if a.upper() == "Y":
                print("\ntier 0")
                probsim(0, 100)
                print("\ntier 1")
                probsim(1, 100)
                print("\ntier 2")
                probsim(2, 100)
                print("\ntier 3")
                probsim(3, 100)
         # run sim with customized parameters
            elif a.upper() == "N":
                t = input("What tier loot?")
                r = input("How many runs?")
                i = input("How many items per run?")
                probsim(t, r, i)
        else:
         # generate a theoretical loot pool based on default probability
            for them in room_list:
                thetier = random.choices([0, 1, 2, 3], weights=[5, 4, 3, 1.5], k=1)[0]
                test = []
                it = gen_loot(3, thetier, any_item)
                test.append(it)
         # clear the loot pool, deleting item instances from all froms
    elif inp == "/clear":
        for rooms in room_list:
            print(f"Clearing rooms... {round((room_list.index(rooms)/len(room_list))*100)}%")
            removal = rooms[5]
            room_list[room_list.index(rooms)].remove(removal)
             # for loots in range(0, len(rooms[5])):
             # room_list[room_list.index(rooms)][5]
            print("Done!")
            removed = True
     # re-generate the loot pool, only works if the /clear command is run first
    elif inp == "/gen" and removed is True:
        for that in room_list:
            roomm = int(room_list.index(that))
            loottier = random.choices([0, 1, 2, 3], weights=[5, 4, 3, 1.5], k=1)[0]
            Loot(roomm).add(gen_loot(3, loottier, any_item))
            print("done")
     # clears the loot pool and regenerates it with one command
    elif inp == "/reset":
        print("Clearing rooms...")
        for rooms in room_list:
            # print(f"Clearing rooms... {round((room_list.index(rooms)/len(room_list))*100)}%")
            removal = rooms[5]
            room_list[room_list.index(rooms)].remove(removal)
            print("Regenerating Loot...")
            for that in room_list:
                roomm = int(room_list.index(that))
                loottier = random.choices([0, 1, 2, 3], weights=[5, 4, 3, 1.5], k=1)[0]
                Loot(roomm).add(gen_loot(3, loottier, any_item))
            print("Done.")
     # spawn an item into the players inventory
    elif inp == "/give":
        print("here you go!")
    # spawn a monster to fight
    elif inp == "/spawn":
        print("mob spawned!")
    # teleport to a specific room
    elif inp == "/tp":
        print("teleported to room!")
    elif inp == "/stats":
        print(f"hp is: {player.hp}")