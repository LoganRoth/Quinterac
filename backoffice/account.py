"""
account.py

This file contains the class that represents a single account in the Master
Accounts File
"""


class Account:
    """
    Class that represents a single account in the Master Accounts File
    """
    def __init__(self, acctStr):
        try:
            splitStr = acctStr.split()
            self.num = splitStr[0]
            self.balance = int(splitStr[1])
            self.name = ' '.join(splitStr[2:])
        except (ValueError, IndexError):
            self.num = '0000000'
            self.name = ''
            self.balance = 0
            print('Account in invalid format: {}'.format(acctStr))
