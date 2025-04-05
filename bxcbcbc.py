class Calculator:
    def __init__(self, a, b):
       if type(a) == int or type(a) == float:
           self.a = a
       else:
           raise TypeError
       if type(b) == int or type(b) == float:
           self.b = b
       else:
           raise TypeError
    def plus(self):
        print(self.a + self.b)
    def minus(self):
        print(self.a - self.b)
    def multiplic(self):
        print(self.a * self.b)
    def divide(self):
        if self.b == 0:
            raise ZeroDivisionError
        else:
            print(self.a / self.b)

try:
    f = Calculator(5, 0)
    print(f.plus())
    print(f.minus())
    print(f.multiplic())
    print(f.divide())
except(TypeError, ZeroDivisionError):
    print("Error")

