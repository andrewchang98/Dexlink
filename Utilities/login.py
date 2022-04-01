"""
Logs into Dexcom

"""

from pydexcom import Dexcom
from getpass import getpass


try:
    #Load account info
    from accounts import passwords
    DEXCOM_USERNAME = passwords.account[0]
    DEXCOM_PASSWORD = passwords.account[1]
except:
    #Prompt manual input if no info is available
    DEXCOM_USERNAME = input('Username: ')
    DEXCOM_PASSWORD = getpass('Password: ')


try:
    print('Connecting to Dexcom servers...')
    dexcom = Dexcom(DEXCOM_USERNAME, DEXCOM_PASSWORD)
except:
    print('Login failed. Please check username and password.')
else:
    print('Logged in as "{}"...'.format(DEXCOM_USERNAME))
