from functools import wraps


def print_before_get(cls):
    for func in dir(cls):
        if func.startswith('get'):
            origin_func = getattr(cls, func)

            def wrapper(*args, **kwargs):
                print("类的装饰器")
                result = origin_func(*args, **kwargs)
                return result

            setattr(cls, func, wrapper)
    return cls


def log_func(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        print("函数的装饰器")
        ret = func(*args, **kwargs)
        return ret

    return wrapped


@print_before_get
class A:
    def get_1(self):
        return 1

    # @log_func
    def get_2(self):
        return 2


if __name__ == '__main__':
    a = A()
    print(dir(a))
    print(a.get_1())
    print(a.get_1())
