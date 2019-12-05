import tempfile
from importlib import reload
import os
import sys
import backoffice.app as app

path = os.path.dirname(os.path.abspath(__file__))


def helper(capsys, test_set, test_id):
    """
    Helper function that test requirements for the frontend app

    @param capsys Object created by pytest to capture stdout and stderr
    @param test_set The test set to use
    @param test_id ID of the specific test to run
    """

    # cleanup package
    reload(app)

    # locate test case folder:
    case_folder = os.path.join(path, test_set)

    # read expected tail portion of the terminal output:
    with open(os.path.join(case_folder, '{}'.format(test_id), 'output',
              'output_tails.txt'.format(test_id))) as rf:
        terminal_output_tail = rf.read().splitlines()

    # create a temporary file in the system to store teh output Master Accounts
    # File
    temp_fd, temp_file = tempfile.mkstemp()
    mafOut = temp_file

    # create a temporary file in the system to store the output Valid Accounts
    # List File
    temp_fd2, temp_file2 = tempfile.mkstemp()
    validAcctsOut = temp_file2

    # prepare program parameters
    sys.argv = [
        'app.py',
        os.path.join(case_folder, '{}'.format(test_id), 'input',
                     'masterAcctsFile.txt'),
        os.path.join(case_folder, '{}'.format(test_id), 'input',
                     'mergedTransactionSummaryFile.txt'),
        mafOut,
        validAcctsOut,
        '--whitebox']

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

    # compare maf:
    with open(mafOut, 'r') as of:
        content = of.read()
        with open(os.path.join(case_folder, '{}'.format(test_id), 'output',
                  'maf.txt'), 'r') as exp_file_of:
            expected_content = exp_file_of.read()
            assert content == expected_content

    # compare validAcctsList:
    with open(validAcctsOut, 'r') as of:
        content = of.read()
        with open(os.path.join(case_folder, '{}'.format(test_id), 'output',
                  'validAcctsListFile.txt'), 'r') as exp_file_of:
            expected_content = exp_file_of.read()
            assert content == expected_content

    # clean up
    os.close(temp_fd)
    os.remove(temp_file)
    os.close(temp_fd2)
    os.remove(temp_file2)
