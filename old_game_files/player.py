from old_game_files.advtools import *


class Player:
    def __init__(self, player_health, stamina, inv=[], pos=0, room_start=None):
        self.hp = player_health
        self.maxhp = 20
        self.stamina = stamina
        self.inv = inv
        self.pos = 0
        self.room = room_start
        self.lastpos = None
        self.msgs = []
        self.inv_size = 5
        
    def damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            fight = False
            kill()
        else:
            amount = ""
            if damage <= 2:
                amount = color.green + color.bold + "a little"
            elif 2 < damage <= 4:
                amount = color.bright_red + "some"
            elif damage >= 5:
                amount = color.red + color.bold + "a lot" + color.reset + color.yellow + " of"
            print(color.yellow + f"You took {amount + color.reset + color.yellow} damage!")
            print(color.yellow + f"Your health is {self.player_health()}")
            # print(color.yellow + f"Your hp is: {color.bright_red}{self.hp}")

    def heal(self, regen):
        if self.hp == self.maxhp:
            print(color.yellow + "You are already at maximum health!")
            healed = False
        else:
            self.hp += regen
            print("You regenerated some health.")
            healed = True
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        return healed

    # searches the room for loot
    def search(self):
        # self.must have available energy to search for loot
        search_bar(2, 0.05)
        print()
        if len(self.room.loot) > 0:
            s = random.choice(self.room.loot)
            self.collect(s)
            self.stamina -= 1
        # if no items remain, print this message
        else:
            dialogue("You found all the items in this room!", col=color.yellow, slp=0.025)

    def collect(self, item):
        self.inv.append(item)
        vowels = ['a', 'e', 'i', 'o', 'u']
        variants = ["picked up", "found", "discovered", "stumbled upon"]
        variant = random.choice(variants)
        if item.name[0].lower() in vowels:
            dialogue(f"You {variant} an ",col=color.yellow, newln=False, slp=0.025)
        else:
           dialogue(f"You {variant} a ",col=color.yellow, newln=False,slp=0.025) 
        dialogue(item.name, col=color.bold_blue, newln=False,slp=0.025)
        dialogue("! " + item.description, col=color.yellow,slp=0.03)
        if item in self.room.loot:
            self.room.del_loot(item)
        # print(random.choice(self.msgs))

    # called when a self.consumes an item
    def consume(self, item):
        effect = item.effect
        if effect == 0:
            regen = random.randint(3, 5)
            self.heal(regen)
            if self.hp is not self.maxhp:
                self.inv.remove(item)
        elif effect == 1:
            print("you aight")
            self.damage(random.randint(1,4))
            self.inv.remove(item)
        elif effect == 2:
            anim = random.choice(shapes)
            print("Thought you'd get out of here that easily, huh?")
            print(f"You turned into a {anim}")
            self.inv.remove(item)
        else:
            print(color.bright_red + "You cant eat that.")

    def throw(self, item):
        pass
    def player_health(self):
        if self.hp/self.maxhp > .70:
            return color.green + "High"
        elif self.hp/self.maxhp > .30:
            return color.bright_yellow + "Low"
        elif self.hp/self.maxhp:
            return color.red + "Critical"
        
shapes = ["Feral Rabbit", "Decrepid Racoon", "Flea Infested Squirrel", "Jumbotron", "Large sewer rat",
          "French Baguette", "Piece of Sidewalk Chalk", "Headless Pigeon", "Piece of Sandpaper"]


