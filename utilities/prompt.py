import sys
from getpass import getpass
from slowprinter import Printer

# ACCOUNT SUBROUTINE TO PROMPT USER INFO
def prompt(msg='Log into Dexcom:'):
    ui = Printer(0.05)
    ui.printer(msg)
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
