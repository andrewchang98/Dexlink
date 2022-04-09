from sys import exit
from login import login
from time import time
from slowprinter import Printer

dexcom = login()
ui = Printer(delay=0.05)

last_reading = 0
while True:
    try:
        if time() - last_reading >= 300:
            bg = dexcom.get_current_glucose_reading()
            ui.printer(str(bg.value), end=' ')
            ui.printer('mg/dL', end=' ')
            ui.printer(bg.trend_description, end=' ')
            ui.printer('|', end=' ')
            ui.printer(bg.time.strftime('%I:%M%p %A %B %d, %Y'), end='\n\n')
            last_reading = time()
    except KeyboardInterrupt:
        print('User KeyboardInterrupt. Exiting now.')
        exit(0)
