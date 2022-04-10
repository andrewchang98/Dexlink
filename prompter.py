import sys
from getpass import getpass
from slowprinter import Printer

# ACCOUNT SUBROUTINE TO PROMPT USER INFO
def prompter(printer=None, message='Log into Dexcom:'):
    if printer is None:
        printer = print
    else:
        printer = printer
    printer(message)
    try:
        printer('\nUsername:', end=' ')
        username = input()
        printer('\nPassword:', end=' ')
        password = getpass(prompt='')
    except KeyboardInterrupt:
        print('\nCancelled by user. Exiting now.')
        sys.exit(0)
    else:
        return username, password
