from sys import stdout
from time import sleep

# PER CHARACTER SINGLE LINE PRINT UI FUNCTION
class UIPrinter:
    def __init__(self, disabled=False):
        self.disabled = disabled

    def printer(self, string, end='\n'):
        if self.disabled:
            print(string, end=end)
            return
        for char in string:
            stdout.write(char)
            stdout.flush()
            sleep(0.1)
        stdout.write(end)
        stdout.flush()

    # ENABLED OR DISABLED SLOW PRINTS
    def enable_slow_prints(self):
        self.disabled = disabled

    def disable_slow_prints(self):
        self.disabled = disabled
