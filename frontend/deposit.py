"""
deposit.py

This file contains the class and all of its methods to handle the frontend
steps to depositing to an account
"""
from frontend.frontendUtility import requiredInput as ri
from frontend.frontendUtility import Modes, Status


class Deposit():
    """
    Class that handles the deposit command.

    @param validAcctsList The dictionary the contains the list of valid
                          accounts
    @param mode The mode that the session is currently in
    """
    def __init__(this, validAcctsList, mode):
        this.mode = mode
        this.validAcctsList = validAcctsList
        this.status = Status.OK
        this.acctNumber = None
        this.amount = None

    def getAcct(this):
        """
        Accepts input and only returns given a valid account number or None
        """
        validNum = False
        num = None
        while not validNum:
            inNum = ri('Input the account number of account to deposit into: ')
            if inNum == 'logout' or inNum == 'off':
                this.status = Status.LOGOUT
                validNum = True
            elif inNum == 'cancel':
                this.status = Status.CANCEL
                validNum = True
            elif inNum not in this.validAcctsList.keys():
                print('{} is not a valid account. Please enter a valid '
                      'account'.format(inNum))
            else:
                validNum = True
                this.acctNumber = inNum
                num = inNum
        return num

    def getNumber(this):
        """
        Returns a given number in cents only when entered in the correct format
        """
        validNumber = False
        # need a way to determine the deposit total for every account
        while not validNumber:
            numberString = ri('Enter a number to deposit in cents: ')
            if numberString.isdigit():
                number = int(numberString)
            else:
                number = 0
            if numberString == "cancel":
                this.status = Status.CANCEL
                validNumber = True
            elif numberString == "off" or numberString == "logout":
                this.status = Status.LOGOUT
                validNumber = True
            elif not numberString.isdigit():
                print("Please only enter digits")
            elif number > 200000 and this.mode == Modes.ATM:
                print("Maximum deposit of "u'\xa2'"200000 per transaction in "
                      "ATM mode")
            elif number > 99999999 and this.mode == Modes.TELLER:
                print("Maximum deposit of "u'\xa2'"99999999 per transaction in"
                      " Teller mode")
            elif number < 1:
                print("Must deposit at least 1 cent")
            elif (this.validAcctsList[this.acctNumber]['deposit']
                  + number) > 500000 and this.mode == Modes.ATM:
                print("maximum deposit of "u'\xa2'"500000 a day")
            else:
                validNumber = True
        return number
