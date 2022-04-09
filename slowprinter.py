from sys import stdout
from time import sleep

# CHARACTER BY CHARACTER PRINT FUNCTION
class Printer:
    def __init__(self, delay=0.05, disabled=False):
        self.disabled = disabled
        self.delay = delay

    # MAIN FUNCTION
    def printer(self, string, end='\n'):
        if self.disabled:
            print(string, end=end)
        else:
            for char in string:
                stdout.write(char)
                stdout.flush()
                sleep(self.delay)
            stdout.write(end)
            stdout.flush()

    # ENABLE SLOW PRINTS
    def enable_printer(self):
        self.disabled = False

    # USE REGULAR PRINTS
    def disable_printer(self):
        self.disabled = True

    # CHANGE DELAY
    def change_delay(self, delay):
        self.delay = delay
