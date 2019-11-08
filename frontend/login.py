"""
login.py

This file contains the class and all of its methods to handle logging in to
the Quinterac banking system.
"""
import os

from frontend.frontendUtility import requiredInput as ri
from frontend.frontendUtility import Modes, Status


class Login:
    """
    Class that handles logging in.
    If a cancel or logout is given as input while getting the mode, the
    classes status will indicate what has happened.
    """
    def __init(self):
        self.status = Status.OK

    def getMode(self):
        """
        Function to ask get the requested banking system mode from the user.

        Logout and cancel may also be given as input rather than completing
        the login.
        Inputs of "?" and "help" can be used to prompt the user of possible
        valid options.
        """
        validMode = False
        retMode = Modes.NA
        while not validMode:
            mode = ri('Enter the desired mode [agent or machine]: ')
            if mode == 'agent':
                validMode = True
                retMode = Modes.TELLER
                self.status = Status.OK
            elif mode == 'machine':
                validMode = True
                retMode = Modes.ATM
                self.status = Status.OK
            elif mode == 'cancel':
                validMode = True
                retMode = Modes.NA
                self.status = Status.CANCEL
            elif mode == 'logout':
                validMode = True
                retMode = Modes.NA
                self.status = Status.LOGOUT
            else:
                string = 'Please enter either agent or machine if you wish to'\
                         ' continue\nIf you do not wish to continue, please '\
                         'enter either cancel or logout'
                if mode != '?' and mode != 'help':
                    string = 'Unrecognized mode "{}". {}'.format(mode, string)
                print(string)
        return retMode

    def getValidAccts(self, validAcctsFile):
        """
        Function to get the list of valid accounts from the valid accounts
        list file.
        """
        accts = {}
        with open(validAcctsFile, 'r') as f:
            tempAccts = f.readlines()
            if '0000000\n' not in tempAccts:
                print('Error processing {}, no special end account '
                      '"0000000"'.format(os.path.basename(validAcctsFile)))
            else:
                for acct in tempAccts:
                    acct = acct.replace('\n', '')
                    if acct == '0000000':
                        break
                    elif acct.isdigit() and len(acct) == 7:
                        accts[acct] = {'withdraw': 0, 'deposit': 0,
                                       'transfer': 0, }
                    else:
                        print('Some accounts in {} are not in valid '
                              'format'.format(
                                             os.path.basename(validAcctsFile)))
        return accts
