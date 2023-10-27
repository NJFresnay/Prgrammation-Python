import math

class Complex():
    def __init__(self, reel, imag):
        """ Constructeur de la classe"""
        self.x = reel
        self.y = imag

    def module(self):
        return math.sqrt(self.x**2 + self.y**2)

    def argument(self):
        return math.atan(self.y/self.x)

    def __str__(self):
        return f"{self.x}+{self.y}i"

    # def conjugue(self):
    #     C= Complex()
    #     C.x = self.x
    #     C.y = - self.y
    #     #init(C,self.x,-self.y )
    #     return C

