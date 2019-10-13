from login import Login
from frontendUtility import requiredInput as ri
from frontendUtility import Modes

class State():
    START, IDLE, LOGIN, WITHDRAW, DEPOSIT, TRANSFER, CREATEACCT, DELETEACCT, LOGOUT, END = range(10)

class Session():
    def __init__(this, validAcctsFile, summaryFile):
        this.state = State.START
        this.mode = None
        this.validAcctsFile = validAcctsFile
        this.validAcctsList = []
        this.summaryFile = summaryFile
        this.login = Login()
        # this.withdraw = Withdraw()
        # this.deposit = Deposit()
        # this.transfer = Transfer()
        # this.createAcct = CreateAcct()
        # this.deleteAcct = DeleteAcct()
        # this.logout = Logout()
    
    def handleCommand(this, command):
        if this.state == State.START and (command != 'login' and command != 'logout' and command != '?' and command != 'help'):
            print('Cannot {} before logging in'.format(command))
        elif command == 'login':
            if this.mode is None or this.mode == Modes.NA:
                this.state = State.LOGIN
                this.mode = this.login.getMode()
                if this.mode == Modes.LOGOUT:
                    this.handleCommand('logout')
                    return
                this.validAcctsList = this.login.getValidAccts(this.validAcctsFile)
                this.state = State.IDLE
            else:
                print('Cannot login while already logged in, please logout first')
        elif command == 'logout':
            # logout
            this.state = State.LOGOUT
            print('logout')
            this.state = State.END
        elif command == 'withdraw':
            # withdraw
            print('withdraw')
        elif command == 'deposit':
            # deposit
            print('deposit')
        elif command == 'transfer':
            # transfer
            print('transfer')
        elif command == 'createacct' and this.mode == Modes.TELLER:
            # createacct
            print('createacct')
        elif command == 'deleteacct' and this.mode == Modes.TELLER:
            # deleteacct
            print('deleteacct')
        else:
            if command != '?' and command != 'help':
                print('Unrecognized command: "{}", Please use a valid command string'.format(command))
            if this.mode is not None and this.mode == Modes.ATM:
                print('Valid Commands: withdraw, deposit, transfer, logout')
            elif this.mode is not None and this.mode == Modes.TELLER:
                print('Valid Commands: withdraw, deposit, transfer, createacct, deleteacct, logout')
            else:
                print('Valid Commands: login, logout')
        
        