import pickle
from pydexcom import Dexcom

with open('data.dex', 'rb') as file:
    data = pickle.load(file)

print data[0]
