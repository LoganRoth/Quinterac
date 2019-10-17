"""
frontendUtility.py

This file contains classes and functions that are used throughout the rest of
the files which make up the frontend.
"""


class RetCode():
    """
    Enum class for return codes to ensure that any function that reuturns a
    return code returns it in a standardized way.
    """
    OK, ERROR, ABORTING = range(3)


class Modes():
    """
    Enum class to represent the different modes that the system can be in.
    NA implies that it is in neither ATM or TELLER mode which means that
    it is waiting to be logged in.
    """
    NA, ATM, TELLER = range(3)


class Status():
    """
    Enum class to represent the different possible statuses of an object.
    This helps to facilitate the ability to alaways logout or cancel any
    command during its execution.
    """
    OK, ERROR, CANCEL, LOGOUT = range(4)


def requiredInput(prompt='Quinterac: ', toLower=True):
    """
    Function to get input from the user and not allow empty input.
    toLower variable can be used to change whether or not the user input is
    converted to all lowercase or not.

    This function removes trailing and leading whitespace from the input and
    also by default will change the input to all lowercase characters.
    """
    noInput = True
    userInput = ''
    while noInput:
        userInput = input(prompt)
        if len(userInput) > 0:
            noInput = False
    if toLower:
        userInput = userInput.lower().strip()
    else:
        userInput = userInput.strip()
    return userInput


def writeToSummaryFile(summaryFile, command, firstAcct='0000000', amount='000',
                       secondAcct='0000000', acctName='***'):
    """
    Function to write to the transaction summary file to ensure that the
    writing is performed in a standardized way.

    @param summaryFile The file to be used for the transaction summary record
    @param command The transaction command that is calling this function
    @param firstAcct The first account number
    @param amount The amoont being transferred/withdrawn/deposited
    @param secondAcct The second account number
    @param acctName The account name of the the account being created or
                    deleted
    """
    txMsg = formatTransactionMessage(command, firstAcct, amount, secondAcct,
                                     acctName)
    ret = RetCode.OK
    if txMsg is not None:
        try:
            with open(summaryFile, 'a') as f:
                f.write(txMsg)
        except Exception:
            print('Failure while writing to summary file. File: '
                  '{}'.format(summaryFile))
            ret = RetCode.ERROR
    else:
        ret = RetCode.ERROR
    return ret


def formatTransactionMessage(command, firstAcct, amount, secondAcct, acctName):
    """
    Function to format the given transaction elements into the proper string
    format. If the amount or code are None then the message will be nothing and
    will not write to the file as this can only occur if some error has
    occurred.

    @param command The transaction command that is calling this function
    @param firstAcct The first account number
    @param amount The amoont being transferred/withdrawn/deposited
    @param secondAcct The second account number
    @param acctName The account name of the the account being created or
                    deleted
    """
    code = lookupCommandCode(command)
    amount = formatAmountString(amount)
    if amount is None or code is None:
        txMsg = None
    else:
        if command == 'logout':
            txMsg = '{}\n'.format(code)
        else:
            txMsg = '{} {} {} {} {}\n'.format(code, firstAcct, amount,
                                              secondAcct, acctName)
    return txMsg


def formatAmountString(amount):
    """
    Function to convert the given amount string into a cents format where
    there is no decimal point, at least 3 digits, and at most 8 digits.

    Amount must be given as either cents or a currency format (ie, #.##).
    Also ensures that the number given is converted to cents with at least 3
    digits (ie, 1 is converted to 001).
    """
    try:
        if not isinstance(amount, str):
            amount = '{}'.format(amount)
        if '.' in amount:
            dollars, cents = amount.split('.')
            if len(dollars) < 1:  # means amount is in form ".#"
                dollars = '0'
            if len(cents) < 1:  # means amount is in form "#."
                cents = '00'
            # means that somehow a non number character is in either the dollar
            # or the cents
            if not dollars.isdigit() or not cents.isdigit():
                raise ValueError
            # means too many digits after ".", ie, 1.000
            if len(amount.split('.')[-1]) > 2:
                cents = cents[:2]
            # means only one digit after ".", ie, 1.0
            elif len(amount.split('.')[-1]) == 1:
                cents = '{}0'.format(cents)
            amount = '{}{}'.format(dollars, cents)
        elif len(amount) < 3:
            # if amount is single digit, need to add 2 leading 0s
            if len(amount) == 1:
                amount = '00{}'.format(amount)
            # if amount is two digits, need to add 1 leading 0s
            elif len(amount) == 2:
                amount = '0{}'.format(amount)
        if len(amount) > 8:
            print('Amount too large: {} cents. Must be less than $999999.99.')
            amount = None
    except ValueError:
        print('Failure when writing amount to summary file. Amount: '
              '{}'.format(amount))
        amount = None
    return amount


def lookupCommandCode(command):
    """
    Function to look up the corresponding transaction code for each of the
    transaction commands.
    """
    code = None
    if command == 'withdraw':
        code = 'WTH'
    elif command == 'deposit':
        code = 'DEP'
    elif command == 'transfer':
        code = 'XFR'
    elif command == 'createacct':
        code = 'NEW'
    elif command == 'deleteacct':
        code = 'DEL'
    elif command == 'logout':
        code = 'EOS'
    else:
        print('Unrecognized command sent to code lookup. Command: '
              '{}'.format(command))
    return code
