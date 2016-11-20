class Complex():
    """Complex Numbers"""

    def __init__(self, real, imaginary):
        self.r = real
        self.i = imaginary

    def printComplexNumber(self):
        print(str(self.r) + "+" + str(self.i) + "i")

x = Complex(4, 5)
print(x.i)
print(x.r)
x.printComplexNumber()
