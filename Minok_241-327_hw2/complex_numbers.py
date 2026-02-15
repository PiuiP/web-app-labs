import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)
        
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)
                
    def __mul__(self, other):
        return Complex(self.real * other.real - self.imaginary * other.imaginary, self.real * other.imaginary + self.imaginary * other.real)
        
    def __truediv__(self, other):
        numerator = self * Complex(other.real, -other.imaginary)
        denominator = other.real**2 + other.imaginary**2
        return Complex(numerator.real / denominator, numerator.imaginary / denominator)
        
    def mod(self):
        return Complex((self.real ** 2 + self.imaginary ** 2) ** 0.5, 0)
        
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
