class A():
    def __init__(self) -> None:
        self.func1 = None
        self.func2 = None

a = A()

print([item for item in dir(a) if not item.startswith('__')])

def xx():
    for i in range(2):
        def func():
            print(1)
        setattr(a, f'func{i+1}', func)


xx()
print([item for item in dir(a) if not item.startswith('__')])

print(a.func1)
print(a.func1)
a.func1()
a.func2()


