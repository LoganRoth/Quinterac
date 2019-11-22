import sys

from backoffice_test.app import main
from utility.utility import RetCode

if __name__ == "__main__":
    try:
        ret = main()
    except KeyboardInterrupt:
        print('Aborting')
        ret = RetCode.ABORTING
    sys.exit(ret)
