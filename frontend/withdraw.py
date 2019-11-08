"""
withdraw.py

This file contains the class and all of its methods to handle the frontend
steps to withdraw from an account.
"""
from frontend.frontendUtility import requiredInput as ri
from frontend.frontendUtility import Modes, Status


class Withdraw:
    """
    Class that handles the withdraw command.

    @param validAcctsList The dictionary the contains the list of valid
                          accounts
    @param mode The mode that the session is currently in
    """
    def __init__(self, validAcctsList, mode):
        self.mode = mode
        self.validAcctsList = validAcctsList
        self.status = Status.OK
        self.acctNumber = None
        self.amount = None

    def getAcct(self):
        """
        Accepts input and only returns given a valid account numberm or None
        """
        validNum = False
        num = None
        while not validNum:
            inNum = ri('Input the account number of account to withdraw '
                       'from: ')
            if inNum == 'logout' or inNum == 'off':
                self.status = Status.LOGOUT
                validNum = True
            elif inNum == 'cancel':
                self.status = Status.CANCEL
                validNum = True
            elif inNum not in self.validAcctsList:
                print('{} is not a valid account. Please enter a valid '
                      'account'.format(inNum))
            else:
                validNum = True
                self.acctNumber = inNum
                num = inNum
        return num

    def getNumber(self):
        """
        Returns a given number in cents only when entered in the correct format
        """
        validNumber = False
        # need a way to determine the withdrawal total for every account
        while not validNumber:
            numberString = ri('Enter a number to withdraw in cents: ')
            if numberString.isdigit():
                number = int(numberString)
            else:
                number = 0
            if numberString == "cancel":
                self.status = Status.CANCEL
                validNumber = True
            elif numberString == "off" or numberString == "logout":
                self.status = Status.LOGOUT
                validNumber = True
            elif not numberString.isdigit():
                print("Please only enter digits")
            elif number > 100000 and self.mode == Modes.ATM:
                print("Maximum withdraw of "u'\xa2'"100000 per transaction in "
                      "ATM mode")
            elif number > 99999999 and self.mode == Modes.TELLER:
                print("Maximum withdraw of "u'\xa2'"99999999 per transaction "
                      "in Teller mode")
            elif number < 1:
                print("Must withdraw at least 1 cent")
            elif (self.validAcctsList[self.acctNumber]['withdraw']
                  + number) > 500000 and self.mode == Modes.ATM:
                print("maximum withdrawal of "u'\xa2'"500000 a day")
            else:
                validNumber = True
        return number
