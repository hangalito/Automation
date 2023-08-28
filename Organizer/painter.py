class Painter:
    def __init__(self, text=''):
        self.text = text
    
    def bold(self):
        return f"\033[1m{self.text}\033[m"
    
    def cyan(self, bold=False):
        if bold:
            return f"\033[1;36m{self.text}\033[m"
        else:
            return f"\033[36m{self.text}\033[m"
    
    def blue(self, bold=False):
        if bold:
            return f"\033[1;34m{self.text}\033[m"
        else:
            return f"\033[34m{self.text}\033[m"

    def indigo(self, bold=False):
        if bold:
            return f"\033[1;35m{self.text}\033[m"
        else:
            return f"\033[35m{self.text}\033[m"

    def green(self, bold=False):
        if bold:
            return f"\033[1;32m{self.text}\033[m"
        else:
            return f"\033[32m{self.text}\033[m"

    def gray(self, bold=True):
        if bold:
            return f"\033[1;37m{self.text}\033[m"
        else:
            return f"\033[37m{self.text}\033[m"

    def red(self, bold = False):
        if bold:
            return f"\033[1;31m{self.text}\033[m"
        else:
            return f"\033[31m{self.text}\033[m"

    def yellow(self, bold=False):
        if bold:
            return f"\033[1;33m{self.text}\033[m"
        else:
            return f"\033[33m{self.text}\033[m"
    
    def __doc__(self) -> str:
        return ("Returns a string representation of the colored text. "
            "The string will br formatted with the specified color.")
    
    def __str__(self) -> str:
        self.text = "You must call a method to get the text painted!"
        return self.red(True)