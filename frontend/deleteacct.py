"""
deleteacct.py

This file contains the class and all of its methods to handle the frontend steps to deleting an account.
"""
from frontendUtility import requiredInput as ri
from frontendUtility import Status

class DeleteAcct():
    """
    Class that handles the deleteacct command.
    Requires a valid accounts list to be given during intialization. This list must be modifiable because a successful
    deletion will remove the account from the list to stop additional transactions being performed on the accout.
    """
    def __init__(this, validAcctsList):
        this.validAcctsList = validAcctsList
        this.status = Status.OK
        this.oldAcctNum = None
        this.oldAcctName = None

    def deleteOldAccount(this):
        """
        Gets the account to delete and the name of the account as well as removes the deleted account from the current
        list of valid accounts, however, does not remove from the official file because that is handled by the back
        office after authentication of the deletion has occurred.
        If logout or cancel are given as the number or name then this will return and the status of this object will
        indicate what caused the return.
        """
        num = this._getOldAcctNum()
        if this.status != Status.OK:
            return
        name = this._getOldAcctName()
        if this.status != Status.OK:
            return
        this.oldAcctNum = num
        this.oldAcctName = name
        try:
            this.validAcctsList.remove(num)
        except ValueError as e:
            print('Account given was not found in the valid list. Account: {}'.format(num))


    def _getOldAcctNum(this):
        """
        Gets the account number of the account to delete.
        If logout or cancel is given as input this funciton will return and the status of this object will indicate
        what caused the return.

        Ensures that the account trying to be deleted is actually a current valid account.
        """
        validNum = False
        num = None
        while not validNum:
            inNum = ri('Input the account number of account to delete: ')
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

    def _getOldAcctName(this):
        """
        Gets the account name of the account to delete.
        If logout or cancel is given as input this funciton will return and the status of this object will indicate
        what caused the return.

        Ensures that the account name given is in a valid format to decrease the chance of a typo causing the deletion
        to fail when the transaction is being authenticated by the back end.
        """
        validName = False
        name = None
        while not validName:
            inName = ri('Input the account name of account to delete: ', toLower=False)
            if inName == 'logout':
                this.status = Status.LOGOUT
                validName = True
            elif inName == 'cancel':
                this.status = Status.CANCEL
                validName = True
            elif len(inName) < 3 or len(inName) > 30:
                print('Account names must be between 3 and 30 characters. Please enter a valid account name.')
            elif not inName.replace(' ', '').isalnum():
                print('Account names must only contain alphanumeric characters and spaces. Please enter a valid '
                      'account name.')
            else:
                validName = True
                name = inName
        return name