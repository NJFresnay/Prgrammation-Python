#!/bin/env python3
# coding: utf-8
import turtle
import Formes

def main():
    turtle.Screen()
    turtle.Screen().setup(640, 480, 100, 100)

    try:
        turtle.reset()
        triangle = Formes.Triangle(g=(50,50),l=100,debug=True)
        triangle.trace()
        cercle=Formes.Cercle(g=(-50,-50),l=100,debug=True)
        #cercle.trace()
        carre=Formes.Carre(g=(-50,-50),l=100,c="blue")
        #carre.trace()
        triangle1=Formes.Triangle(g=(-50,-50),l=100,epais=2,c="lime")
    finally:
        # turtle.exitonclick()
        pass

if __name__ == "__main__":
    main()
