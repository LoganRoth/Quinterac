"""============================================================================
R3: Valid Accounts List File
============================================================================"""
from frontend_test.test_helper import helper


def test_r3t1(capsys):
    """
    Testing r3t1. All required information stored in folder
    r3_validAccountsListFile.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='r3_validAccountsListFile',
        accts_file='tooLongFile.txt',
        test_id='R3T1'
    )


def test_r3t2(capsys):
    """
    Testing r3t2. All required information stored in folder
    r3_validAccountsListFile.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='r3_validAccountsListFile',
        accts_file='tooShortFile.txt',
        test_id='R3T2'
    )


def test_r3t3(capsys):
    """
    Testing r3t3. All required information stored in folder
    r3_validAccountsListFile.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='r3_validAccountsListFile',
        accts_file='nonDigitFile.txt',
        test_id='R3T3'
    )


def test_r3t4(capsys):
    """
    Testing r3t4. All required information stored in folder
    r3_validAccountsListFile.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='r3_validAccountsListFile',
        accts_file='zeroStartFile.txt',
        test_id='R3T4'
    )


def test_r3t5(capsys):
    """
    Testing r3t5. All required information stored in folder
    r3_validAccountsListFile.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='r3_validAccountsListFile',
        accts_file='acctsAfterSpecialFile.txt',
        test_id='R3T5'
    )


def test_r3t6(capsys):
    """
    Testing r3t6. All required information stored in folder
    r3_validAccountsListFile.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='r3_validAccountsListFile',
        accts_file='noSpecialFile.txt',
        test_id='R3T6'
    )
