import tempfile
from importlib import reload
import os
import io
import sys
import frontend.app as app

path = os.path.dirname(os.path.abspath(__file__))


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
        os.path.join(case_folder, 'testValidAccountsListFiles', accts_file),
        transaction_summary_file]

    # set terminal input
    sys.stdin = io.StringIO(
        os.linesep.join(terminal_input))

    # run the program
    app.main()

    # capture terminal output / errors
    # assuming that in this case we don't use stderr
    # out, err = capsys.readouterr()

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
