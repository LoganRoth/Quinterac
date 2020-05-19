import sys

from integration_test.one_week import main as week
from integration_test.one_day import main as day
from utility.utility import RetCode

if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            ret = day()
        else:
            ret = week()
    except KeyboardInterrupt:
        print('Aborting')
        ret = RetCode.ABORTING
    sys.exit(ret)
