'''
withdraw.py

This file contains the class and all its methods to withdraw money from an account
'''
from frontendUtility import requiredInput as ri
from frontendUtility import Modes, Status

class Withdraw():
    '''
    Class that handles withdraw from account
    Requires a valid accounts list and the current mode of operation (machine or agent)
    a successful withdrawal will result in the transaction going onto the transaction summary file
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

    def getNumber(this):
        '''
        Asks for a number to withdraw in cents and returns the number if a valid amount is given
        Also finishes if the user attampts to logout or cancel
        '''
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
