class AAA(object):
    def __init__(self) -> None:
        pass

    def method_a(self, param1):
        print(param1)
    
    def method_b(self, param2):
        print(param2)

if __name__ == '__main__':
    param1 = 1
    AAA.method_a(param1)
    param2 = 2
    AAA.method_b(param2)