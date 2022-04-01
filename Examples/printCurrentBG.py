print('--- PRINT CURRENT BLOOD GLUCOSE ---')
print('Importing APIs...')
from pydexcom import Dexcom
from getpass import getpass


DEXCOM_USERNAME = input('Username: ')
DEXCOM_PASSWORD = getpass('Password: ')


try:
    print('Connecting to Dexcom servers...')
    dexcom = Dexcom(DEXCOM_USERNAME, DEXCOM_PASSWORD)
    print('Logged in as "{}"...'.format(DEXCOM_USERNAME))
except:
    print('Login failed. Please check username and password.')
    print('Exiting.')
    exit()

try:
    #Start by fetching current BG
    print('Fetching current BG...')
    bg = dexcom.get_current_glucose_reading()
    if bg == None:
        #If current BG is unavailable fall back to last BG
        print('!!!WARNING!!! NO DATA. FETCHING LAST BG WITHIN 24 HOURS.')
        bg = dexcom.get_latest_glucose_reading()
        if bg == None:
            #Exit if no data avaiable
            print('No data available within the last 24 hours!')
            print('Please check if Dexcom and Dexlink are working correctly.')
            print('Exiting.')
            exit()
        else:
            print('Success.')
    else:
        print('Success.')
except:
    print('Failed.')

timestamp = bg.time
print('|', bg.value, 'mg/dL', bg.trend_description, '|', timestamp.strftime('%c'))
