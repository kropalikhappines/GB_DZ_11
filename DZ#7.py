class Complex_number:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex_number(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return Complex_number(self.real * other.real - self.imag * other.imag,
                                self.imag * other.real + self.real * other.imag)


    def __str__(self):
        return f'{self.real} {self.imag}'

a = Complex_number(6, 15)
b = Complex_number(3, 8)
print(a + b)

print(a * b)