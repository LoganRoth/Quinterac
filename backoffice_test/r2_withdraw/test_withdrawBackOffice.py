"""============================================================================
R2: Withdraw
============================================================================"""
from backoffice_test.test_helper import helper


def test_r2t1(capsys):
    """
    Testing r2t1. All required information stored in folder r1_general.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='r2_withdraw',
        test_id='R2T1'
    )


def test_r2t2(capsys):
    """
    Testing r2t2. All required information stored in folder r1_general.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='r2_withdraw',
        test_id='R2T2'
    )


def test_r2t3(capsys):
    """
    Testing r2t3. All required information stored in folder r1_general.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='r2_withdraw',
        test_id='R2T3'
    )
