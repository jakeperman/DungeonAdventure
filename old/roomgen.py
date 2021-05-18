# room class
import random
from old import advtools
import math

color = advtools.Color()


class Room:
    def __init__(self, num, name, r_north=None, r_south=None, r_east=None, r_west=None, desc=""):
        self.num = num
        self.name = name
        self.description = desc
        self.north = r_north
        self.south = r_south
        self.east = r_east
        self.west = r_west
        self.rooms = [self.north, self.south, self.east, self.west]
        self.monsters = []
        self.loot = []
        self.first = True
        self.func = None

    def add_loot(self, item):
        # if multiple items specified, add them to list using this method   
        items = []
        if isinstance(item, list):
            for x in item:
                items.append(x)
        else:
            items.append(item)
        for those in items:
            # add each item to the loot index [5] of the room
            self.loot.append(those)

    def del_loot(self, item):
        # if multiple items specified, remove them from the list using this method
        items = []
        if isinstance(item, list):
            for x in item:
                items.append(x)
        else:
            items.append(item)
        for them in items:
            # remove each item from the loot of the room
            self.loot.remove(them)

    def spawn_mob(self, creature="any"):
        print("mob")

# loot gen


stri = """ ------------------
| hey!
|
|
|
        """
width = 34
height = math.trunc(width/2)
tops = ''.join([str(x) for x in ['-']*width])
left = ''.join([str(x+"\n") for x in ['|']*height]) + (' '*width).join([str(x+"\n") for x in ['|']*height])
right = (' '*width).join([str(x+"\n") for x in ['|']*height])
#print(tops)
#print(left)
#print(right)
#print(tops)


def room_map(room, size=34):
    spots = ['1','2','3','4']
    leng = size
    height = size * (15/34)
    loc = False
    print(color.bold + room)
    print(' ' + '-'*34)
    for i in range(height):
        if len(spots) > 0:
            if random.randint(1,5) == 2:
                loc = True
        if loc:
            rand = random.randint(0, 34)
            num = random.choice(spots)
            print('|' + ' ' * rand + str(color.bright_magenta + num  + color.reset) + ' ' * (leng-rand-1) + '|')
            spots.remove(num)
            loc = False
        else:
            print('|' + ' '*leng + '|')
    print(' ' + '-'*34)

 
#room_map("Downstairs")



stairwell = Room(0, "Grungy Stairwell", r_north=3)
washroom = Room(1, "Public Washroom", r_north=4)
torture = Room(2, "Torture Hall")
main_corridor = Room(3, "Main Corridor", 9, 0, 4, 7)
east_corridor = Room(4, "East Corridor", 8, 1, 5, 3)
closet = Room(5, "Storage Closet", r_west=4)
keepers_quarters = Room(6, "Keepers Quarters", 12, 11, 7)
west_corridor = Room(7, "West Corridor", None, 2, 3, 6)
kitchen = Room(8, "Desolate Kitchen", r_south=4)
prisoners_quarters = Room(9, "Prisoners Quarters", r_south=3, r_east=10)
prison_passage = Room(10, "Secret Passage", r_south=5, r_west=9)
keepers_passage = Room(11, "Secret Passage", r_east=0, r_north=6)
keepers_hall = Room(12, "Keepers Hall", r_south=6, r_east=13)
private_washroom = Room(13, "Private Washroom", r_west=12)
rooms = [stairwell, washroom, torture, main_corridor, east_corridor, closet, keepers_quarters, west_corridor, kitchen, prisoners_quarters, prison_passage,
         keepers_passage, keepers_hall, private_washroom]