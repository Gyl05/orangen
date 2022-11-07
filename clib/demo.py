class python_int(object):
    def __init__(self, value) -> None:
        self.value = value
    
    def add_func(self, num):
        return self.value + num
    
    def mul_func(self, num):
        return self.value * num
    
    def equal_func(self, num):
        pass


if __name__ == "__main__":
    int_obj = python_int(42)
    add_res = int_obj.add_func(2)
    mul_res = int_obj.mul_func(3)
    print(add_res, mul_res)