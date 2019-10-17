'''
transfer.py

This file contains the class and all its methods to transfer money between two accounts
'''
from frontendUtility import requiredInput as ri
from frontendUtility import Modes, Status

class Transfer():
    '''
    Class that handles transfer between accounts
    Requires a valid accounts list and the current mode of operation (machine or agent)
    a successful transfer will result in the transaction going onto the transaction summary file
    '''
    def __init__(this, validAcctsList, mode):
        this.mode = mode
        this.validAcctsList = validAcctsList
        this.status = Status.OK
        this.acctNumber = None
        this.amount = None

    def getAcct(this, text):
        '''
        Asks for an account number and returns the account number if it is valid
        Also finishes if the user attempts to logout or cancel
        '''
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
        '''
        Asks for a number to transfer in cents and returns the number if a valid amount is given
        Also finishes if the user attampts to logout or cancel
        '''
        validNumber = False
        #need a way to determine the transfer total for every account
        while not validNumber:
            numberString = ri('Enter a number to deposit in cents: ')
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
