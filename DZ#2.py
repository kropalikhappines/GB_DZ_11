class ZeroDivisionError_1():
    def __init__(self, num):
        self.num = num
    @classmethod
    def division(self, num):
        if num == 0:
            print('Nope "0"')




def div(a, b):
    if b == 0:
        ZeroDivisionError_1.division(b)
        return
    return print(a // b)
div(5, 0)
