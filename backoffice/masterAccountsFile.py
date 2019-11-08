"""
masterAccountsFile.py

This file contains the class and all of its methods to handle updating the
Master Accounts File and writing the new Valid Accounts List File.
"""
from utility.utility import RetCode


class MasterAccountsFile:
    """
    Class that handles the updating the Master Accounts File and creating the
    new Valid Accounts List File.

    @param masterAcctsFile The file containing the current master accounts file
    """
    def __init__(self, masterAcctsFile):
        self.file = masterAcctsFile
        self.masterAccts = {}
        self.__createMasterAcctsDct()

    def __createMasterAcctsDct(self):
        """
        Reads through all of the accounts in the Master Accounts File and
        creates a Account object for each one, adding each one to the
        masterAccts dct class attribute.
        """
        accts = []
        with open(self.file, 'r') as f:
            accts = f.readlines()
        for acctStr in accts:
            try:
                splitStr = acctStr.split()
                num = splitStr[0]
                balance = int(splitStr[1])
                name = ' '.join(splitStr[2:])
                self.masterAccts[num] = {'Name': name,
                                         'Balance': balance}
            except (ValueError, IndexError):
                print('Account in invalid format: {}'.format(acctStr))

    def updateMAF(self, transactions):
        """
        Updates the Master Accounts File dicitonary based on the transactions
        from the Merged Transaction Summary File.

        @param transactions The list of transactions from the Merged
                            Transaction Summary File.
        """
        if transactions is None:
            return RetCode.ERROR
        for tx in transactions:
            tx.update(self.masterAccts)
        return RetCode.OK

    def writeNewMAF(self):
        """
        Writes a new MAF file to be used for the next day.
        """
        with open(self.file, 'w') as f:
            acctNumList = sorted(self.masterAccts.keys())
            for acct in acctNumList:
                formattedStr = self.__formatAccount(acct)
                if formattedStr is not None:
                    f.write(formattedStr)

    def writeNewValidAccountsListFile(self):
        """
        Writes a new valid accounts list file to be used be the Front Ends
        on the next day.
        """
        with open('validAcctsListFile.txt', 'w+') as f:
            acctNumList = sorted(self.masterAccts.keys())
            for acct in acctNumList:
                f.write('{}\n'.format(acct))
            f.write('0000000\n')

    def __formatAccount(self, acctNum):
        """
        Formats the given account information into the proper string format
        to be written into the actual Master Accounts File.
        """
        name = '{}'.format(self.masterAccts[acctNum]['Name'])
        amount = self.__formatAmount(self.masterAccts[acctNum]['Balance'])
        str = '{} {} {}\n'.format(acctNum, amount, name)
        if len(str) > 47:
            print('Master Accounts File, line too long {}.'.format(str))
            str = None
        return str

    def __formatAmount(self, amount):
        """
        Formats the amount stirng to follow the conventions of being at least
        3 digits, 000 if 0, 00# if one digit, 0##, if two digits.
        """
        amount = '{}'.format(amount)
        if len(amount) == 0:
            amount = '000'
        elif len(amount) == 1:
            amount = '00{}'.format(amount)
        elif len(amount) == 2:
            amount = '0{}'.format(amount)
        return amount
