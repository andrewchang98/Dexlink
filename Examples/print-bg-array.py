print('--- PRINT BLOOD GLUCOSE ARRAY ---')
print('Importing APIs...')
from pydexcom import Dexcom
from getpass import getpass


DEXCOM_USERNAME = None
DEXCOM_PASSWORD = None

if(DEXCOM_USERNAME is None or DEXCOM_PASSWORD is None):
    DEXCOM_USERNAME = input('Username: ')
    DEXCOM_PASSWORD = getpass('Password: ')


print('Connecting to Dexcom servers...')
try:
    dexcom = Dexcom(DEXCOM_USERNAME, DEXCOM_PASSWORD)
    print('Logged in as "{}"...'.format(DEXCOM_USERNAME))
except:
    print('Login failed. Please check username and password.')
    print('Exiting.')
    exit()


print('Retrieving current BG...')
bg = dexcom.get_current_glucose_reading()
if(bg == None):
    print('!!!WARNING!!! ATTEMPT FAILED. RETRIEVING LAST BG WITHIN 24 HOURS.')
    bg = dexcom.get_latest_glucose_reading()
    if(bg == None):
        print('No glucose readings available within the last 24 hours!')
        print('Please check if Dexcom and Dexlink are working correctly.')
else:
    print('Success.')

timestamp = bg.time
print('|', bg.value, 'mg/dL', bg.trend_arrow, '|', timestamp.strftime('%c'))


print('Retrieving BG data over the last ')
bg = dexcom.get_glucose_readings(1440, 288)
return(bg) 