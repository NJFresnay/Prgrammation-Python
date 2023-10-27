#!/bin/env python3

import Point

p1 = Point.Point()
p1.nom = "A"
p1.x = 1
p1.y = 2
print(Point.examine(p1))
print(type(p1).__name__)

p2 = Point.Point()
p2.nom = 'B'
p2.x = 0
p2.y = -1
print(Point.examine(p2),"\n")
print(type(p2).__name__)

Point.deplace(p1, 5,-7)
print(Point.examine(p1),"\n")



