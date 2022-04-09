from login import login
from time import time
from slowprinter import Printer

dexcom = login()
printer = ui.Printer(delay=0.05)

last_reading = 0
while True:
    if time() - last_reading >= 300:
        bg = dexcom.get_current_glucose_reading()
        print(bg.value, 'mg/dL', bg.trend_description, '|', bg.time.strftime('%I:%M%p %A %B %d, %Y'))
        printer(str(bg.value), end=' ')
        printer('mg/dL', end=' ')
        printer(bg.trend_description, end=' ')
        printer('|', end=' ')
        printer(bg.time.strftime('%I:%M%p %A %B %d, %Y'), end='\n\n')
        last_reading = time()
