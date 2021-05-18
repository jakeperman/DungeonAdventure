from old.loot import *

# Creation of object instances
# Creation of Junk
hairbrush = Junk("Plastic Hairbrush", "It's bristles are slimy. You run it through your hair.")
screwdriver = Junk('Broken Screwdriver', "Who are you, Fix it Felix?")
bandage = Junk('Used Bandage', 'It may be used, but you can still use it again!')
eyepatch = Junk('Bloody Eyepatch', "You put it on. It feels sticky and warm.")
femur = Junk("Cracked Femur", "Finders keepers!")
plank = Junk("Rotted Wooden Plank", "Quick, hit yourself over the head with it! Maybe this is all just a dream...")
pen = Junk("Ballpoint Pen", "Never a bad time to start writing your obituary.", 1, 1)
letteropen = Junk("Wooden Letter Opener", "Who are you expecting mail from down here?",1, 2)
rubberband = Junk("Rubber Band", "Strike down your enemies!", 3, 1)
hair = Junk("Ball of Hair", "Did you cough that up? Gross.")
mirror = Junk("Broken Mirror", "It may be broken, but you can still see how ugly you are!")
gameboy = Junk("Gameboy Advanced", "An escape from your life! The video games make the pain go away!")
soap = Junk("Used Bar Of Soap", "Should you eat it...? No. ")
# add junk to list
junks = [hair, hairbrush, screwdriver, bandage, eyepatch, femur, plank, pen, letteropen, rubberband, hair,
         mirror, gameboy]
         
# Creation of Weapons
swiss = Weapon("Swiss Army Knife", "Maybe you can use it to cut swiss cheese?", 3, 5)
switchblade = Weapon("Rusty Switchblade", "Better hope you have your tetanus shot...", 2, 3)
chefknife = Weapon("Dull Chef's Knife", "Maybe you should prepare a meal before you become one.", 3.5, 5)
machette = Weapon("Steel Machete", "Too bad you arent trapped in a jungle!", 5, 8)
staff = Weapon("Iron bow-staff", "Is it a bow, or a staff? Maybe both...?", 3, -1)
pencil = Weapon("#2 Pencil", "Sharper than your wits!", 1, 1)
fork = Weapon("Bent Fork", "Try and bend it back, then you'll just have a fork.", 1, 2)
nail = Weapon("6 inch Iron Nail", "Quick! Drive it through your skull and end the harsh reality that is your life.", 2, 5)
woodenstake = Weapon("Wooden Stake", "You can protect yourself from vampires!", 2.5, 6)
# add weapons to list
weapons = [swiss, switchblade, chefknife, machette, pencil, fork, nail, woodenstake, staff]


# Materials
nails = Material("Box of Nails", "Maybe you can build something...")
battery = Material('AAA battery', "Too bad you don't have a flashlight...")
matches = Material("Soggy Box of Matches", "Better hope they still work...")
stones = Material("Pile of Stones", "Don't eat them.")
splint = Material("Wooden Splint", "Try not to break your leg. But if you do, you've got a splint!")
stick = Material("Stick", "How'd this get here?? I don't see any trees...")
gauze = Material("Fresh Gauze", "I have a feeling you'll be needing this...")
rope = Material("Knotted Rope", "Undo the knots and you can make a noose!")
hammer = Material("Small Hammer", "Who are you, bob the builder?")
bhammer = Material("Big Hammer", "Don't drop that on your foot... you wont last long with a broken foot")
bhammer.damage = 2
flint = Material("Flint and Striker", "Do you even know how to use this?")
# add materials to list
materials = [nails, matches, stones, gauze, rope, hammer, bhammer, battery]


# Consumables
cheese = Consumable("Swiss Cheese", "It's got holes in it!", saturation=1, effect=0)
flesh = Consumable("Rotten Flesh", "Wait, this isn't minecraft!", saturation=3, effect=1)
apple = Consumable("Bruised Apple", "Watch your back, before you get bruised too...", saturation=1.5, effect=0)
mouse = Consumable("Mutilated Mouse", "Not very appetizing... yet.", saturation=4, effect=0)
bread = Consumable("Stale loaf of Bread", "This could do some damage... Or you could eat it.", saturation=2.5, effect=0)
medicine = Consumable("Mysterious Bottle Of Medicine", "At least you have a painless way out...", saturation=0, effect=2)
ratpoison = Consumable("Rat Poison", "You shouldn't eat this... Should you?", saturation=0, effect=2)
# add consumables to list
consumables = [cheese, flesh, apple, mouse, bread, medicine]
bread.effect = 5
effects = [0,1,0,0,0,2,2]
sats = [1,3,1.5,4,2.5,0,0]
for i, each in enumerate(consumables):
    each.effect = effects[i]
    each.saturation = sats[i]
    
    
# creates progression items

shoes = Integral("Padded Leather Boots", "Maybe these will help dampen your footsteps...")
torch = Integral("Torch", "This might shed some light on the situation")
crowbar = Integral("Rusted Crowbar", "It may be rusty, but it's still rather trusty!")
key = Integral("Key", "This probably opens something.")
integrals = [shoes, torch, crowbar]


loot_pool = [consumables, materials, junks, weapons]
rooms_loot = []