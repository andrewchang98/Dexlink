"""
Logs into Dexcom

"""
import sys
from getpass import getpass


#Import API
try:
    print('Loading API...')
    from pydexcom import Dexcom
except:
    print('Missing or damaged API module.')
    print('Exiting.')
    exit()

#Login option if account info is avaiable
def auth(pair):
    try:
        global DEXCOM_USERNAME
        global DEXCOM_PASSWORD
        print('Login as {}?'.format(pair[0]), end = ' ')
        keystroke = input('(Y/n): ')
        if keystroke == 'y' or keystroke == 'Y':
            DEXCOM_USERNAME = pair[0]
            DEXCOM_PASSWORD = pair[1]
        elif keystroke == 'n' or keystroke == 'N':
            DEXCOM_USERNAME = input('Username: ')
            DEXCOM_PASSWORD = getpass('Password: ')
        else:
            auth(pair)
    except KeyboardInterrupt:
        print()
        print('Canceled by user. Exiting.')
        sys.exit(0)

#Load account info
try:
    print('Loading account info...')
    from accounts import passwords
    auth(passwords.account)
except ImportError:
    try:
        print('No account info in ~/.local/lib/python3.9/site-packages/')
        DEXCOM_USERNAME = input('Username: ')
        DEXCOM_PASSWORD = getpass('Password: ')
    except KeyboardInterrupt:
        print()
        print('Canceled by user. Exiting.')
        sys.exit(0)
finally:
    #Login to Dexcom
    try:
        print('Connecting to Dexcom servers...')
        dexcom = Dexcom(DEXCOM_USERNAME, DEXCOM_PASSWORD)
    except:
        print('Login failed. Please check username and password.')
    else:
        print('Logged in as {}'.format(DEXCOM_USERNAME))
