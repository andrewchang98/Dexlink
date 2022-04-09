import sys
from getpass import getpass
from slowprinter import Printer

# ACCOUNT SUBROUTINE TO PROMPT USER INFO
def prompter(printer=None):
    if printer is None:
        printer = print
    else:
        printer = printer
    printer('Log into Dexcom:')
    try:
        printer('Username:', end=' ')
        username = input()
        printer('Password:', end=' ')
        password = getpass()
    except KeyboardInterrupt:
        printer('\n', 'Cancelled by user. Exiting now.', sep='')
        sys.exit(0)
    else:
        return username, password
