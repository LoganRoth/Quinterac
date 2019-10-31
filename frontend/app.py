#!/usr/bin/env python3
"""
app.py

This is the actual executable python file that contains the main control loop
for the Quinterac banking system.

INTENT:
A user should use this program to interact with the Quinterac banking system.
There are two possible modes to use: agent or machine.
Machine puts the system into ATM mode and so a user can only use the deposit,
transfer, and withdraw commands.
Agent puts the system into Teller mode and gives the user the ability to
access the create and delete account transaction commands as well as the
commands available to ATM mode.
One run of the program is one "session" and thus, after a logout, a session is
over at that is considered the end of a processing day.

INTENDED USAGE:
run "frontend.py validAcctsFile.txt summaryFile.txt"

Followed by entering valid transaction commands and following resulting
prompts.
If unsure what a valid transaction command is, user can use ? or help to prompt
what transaction commands are currenty valid.
A user can always input off, or logout to terminate the session from any point
during execution.
A user can input cancel if at any point they want to cancel a current
transaction.

IN/OUT:
Input file: validAcctsFile.txt
This file should contain the list of valid accouts

Output file: summaryFile.txt
This file will be written to during execution of the program based on which
transactions occur during a session
"""
import os
import argparse

from frontend.session import Session, State
from frontend.frontendUtility import requiredInput as ri
from frontend.frontendUtility import RetCode, Modes


def areFilesValid(validAccts, summaryFile):
    """
    Checks if the given validAccts and summaryFile variables are actually
    valid files.

    @param validAccts  The file containing the valid accounts list
    @param summaryFile The file to be used for the transaction summary record
    """
    if validAccts is None or not os.path.exists(validAccts):
        print('Valid accounts list file not found')
        return False
    if summaryFile is None or not os.path.exists(summaryFile):
        print('Summary output file not found')
        return False
    return True


def parseArgs():
    """
    Parses the arguments given to the script and returns the validAccts and
    summaryFile.
    """
    parser = argparse.ArgumentParser(usage='frontend.py validAcctsList.txt '
                                           'summaryFile.txt')
    parser.add_argument(
        'validAccts',
        action='store',
        default=None,
        help='The name of the file containing the valid accounts list.'
    )
    parser.add_argument(
        'summaryFile',
        action='store',
        default=None,
        help='The name of the file to be used to keep track of the summary '
             'of transactions for the session.'
    )
    args = parser.parse_args()
    return args.validAccts, args.summaryFile


def main():
    """
    The main loop of the Quinterac banking system. Creates a session object
    and then passes commands to it from the user input.
    Commands at this level will only be the transaction commands, ie, login,
    logout, withdraw, etc. Not the sub-commands such as the amount to
    withdraw/transfer/deposit or the login mode of agent or machine.

    @param validAccts  The file containing the valid accounts list
    @param summaryFile The file to be used for the transaction summary record
    """
    validAccts, summaryFile = parseArgs()
    if not areFilesValid(validAccts, summaryFile):
        return RetCode.ERROR
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
