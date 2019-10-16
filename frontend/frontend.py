#!/usr/bin/env python3
"""
frontend.py

This is the actual executable python file that contains the main control loop for the Quinterac banking system.
"""
import sys
import os
import argparse

from session import Session, State
from frontendUtility import requiredInput as ri
from frontendUtility import RetCode, Modes


def areFilesValid(validAccts, summaryFile):
    """
    Checks if the given validAccts and summaryFile variables are actually valid files.
    """
    if validAccts is None or not os.path.exists(validAccts):
        print('Valid accounts list file not found')
        return False
    if summaryFile is None or not os.path.exists(summaryFile):
        print('Summary output file not found')
        return False
    return True

def main(validAccts, summaryFile):
    """
    The main loop of the Quinterac banking system. Creates a session object and then passes commands to it from the
    user input.
    Commands at this level will only be the transaction commands, ie, login, logout, withdraw, etc. Not the
    sub-commands such as the amount to withdraw/transfer/deposit or the login mode of agent or machine.
    """
    if not areFilesValid(validAccts, summaryFile):
        return RetCode.ERROR
    terminalOn = True
    session = Session(validAccts, summaryFile)
    prompt = 'Quinterac: '
    while session.state != State.END:
        if session.mode == Modes.TELLER:
            prompt = 'Quinterac [Teller]: '
        elif session.mode == Modes.ATM:
            prompt = 'Quinterac [ATM]: '
        else:
            prompt = 'Quinterac: '
        command = ri(prompt=prompt)
        session.handleCommand(command)
             
    return RetCode.OK

def parseArgs():
    """
    Parses the arguments given to the script and returns the validAccts and summaryFile.
    """
    parser = argparse.ArgumentParser(usage='frontend.py validAcctsList.txt summaryFile.txt')
    parser.add_argument(
        'validAccts',
        action ='store',
        default=None,
        help   ='The name of the file containing the valid accounts list.'
    )
    parser.add_argument(
        'summaryFile',
        action ='store',
        default=None,
        help   ='The name of the file to be used to keep track of the summary of transactions for the session.'
    )
    args = parser.parse_args()
    return args.validAccts, args.summaryFile

if __name__ == "__main__":
    try:
        validAccts, summaryFile = parseArgs()
        ret = main(validAccts, summaryFile)
    except KeyboardInterrupt:
        print('Aborting')
        ret = RetCode.ABORTING
    sys.exit(ret)

