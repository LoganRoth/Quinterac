import tempfile
from importlib import reload
import os
import io
import sys
import frontend.app as app

path = os.path.dirname(os.path.abspath(__file__))


"""============================================================================
R1: General
============================================================================"""


def test_r1t1(capsys):
    """
    Testing r1t1. All required information stored in folder r1.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='general',
        accts_file='validAccountsList.txt',
        test_id='R1T1'
    )


def test_r1t2(capsys):
    """
    Testing r1t2. All required information stored in folder r1.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='general',
        accts_file='validAccountsList.txt',
        test_id='R1T2'
    )


"""============================================================================
R2: Login
============================================================================"""


def test_r2t1(capsys):
    """
    Testing r2t1. All required information stored in folder r2.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='login',
        accts_file='validAccountsList.txt',
        test_id='R2T1'
    )


def test_r2t2(capsys):
    """
    Testing r2t2. All required information stored in folder r2.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='login',
        accts_file='validAccountsList.txt',
        test_id='R2T2'
    )


def test_r2t3(capsys):
    """
    Testing r2t3. All required information stored in folder r2.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='login',
        accts_file='validAccountsList.txt',
        test_id='R2T3'
    )


def test_r2t4(capsys):
    """
    Testing r2t4. All required information stored in folder r2.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='login',
        accts_file='validAccountsList.txt',
        test_id='R2T4'
    )


"""============================================================================
R3: Valid Accounts List File
============================================================================"""


# def test_r3t1(capsys):
#     """
#     Testing r3t1. All required information stored in folder r3.

#     @param capsys Object created by pytest to capture stdout and stderr
#     """
#     helper(
#         capsys=capsys,
#         test_set='validAccountsListFile',
#         accts_file='validAccountsList.txt',
#         test_id='R3T1'
#     )


"""============================================================================
R4: Logout
============================================================================"""


# def test_r4t1(capsys):
#     """
#     Testing r4t1. All required information stored in folder r4.

#     @param capsys Object created by pytest to capture stdout and stderr
#     """
#     helper(
#         capsys=capsys,
#         test_set='logout',
#         accts_file='validAccountsList.txt',
#         test_id='R4T1'
#     )


"""============================================================================
R5: Create Account
============================================================================"""


def test_r5t1(capsys):
    """
    Testing r5t1. All required information stored in folder r5.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='createAccount',
        accts_file='emptyValidAccountsList.txt',
        test_id='R5T1'
    )


def test_r5t2(capsys):
    """
    Testing r5t2. All required information stored in folder r5.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='createAccount',
        accts_file='emptyValidAccountsList.txt',
        test_id='R5T2'
    )


def test_r5t3(capsys):
    """
    Testing r5t3. All required information stored in folder r5.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='createAccount',
        accts_file='emptyValidAccountsList.txt',
        test_id='R5T3'
    )


def test_r5t4(capsys):
    """
    Testing r5t4. All required information stored in folder r5.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='createAccount',
        accts_file='emptyValidAccountsList.txt',
        test_id='R5T4'
    )


def test_r5t5(capsys):
    """
    Testing r5t5. All required information stored in folder r5.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='createAccount',
        accts_file='emptyValidAccountsList.txt',
        test_id='R5T5'
    )


def test_r5t6(capsys):
    """
    Testing r5t6. All required information stored in folder r5.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='createAccount',
        accts_file='emptyValidAccountsList.txt',
        test_id='R5T6'
    )


def test_r5t7(capsys):
    """
    Testing r5t7. All required information stored in folder r5.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='createAccount',
        accts_file='emptyValidAccountsList.txt',
        test_id='R5T7'
    )


def test_r5t8(capsys):
    """
    Testing r5t8. All required information stored in folder r5.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='createAccount',
        accts_file='acctWithAll1s.txt',
        test_id='R5T8'
    )


def test_r5t9(capsys):
    """
    Testing r5t9. All required information stored in folder r5.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='createAccount',
        accts_file='emptyValidAccountsList.txt',
        test_id='R5T9'
    )


def test_r5t10(capsys):
    """
    Testing r5t10. All required information stored in folder r5.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='createAccount',
        accts_file='emptyValidAccountsList.txt',
        test_id='R5T10'
    )


def test_r5t11(capsys):
    """
    Testing r5t11. All required information stored in folder r5.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='createAccount',
        accts_file='emptyValidAccountsList.txt',
        test_id='R5T11'
    )


def test_r5t12(capsys):
    """
    Testing r5t12. All required information stored in folder r5.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='createAccount',
        accts_file='emptyValidAccountsList.txt',
        test_id='R5T12'
    )


def test_r5t13(capsys):
    """
    Testing r5t13. All required information stored in folder r5.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='createAccount',
        accts_file='emptyValidAccountsList.txt',
        test_id='R5T13'
    )


def test_r5t14(capsys):
    """
    Testing r5t14. All required information stored in folder r5.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='createAccount',
        accts_file='emptyValidAccountsList.txt',
        test_id='R5T14'
    )


"""============================================================================
R6: Delete Account
============================================================================"""


# def test_r4t1(capsys):
#     """
#     Testing r4t1. All required information stored in folder r4.

#     @param capsys Object created by pytest to capture stdout and stderr
#     """
#     helper(
#         capsys=capsys,
#         test_set='logout',
#         accts_file='validAccountsList.txt',
#         test_id='R4T1'
#     )


"""============================================================================
R7: Deposit
============================================================================"""


# def test_r4t1(capsys):
#     """
#     Testing r4t1. All required information stored in folder r4.

#     @param capsys Object created by pytest to capture stdout and stderr
#     """
#     helper(
#         capsys=capsys,
#         test_set='logout',
#         accts_file='validAccountsList.txt',
#         test_id='R4T1'
#     )


"""============================================================================
R8: Withdraw
============================================================================"""


# def test_r4t1(capsys):
#     """
#     Testing r4t1. All required information stored in folder r4.

#     @param capsys Object created by pytest to capture stdout and stderr
#     """
#     helper(
#         capsys=capsys,
#         test_set='logout',
#         accts_file='validAccountsList.txt',
#         test_id='R4T1'
#     )


"""============================================================================
R9: Transfer
============================================================================"""


# def test_r4t1(capsys):
#     """
#     Testing r4t1. All required information stored in folder r4.

#     @param capsys Object created by pytest to capture stdout and stderr
#     """
#     helper(
#         capsys=capsys,
#         test_set='logout',
#         accts_file='validAccountsList.txt',
#         test_id='R4T1'
#     )


def helper(capsys, test_set, accts_file, test_id):
    """
    Helper function that test requirements for the frontend app

    @param capsys Object created by pytest to capture stdout and stderr
    @param test_set The test set to use
    @param accts_file The valid accounts list file to use for the test
    @param test_id ID of the specific test to run
    """

    # cleanup package
    reload(app)

    # locate test case folder:
    case_folder = os.path.join(path, test_set)

    # read terminal input:
    with open(
        os.path.join(
            case_folder, 'input', '{}.txt'.format(test_id))) as rf:
        terminal_input = rf.read().splitlines()

    # # read expected tail portion of the terminal output:
    # NOTE: Don't know if we really need to do this.
    # with open(
    #     os.path.join(
    #         case_folder, 'terminal_output_tail.txt')) as rf:
    #     terminal_output_tail = rf.read().splitlines()

    # create a temporary file in the system to store output transactions
    temp_fd, temp_file = tempfile.mkstemp()
    transaction_summary_file = temp_file

    # prepare program parameters
    sys.argv = [
        'app.py',
        os.path.join(path, 'testValidAccountsListFiles', accts_file),
        transaction_summary_file]

    # set terminal input
    sys.stdin = io.StringIO(
        os.linesep.join(terminal_input))

    # run the program
    app.main()

    # capture terminal output / errors
    # assuming that in this case we don't use stderr
    # _, _ = capsys.readouterr()

    # split terminal output in lines
    # out_lines = out.splitlines()

    # # compare terminal outputs at the end.`
    # NOTE: May not need to do
    # for i in range(1, len(terminal_output_tail)+1):
    #     index = i * -1
    #     assert terminal_output_tail[index] == out_lines[index]

    # compare transactions:
    with open(transaction_summary_file, 'r') as of:
        content = of.read()
        with open(os.path.join(case_folder, 'output',
                  '{}out.txt'.format(test_id)), 'r') as exp_file_of:
            expected_content = exp_file_of.read()
            assert content == expected_content

    # clean up
    os.close(temp_fd)
    os.remove(temp_file)
