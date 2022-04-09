import sys
from prompter import prompter
from pydexcom import Dexcom
from slowprinter import Printer

# MAIN ROUTINE TO LOAD ACCOUNT INFO
def login():
    # TRY TO LOAD PASSWORDS FILE
    ui = Printer(0.1)
    ui.printer('Loading account info...')
    try:
        import passwords
    except ImportError:
        ui.printer('No account info found in ~/.local/lib/python3.9/site-packages/accounts/')
        DEXCOM_USERNAME, DEXCOM_PASSWORD = prompter(ui.printer)
    else:
        # ASK TO LOGIN AS USER
        ui.printer('Login as {} (Y/n)?'.format(passwords.account[0]), end = ' ')
        try:
            keystroke = input()
            if keystroke == 'y' or keystroke == 'Y':
                DEXCOM_USERNAME = passwords.account[0]
                DEXCOM_PASSWORD = passwords.account[1]
            elif keystroke == 'n' or keystroke == 'N':
                DEXCOM_USERNAME, DEXCOM_PASSWORD = prompter(ui.printer)
            else:
                ui.printer('\n', 'Cancelled by user. Exiting now.', sep='')
                sys.exit(0)
        except KeyboardInterrupt:
            ui.printer('\n', 'Cancelled by user. Exiting now.', sep='')
            sys.exit(0)
    # CONNECT TO DEXCOM SHARE API
    try:
        ui.printer('\n', 'Connecting to Dexcom servers...', sep='')
        dexcom = Dexcom(DEXCOM_USERNAME, DEXCOM_PASSWORD)
    except:
        ui.printer('\n', 'Login failed. Please check username and password.', sep='')
        ui.printer('Exiting now.')
        sys.exit(0)
    else:
        ui.printer('Logged in as {}'.format(DEXCOM_USERNAME), '\n', sep='')
        return dexcom
