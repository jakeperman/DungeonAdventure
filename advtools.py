import random
import time
import loot
import shutil
import sys
weapon = "weapon"
consumable = "consumable"
junk = "junk"
material = "material"
any_item = "any"
hostile = "hostile"
passive = "passive"
# Creature Class


# Color class
class Color:
    # standard colors
    black = '\u001b[30m'
    red = '\u001b[31m'
    green = '\u001b[32m'
    yellow = '\u001b[33m'
    blue = '\u001b[34m'
    magenta = '\u001b[35m'
    cyan = '\u001b[36m'
    white = '\u001b[37m'
    reset = '\u001b[0m'
    # bold colors
    bold_black = '\u001b[30;1m'
    bold_red = '\u001b[31;1m'
    bold_green = '\u001b[32;1m'
    bold_yellow = '\u001b[33;1m'
    bold_blue = '\u001b[34;1m'
    bold_magenta = '\u001b[35;1m'
    bold_cyan = '\u001b[36;1m'
    bold_white = '\u001b[37;1m'
    # bright colors
    # may not display as expected depending on IDE and console used
    #bright_black = '\u001b[90m'
    bright_red = '\u001b[91m'
#    bright_green = '\u001b[92m'
#    bright_yellow = '\u001b[93m'
#    bright_blue = '\u001b[94m'
#    bright_magenta = '\u001b[95m'
#    bright_cyan = '\u001b[96m'
#    bright_white = '\u001b[97m'
    
    bright_green = "\u001b[90m"
    bright_yellow = "\u001b[91m"
    bright_blue = "\u001b[92m"
    bright_magenta = "\u001b[93m"
    bright_cyan = "\u001b[94m"
    bright_white = "\u001b[95m"
    bright_black = "\u001b[96m"
    dark_blue = "\u001b[97m"

    # standard background colors
    background_black = '\u001b[40m'
    background_red = '\u001b[41m'
    background_green = '\u001b[42m'
    background_yellow = '\u001b[43m'
    background_blue = '\u001b[44m'
    background_magenta = '\u001b[45m'
    background_cyan = '\u001b[46m'
    background_white = '\u001b[47m'

    # decorative
    bold = '\u001b[1m'
    underline = '\u001b[4m'
    reversed = '\u001b[7m'
    

color = Color


# creates text border to break up dialogue
def border(leng, colour=""):
    # if argument 'leng' is int, set border length equal to it
    if isinstance(leng, int):
        length = leng
    # if argument 'leng' is a string, get the len() and set border length equal to that
    elif isinstance(leng, str):
        length = len(leng)
    else:
        length = 0
    # if color is specified and is of the class 'Color', set argument to that color
    if colour != "":
        col = colour
    # set color to white if no argument, or non-color argument, is specified
    else:
        col = color.reset
    x, y = shutil.get_terminal_size()
    if length > x:
        length = x -1
#    print(col + '-'*length)
    for i in range(0, length):
        print(col + '-', end='')
    print('', end='\n')
    
def new_border(leng, colour=color.bright_white):
    if isinstance(leng, int):
        length = leng
    # if argument 'leng' is a string, get the len() and set border length equal to that
    elif isinstance(leng, str):
        length = len(leng)
    else:
        length = 0
    x, y = shutil.get_terminal_size()
    if length > x:
        length = x -1
    bord = "-"*length
    print(colour + bord)

border = new_border

def load_bar(txt="Loading...", delay=.05, length=20):   
    print(color.bold + txt)
    x, y = shutil.get_terminal_size()
    if length > x:
        length = x - 5
    for i in range(length):   
        bar = color.blue + "█"*i
        dots = color.bright_white + "•"*(length-i-1)
        stat = color.bright_white + " " + str(round((i+1)/length*100)) + '%'
        sys.stdout.write("\r" + bar + dots + stat)
        sys.stdout.flush()
        time.sleep(delay)
    print()



def dialogue(text, newln=True, col=color.yellow, slp=0.05):
    for item in text:
        sys.stdout.write(f"{col + item}")
        sys.stdout.flush()
        time.sleep(slp)
    if newln:
        print()
    else:
        print('', end='')
        
def search_bar_old(loops=3, slp=0.08):
    col = color.green
    msgs = ['Searching', 'Foraging', 'Inspecting']
    msg = random.choice(msgs)
    sys.stdout.write(f"\r{col + msg}")
    while True:
        for i in range(loops):
            for i in range(6):
                sys.stdout.write(col+".")
                time.sleep(slp)
            sys.stdout.write(f'\r{col + msg}')
        break
    sys.stdout.write("\r")

def load_text(text, loops=3, slp=0.1, col=color.bright_white, lnslp=0.15):
    for i in range(loops):
        sys.stdout.write("\r")
        for letter in text:
            sys.stdout.write(col + letter)
            sys.stdout.flush()
            time.sleep(slp)
        time.sleep(lnslp)
    sys.stdout.write("\r")
        
def search_bar(loops=3, slp=0.08):
    msgs = ['Searching.....', 'Foraging.....', 'Inspecting.....']
    msg = random.choice(msgs)
    col = color.green
    load_text(msg, loops, slp, col)
            




