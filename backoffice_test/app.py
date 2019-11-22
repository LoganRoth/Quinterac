"""
app.py

This is the python file that contains the main control loop for the Quinterac
banking system's Back Office.

INTENT:
A user should use this program to activate the Back Office of the Quinterac
banking system to update the Master Accounts File (MAF) using the Merged
Transaction Summary File (MTSF). After updating the MAF the back office will
create a new Valid Accounts List File to be used by the frontend during the
next day of transactions.

INTENDED USAGE:
run "python -m backoffice masterAcctsFile.txt mergedTransactionSummaryFile.txt"
From the base dierctory of the QuinteracPrestigeWorldwide repo

IN/OUT:
Input file: masterAcctsFile.txt
This file should contain the list of all the valid accounts along with how much
money is in each account. This file also tracks the account names to be used as
psuedo passwords when deleting accounts.

Input file: mergedTransactionSummaryFile.txt
This file should contain the concatenation of any number of Transaction
Summary Files output from Front Ends during the previous day.

Output file: masterAcctsFile.txt
This file will be the same as the input masterAcctsFile.txt but updated with
any transactions that occured.

Output file: validAcctsListFile.txt
This file will contain the list of valid accounts to be used by the Front Ends
during the next day.
"""
import argparse

from backoffice.masterAccountsFile import MasterAccountsFile
from backoffice.transactions import Transactions
from utility.utility import RetCode, isFileValid


def areFilesValid(masterAcctsFile, mergedSummaryFile):
    """
    Checks if the given masterAcctsFile and mergedSummaryFile variables are
    actually valid files.

    @param masterAcctsFile  The file containing the Master Accounts File.
    @param mergedSummaryFile The file containing the concatenation of all of
                             the transaction summary files from the previous
                             day.
    """
    if not isFileValid(masterAcctsFile, "Master Accounts File"):
        return False
    if not isFileValid(mergedSummaryFile, "Merged Transaction Summary File"):
        return False
    return True


def parseArgs():
    """
    Parses the arguments given to the script and returns the masterAcctsFile
    and mergedSummaryFile.
    """
    parser = argparse.ArgumentParser(usage='app.py masterAcctsFile.txt '
                                           'mergedSummaryFile.txt')
    parser.add_argument(
        'masterAcctsFile',
        action='store',
        default=None,
        help='The name of the file containing the Master Accounts File.'
    )
    parser.add_argument(
        'mergedSummaryFile',
        action='store',
        default=None,
        help='The name of the file containing the concatenation of all of the '
             'transaction summary files from the previous day.'
    )
    args = parser.parse_args()
    return args.masterAcctsFile, args.mergedSummaryFile


def main():
    """
    The main function of the Quinterac banking system's back office.
    """
    masterAcctsFile, mergedSummaryFile = parseArgs()
    if not areFilesValid(masterAcctsFile, mergedSummaryFile):
        return RetCode.ERROR
    maf = MasterAccountsFile(masterAcctsFile)
    transactions = Transactions(mergedSummaryFile)
    ret = maf.updateMAF(transactions.lst)
    if ret == RetCode.OK:
        maf.writeNewMAF()
        maf.writeNewValidAccountsListFile()
    else:
        print('New Master Accounts File and Valid Accounts List File not '
              'written due to earilier errors.')
    return RetCode.OK
