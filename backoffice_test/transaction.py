"""
transaction.py

This file contains the class and all of its methods to handle a single
transaction.
"""


class Transaction:
    """
    Class that handles all of the needed operations for any transaction.

    @param txString The file containing the current master accounts file
    """
    def __init__(self, txString):
        splitTx = txString.split()
        try:
            self.code = splitTx[0]
            self.acct1 = splitTx[1]
            self.amt = int(splitTx[2])
            self.acct2 = splitTx[3]
            self.acctName = ' '.join(splitTx[4:])
        except (ValueError, IndexError):
            print('Transaction in invalid format {}.'.format(txString))
            self.acct1 = '00000000'
            self.acct2 = '00000000'
            self.amt = 0

    def update(self, mafDct):
        """
        Update the given dictionary based on the transaction.

        @param mafDct The dictionary describing the MAF
        """
        if self.code == 'NEW':
            self.__createAcct(mafDct)
        elif self.code == 'DEL':
            self.__deleteAcct(mafDct)
        elif self.code == 'WDR':
            self.__withdraw(mafDct)
        elif self.code == 'DEP':
            self.__deposit(mafDct)
        elif self.code == 'XFR':
            self.__transfer(mafDct)

    def __createAcct(self, mafDct):
        """
        Performs the necessary update to the MAF to add an account.

        @param mafDct The dictionary describing the MAF
        """
        # Ensure account is not already in MAF
        if self.acct1 in mafDct.keys(): #1
            print('line 1')
            print('Account {} already in Master Accounts File. A new account '
                  'cannot use a number already in the File'.format(self.acct1)) #2
            print('line 2')
        else: #3
            print('line 3')
            mafDct[self.acct1] = {'Name': self.acctName, 'Balance': 0} #4
            print('line 4')

    def __deleteAcct(self, mafDct):
        """
        Performs the necessary update to the MAF to delete an account.

        @param mafDct The dictionary describing the MAF
        """
        # Ensure account is in MAF
        if self.acct1 in mafDct.keys():
            # Ensure that the given account name matches the name in the MAF
            if mafDct[self.acct1]['Name'] == self.acctName:
                del mafDct[self.acct1]
            else:
                print('Account name {} does not match for account {}. Account '
                      'will not be deleted.'.format(self.acctName, self.acct1))

        else:
            print('Account {} not in Master Accounts File. Therefore, cannot '
                  'delete it.'.format(self.acct1))

    def __withdraw(self, mafDct):
        """
        Performs the necessary update to the MAF to withdraw from an account.

        @param mafDct The dictionary describing the MAF
        """
        # Ensure account is in MAF
        if self.acct1 in mafDct.keys():
            result = mafDct[self.acct1]['Balance'] - self.amt
            # Ensure withdraw will result in a valid amount in the account
            if result < 0:
                print('Attempt to overdraw from account {}, withdraw '
                      'rejected.'.format(self.acct1))
            else:
                mafDct[self.acct1]['Balance'] = result
                print('Withdraw Passed')
        else:
            print('Account {} not found in Master Accounts File, cannot '
                  'withdraw.'.format(self.acct1))

    def __deposit(self, mafDct):
        """
        Performs the necessary update to the MAF to deposit to an account.

        @param mafDct The dictionary describing the MAF
        """
        # Ensure account is in MAF
        if self.acct1 in mafDct.keys():
            # Ensure deposit will result in a valid amount in the account
            result = mafDct[self.acct1]['Balance'] + self.amt
            if result > 99999999:
                print('Attempt to overdeposit into account {}, deposit '
                      'rejected. Max amount of 99999999 '
                      'cents'.format(self.acct1))
            else:
                mafDct[self.acct1]['Balance'] = result
        else:
            print('Account {} not found in Master Accounts File, cannot '
                  'deposit.'.format(self.acct1))

    def __transfer(self, mafDct):
        """
        Performs the necessary update to the MAF to transfer from one account
        to another.

        @param mafDct The dictionary describing the MAF
        """
        # Ensure both accounts are in MAF
        if self.acct1 not in mafDct.keys():
            print('Account {} not found in Master Accounts File, cannot '
                  'transfer.'.format(self.acct1))
        elif self.acct2 not in mafDct.keys():
            print('Account {} not found in Master Accounts File, cannot '
                  'transfer.'.format(self.acct2))
        else:
            # Both accounts are in the MAF, make sure tranfer will result in
            # valid amounts in both accounts
            fromRes = mafDct[self.acct1]['Balance'] - self.amt
            toRes = mafDct[self.acct2]['Balance'] + self.amt
            if fromRes < 0:
                print('Attempt to overdraw from account {}, transfer '
                      'rejected.'.format(self.acct1))
            elif toRes > 99999999:
                print('Attempt to overdeposit into account {}, transfer '
                      'rejected. Max amount of 99999999 '
                      'cents'.format(self.acct2))
            else:
                mafDct[self.acct1]['Balance'] = fromRes
                mafDct[self.acct2]['Balance'] = toRes
