from application.message import showerror
from application.errors import GuiFileAskWarning

import threading


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


def application_thread(func):
    """ 多线程 """
    def wrapper(*args, **kwargs):
        t = Thread(func, *args, **kwargs)
        t.start()
        return t
    wrapper.__name__ = func.__name__
    return wrapper


def application_error(func):
    """ 报错退出程序 """
    def wrapper(*args, **kwargs):
        try:
            results = func(*args, **kwargs)
        except Exception as e:
            if e.__class__ == GuiFileAskWarning:
                return None
            showerror(getattr(e, "title", "错误"), e)
        else:
            return results
    wrapper.__name__ = func.__name__
    return wrapper
