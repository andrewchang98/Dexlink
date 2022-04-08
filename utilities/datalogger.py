import time
import login
import pickle
import datetime
from pydexcom import Dexcom

dexcom = login.account()

bg = dexcom.get_current_glucose_reading()

data = [bg]

with open('data.dex', 'wb') as file:
    pickle.dump(data, file, pickle.HIGHEST_PROTOCOL)
