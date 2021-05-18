'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
from old_game_files.roomgen import *
from old_game_files import loot
from old_game_files.entities import *
import os
from old_game_files.player import *
from old_game_files.loot_table import *

border = advtools.border
# room instances



# Player class


class RoomFuncs:
    def __init__(self):
        self.room = ""

    def loose_brick(self):
        if crowbar in player.inv:
            dialogue("You spot a loose stone in the wall.")
            user_input("custom", "Press q to use your crowbar and pry it loose.", "Q")
        else:
            dialogue("You spot a loose stone in the wall. You think you could pry it loose if you had some sort of prying tool")
    def locked_door(self):
        print("locked")

    # def stairwell(self):




# assign commonly used string values to variables for easy access

hostile = "hostile"
passive = "passive"
room = 0
removed = False
fight = False
last_encounter = ""
escmsg = ""
action = 0
fight_msg = ""
attackmsg = ""
# spawn player, set starting variables
# location tracking
current_room = 0
last_room = 0
first = True
playerinv = []
# sets game controls
controlkeys = ('Q', 'E')
keys = ('directional keys', 'W', 'S', 'D', 'A')
directions = ('cardinal letters/words', 'N', 'S', 'E', 'W')
controls = keys
# enable/disable developer tools
dev_mode = True
death = False
# main game loop
done = False
firstdeath = True
moves = 0
Loot = loot.Loot()


# create instance of player
player = Player(12, 12, [], 0, stairwell)
# add all items to loot pool
item_types = ["consumable", "material", "junk", "weapon"]

# transformations. some consumables allow you to transform



# TODO: Add Crafting

# Combat System
def enemy():
    global done
    global fight
    global last_encounter
    global escmsg
    global action
    global fight_msg
    global attackmsg
    global moves
    moves = 0
    last_item = ""
    last_move = 0
    mob = random.choice(monsters)
    fight = True
    # if the player successfully runs from a monster, only to encounter it again immediately after, run this statement
    if last_encounter == mob and last_move == 2 or last_move == 1:
        border(45)
        print(color.red + f"{last_encounter.name + color.yellow} has followed you to the {color.blue + room_list[current_room][0] + color.yellow}. You may have escaped their clutches before, "
              f"but will you be so lucky again?")
        border(45)
    # if the user kills a monster but encounters it again, run this statement
    elif last_encounter == mob and last_move == 1:
        border(45)
        print(color.red + f"{last_encounter.name + color.yellow} has risen from the dead! Now even stronger, and with a thirst for vengeance!")
        border(45)
    # run the normal message if not a special encounter
    else:
        if mob.description[0] == mob.name[0]:
            x = 1
        else:
            x = 2
        border(len(mob.description), color.red)
        dialogue(mob.description[0:mob.description.index(mob.name[0])], newln=False, col=color.bold + color.yellow,slp=0.03)
        dialogue(mob.description[mob.description.index(mob.name[0]):len(mob.name)+x], newln=False, col=color.red,slp=0.03)
        dialogue(mob.description[len(mob.name)+x:], col= color.yellow + color.bold, slp=0.03)
        border(len(mob.description), color.red)
    # continue the fighting loop until fight is set to false. either by the monster defeating you, it being defeated
    while fight is True:
        # give user 3 actions to take upon encountering monster
        opt = ['F', 'R', 'C', 'L']
        act = user_input("custom", "What will you do? [F]ight [R]un [C]hat [L]ast Action", opt)
        actions = [1, 2, 3, 4]
        action = actions[opt.index(act)]
        # first action is to fight, user can choose eligible item from inventory to attack with
        if action == 1 or action == 4 and last_move == 1:
            if player.inv:
                # choice = int(user_input("custom", "Select an item to use in battle!", range(0, len(playerinv)+1)))
                if action == 4 and last_item != "":
                    if last_item in player.inv:
                        item = last_item
                    else:
                        dialogue(f"You don't have the {last_item} anymore!", col=color.red)
                else:
                    item, act = open_inv()
                    last_item = item
                # some weapons can kill a mob in one hit
                attackmsg = color.yellow + f"You attacked the {color.reset + color.bright_red + mob.name + color.reset + color.yellow} with your {color.blue + color.bold + item.name + color.reset}"
                border(attackmsg, color.yellow + color.bold)
                if act == 'u':
                    print(attackmsg)
                elif act == 'c':
                    print(color.yellow + f"You consumed your {color.blue + item.name}")
                elif act == 't':
                    print(color.yellow + f"You threw your {color.blue + item.name + color.yellow} at {color.red + mob.name}")
                border(attackmsg, color.red)
                time.sleep(.25)
                if item.damage >= mob.maxhp:
                    print(color.yellow + f"You beat {color.bright_red + mob.name}!")
                    if isinstance(item, Weapon):
                        item.uses -= 1
                    print(color.red + f"{item.uses}{color.yellow} uses left on your {color.blue + color.bold + item.name}")
                    fight = False
                # if the player still has health, damage the monster
                else:
                    # take durability off of item if applicable
                    if isinstance(item, Weapon):
                        item.uses -= 1
                    mob.hp -= item.damage
                    # inform the player of the damage dealt
                    print(color.yellow + f"You did {mob_dmg(item.damage)} damage" + color.reset)
                    print(color.yellow + f"{mob.name} hp is {color.bright_red}{mob_health(mob)}" + color.reset)
                    # monster dies if hp drops below 0
                    if mob.hp <= 0:
                        print(color.yellow + f"You beat {mob.name}. Well done!")
                        fight = False
                    else:
                        last_encounter = mob
                        player.damage(random.randint(mob.damage-1, mob.damage+1))
                        if player.hp == player.maxhp:
                            border(attackmsg, color.red)
                            break
                    if isinstance(item, Weapon) and item.uses <= 0:
                        print(color.yellow + f"Your {color.bright_blue + item.name + color.reset + color.yellow} broke!")
                        player.inv.remove(item)
                    border(attackmsg, color.reset + color.red)
            else:
                print(color.red + "Theres nothing in your inventory!")
                continue
            last_move = 1
        # second combat option is to run
        elif action == 2:
            while True:
                # a pre-determined correct direction is generated. This cannot be a null direction, only one which the player can travel
                r = random.choice(player.room.rooms)
                if r is None:
                    continue
                else:
                    x = player.room.rooms.index(r) + 1
                    break
            print(f"direction is {controls[x]}")
            # ask user which direcion they will run from the monster
            direction = user_input("custom", f"Which way will you run?", controls[1:5])
            # if the player correctly guesses the direction, they escape
            if controls.index(direction) == x:
                print(color.yellow + f"You successfully escaped {color.red + color.bold + mob.name}!")
                fight = False
                travel(direction)
            # if the player guesses incorrectly, they die.
            else:
                if player.room.rooms[controls.index(direction)-1] is None:
                    escmsg = color.yellow + f"You tried to escape, but you ran into a wall!"
                else:
                    escmsg = color.yellow + f"You tried to escape but {color.bright_red + mob.name + color.reset + color.yellow} was too fast!"
                border(escmsg, color.red)
                print(escmsg)
                print(color.bright_red + f"{mob.name + color.reset + color.yellow} attacks you.")
                last_encounter = mob
                player.damage(mob.damage)
            last_move = 2
        # the third option is to sit down in front of the monster. In some cases this will provide success over other alternatives
        elif action == 3:
            talk = input("What would you like to talk about?")
            isdead = random.randint(0,4)
            last_encounter = mob
            if isdead == 1:
                dialogue(f"{mob.name} enjoys talking about {talk}! You chat for a few minutes, then you are free to pass.", col=color.yellow)
                fight = False
            else:
                dialogue(f"{mob.name} hates talking about {talk}! {color.red + mob.name} is angry that they sacrifice their life to ensure your death.",col=color.yellow)
                dialogue(f"{mob.name} attacks you with the force of a thousand men.", col=color.yellow)
                kill()
            last_move = 3
        else:
            continue
    # tracks the last monster encountered and how it was defeated
def explore():
    player.room.func()
    pass
    

# Player control functions

# opens payer inventory
def open_inv():
    if player.inv:
        print(color.bright_yellow + "Your satchel contains:" + color.reset)
    else:
        print(color.bright_yellow + "You have no items.")
        return
    i = 1
    # print the name of each item instance with a number in front of each for organization and selection
    border(45)
    for z in player.inv:
        if isinstance(z, Weapon):
            print(color.blue + f"{color.yellow}{i}) {color.blue + z.name} {color.white}[{z.item_type}] {color.green}[uses: {z.uses}] [tier: {z.tier}]")
        else:
            print(color.blue + f"{color.yellow}{i}) {color.blue + z.name} {color.white}[{z.item_type}]")
        i += 1
    border(45)
    if first:
        return
    
    it = user_input("custom", color.bright_yellow + "Enter an item number to select it (Or enter '0' for none)", [x for x in range(0, i+1)])
    if it == 0:
        return
    item = player.inv[int(it)-1]
    print(color.yellow + f"{item.name} selected")
    if isinstance(item, Weapon):
        return item, 'u'
    
    select = user_input("custom","Would you like to [U]se, [C]onsume, or [T]hrow?", ['U', 'C', 'T', 'Q'])
    if select == 'U':
        action = 'u'
        if not fight:
            print("You cant use that right now.")
    elif select == 'C':
        action = 'c'
        if not fight:
            print(color.green + f"You consumed your {item.name}")
            player.consume(item)
    elif select == 'T':
        action = "t"
        if not fight:
            print(f"You threw your {item.name}")
        player.inv.remove(item)
    else:
        action = None
    return item, action
        



# def obstacle():
#




# function allow player to use an item, for example a material or consumable
def use():
    print("item used")


# moves player based on directional input
def travel(direction):
    global current_room
    global last_room
    global moves
    global room
    d = None
    true = False
    # move the player in the specified direction, or inform them to select a valid direction if one is not provided
    while d is None and true is False:
        if direction in controls:
            d = controls.index(direction.upper())
            if d is None:
                print(color.bright_red + "Invalid direction")
                break
            next_room = player.room.rooms[d-1]
            # if the direction selected yields an available room, move the player and inform them of it.
            if next_room is not None:
                player.lastpos = player.pos
                player.last_room = rooms[player.lastpos]
                player.pos = next_room
                player.room = rooms[player.pos]
                room = player.room
                loc()
                moves += 1
                
                if shoes in player.inv:
                    # if player has shoes, less likely to encounter monster
                    if random.randint(0,3) == 1:
                        enemy()
                elif moves > 3:
                    print(color.magenta + "You're making a lot of noise. Be more careful...")
                    if random.randint(0, 1) == 1:
                        enemy()
                # 33% chance that a monster will spawn on any given move, other than the first move
                else:
                    if random.randint(0, 2) == 1 and first is not True:
                        enemy()
            # inform the user the direction they selected is not valid
            else:
                dialogue("You cant go that direction.", col=color.bold_red, slp=0.01)
        elif direction in room.rooms:
            player.lastpos = player.pos
            player.last_room = rooms[player.lastpos]
            player.pos = direction
            player.room = rooms[player.pos]
            loc()
        else:
            dialogue("You cant go that direction.", slp=0.01, col=color.bold_red)

def kill():
    def pause():
        time.sleep(1.5)
    global death
    global firstdeath
    global done
    global fight
    global fight_msg
    global attackmsg
    border(attackmsg, color.reset + color.red)
    if death:
        print(color.bright_red + "You died.")
        done = True
    else:
        if firstdeath:
            pause()
            dialogue("That's strange... You're back in the grungy stairwell")
            pause()
            dialogue(f"Last you remember you were being struck down by", newln=False)
            dialogue(f" {last_encounter.name}", col=color.red)
            pause()
            dialogue("You notice your items are gone. Your head is pounding.")
            firstdeath = False
            fight = False

        else:
            dialogue("You died.", col=color.red)
            dialogue("You have been returned to the grungy stairwell", col=color.red)
            dialogue(f"Your items were dropped in the {player.last_room.name}", col=color.red)
        player.room.add_loot(player.inv)
        for k in range(len(player.inv)):
            player.inv.pop()
        
            
        player.hp = player.maxhp
        player.stamina = 12
        player.pos = 0
        player.lastpos = player.pos
        player.room = rooms[0]
        player.last_room = player.room





# Configures settings
def settings():
    global controls
    # change control scheme used by the game to control the player.
    while controls is None:
        cont = input(f"Would you like to use: [D]irectional Keys (W,A,S,D) or [C]ardinal Directions (N,S,E,W)?")
        if cont.lower() == "d":
            controls = keys
        elif cont.lower() == "c":
            controls = directions
        else:
            print(color.bright_red + "invalid selection.")

    # inform player of selected control scheme
    print(color.bright_white + f"Movement Controls: {color.bright_cyan + str(controls[1:])}")   
    print(color.bright_white + f"Interact/Collect Item: {color.bright_cyan}'Q'")
    print(color.bright_white+ f"Open Inventory:{color.bright_cyan} 'E'")
    print(color.bright_cyan + color.bold + "Type 'h' for help at any time")


# Prints location of player
def loc():
    dialogue("You are in the ", col=color.yellow, newln=False, slp= 0.02)
    dialogue(player.room.name, col=color.bright_blue, slp=0.02)


# Takes various forms of user input. designed as a more flexible, specialized form of the default input() as needed for the game
def user_input(userinput="none", prompt="default", options=()):
    inp = None
    while inp is None:
        try:
            # if no parameter is specified when the function is called, ask the user to input a command.
            if userinput == "none":
                cmd = input(color.white + color.bold + "Please enter a command:" + color.reset)
                # if movement key is selected, then move player
                if cmd.upper()[0] in controls[1:5]:
                    inp = cmd[0].upper()
                    travel(inp)
                # e to open player inventory
                elif cmd.upper()[0] == "E":
                    open_inv()
                # v enables developer mode, with in game commands
                # if user presses q, search the room for loot
                elif cmd.upper()[0] == "Q":
                    player.search()
                elif cmd.upper()[0] == "H":
                    print(color.bright_white + f"Movement: {color.bright_cyan + str(controls[1:])}")   
                    print(color.bright_white + f"Interact/Collect Item: {color.bright_cyan}'Q'")
                    print(color.bright_white+ f"Open Inventory:{color.bright_cyan} 'E'")
                # first character of any dev command
                # print invalid command if key pressed is not within control scheme, and inform player of valid commands
                else:
                    print(color.red + f"Invalid Command.{color.bright_yellow}\nValid Commands:\n{controls[1:] + controlkeys}")
                    continue
            # if direction is specified as function input type upon being called, automatically run the direction travel function
            elif userinput == "direction":
                if prompt == "default":
                    prompt = "Please input a direction:"
                direct = input(color.bright_white + prompt.upper() + color.reset)
                inp = direct[0]

            # most useful part of user_input function. allows for custom prompts and limits allowed user input to specified keys
            # allows for customized input, best used to handle mis-pressed keys on custom inputs
            elif userinput == "custom" and options != "default" and prompt != "default":
                # can check if the program should be looking for integer input or char input. avoids many errors
                if isinstance(options[0], int):
                    # try/except block handles errors in the event of mispressed key
                    try:
                        cmd = int(input(color.bright_magenta + color.bold + prompt + color.reset))
                        if cmd in options:
                            return cmd
                        else:
                            print(color.bright_red + "Invalid input.")
                    except ValueError:
                        print(color.bright_red + 'Please enter a number.')
                        continue
                else:
                    cmd = input(color.bright_magenta + color.bold + prompt + color.reset).upper()
                    if cmd in options:
                        inp = cmd
                    else:
                        print(color.bright_red + "Invalid input.")
                        continue

            else:
                print(color.bright_red + "Invalid Command")
                continue
        except IndexError:
            print("index error")
            print(color.bright_red + "Invalid Command")
            continue
        # the function returns the user input as a value usable as required by a function or otherwise
        return inp
    


def main():
    global first
    for each in rooms[1:]:
        loot_tier = random.choices([0, 1, 2, 3], weights=[5, 4, 3, 1.5], k=1)[0]
        loot = Loot.generate(3, loot_tier, loot_pool)
        each.add_loot(loot)
    # creates starting item in the entry room
    stairwell.add_loot(eyepatch)
    spec_rooms = random.choices(rooms, k=4)
    for i, each in enumerate(integrals):
        spec_rooms[i].add_loot(each)
    if os.path.isfile('player.txt'):
        load_bar("Loading save...", .01, 100)
        print(color.bright_green + color.bold + "Welcome Back!")
        resume = True 
        first = False
    else:
        open('player.txt', 'w').close() 
        print(color.bright_green + "New save file created!")
        load_bar("Generating world...", .01, 100)
        resume = False
    if not resume:    
        #print("You wake up in a room", end='')
#        time.sleep(2)
#        print(color.yellow + ", its dark.")
#        time.sleep(2)
#        print(color.yellow + f"Cold.")
#        time.sleep(1)
#        print(color.yellow + f"Afraid.")
#        time.sleep(1)
#        print(color.yellow + f"And Alone...")
#        time.sleep(1)
#        dialogue(color.yellow + f"You stand up, your legs shaking")
#        time.sleep(1)
        input(f"Press {color.red + controls[1] + color.yellow} to take a step")
        dialogue("You feel a small object press against your bare foot as you shakily take a step.")
        user_input("custom", " Press 'q' to pick it up.", 'Q')
        player.collect(flint)
        print(color.magenta + "*you place it in your satchel*")
        time.sleep(1)
        user_input("custom", "Press 'e' to open your satchel", 'E')
        open_inv()
        user_input("custom", f"Press 1 to select your {flint.name}", '1')
        speak = f"You take out your {flint.name} and strike it. "
        dialogue(speak)
        time.sleep(2)
        dialogue(f"The room bursts into view for a split second as the sparks illuminate it")
        dialogue(f"You spot a locked trap door on the floor. You take note.")
        time.sleep(2.5)
        dialogue("then darkness again... as the flame sputters out ")
        time.sleep(1.5)
        dialogue("If only you had something to light on fire...")
        first = False
        user_input()
        dialogue("This whole place looks abandonded...")
    while done is False:

        # runs each time the game loops, primary point of interaction
        user_input()

    # if the player dies and the loop breaks, the game ends.
    print("Game Over.")


if __name__ == "__main__":
    main()


