print('Importing API...')
from pydexcom import Dexcom
#from datetime import datetime
print('Logging in...')
dexcom = Dexcom('staciepeterson', 'Finn2019312!')
print('Logged in as "staciepeterson"')

print('Getting current BG.')
bg = dexcom.get_current_glucose_reading()
if(bg == None):
    print('No recent readings availale, getting last BG within 24 hours.')
    bg = dexcom.get_latest_glucose_reading()
    if(bg == None):
        print('No glucose readings available within the last 24 hours.')
        print('Exiting.')
        exit()

timestamp = bg.time
print(bg.value, 'mg/dL', bg.trend_arrow, timestamp.strftime('%c'))
