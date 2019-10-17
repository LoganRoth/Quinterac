"""
session.py

This file is the the main control of the Quinterac banking system. All
commands are handled here and the appropriate objects are created to handle
the commands. Writing to the transaction summary file also occurs here.
"""
from login import Login
from createacct import CreateAcct
from deleteacct import DeleteAcct
from deposit import Deposit
from withdraw import Withdraw
from transfer import Transfer
from frontendUtility import writeToSummaryFile as wtsf
from frontendUtility import Modes, Status


class State():
    """
    Enumeration class to represent the different possible states that any
    session can be in.
    """
    START, IDLE, LOGIN, WITHDRAW, DEPOSIT, TRANSFER, CREATEACCT, DELETEACCT, \
        LOGOUT, END = range(10)


class Session():
    """
    Class to handle a session of the Quinterac banking system. A valid
    accounts life file and a transaction summary file must be given during
    initialization of an object of this class.

    @param validAcctsFile The file containing the valid accounts list
    @param summaryFile The file to be used for the transaction summary record
    """
    def __init__(this, validAcctsFile, summaryFile):
        this.state = State.START
        this.mode = Modes.NA
        this.validAcctsFile = validAcctsFile
        this.validAcctsList = {}
        this.summaryFile = summaryFile

    def handleCommand(this, command):
        """
        Handles a given transaction command.

        Off command was also created to shut down the program, this will cause
        a logout and then change the state of the session to "END".
        Commands of "?" and "help" can be used to prompt the user of possible
        valid options.

        @param command The transaction command that needs to be handled
        """
        if this.state == State.START and (command != 'login' and command != '?'
           and command != 'help' and command != 'off'):
            print('Cannot {} before logging in'.format(command))
        elif command == 'off':
            # off
            if this.state != State.START:
                this.handleCommand('logout')
            this.state = State.END
        elif command == 'login':
            # login
            if this.mode == Modes.NA:
                login = Login()
                this.state = State.LOGIN
                this.mode = login.getMode()
                if login.status == Status.LOGOUT:
                    this.handleCommand('logout')
                else:
                    this.validAcctsList = login.getValidAccts(
                                                           this.validAcctsFile)
                    this.state = State.IDLE
            else:
                print('Cannot login while already logged in, please logout '
                      'first')
        elif command == 'logout':
            # logout
            this.mode = Modes.NA
            this.state = State.LOGOUT
            wtsf(this.summaryFile, 'logout')
            this.state = State.END
        elif command == 'withdraw':
            # withdraw
            withdraw = Withdraw(this.validAcctsList, this.mode)
            this.state = State.WITHDRAW
            withdrawAcct = withdraw.getAcct()
            if withdraw.status == Status.LOGOUT:
                this.handleCommand('logout')
            if withdraw.status == Status.OK:
                withdrawAmount = withdraw.getNumber()
            if withdraw.status == Status.LOGOUT:
                this.handleCommand('logout')
            elif withdraw.status == Status.OK:
                this.validAcctsList[withdrawAcct]['withdraw']\
                                                              += withdrawAmount
                wtsf(this.summaryFile, command, firstAcct=withdrawAcct,
                     amount=withdrawAmount)
                this.state = State.IDLE
        elif command == 'deposit':
            # deposit
            deposit = Deposit(this.validAcctsList, this.mode)
            this.state = State.DEPOSIT
            depositAcct = deposit.getAcct()
            if deposit.status == Status.LOGOUT:
                this.handleCommand('logout')
            if deposit.status == Status.OK:
                depositAmount = deposit.getNumber()
            if deposit.status == Status.LOGOUT:
                this.handleCommand('logout')
            elif deposit.status == Status.OK:
                this.validAcctsList[depositAcct]['deposit'] += depositAmount
                wtsf(this.summaryFile, command, firstAcct=depositAcct,
                     amount=depositAmount)
                this.state = State.IDLE
        elif command == 'transfer':
            # transfer
            transfer = Transfer(this.validAcctsList, this.mode)
            message = 'Input your account number: '
            transferFromAcct = transfer.getAcct(message)
            if transfer.status == Status.LOGOUT:
                this.handleCommand('logout')
            if transfer.status == Status.OK:
                transferAmount = transfer.getNumber(transferFromAcct)
            if transfer.status == Status.LOGOUT:
                this.handleCommand('logout')
            if transfer.status == Status.OK:
                message = "Input the destination account number: "
                transferToAcct = transfer.getAcct(message)
            if transfer.status == Status.LOGOUT:
                this.handleCommand('logout')
            elif transferFromAcct == transferToAcct:
                print("sorry cannot transfer to your own account")
            elif transfer.status == Status.OK:
                this.validAcctsList[transferFromAcct]['transfer'] += \
                                                                 transferAmount
                wtsf(this.summaryFile, command, firstAcct=transferFromAcct,
                     amount=transferAmount, secondAcct=transferToAcct)
                this.state = State.IDLE

        elif command == 'createacct' and this.mode == Modes.TELLER:
            # createacct
            this.state = State.CREATEACCT
            createAcct = CreateAcct(this.validAcctsList)
            createAcct.createNewAccount()
            if createAcct.status == Status.LOGOUT:
                this.handleCommand('logout')
            elif createAcct.status == Status.OK:
                wtsf(this.summaryFile, command,
                     firstAcct=createAcct.newAcctNum,
                     acctName=createAcct.newAcctName)
                this.state = State.IDLE
        elif command == 'deleteacct' and this.mode == Modes.TELLER:
            # deleteacct
            this.state = State.DELETEACCT
            deleteacct = DeleteAcct(this.validAcctsList)
            deleteacct.deleteOldAccount()
            if deleteacct.status == Status.LOGOUT:
                this.handleCommand('logout')
            elif deleteacct.status == Status.OK:
                wtsf(this.summaryFile, command,
                     firstAcct=deleteacct.oldAcctNum,
                     acctName=deleteacct.oldAcctName)
                this.state = State.IDLE
        else:
            # Helper prompts
            if command != '?' and command != 'help':
                print('Unrecognized command: "{}", Please use a valid command '
                      'string'.format(command))
            if this.mode is not None and this.mode == Modes.ATM:
                print('Valid Commands: withdraw, deposit, transfer, logout, '
                      'off')
            elif this.mode is not None and this.mode == Modes.TELLER:
                print('Valid Commands: withdraw, deposit, transfer, '
                      'createaccct, deleteacct, logout, off')
            else:
                print('Valid Commands: login, off')
