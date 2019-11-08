"""
deleteacct.py

This file contains the class and all of its methods to handle the frontend
steps to deleting an account.
"""
from frontend.frontendUtility import requiredInput as ri
from frontend.frontendUtility import Status


class DeleteAcct:
    """
    Class that handles the deleteacct command.

    @param validAcctsList The dictionary the contains the list of valid
                          accounts
    """
    def __init__(self, validAcctsList):
        self.validAcctsList = validAcctsList
        self.status = Status.OK
        self.oldAcctNum = None
        self.oldAcctName = None

    def deleteOldAccount(self):
        """
        Gets the account to delete and the name of the account as well as
        removes the deleted account from the current list of valid accounts,
        however, does not remove from the official file because that is
        handled by the back office after authentication of the deletion has
        occurred.
        If logout or cancel are given as the number or name then this will
        return and the status of this object will indicate what caused the
        return.
        """
        num = self.__getOldAcctNum()
        if self.status != Status.OK:
            return
        name = self.__getOldAcctName()
        if self.status != Status.OK:
            return
        self.oldAcctNum = num
        self.oldAcctName = name
        try:
            del self.validAcctsList[num]
        except ValueError:
            print('Account given was not found in the valid list. Account: '
                  '{}'.format(num))

    def __getOldAcctNum(self):
        """
        Gets the account number of the account to delete.
        If logout or cancel is given as input this funciton will return and
        the status of this object will indicate what caused the return.

        Ensures that the account trying to be deleted is actually a current
        valid account.
        """
        validNum = False
        num = None
        while not validNum:
            inNum = ri('Input the account number of account to delete: ')
            if inNum == 'logout' or inNum == 'off':
                self.status = Status.LOGOUT
                validNum = True
            elif inNum == 'cancel':
                self.status = Status.CANCEL
                validNum = True
            elif inNum not in self.validAcctsList.keys():
                print('{} is not a valid account. Please enter a valid '
                      'account'.format(inNum))
            else:
                validNum = True
                num = inNum
        return num

    def __getOldAcctName(self):
        """
        Gets the account name of the account to delete.
        If logout or cancel is given as input this funciton will return and
        the status of this object will indicate what caused the return.

        Ensures that the account name given is in a valid format to decrease
        the chance of a typo causing the deletion to fail when the transaction
        is being authenticated by the back end.
        """
        validName = False
        name = None
        while not validName:
            inName = ri('Input the account name of account to delete: ',
                        toLower=False)
            if inName == 'logout' or inName == 'off':
                self.status = Status.LOGOUT
                validName = True
            elif inName == 'cancel':
                self.status = Status.CANCEL
                validName = True
            elif len(inName) < 3 or len(inName) > 30:
                print('Account names must be between 3 and 30 characters. '
                      'Please enter a valid account name.')
            elif not inName.replace(' ', '').isalnum():
                print('Account names must only contain alphanumeric characters'
                      ' and spaces. Please enter a valid account name.')
            else:
                validName = True
                name = inName
        return name
