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
#    bright_red = '\u001b[91m'
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
    
    # speciality messages
    error = red + bold
    warning = bright_yellow + bold + background_red
    inp = bright_magenta
    

class Cursor:
    def up(dist):
        return f'\u001b[{dist}A'
    def down(dist):
        return f'\u001b[{dist}B'
    def right(dist):
        return f'\u001b[{dist}C'
    def left(dist):
        return f'\u001b[{dist}D'
    

    