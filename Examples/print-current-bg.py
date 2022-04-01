print('--- PRINT CURRENT BLOOD GLUCOSE ---')
print('Importing APIs...')
from pydexcom import Dexcom
from getpass import getpass


DEXCOM_USERNAME = input('Username: ')
DEXCOM_PASSWORD = getpass('Password: ')


print('Logging in as "{}"...'.format(DEXCOM_USERNAME))
try:
    dexcom = Dexcom(DEXCOM_USERNAME, DEXCOM_PASSWORD)
    print('Success.')
except:
    print('Login failed. Please check username and password.')
    print('Exiting.')
    exit()


print('Getting current BG.')
bg = dexcom.get_current_glucose_reading()
if(bg == None):
    print('!!!WARNING: ATTEMPT FAILED. GETTING LAST BG WITHIN 24 HOURS!!!')
    bg = dexcom.get_latest_glucose_reading()
    if(bg == None):
        print('No glucose readings available within the last 24 hours!')
        print('Please check if Dexcom and Dexlink are working correctly.')
        print('Exiting.')
        exit()
print('Success.')


timestamp = bg.time
print(bg.value, 'mg/dL', bg.trend_arrow, timestamp.strftime('%c'))
