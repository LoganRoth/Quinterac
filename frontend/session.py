"""
session.py

This file is the the main control of the Quinterac banking system. All
commands are handled here and the appropriate objects are created to handle
the commands. Writing to the transaction summary file also occurs here.
"""
from frontend.login import Login
from frontend.createacct import CreateAcct
from frontend.deleteacct import DeleteAcct
from frontend.deposit import Deposit
from frontend.withdraw import Withdraw
from frontend.transfer import Transfer
from frontend.frontendUtility import writeToSummaryFile as wtsf
from frontend.frontendUtility import Modes, Status


class State():
    """
    Enumeration class to represent the different possible states that any
    session can be in.
    """
    START, IDLE, LOGIN, WITHDRAW, DEPOSIT, TRANSFER, CREATEACCT, DELETEACCT, \
        LOGOUT, END = range(10)


class Session:
    """
    Class to handle a session of the Quinterac banking system. A valid
    accounts life file and a transaction summary file must be given during
    initialization of an object of this class.

    @param validAcctsFile The file containing the valid accounts list
    @param summaryFile The file to be used for the transaction summary record
    """
    def __init__(self, validAcctsFile, summaryFile):
        self.state = State.START
        self.mode = Modes.NA
        self.validAcctsFile = validAcctsFile
        self.validAcctsList = {}
        self.summaryFile = summaryFile
        self.createAcct = CreateAcct()

    def handleCommand(self, command):
        """
        Handles a given transaction command.

        Off command was also created to shut down the program, this will cause
        a logout and then change the state of the session to "END".
        Commands of "?" and "help" can be used to prompt the user of possible
        valid options.

        @param command The transaction command that needs to be handled
        """
        if self.state == State.START and (command != 'login' and command != '?'
           and command != 'help' and command != 'off'):
            print('Cannot {} before logging in'.format(command))
        elif command == 'off':
            # off
            if self.state != State.START:
                self.handleCommand('logout')
            self.state = State.END
        elif command == 'login':
            # login
            if self.mode == Modes.NA:
                login = Login()
                self.state = State.LOGIN
                self.mode = login.getMode()
                if login.status == Status.LOGOUT:
                    self.handleCommand('logout')
                else:
                    self.validAcctsList = login.getValidAccts(
                                                           self.validAcctsFile)
                    self.createAcct.updateValidAcctsList(self.validAcctsList)
                    self.state = State.IDLE
            else:
                print('Cannot login while already logged in, please logout '
                      'first')
        elif command == 'logout':
            # logout
            self.mode = Modes.NA
            self.state = State.LOGOUT
            wtsf(self.summaryFile, 'logout')
            self.state = State.END
        elif command == 'withdraw':
            # withdraw
            withdraw = Withdraw(self.validAcctsList, self.mode)
            self.state = State.WITHDRAW
            withdrawAcct = withdraw.getAcct()
            if withdraw.status == Status.LOGOUT:
                self.handleCommand('logout')
                return
            if withdraw.status == Status.OK:
                withdrawAmount = withdraw.getNumber()
            if withdraw.status == Status.LOGOUT:
                self.handleCommand('logout')
                return
            elif withdraw.status == Status.OK:
                self.validAcctsList[withdrawAcct]['withdraw']\
                                                              += withdrawAmount
                wtsf(self.summaryFile, command, firstAcct=withdrawAcct,
                     amount=withdrawAmount)
                self.state = State.IDLE
        elif command == 'deposit':
            # deposit
            deposit = Deposit(self.validAcctsList, self.mode)
            self.state = State.DEPOSIT
            depositAcct = deposit.getAcct()
            if deposit.status == Status.LOGOUT:
                self.handleCommand('logout')
                return
            if deposit.status == Status.OK:
                depositAmount = deposit.getNumber()
            if deposit.status == Status.LOGOUT:
                self.handleCommand('logout')
                return
            elif deposit.status == Status.OK:
                self.validAcctsList[depositAcct]['deposit'] += depositAmount
                wtsf(self.summaryFile, command, firstAcct=depositAcct,
                     amount=depositAmount)
                self.state = State.IDLE
        elif command == 'transfer':
            # transfer
            transfer = Transfer(self.validAcctsList, self.mode)
            message = 'Input your account number: '
            transferFromAcct = transfer.getAcct(message)
            if transfer.status == Status.LOGOUT:
                self.handleCommand('logout')
                return
            if transfer.status == Status.OK:
                transferAmount = transfer.getNumber(transferFromAcct)
            if transfer.status == Status.LOGOUT:
                self.handleCommand('logout')
                return
            if transfer.status == Status.OK:
                message = "Input the destination account number: "
                transferToAcct = transfer.getAcct(message)
            if transfer.status == Status.LOGOUT:
                self.handleCommand('logout')
                return
            elif transferFromAcct == transferToAcct:
                print("sorry cannot transfer to your own account")
            elif transfer.status == Status.OK:
                self.validAcctsList[transferFromAcct]['transfer'] += \
                                                                 transferAmount
                wtsf(self.summaryFile, command, firstAcct=transferFromAcct,
                     amount=transferAmount, secondAcct=transferToAcct)
                self.state = State.IDLE

        elif command == 'createacct' and self.mode == Modes.TELLER:
            # createacct
            self.state = State.CREATEACCT
            self.createAcct.createNewAccount()
            if self.createAcct.status == Status.LOGOUT:
                self.handleCommand('logout')
            elif self.createAcct.status == Status.OK:
                wtsf(self.summaryFile, command,
                     firstAcct=self.createAcct.newAcctNum,
                     acctName=self.createAcct.newAcctName)
                self.state = State.IDLE
        elif command == 'deleteacct' and self.mode == Modes.TELLER:
            # deleteacct
            self.state = State.DELETEACCT
            deleteacct = DeleteAcct(self.validAcctsList)
            deleteacct.deleteOldAccount()
            if deleteacct.status == Status.LOGOUT:
                self.handleCommand('logout')
            elif deleteacct.status == Status.OK:
                wtsf(self.summaryFile, command,
                     firstAcct=deleteacct.oldAcctNum,
                     acctName=deleteacct.oldAcctName)
                self.state = State.IDLE
        else:
            # Helper prompts
            if command != '?' and command != 'help':
                print('Unrecognized command: "{}", Please use a valid command '
                      'string'.format(command))
            if self.mode is not None and self.mode == Modes.ATM:
                print('Valid Commands: withdraw, deposit, transfer, logout, '
                      'off')
            elif self.mode is not None and self.mode == Modes.TELLER:
                print('Valid Commands: withdraw, deposit, transfer, '
                      'createaccct, deleteacct, logout, off')
            else:
                print('Valid Commands: login, off')
