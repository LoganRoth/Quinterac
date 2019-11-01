"""============================================================================
R1: General
============================================================================"""
from frontend_test.test_helper import helper


def test_r1t1(capsys):
    """
    Testing r1t1. All required information stored in folder r1_general.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='r1_general',
        accts_file='validAccountsList.txt',
        test_id='R1T1'
    )


def test_r1t2(capsys):
    """
    Testing r1t2. All required information stored in folder r1_general.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='r1_general',
        accts_file='validAccountsList.txt',
        test_id='R1T2'
    )
