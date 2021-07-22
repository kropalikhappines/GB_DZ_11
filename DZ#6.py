from collections import defaultdict


class Warehous:
    reception = defaultdict(int)
    subdivisions = {}

    @staticmethod
    def check_dict(dicts, key):
        if dicts.get(key) is None:
            dicts[key] = {}

        return dicts

    @classmethod
    def reception_equipment(cls, name_equip: str, quantity: int):
        if isinstance(quantity, str):
            raise ValueError('Надо цифры')
        cls.reception[name_equip] += quantity

    @classmethod
    def broadcast_equipment(cls, subdivision, name_equip: str, quantity: int):
        if isinstance(quantity, str):
            raise ValueError('Надо цифры')

        if quantity > cls.reception.get(name_equip, 0):
            raise ValueError('Закончились')

        cls.check_dict(cls.subdivisions, subdivision)
        cls.check_dict(cls.subdivisions[subdivision], name_equip)
        cls.subdivisions[subdivision][name_equip] = quantity

        cls.reception[name_equip] -= quantity


class Equipment:
    def __init__(self, serial_num, interface):
        self.serial_num = serial_num
        self.interface = interface


class Printer(Equipment):
    def __init__(self, serial_num, interface, multifunctional):
        super().__init__(serial_num, interface)
        self.multifuctional = multifunctional


class Scanner(Equipment):
    def __init__(self, serial_num, interface, resolution):
        super().__init__(serial_num, interface)
        self.resolution = resolution


class Xerox(Equipment):
    def __init__(self, serial_num, interface, color):
        super().__init__(serial_num, interface)
        self.color = color




war = Warehous()
war.reception_equipment('printer', 3)
print(war.reception)
war.reception_equipment('printer', 1)
print(war.reception)
war.broadcast_equipment('sale', 'printer', 2)

print(war.subdivisions)
war.broadcast_equipment('sale', 'printer', 2)
print(war.subdivisions)
war.broadcast_equipment('sale', 'printer', 2)
print(war.subdivisions)
print(war.reception)