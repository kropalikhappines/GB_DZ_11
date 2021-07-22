class Warehous:
    pass


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