"""
utility.py

This file contains classes and functions that are used throughout the rest of
the files which make up the Quinterac banking system.
"""
import os


class RetCode():
    """
    Enum class for return codes to ensure that any function that reuturns a
    return code returns it in a standardized way.
    """
    OK, ERROR, ABORTING = range(3)


def isFileValid(fileToTest, nameOfFile):
    """
    Checks if the given file is a valid file, if not, prints out that the
    indicated file could not be found.

    @param fileToTest The file to check if it is valid
    @param nameOfFile The name of the file under test.
    """
    if fileToTest is None or not os.path.exists(fileToTest):
        print('{} file not found'.format(nameOfFile))
        return False
    return True


class WhiteBoxPrinter:
    """
    Class to set up a printer if whitebox testing is being done.
    """
    def __init__(self, whitebox):
        self.whitebox = whitebox

    def print(self, str):
        """
        Whitebox print function.
        """
        if self.whitebox:
            print(str)
