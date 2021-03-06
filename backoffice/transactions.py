"""
transactions.py

This file contains the class and all of its methods to handle dealing with a
list of transactions.
"""
from backoffice.transaction import Transaction


class Transactions:
    """
    Class that handles the list of transactions.

    @param mergedSummaryFile The file containing the concatenation of all of
                             the transaction summary files from the previous
                             day.
    """
    def __init__(self, mergedSummaryFile, whitebox):
        self.file = mergedSummaryFile
        self.lst = []
        self.__createTxList(whitebox)

    def __createTxList(self, whitebox):
        """
        Reads through all of the transactions in the Merged Transaction Summary
        File and creates a Transaction object for each one that is not an EOS
        adding them to the class 'lst' attribute
        """
        transactions = None
        with open(self.file, 'r') as f:
            transactions = f.readlines()
        for tx in transactions:
            try:
                if tx != 'EOS\n':
                    self.lst.append(Transaction(tx, whitebox))
            except ValueError:
                print('Invalid transaction in the summary file: {}'.format(tx))
