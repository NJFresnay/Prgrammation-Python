#!/bin/env python3

import Fraction

f = Fraction.Fraction(15,27)
f2 = f.inverse()
#print(f.__str__())
#print(f2)

#print("la fraction réduite :", f.reduire())

f1 = Fraction.Fraction(2,-3)
f3 = f1.inverse()
#print(f1.__str__())
#print(f3)

f4 = Fraction.Fraction(2,1)
f5 = f4.inverse()
#print(f4.__str__())
#print(f5)

p = Fraction.Fraction(9,15)
q = Fraction.Fraction(2,3)

# print(p+q)
#print((p+1)/(p-1))
#print(-p)
#print(p/2)

def calc(a,b):
    try:
        f1 = Fraction.Fraction(a,b)
        f2 = Fraction.Fraction(b,a)
    except ZeroDivisionError as e:
        #print("Une division par 0 a été détectée!")
        print(e)
        exit(1)
    return (f1+f2).reduire()


if __name__ == "__main__":
    a = int(input("entrer un premier entier :"))
    b = int(input("entrer un second entier :"))
    print(f"calc({a},{b})={calc(a,b)}")
    #pass
