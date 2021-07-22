class OnlyForNumber:

    @classmethod
    def checking_num(self, number):

        n = str(number)
        if n.isnumeric():
            print('Dobavleno')
        elif n == 'stop':
            return
        else:
            print('Note number')
        return
    

def input_number():
    result = []
    while True:
        a = input('Введите число: ')
        OnlyForNumber.checking_num(a)
        if a.isnumeric():
            result.append(int(a))
        elif a == 'stop':
            break
    return print(result)

input_number()

# --------------------------

class OnlyForNumber:
    res = []
    @classmethod
    def checking_num(cls, number):

        n = str(number)
        if n.isnumeric():
            cls.res.append(int(n))
        else:
            print('Note number')

def input_number():
    result = OnlyForNumber()
    while True:
        a = input('Введите число: ')

        if a == 'stop':
            print(result.res)
            break
        result.checking_num(a)

input_number()

