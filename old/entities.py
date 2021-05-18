from old import advtools

color = advtools.Color()
hostile = "hostile"
passive = "passive"


class Creature:
    def __init__(self, kind, name="", description="", mob_hp=-1, damage=-1, items=None):
        self.name = name
        self.damage = damage
        self.description = description
        self.hp = mob_hp
        self.maxhp = mob_hp
        self.kind = kind
        self.list = []
        self.value = None
        self.drop = None

    # creates instance of a creature
    def create(self, lst):
        self.value = lst
        for y in self.value:
            self.list.append(y)

    # list instnaces of creatures
    def lst(self):
        for z in self.list:
            print(z)


def mob_dmg(damage):
    if damage <= 2:
        return color.green + "a little"
    elif 2 < damage <= 4:
        return color.bright_red + "some"
    elif damage >= 5:
        return color.red + color.bold + "significant"
        

def mob_health(mob):
    if mob.hp/mob.maxhp > .80:
        return color.green + "High"
    elif mob.hp/mob.maxhp > .40:
        return color.bright_yellow + "Low"
    elif mob.hp/mob.maxhp:
        return color.red + "Critical"


# creation of enemies
jumbo_rat = Creature(hostile, "Jumbo Rat", "A Jumbo Rat Appears! He looms over you, waiting to strike...", 5, 5)
miniature_dragon = Creature(hostile, "Miniature Dragon", "A Miniature Dragon leaps out of the shadows! Me may be small, but he still breathes fire!", 14, 4)
abraham = Creature(hostile, "Abraham Lincoln", "Abraham Lincoln jumps down from the ceiling! He think's you're a slave trader!", 10, 3)
hermon = Creature(hostile, "Mr. Hermon", "Mr. Hermon crawls out from the corner! Quick, solve his boom/chain problem before he sucks out your brains!", 2, 5)
joe = Creature(hostile, "Joe", "Joe materializes out of thin air! Wait, that's not very threatening! He gives you a bag of almonds", 6, 3)
monk = Creature(hostile, "Decrepid Monk", "A Decrepid Monk appears! He tries to shave your head.", 15, 4)
luke = Creature(hostile, "Luke Skywalker", "Luke skywalker sprints into the corridor. His light saber hums at his side, ready to slice off your philanges", 20, 5)
# add monsters to pool
monsters = [jumbo_rat, miniature_dragon, abraham, hermon, joe, monk, luke]