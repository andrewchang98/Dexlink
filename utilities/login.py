import sys
from pydexcom import Dexcom

# MAIN ROUTINE TO LOAD ACCOUNT INFO
def account():
    # TRY TO LOAD PASSWORDS FILE
    print('Loading account info...')
    try:
        from accounts import passwords
    except ImportError:
        print('No account info found in ~/.local/lib/python3.9/site-packages/accounts/')
        DEXCOM_USERNAME, DEXCOM_PASSWORD = prompt()
    else:
        # ASK TO LOGIN AS USER
        print('Login as {} (Y/n)?'.format(passwords.account[0]), end = ' ')
        try:
            keystroke = input()
            if keystroke == 'y' or keystroke == 'Y':
                DEXCOM_USERNAME = passwords.account[0]
                DEXCOM_PASSWORD = passwords.account[1]
            elif keystroke == 'n' or keystroke == 'N':
                DEXCOM_USERNAME, DEXCOM_PASSWORD = prompt()
            else:
                print('\n', 'Cancelled by user. Exiting now.', sep='')
                sys.exit(0)
        except KeyboardInterrupt:
            print('\n', 'Cancelled by user. Exiting now.', sep='')
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
