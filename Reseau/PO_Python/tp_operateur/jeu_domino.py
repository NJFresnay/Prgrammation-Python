#!/bin/env python3

import Domino
import Chaine

d1 = Domino.Domino(1,2)
print(d1)
print()
d2 = Domino.Domino(3,2)
print(d2)
print()

#d3 = Domino.Domino(1,7)
#print(d3)

d3 = d1.retourne()
print(d3)
print()

c = Chaine.Chaine()
c += d1
c += d2

#print(c)

d4 = Domino.Domino(0,0)
c1 = d1+d2
c1 += d4
print(type(c1))

if __name__ == "__main__":
    pass
