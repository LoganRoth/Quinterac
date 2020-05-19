from importlib import reload
import sys

import integration_test.one_day as od
from utility.utility import RetCode


def main():
    reload(od)
    for i in range(1, 6):
        sys.argv = [
            'one_day.py',
            str(i)]
        od.main()
    return RetCode.OK
