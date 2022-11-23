from functools import wraps

def log_decorator(func):
    @wraps(func)
    def wrapped(*args, **kws):
        # print(func.__name__, func.__doc__)
        print('函数装饰器先装饰')
        return func(*args, **kws)
    return wrapped

class A():
    @log_decorator
    def get1(self):
        """这是get1的doc"""
        return 1
    def get2(self):
        return 2
    def get3(self):
        return 3
    def __getattribute__(self, __name):
        x = super().__getattribute__(__name)
        if __name.startswith('get') and callable(x) and not __name.startswith('_'):
            @wraps(x)
            def wrapper(*args, **kwargs):
                print(__name, '>>>')
                ret = x(*args, **kwargs)
                return ret
            return wrapper
        return x



if __name__ == '__main__':
    a = A()
    print(a.get1(), 'a.get1 函数的名称是', a.get1.__name__)
    # print(a.get2())
    # print(a.get3())
