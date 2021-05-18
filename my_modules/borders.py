from my_modules.colors import Color as color
import sys
import time

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
    for i in range(0, length+1):
        print(col + '-', end='')
    print('', end='\n')
 
def load_bar():   
    print("Loading...")
    length = 20
    for i in range(length):   
        bar = color.blue + "█"*i
        dots = color.white + "•"*(20-i-1)
        stat = color.bright_white + " " + str(round((i+1)/length*100)) + '%'
        sys.stdout.write("\r" + bar + dots + stat)
        sys.stdout.flush()
        time.sleep(0.05)
    print("")

    