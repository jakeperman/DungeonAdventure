import random
weapon = "weapon"
consumable = "consumable"
junk = "junk"
material = "material"
any_item = "any"
hostile = "hostile"
passive = "passive"


class Loot:
    def __init__(self):
        self.room = ""
        self.loot = []
        self.item = []
        self.one = None

    # add randomly generated loot to a room
    @staticmethod
    def generate(count, tier, loot_pool, prob=None):
        nums = [0, 1, 2, 3]
        rooms_loot = []
        # if item generation is set to any, run random generation
        while count > 0:
            count -= 1
            if prob is None:
                # different odds for each tier of loot, 0 is the worst, 3 is the highest
                # mostly junk, some consumables and materials, no weapons
                if tier == 0:
                    index = random.choices(nums, weights=[2, 2, 6, 0], k=1)
                    room_loot = random.choices(loot_pool[index[0]], k=1)
                # even amount of consumables, materials, and weapons, but mostly junk
                elif tier == 1:
                    index = random.choices(nums, weights=[2, 2, 5, 2], k=1)
                    room_loot = random.choices(loot_pool[index[0]], k=1)
                # even amount of all items
                elif tier == 2:
                    index = random.choices(nums, weights=[3, 3, 3, 3], k=1)
                    room_loot = random.choices(loot_pool[index[0]], k=1)
                # almost no junk, mostly weapons and materials, some consumables
                elif tier == 3:
                    index = random.choices(nums, weights=[3, 4, 1, 5], k=1)
                    room_loot = random.choices(loot_pool[index[0]], k=1)
                else:
                    print("No items generated")
                    room_loot = "none"
            else:
                index = random.choices(nums, weights=prob, k=1)
                room_loot = random.choices(loot_pool[index[0]], k=1)
            # add loot data to the room
            rooms_loot.append(room_loot[0])

        return rooms_loot

    def add(self, room, item):
        self.room = room
        # if multiple items specified, add them to list using this method
        if type(item) == list:
            self.item = item
            for x in self.item:
                self.one = self.item[self.item.index(x)]
                self.loot.append(self.one)
        else:
            self.loot.append(item)

    # list generated loot
    def list(self):
        for z in self.loot:
            print(z.name)


# Item classes
# enables creation of items with various properties dependent on item type
class Item:

    def __init__(self, name, desc=""):
        self.name = name
        self.description = desc
        self.effect = ""
        self.saturation = 0
        self.special = ""
        self.craftable = ""


# weapon subclass for combat items. has unique parameters of damage, uses, tier, and special
class Weapon(Item):
    def __init__(self, name, desc, damage, uses=-1, tier=0, special="None"):
        self.item_type = weapon
        self.damage = damage
        self.uses = uses
        if self.uses == -1:
            self.uses = 99999
        self.tier = tier
        self.special = special
        if self.uses <= 0:
            print("your item broke")
        if self.damage <=2:
            self.tier = 1
        elif 2 < self.damage <= 5:
            self.tier = 2
        elif 5 < self.damage <= 7:
            self.tier = 3
        super(Weapon, self).__init__(name, desc)


# consumables subclass for healing/special effects items. parameters of saturation and effect
class Consumable(Item):
    def __init__(self, name, desc, saturation=0, effect=-1):
        self.item_type = consumable
        self.saturation = saturation
        self.effect = effect
        self.damage = 0
        super(Consumable, self).__init__(name, desc)


# Junk subclass, most items in this class are useless. some do damage
class Junk(Item):
    def __init__(self, name, desc, damage=0, uses=-1):
        self.item_type = junk
        self.damage = 0
        self.uses = uses
        super(Junk, self).__init__(name, desc)


# material subclass. materials are used for crafting or other special uses
class Material(Item):
    def __init__(self, name, desc, craftable="no"):
        self.item_type = material
        self.craftable = craftable
        self.damage = 0
        super(Material, self).__init__(name, desc)


# subclass for integral items (those needed to progress through stages in the game)
class Integral(Item):
    def __init__(self, name, desc):
        self.item_type = "Integral Item"
        self.name = name
        self.description = desc
        

# function for generating the loot pool

