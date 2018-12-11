import time


def timing(func):
    def wrap(*args):
        time1 = time.time()
        ret = func(*args)
        time2 = time.time()
        print('%s function took %0.3f ms' % (
            func.__name__, (time2 - time1) * 1000.0)
        )
        return ret
    return wrap
