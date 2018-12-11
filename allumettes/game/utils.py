import time
from colorama import Fore
from colorama import Style


def timing(func):
    def wrap(*args):
        time1 = time.time()
        ret = func(*args)
        time2 = time.time()
        print(Fore.RED + '%s function took %0.3f ms' % (
            func.__name__, (time2 - time1) * 1000.0) + Style.RESET_ALL
        )
        return ret
    return wrap
