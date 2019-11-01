"""============================================================================
R2: Login
============================================================================"""
from frontend_test.test_helper import helper


def test_r2t1(capsys):
    """
    Testing r2t1. All required information stored in folder r2_login.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='r2_login',
        accts_file='validAccountsList.txt',
        test_id='R2T1'
    )


def test_r2t2(capsys):
    """
    Testing r2t2. All required information stored in folder r2_login.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='r2_login',
        accts_file='validAccountsList.txt',
        test_id='R2T2'
    )


def test_r2t3(capsys):
    """
    Testing r2t3. All required information stored in folder r2_login.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='r2_login',
        accts_file='validAccountsList.txt',
        test_id='R2T3'
    )


def test_r2t4(capsys):
    """
    Testing r2t4. All required information stored in folder r2_login.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='r2_login',
        accts_file='validAccountsList.txt',
        test_id='R2T4'
    )
