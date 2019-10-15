#!/usr/bin/env python3
import sys
import os
import argparse

from session import Session, State
from frontendUtility import requiredInput as ri
from frontendUtility import RetCode, Modes


def areFilesValid(validAccts, summaryFile):
    if validAccts is None or not os.path.exists(validAccts):
        print('Valid accounts list file not found')
        return False
    if summaryFile is None or not os.path.exists(summaryFile):
        print('Summary output file not found')
        return False
    return True

def main(validAccts, summaryFile):
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

