'''
deposit.py

This file contains the class and all its methods to deposit into an account
'''
from frontendUtility import requiredInput as ri
from frontendUtility import Modes, Status

class Deposit():
    '''
    Class that handles deposits into an account
    Requires a valid accounts list and the current mode of operation (machine or agent)
    a successful deposit will result in the transaction going onto the transaction summary file
    '''
    def __init__(this, validAcctsList, mode):
        this.mode = mode
        this.validAcctsList = validAcctsList
        this.status = Status.OK
        this.acctNumber = None
        this.amount = None

    def getAcct(this):
        '''
        Asks for an account number and returns the account number if it is valid
        Also finishes if the user attempts to logout or cancel
        '''
        validNum = False
        num = None
        while not validNum:
            inNum = ri('Input the account number of account to deposit into: ')
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
        Asks for a number to deposit in cents and returns the number if a valid amount is given
        Also finishes if the user attampts to logout or cancel
        '''
        validNumber = False
        #need a way to determine the deposit total for every account
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
            elif number > 200000 and this.mode == Modes.ATM:
                print("Maximum deposit of "u'\xa2'"200000 per transaction in ATM mode")
            elif number > 99999999 and this.mode == Modes.TELLER:
                print("Maximum deposit of "u'\xa2'"99999999 per transaction in Teller mode")
            elif number < 1:
                print("Must deposit at least 1 cent")
            elif depositTotal > 500000 and this.mode == Modes.ATM:
                print("maximum deposit of "u'\xa2'"500000 a day")
            else:
                validNumber = True
        return number
