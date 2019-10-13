from frontendUtility import requiredInput as ri
from frontendUtility import Modes

class Login():

    def getMode(this):
        validMode = False
        retMode = Modes.NA
        while not validMode:
            mode = ri('Enter the desired mode [agent or machine]: ')
            if mode == 'agent':
                validMode = True
                retMode = Modes.TELLER
            elif mode == 'machine':
                validMode = True
                retMode = Modes.ATM
            elif mode == 'cancel':
                validMode = True
                retMode = Modes.NA
            elif mode == 'logout':
                validMode = True
                retMode = Modes.LOGOUT
            else:
                string = 'Please enter either agent or machine if you wish to continue\nIf you do not wish to continue, please enter either cancel or logout'
                if mode != '?' and mode != 'help':
                    string = 'Unrecognized mode "{}". {}'.format(mode, string)
                print(string)
        return retMode

    def getValidAccts(this, validAcctsFile):
        accts = []
        with open(validAcctsFile, 'r') as f:
            tempAccts = f.readlines()
            if '0000000\n' not in tempAccts:
                print('Error processing {}, no special end account "0000000"'.format(validAcctsFile))
            else:
                for acct in tempAccts:
                    acct = acct.replace('\n', '')
                    if acct == '0000000':
                        break
                    elif acct.isdigit() and len(acct) == 7:
                        accts.append(acct)
                    else:
                        print('Some accounts in {} are not in valid format'.format(validAcctsFile))
        return accts