import threading
import sys


class Thread(threading.Thread):
    def __init__(self, func, *args, **kwargs):
        super(Thread, self).__init__()

        self.func = func
        self.args = args
        self.kwargs = kwargs

        self._result = None

    def run(self) -> None:
        self._result = self.func(*self.args, **self.kwargs)

    def result(self) -> any:
        self.join()
        return self._result


def thread(func):
    """ 多线程 """
    def wrapper(*args, **kwargs):
        t = Thread(func, *args, **kwargs)
        t.start()
        return t
    return wrapper


def error(func):
    """ 报错退出程序 """
    def wrapper(*args, **kwargs):
        try:
            results = func(*args, **kwargs)
        except Exception as e:
            sys.exit(e)
        else:
            return results
    return wrapper
