from frontendUtility import requiredInput as ri
from frontendUtility import Status

class CreateAcct():
    def __init__(this, validAcctsList):
        this.validAcctsList = validAcctsList
        this.status = Status.OK
        this.newAcctNum = None
        this.newAcctName = None

    def createNewAccount(this):
        num = this._getNewAcctNum()
        if this.status != Status.OK:
            return
        name = this._getNewAcctName()
        if this.status != Status.OK:
            return
        this.newAcctNum = num
        this.newAcctName = name


    def _getNewAcctNum(this):
        validNum = False
        num = None
        while not validNum:
            inNum = ri('Input the account number for the new account: ')
            if inNum == 'logout':
                this.status = Status.LOGOUT
                validNum = True
            elif inNum == 'cancel':
                this.status = Status.CANCEL
                validNum = True
            elif not inNum.isdigit():
                print('Account numbers must be comprised of only digits. Please choose a different account number.')
            elif len(inNum) != 7:
                print('Account numbers must be exactly 7 digits in length. Please choose a different account number.')
            elif inNum == '0000000':
                print('0000000 is a reserved account number. Please choose a different account number.')
            elif inNum[0] == '0':
                print('Account numbers must not begin with a "0". Please choose a different account number.')
            elif inNum in this.validAcctsList:
                print('{} is already in use. Please choose a different account number.'.format(inNum))
            else:
                validNum = True
                num = inNum
        return num

    def _getNewAcctName(this):
        validName = False
        name = None
        while not validName:
            inName = ri('Input the account name for the new account: ', toLower=False)
            if inName == 'logout':
                this.status = Status.LOGOUT
                validName = True
            elif inName == 'cancel':
                this.status = Status.CANCEL
                validName = True
            elif len(inName) < 3 or len(inName) > 30:
                print('Account names must be between 3 and 30 characters. Please choose a different account name.')
            elif not inName.replace(' ', '').isalnum():
                print('Account names must only contain alphanumeric characters and spaces. Please choose a different account name.')
            else:
                validName = True
                name = inName
        return name
    