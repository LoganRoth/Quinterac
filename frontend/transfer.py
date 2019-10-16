from frontendUtility import requiredInput as ri
from frontendUtility import Modes, Status

class Transfer():

    def __init__(this, validAcctsList, mode):
        this.mode = mode
        this.validAcctsList = validAcctsList
        this.status = Status.OK
        this.acctNumber = None
        this.amount = None

    def getAcct(this, text):
        validNum = False
        num = None
        while not validNum:
            inNum = ri(text)
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
    def getNumber(this):
        validNumber = False
        depositTotal = 0 #need a way to determine the deposit total
        while not validNumber:
            numberString = ri('Enter a number to deposit in cents: ')
            if numberString.isdigit == True:
                number = int(numberString)
            else:
                number = 0
            if numberString == "cancel":
                this.status = Status.CANCEL
                validNumber = True
            elif numberString == "off":
                this.status = Status.OFF
                validNumber = True
            elif numberString.isdigit == False:
                print("Please only enter digits")
            elif number > 1000000 and this.mode == Modes.ATM:
                print("Maximum transfer of "u'\xa2'"1000000 per transaction in ATM mode")
            elif number > 99999999 and this.mode == Modes.TELLER:
                print("Maximum transfer of "u'\xa2'"99999999 per transaction in Teller mode")
            elif number < 1:
                print("Must deposit at least 1 cent")
            elif depositTotal > 500000 and this.mode == Modes.ATM:
                print("maximum transfer of "u'\xa2'"1000000 a day")
            else:
                validNumber = True
        return number
