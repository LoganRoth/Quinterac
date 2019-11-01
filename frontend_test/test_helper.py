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
    Testing r1t1. All required information stored in folder general.

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
    Testing r1t2. All required information stored in folder general.

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
    Testing r2t1. All required information stored in folder login.

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
    Testing r2t2. All required information stored in folder login.

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
    Testing r2t3. All required information stored in folder login.

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
    Testing r2t4. All required information stored in folder login.

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


def test_r3t1(capsys):
    """
    Testing r3t1. All required information stored in folder r3.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='validAccountsListFile',
        accts_file='tooLongFile.txt',
        test_id='R3T1'
    )


def test_r3t2(capsys):
    """
    Testing r3t2. All required information stored in folder r3.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='validAccountsListFile',
        accts_file='tooShortFile.txt',
        test_id='R3T2'
    )


def test_r3t3(capsys):
    """
    Testing r3t3. All required information stored in folder r3.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='validAccountsListFile',
        accts_file='nonDigitFile.txt',
        test_id='R3T3'
    )


def test_r3t4(capsys):
    """
    Testing r3t4. All required information stored in folder r3.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='validAccountsListFile',
        accts_file='zeroStartFile.txt',
        test_id='R3T4'
    )


def test_r3t5(capsys):
    """
    Testing r3t5. All required information stored in folder r3.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='validAccountsListFile',
        accts_file='acctsAfterSpecialFile.txt',
        test_id='R3T5'
    )


def test_r3t6(capsys):
    """
    Testing r3t6. All required information stored in folder r3.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='validAccountsListFile',
        accts_file='noSpecialFile.txt',
        test_id='R3T6'
    )


"""============================================================================
R4: Logout
============================================================================"""


def test_r4t1(capsys):
    """
    Testing r4t1. All required information stored in folder r4.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='logout',
        accts_file='validAccountsList.txt',
        test_id='R4T1'
    )


def test_r4t2(capsys):
    """
    Testing r4t2. All required information stored in folder r4.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='logout',
        accts_file='validAccountsList.txt',
        test_id='R4T2'
    )


def test_r4t3(capsys):
    """
    Testing r4t3. All required information stored in folder r4.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='logout',
        accts_file='validAccountsList.txt',
        test_id='R4T3'
    )


def test_r4t4(capsys):
    """
    Testing r4t4. All required information stored in folder r4.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='logout',
        accts_file='validAccountsList.txt',
        test_id='R4T4'
    )


def test_r4t5(capsys):
    """
    Testing r4t5. All required information stored in folder r4.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='logout',
        accts_file='validAccountsList.txt',
        test_id='R4T5'
    )


def test_r4t6(capsys):
    """
    Testing r4t6. All required information stored in folder r4.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='logout',
        accts_file='validAccountsList.txt',
        test_id='R4T6'
    )


def test_r4t7(capsys):
    """
    Testing r4t7. All required information stored in folder r4.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='logout',
        accts_file='validAccountsList.txt',
        test_id='R4T7'
    )


def test_r4t8(capsys):
    """
    Testing r4t8. All required information stored in folder r4.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='logout',
        accts_file='validAccountsList.txt',
        test_id='R4T8'
    )


def test_r4t9(capsys):
    """
    Testing r4t9. All required information stored in folder r4.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='logout',
        accts_file='validAccountsList.txt',
        test_id='R4T9'
    )


"""============================================================================
R5: Create Account
============================================================================"""


def test_r5t1(capsys):
    """
    Testing r5t1. All required information stored in folder createAccount.

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
    Testing r5t2. All required information stored in folder createAccount.

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
    Testing r5t3. All required information stored in folder createAccount.

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
    Testing r5t4. All required information stored in folder createAccount.

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
    Testing r5t5. All required information stored in folder createAccount.

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
    Testing r5t6. All required information stored in folder createAccount.

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
    Testing r5t7. All required information stored in folder createAccount.

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
    Testing r5t8. All required information stored in folder createAccount.

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
    Testing r5t9. All required information stored in folder createAccount.

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
    Testing r5t10. All required information stored in folder createAccount.

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
    Testing r5t11. All required information stored in folder createAccount.

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
    Testing r5t12. All required information stored in folder createAccount.

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
    Testing r5t13. All required information stored in folder createAccount.

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
    Testing r5t14. All required information stored in folder createAccount.

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


def test_r6t1(capsys):
    """
    Testing r6t1. All required information stored in folder r6.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='deleteAccount',
        accts_file='validAccountsList.txt',
        test_id='R6T1'
    )


def test_r6t2(capsys):
    """
    Testing r6t2. All required information stored in folder r6.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='deleteAccount',
        accts_file='validAccountsList.txt',
        test_id='R6T2'
    )


def test_r6t3(capsys):
    """
    Testing r6t3. All required information stored in folder r6.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='deleteAccount',
        accts_file='validAccountsList.txt',
        test_id='R6T3'
    )


def test_r6t4(capsys):
    """
    Testing r6t4. All required information stored in folder r6.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='deleteAccount',
        accts_file='validAccountsList.txt',
        test_id='R6T4'
    )


def test_r6t5(capsys):
    """
    Testing r6t5. All required information stored in folder r6.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='deleteAccount',
        accts_file='validAccountsList.txt',
        test_id='R6T5'
    )


def test_r6t6(capsys):
    """
    Testing r6t6. All required information stored in folder r6.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='deleteAccount',
        accts_file='validAccountsList.txt',
        test_id='R6T6'
    )


def test_r6t7(capsys):
    """
    Testing r6t7. All required information stored in folder r6.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='deleteAccount',
        accts_file='validAccountsList.txt',
        test_id='R6T7'
    )


def test_r6t8(capsys):
    """
    Testing r6t8. All required information stored in folder r6.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='deleteAccount',
        accts_file='validAccountsList.txt',
        test_id='R6T8'
    )


"""============================================================================
R7: Deposit
============================================================================"""


def test_r7t1(capsys):
    """
    Testing r7t1. All required information stored in folder deposit.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='deposit',
        accts_file='validAccountsList.txt',
        test_id='R7T1'
    )


def test_r7t2(capsys):
    """
    Testing r7t2. All required information stored in folder deposit.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='deposit',
        accts_file='validAccountsList.txt',
        test_id='R7T2'
    )


def test_r7t3(capsys):
    """
    Testing r7t3. All required information stored in folder deposit.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='deposit',
        accts_file='validAccountsList.txt',
        test_id='R7T3'
    )


def test_r7t4(capsys):
    """
    Testing r7t4. All required information stored in folder deposit.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='deposit',
        accts_file='validAccountsList.txt',
        test_id='R7T4'
    )


def test_r7t5(capsys):
    """
    Testing r7t5. All required information stored in folder deposit.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='deposit',
        accts_file='validAccountsList.txt',
        test_id='R7T5'
    )


def test_r7t6(capsys):
    """
    Testing r7t6. All required information stored in folder deposit.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='deposit',
        accts_file='validAccountsList.txt',
        test_id='R7T6'
    )


def test_r7t7(capsys):
    """
    Testing r7t7. All required information stored in folder deposit.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='deposit',
        accts_file='validAccountsList.txt',
        test_id='R7T7'
    )


def test_r7t8(capsys):
    """
    Testing r7t8. All required information stored in folder deposit.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='deposit',
        accts_file='validAccountsList.txt',
        test_id='R7T8'
    )


def test_r7t9(capsys):
    """
    Testing r7t2. All required information stored in folder deposit.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='deposit',
        accts_file='validAccountsList.txt',
        test_id='R7T9'
    )


def test_r7t10(capsys):
    """
    Testing r7t10. All required information stored in folder deposit.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='deposit',
        accts_file='validAccountsList.txt',
        test_id='R7T10'
    )


def test_r7t11(capsys):
    """
    Testing r7t11. All required information stored in folder deposit.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='deposit',
        accts_file='validAccountsList.txt',
        test_id='R7T11'
    )


def test_r7t12(capsys):
    """
    Testing r7t12. All required information stored in folder deposit.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='deposit',
        accts_file='validAccountsList.txt',
        test_id='R7T12'
    )


def test_r7t13(capsys):
    """
    Testing r7t13. All required information stored in folder deposit.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='deposit',
        accts_file='validAccountsList.txt',
        test_id='R7T13'
    )


def test_r7t14(capsys):
    """
    Testing r7t14. All required information stored in folder deposit.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='deposit',
        accts_file='validAccountsList.txt',
        test_id='R7T14'
    )


def test_r7t15(capsys):
    """
    Testing r7t15. All required information stored in folder deposit.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='deposit',
        accts_file='validAccountsList.txt',
        test_id='R7T15'
    )


def test_r7t16(capsys):
    """
    Testing r7t16. All required information stored in folder deposit.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='deposit',
        accts_file='validAccountsList.txt',
        test_id='R7T16'
    )


"""============================================================================
R8: Withdraw
============================================================================"""


def test_r8t1(capsys):
    """
    Testing r8t1. All required information stored in folder withdraw.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='withdraw',
        accts_file='validAccountsList.txt',
        test_id='R8T1'
    )


def test_r8t2(capsys):
    """
    Testing r8t2. All required information stored in folder withdraw.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='withdraw',
        accts_file='validAccountsList.txt',
        test_id='R8T2'
    )


def test_r8t3(capsys):
    """
    Testing r8t3. All required information stored in folder withdraw.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='withdraw',
        accts_file='validAccountsList.txt',
        test_id='R8T3'
    )


def test_r8t4(capsys):
    """
    Testing r8t4. All required information stored in folder withdraw.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='withdraw',
        accts_file='validAccountsList.txt',
        test_id='R8T4'
    )


def test_r8t5(capsys):
    """
    Testing r8t5. All required information stored in folder withdraw.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='withdraw',
        accts_file='validAccountsList.txt',
        test_id='R8T5'
    )


def test_r8t6(capsys):
    """
    Testing r8t6. All required information stored in folder withdraw.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='withdraw',
        accts_file='validAccountsList.txt',
        test_id='R8T6'
    )


def test_r8t7(capsys):
    """
    Testing r8t7. All required information stored in folder withdraw.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='withdraw',
        accts_file='validAccountsList.txt',
        test_id='R8T7'
    )


def test_r8t8(capsys):
    """
    Testing r8t8. All required information stored in folder withdraw.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='withdraw',
        accts_file='validAccountsList.txt',
        test_id='R8T8'
    )


def test_r8t9(capsys):
    """
    Testing r8t9. All required information stored in folder withdraw.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='withdraw',
        accts_file='validAccountsList.txt',
        test_id='R8T9'
    )


def test_r8t10(capsys):
    """
    Testing r8t10. All required information stored in folder withdraw.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='withdraw',
        accts_file='validAccountsList.txt',
        test_id='R8T10'
    )


def test_r8t11(capsys):
    """
    Testing r8t11. All required information stored in folder withdraw.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='withdraw',
        accts_file='validAccountsList.txt',
        test_id='R8T11'
    )


def test_r8t12(capsys):
    """
    Testing r8t12. All required information stored in folder withdraw.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='withdraw',
        accts_file='validAccountsList.txt',
        test_id='R8T12'
    )


def test_r8t13(capsys):
    """
    Testing r8t13. All required information stored in folder withdraw.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='withdraw',
        accts_file='validAccountsList.txt',
        test_id='R8T13'
    )


def test_r8t14(capsys):
    """
    Testing r8t14. All required information stored in folder withdraw.

    @param capsys Object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_set='withdraw',
        accts_file='validAccountsList.txt',
        test_id='R8T14'
    )


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

    # read expected tail portion of the terminal output:
    with open(os.path.join(case_folder, 'output',
              '{}output_tail.txt'.format(test_id))) as rf:
        terminal_output_tail = rf.read().splitlines()

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
    out, _ = capsys.readouterr()

    # split terminal output in lines
    out_lines = out.splitlines()

    # # compare terminal outputs at the end.`
    for i in range(1, len(terminal_output_tail)+1):
        index = i * -1
        assert terminal_output_tail[index] == out_lines[index]

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
