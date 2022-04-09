from dexutils import login
from time import time

dexcom = login()

last_reading = 0
while True:
    if time() - last_reading >= 300:
        bg = dexcom.get_current_glucose_reading()
        print(bg.value, 'mg/dL', bg.trend_description, '|', bg.time.strftime('%I:%M%p %A %B %d, %Y'))
        last_reading = time()
