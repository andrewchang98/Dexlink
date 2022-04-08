from sys import stdout
from time import sleep
from random import uniform

# PER CHARACTER SINGLE LINE PRINT UI FUNCTION
class UIPrinter:
    def __init__(self, disabled=False):
        self.disabled = disabled

        def printer(self, line='\n'):
            if not self.disabled:
                for char in line:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    print(char, end='')
                    seconds = uniform(0.1, 0.2)
                    sleep(seconds)
            else:
                print(line)

        def disable_slow_prints(self, disabled=True):
            self.disabled = disabled

        def enable_slow_prints(self, disabled=False):
            self.disabled = disabled
