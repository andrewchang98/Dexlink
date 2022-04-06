import sys
from getpass import getpass
from pydexcom import Dexcom

# PROMPT USER INFO
def prompt():
    print('Log into Dexcom:')
    try:
        username = input('Username: ')
        password = getpass('Password: ')
    except KeyboardInterrupt:
        print('\n', 'Canceled by user. Exiting now.', sep='')
        sys.exit(0)
    else:
        return username, password

# LOAD ACCOUNT INFO
def account():
    # TRY TO LOAD PASSWORDS FILE
    print('Loading account info...')
    try:
        from accounts import passwords
    except ImportError:
        print('No account info found.')
        DEXCOM_USERNAME, DEXCOM_PASSWORD = prompt()
    else:
        # ASK TO LOGIN AS USER
        print('Login as {} (y/n)?'.format(passwords.account[0]), end = ' ')
        try:
            keystroke = input()
            if keystroke == 'y' or keystroke == 'Y':
                DEXCOM_USERNAME = passwords.account[0]
                DEXCOM_PASSWORD = passwords.account[1]
            elif keystroke == 'n' or keystroke == 'N':
                DEXCOM_USERNAME, DEXCOM_PASSWORD = prompt()
            else:
                print('\n', 'Canceled by user. Exiting now.', sep='')
                sys.exit(0)
        except KeyboardInterrupt:
            print('\n', 'Canceled by user. Exiting now.', sep='')
            sys.exit(0)
    # CONNECT TO DEXCOM SHARE API
    try:
        print('\n', 'Connecting to Dexcom servers...', sep='')
        dexcom = Dexcom(DEXCOM_USERNAME, DEXCOM_PASSWORD)
    except:
        print('\n', 'Login failed. Please check username and password.', sep='')
        print('Exiting now.')
        sys.exit(0)
    else:
        print('Logged in as {}'.format(DEXCOM_USERNAME), '\n', sep='')
        return dexcom
