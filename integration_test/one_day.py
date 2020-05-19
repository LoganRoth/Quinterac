import argparse
import sys
import os
import io

import frontend.app as f_app
import backoffice.app as b_app
from utility.utility import RetCode

path = os.path.dirname(os.path.abspath(__file__))


def parseArgs():
    """
    Parses the arguments given to the script to determine which day it is.
    """
    parser = argparse.ArgumentParser(usage='one_day.py #')
    parser.add_argument(
        'day',
        action='store',
        default='0',
        help='Which day of the week it is, as an integer.'
    )
    args = parser.parse_args()
    return int(args.day)


def combine_summaries(day_folder):
    merged_out = os.path.join(day_folder, 'output', 'mergedTxSummaryFile.txt')
    lines_list = []
    for i in range(1, 4):
        with open(os.path.join(day_folder, 'output',
                               'summary{}.txt'.format(i)), 'r') as f:
            lines_list += f.readlines()
    with open(merged_out, 'w+') as f:
        for line in lines_list:
            f.write(line)


def main():
    # Hide stdout
    text_trap = io.StringIO()
    sys.stdout = text_trap

    day = parseArgs()
    prev_day = day - 1
    day_folder = os.path.join(path, 'day{}'.format(day))
    prev_day_folder = os.path.join(path, 'day{}'.format(prev_day))
    val_accts_in = os.path.join(prev_day_folder, 'output',
                                'validAcctsListFile.txt')
    for i in range(1, 4):
        summary_out = os.path.join(day_folder, 'output',
                                   'summary{}.txt'.format(i))
        with open(summary_out, 'w+'):  # clear summary
            pass
        with open(os.path.join(day_folder, 'input',
                  'session{}.txt'.format(i)), 'r') as in_f:
            terminal_input = in_f.read().splitlines()
        sys.argv = [
            os.path.join('frontend', 'app.py'),
            val_accts_in,
            summary_out]
        sys.stdin = io.StringIO(os.linesep.join(terminal_input))
        f_app.main()

    combine_summaries(day_folder)

    maf_in = os.path.join(prev_day_folder, 'output', 'masterAcctsFile.txt')
    merged = os.path.join(day_folder, 'output', 'mergedTxSummaryFile.txt')
    maf_out = os.path.join(day_folder, 'output', 'masterAcctsFile.txt')
    val_accts_out = os.path.join(day_folder, 'output',
                                 'validAcctsListFile.txt')
    sys.argv = [
        os.path.join('backoffice', 'app.py'),
        maf_in,
        merged,
        maf_out,
        val_accts_out]
    b_app.main()

    # Restore stdout
    sys.stdout = sys.__stdout__
    return RetCode.OK
