from frontendUtility import requiredInput as ri
from frontendUtility import Modes, Status

class Deposit():

    def __init__(this):
        this.status = Status.OK
        this.acctNumber = None
        this.amount = None

    def depositIntAcct():
         x = 2
    def getNumber(this):
        validNumber = False
        while not validNumber:
            numberString = ri('Enter a number to deposit in cents: ')
            if numberString.isdigit == 0:
                print("Please only enter digits")
            number = int(numberString)
            if number > 200000 and session.mode == Modes.ATM:
                print("Maximum deposit of ¢200000 per transaction in ATM mode")
            elif number > 99999999 and session.mode == Modes.TELLER:
                print("Maximum deposit of ¢99999999 per transaction in Teller mode")
            elif number > 0:
                this.status = Status.OK
            elif mode == 'machine':
                this.status = Status.OK
            else:
                string = 'Please enter either agent or machine if you wish to continue\nIf you do not wish to continue, please enter either cancel or logout'
                if mode != '?' and mode != 'help':
                    string = 'Unrecognized mode "{}". {}'.format(mode, string)
                print(string)
        return number
