#!/bin/env python3

import Point
import Cercle

p1 = Point.Point()
p1.nom ='O'
p1.x = 0
p1.y = 1

p2 = Point.Point()
p2.nom = "B"
p2.x = 0
p2.y = -1


c = Cercle.Cercle()
c.nom = "C1"
c.centre = p1
c.rayon = 7

un_autre_cercle = Cercle.copie(c)

print(Cercle.examine(c), "\n")
print(Cercle.deplace(c,p2), "\n")
#print(Cercle.examine(c), "\n")
print(Cercle.examine(un_autre_cercle))

