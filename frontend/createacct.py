"""
createacct.py

This file contains the class and all of its methods to handle the frontend
steps to creating a new account.
"""
from frontendUtility import requiredInput as ri
from frontendUtility import Status


class CreateAcct():
    """
    Class that handles the createacct command.

    @param validAcctsList The dictionary the contains the list of valid
                          accounts
    """
    def __init__(this, validAcctsList):
        this.validAcctsList = validAcctsList
        this.status = Status.OK
        this.newAcctNum = None
        this.newAcctName = None

    def createNewAccount(this):
        """
        Gets the new account number and name.
        If logout or cancel are given as the number or name then this will
        return and the status of this object will indicate what caused the
        return.
        """
        num = this.__getNewAcctNum()
        if this.status != Status.OK:
            return
        name = this.__getNewAcctName()
        if this.status != Status.OK:
            return
        this.newAcctNum = num
        this.newAcctName = name

    def __getNewAcctNum(this):
        """
        Gets the requested account number of the new account.
        If logout or cancel is given as input this funciton will return and
        the status of this object will indicate what caused the return.

        Ensures that the given account number is in valid format as described
        by the requirements.
        """
        validNum = False
        num = None
        while not validNum:
            inNum = ri('Input the account number for the new account: ')
            if inNum == 'logout' or inNum == 'off':
                this.status = Status.LOGOUT
                validNum = True
            elif inNum == 'cancel':
                this.status = Status.CANCEL
                validNum = True
            elif not inNum.isdigit():
                print('Account numbers must be comprised of only digits. '
                      'Please choose a different account number.')
            elif len(inNum) != 7:
                print('Account numbers must be exactly 7 digits in length. '
                      'Please choose a different account number.')
            elif inNum == '0000000':
                print('0000000 is a reserved account number. Please choose a '
                      'different account number.')
            elif inNum[0] == '0':
                print('Account numbers must not begin with a "0". Please '
                      'choose a different account number.')
            elif inNum in this.validAcctsList.keys():
                print('{} is already in use. Please choose a different account'
                      ' number.'.format(inNum))
            else:
                validNum = True
                num = inNum
        return num

    def __getNewAcctName(this):
        """
        Gets the requested account name of the new account.
        If logout or cancel is given as input this funciton will return and
        the status of this object will indicate what caused the return.

        Ensures that the given account name is in valid format as described by
        the requirements.
        """
        validName = False
        name = None
        while not validName:
            inName = ri('Input the account name for the new account: ',
                        toLower=False)
            if inName == 'logout' or inName == 'off':
                this.status = Status.LOGOUT
                validName = True
            elif inName == 'cancel':
                this.status = Status.CANCEL
                validName = True
            elif len(inName) < 3 or len(inName) > 30:
                print('Account names must be between 3 and 30 characters. '
                      'Please choose a different account name.')
            elif not inName.replace(' ', '').isalnum():
                print('Account names must only contain alphanumeric characters'
                      ' and spaces. Please choose a different account name.')
            else:
                validName = True
                name = inName
        return name
