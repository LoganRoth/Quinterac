class RetCode():
    OK, ERROR, ABORTING = range(3)

class Modes():
    NA, ATM, TELLER, LOGOUT = range(4)

def requiredInput(prompt='Quinterac: '):
    noInput = True
    userInput = ''
    while noInput:
        userInput = input(prompt)
        if len(userInput) > 0:
            noInput = False
    return userInput.lower()