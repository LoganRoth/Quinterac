class RetCode():
    OK, ERROR, ABORTING = range(3)


class Modes():
    NA, ATM, TELLER = range(3)


class Status():
    OK, ERROR, CANCEL, LOGOUT = range(4)


class State():
    START, IDLE, LOGIN, WITHDRAW, DEPOSIT, TRANSFER, CREATEACCT, DELETEACCT, LOGOUT, END = range(10)


def requiredInput(prompt='Quinterac: ', toLower=True):
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

def writeToSummaryFile(summaryFile, command, firstAcct='0000000', amount='0.00', secondAcct='0000000', acctName='***'):
    if command == 'logout':
        txMsg = 'EOS\n'
    else:
        txMsg = formatTransactionMessage(command, firstAcct, amount, secondAcct, acctName)
    ret = RetCode.OK
    if txMsg is not None:
        try:
            with open(summaryFile, 'a') as f:
                f.write(txMsg)
        except Exception as e:
            print('Failure while writing to summary file. File: {}'.format(summaryFile))
            ret = RetCode.ERROR
    else:
        ret = RetCode.ERROR
    return ret
            
def formatTransactionMessage(command, firstAcct, amount, secondAcct, acctName):
    code = lookupCommandCode(command)
    amount = formatAmountString(amount)
    if amount is None or code is None:
        txMsg = None
    else:
        txMsg = '{} {} {} {} {}\n'.format(code, firstAcct, amount, secondAcct, acctName)
    return txMsg

def formatAmountString(amount):
    try:
        if not isinstance(amount, str):
            amount = '{:,.2f}'.format(amount)
        elif '.' in amount:
            dollars, cents = amount.split('.')
            if len(dollars) < 1:  # means amount is in form ".#" 
                dollars = '0'
            if len(cents) < 1:  # means amount is in form "#."
                cents = '00'
            if not dollars.isdigit() or not cents.isdigit():
                raise ValueError  # means that somehow a non number character is in either the dollar or the cents
            if len(amount.split('.')[-1]) > 2:  # means too many digits after ".", ie, 1.000
                cents = cents[:2]
            elif len(amount.split('.')[-1]) == 1:  # means only one digit after ".", ie, 1.0
                cents = '{}0'.format(cents)
            amount = '{}.{}'.format(dollars, cents)
        elif '.' not in amount: # means no decimal point in the string after ".", ie, 1
            amount = '{}.00'.format(amount)
    except ValueError as e:
        print('Failure when writing amount to summary file. Amount: {}'.format(amount))
        amount = None
    return amount

def lookupCommandCode(command):
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
    else:
        print('Unrecognized command sent to code lookup. Command: {}'.format(command))
    return code
    