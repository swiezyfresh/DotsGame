import inspect
class colors:
    '''Colors class:reset all colors with colors.reset; two
    sub classes fg for foreground
    and bg for background; use as colors.subclass.colorname.
    i.e. colors.fg.red or colors.bg.greenalso, the generic bold, disable,
    underline, reverse, strike through,
    and invisible work with the main class i.e. colors.bold'''
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'
    
    class fg:
        reset = '\033[0m'
        bold = '\033[01m'
        purple = '\033[35m'
        red = '\033[91m'
        green = '\033[92m'
        yellow = '\033[93m'
        blue = '\033[94m'
        pink = '\033[95m'
        cyan = '\033[96m'

        def display_colors(self):
            available_colors = ""
            for (attr, value) in inspect.getmembers(self):
                if not attr.startswith("_") and not inspect.ismethod(value):
                    available_colors += "| "+ self.bold + value + attr + " " + self.reset
            return available_colors

    
    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'