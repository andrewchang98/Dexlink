from pydexcom import Dexcom
#from datetime import datetime

dexcom = Dexcom('staciepeterson', 'Finn2019312!')

bg = dexcom.get_current_glucose_reading()
if(bg == None):
    bg = dexcom.get_latest_glucose_reading()
    if(bg == None):
        print('No glucose readings available within the last 24 hours.')
        print('Exiting.')
        exit()

timestamp = bg.time
print(bg.value, 'mg/dL', timestamp.strftime('%c'))
