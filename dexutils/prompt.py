import sys
from getpass import getpass
from slowprinter import Printer

# ACCOUNT SUBROUTINE TO PROMPT USER INFO
def prompt():
    ui = Printer(0.05)
    ui.printer('Log into Dexcom:')
    try:
        ui.printer('Username:', end=' ')
        username = input()
        ui.printer('Password:', end=' ')
        password = getpass()
    except KeyboardInterrupt:
        print('\n', 'Cancelled by user. Exiting now.', sep='')
        sys.exit(0)
    else:
        return username, password
