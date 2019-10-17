from frontendUtility import requiredInput as ri
from frontendUtility import Modes, Status

class Withdraw():

    def __init__(this, validAcctsList, mode):
        this.mode = mode
        this.validAcctsList = validAcctsList
        this.status = Status.OK
        this.acctNumber = None
        this.amount = None
    #accepts input and only returns given a valid account numberm or cancel or logout
    def getAcct(this):
        validNum = False
        num = None
        while not validNum:
            inNum = ri('Input the account number of account to withdraw from: ')
            if inNum == 'logout':
                this.status = Status.LOGOUT
                validNum = True
            elif inNum == 'cancel':
                this.status = Status.CANCEL
                validNum = True
            elif not inNum in this.validAcctsList:
                print('{} is not a valid account. Please enter a valid account'.format(inNum))
            else:
                validNum = True
                num = inNum
        return num

    #returns a given number in cents only when entered in the correct format
    def getNumber(this):
        validNumber = False
        #need a way to determine the withdrawal total for every account
        while not validNumber:
            numberString = ri('Enter a number to withdraw in cents: ')
            if numberString.isdigit() == True:
                number = int(numberString)
            else:
                number = 0
            if numberString == "cancel":
                this.status = Status.CANCEL
                validNumber = True
            elif numberString == "off":
                this.status = Status.OFF
                validNumber = True
            elif numberString.isdigit() == False:
                print("Please only enter digits")
            elif number > 100000 and this.mode == Modes.ATM:
                print("Maximum withdraw of "u'\xa2'"100000 per transaction in ATM mode")
            elif number > 99999999 and this.mode == Modes.TELLER:
                print("Maximum withdraw of "u'\xa2'"99999999 per transaction in Teller mode")
            elif number < 1:
                print("Must withdraw at least 1 cent")
            elif depositTotal > 500000 and this.mode == Modes.ATM:
                print("maximum withdrawal of "u'\xa2'"500000 a day")
            else:
                validNumber = True
        return number
