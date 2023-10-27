from math import gcd

class Fraction:
    def __init__(self, num=0,denom=1):
        self.num = num
        if denom == 0:
            raise "Impossible de faire une division par 0!"
        self.denom = denom

    def reduire(self):
        pgcd = gcd(self.num, self.denom)
        self.num = int(self.num // pgcd)
        self.denom = self.denom // pgcd
        return self


    def __str__(self):
        if self.num != 0 and self.denom == 1 :
            return f"{abs(self.num)}"
        else:
            if self.num < 0 and self.denom > 0 :
                return f"-{abs(self.num)}/{abs(self.denom)}"
            elif self.num > 0 and self.denom < 0 :
                return f"-{abs(self.num)}/{abs(self.denom)}"
            else:
                return f"{abs(self.num)}/{abs(self.denom)}"

    def inverse(self):
        copie = Fraction()
        if self.denom != 0:
            copie.num = self.denom
            copie.denom = self.num
        return copie


    def __add__(self, f):
        if isinstance(f, Fraction):
            n = (self.num*f.denom) + (self.denom*f.num)
            d = self.denom*f.denom
            return Fraction(n,d)
        elif isinstance(f, int) or isinstance(f, float) :
            return Fraction(self.num+f*self.denom, self.denom)
        else:
            raise RuntimeError("opération non implémentée")

    def __sub__(self, f):
        if isinstance(f, Fraction):
            n = (self.num*f.denom) - (self.denom*f.num)
            d = self.denom*f.denom
            return Fraction(n,d)
        elif isinstance(f, int) or isinstance(f, float) :
            return Fraction(self.num-f*self.denom, self.denom)
        else:
            raise RuntimeError("opération non implémentée")

    def __mul__(self,f):
        if isinstance(f, Fraction):
            return Fraction(self.num*f.num, self.denom*f.denom)
        elif isinstance(f, int) or isinstance(f, float) :
            return Fraction(self.num*f, self.denom)
        else:
            raise RuntimeError("opération non implémentée")

    def __truediv__(self,f):
        if isinstance(f, Fraction):
            f1 = f.inverse()
            return Fraction(self.num*f1.num, self.denom*f1.denom)
        elif isinstance(f, int) or isinstance(f, float) :
            f1 = Fraction(1,f)
            return Fraction(self.num*f1.num, self.denom*f1.denom)
        else:
            raise RuntimeError("opération non implémentée")

    def __neg__(self):
       return Fraction(-self.num,self.denom)

    def __ge__(self,f):
        res1 = Fraction(self.num*f.denom, self.denom*f.denom)
        res2 = Fraction(self.denom*f.num, self.denom*f.denom)
        if (res1.num >= res2.num):
            return "ok"
        elif (res1.num < res2.num):
            return False


