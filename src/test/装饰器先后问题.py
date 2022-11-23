import copy
from functools import wraps


def print_before_get(cls):
    for func in dir(cls):
        if func.startswith('get') and callable(getattr(cls, func)):
            origin_func = getattr(cls, func)
            @wraps(origin_func)
            def wrapper(*args, **kwargs):
                print("类的装饰器")
                result = origin_func(*args, **kwargs)
                return result

            setattr(cls, func, wrapper)
        elif func.startswith('get'):
            setattr(cls, func, '666')
    return cls

@print_before_get
class A:

    def get_1(self):
        return 1

    def get_2(self):
        return 2

if __name__ == '__main__':
    a = A()
    print(a.get_1())
    print(a.get_2())

