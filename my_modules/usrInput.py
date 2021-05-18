'''
usrInput module allows you to easily ask for user commands.
You can specify allowed answers without having to clutter your code with if else statements for error checking. You can also use a specific color for priting.
'''
from my_modules.colors import Color as color
def user_input(prompt="default", options=None , clr="white", val=None):
#    options = tuple(o for o in options if )
    if options is None and val is None:
        inp = input(color.magenta + color.bold + prompt + color.reset)
    elif isinstance(options, int):
        options = (options,)
    else:
        inp = None
    while inp is None:
        try:
            if options is None:
                if val == "i":
                    try:
                        inp = int(input(color.magenta + color.bold + prompt + color.reset))
                    except ValueError:
                        print(color.red + "Please enter a number")
                        continue
                elif val == "s":
                    try:
                        cmd = input(color.magenta + color.bold + prompt + color.reset)
                        if not isinstance(int(cmd), int):
                            inp = cmd
                        else:
                            print(color.red + "Please enter a string")
                            continue
                    except ValueError:
                        inp = cmd
            else:   
                # checks for str or int, avoids errors on mispress
                if isinstance(options[0], int):
                    # try/except block handles errors in the event of mishandled key
                    try:
                        cmd = int(input(color.magenta + color.bold + prompt + color.reset))
                        if cmd in options:
                            inp = cmd
                        else:
                            print(color.red + "Invalid input.")
                    except ValueError:
                        print(color.red + 'Please enter a number.')
                        continue
                else:
                    cmd = input(color.magenta + color.bold + prompt + color.reset)
                    
                    if cmd.upper() in options or cmd.lower() in options:
                        inp = cmd
                    elif isinstance(cmd, int):
                        print(color.red + "Please enter a string.")
                    else:
                        print(color.red + "Invalid input.")
                        continue

        except IndexError:
            print(color.red + "Invalid Command")
            continue
    # the function returns the user input as a value usable as required by a function or otherwise
    return inp


        
def equal(value1, value2):
    if isinstance(value1, type(value2)):
        if isinstance(value1, str):
            if value1.upper() == value2.upper():
                return True
            else:
                return False
        elif isinstance(value1, int):
            if value1 == value2:
                return True
            else:
                return False
        else:
            try:
                if value1 == value2:
                    return True
                else:
                    return False
            except:
                print("Values cannot be compared")
            
    else:
        print(color.error + f"ERROR: {value1} and {value2} are not of the same type and cannot be compared")
        



        
