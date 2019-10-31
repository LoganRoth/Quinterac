import sys

from frontend.app import main
from frontend.frontendUtility import RetCode

if __name__ == "__main__":
    try:
        ret = main()
    except KeyboardInterrupt:
        print('Aborting')
        ret = RetCode.ABORTING
    sys.exit(ret)
