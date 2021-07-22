import re

from datetime import datetime


class Date:

    def __init__(self, dat):
        self.dat = dat

    @classmethod
    def date(cls, dat):
        if cls.validate(dat):
            return datetime.strptime(dat, '%d-%m-%Y').date()

    @staticmethod
    def validate(dat):
        valid = re.compile('[0-9]{2}-[0-9]{2}-[0-9]{4}')
        if not valid.match(dat):
            print('Nope')
            return False
        else:
            day, month, year = map(int, dat.split('-'))

            if not 31 >= day > 0:
                print('Nope day')
                return False
            if not 12 >= month > 0:
                print('Nope month')
                return False

            return True



Date.validate('53-13-2021')
print(Date.date('22-12-2021'))
        
