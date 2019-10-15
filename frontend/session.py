from login import Login
from createacct import CreateAcct
from frontendUtility import requiredInput as ri
from frontendUtility import writeToSummaryFile as wtsf
from frontendUtility import Modes, RetCode, Status

class State():
    START, IDLE, LOGIN, WITHDRAW, DEPOSIT, TRANSFER, CREATEACCT, DELETEACCT, LOGOUT, END = range(10)

class Session():
    def __init__(this, validAcctsFile, summaryFile):
        this.state = State.START
        this.mode = None
        this.validAcctsFile = validAcctsFile
        this.validAcctsList = []
        this.summaryFile = summaryFile
        # this.withdraw = Withdraw()
        # this.deposit = Deposit()
        # this.transfer = Transfer()
        # this.deleteAcct = DeleteAcct()
    
    def handleCommand(this, command):
        if this.state == State.START and (command != 'login' and command != 'logout' and command != '?' and command != 'help' and command != 'off'):
            print('Cannot {} before logging in'.format(command))
        elif command == 'off':
            this.handleCommand('logout')
            this.state = State.END
        elif command == 'login':
            if this.mode is None or this.mode == Modes.NA:
                login = Login()
                this.state = State.LOGIN
                this.mode = login.getMode()
                if login.status == Status.LOGOUT:
                    this.handleCommand('logout')
                else:
                    this.validAcctsList = login.getValidAccts(this.validAcctsFile)
                    this.state = State.IDLE
            else:
                print('Cannot login while already logged in, please logout first')
        elif command == 'logout':
            # logout
            this.mode = Modes.NA
            this.state = State.LOGOUT
            ret = wtsf(this.summaryFile, 'logout')
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
            this.state = State.CREATEACCT
            createAcct = CreateAcct(this.validAcctsList)
            createAcct.createNewAccount()
            if createAcct.status == Status.LOGOUT:
                this.handleCommand('logout')
            elif createAcct.status == Status.OK:
                wtsf(this.summaryFile, command, firstAcct=createAcct.newAcctNum, acctName=createAcct.newAcctName)
                this.state = State.IDLE
        elif command == 'deleteacct' and this.mode == Modes.TELLER:
            # deleteacct
            print('deleteacct')
        else:
            if command != '?' and command != 'help':
                print('Unrecognized command: "{}", Please use a valid command string'.format(command))
            if this.mode is not None and this.mode == Modes.ATM:
                print('Valid Commands: withdraw, deposit, transfer, logout, off')
            elif this.mode is not None and this.mode == Modes.TELLER:
                print('Valid Commands: withdraw, deposit, transfer, createacct, deleteacct, logout, off')
            else:
                print('Valid Commands: login, logout, off')
        
        