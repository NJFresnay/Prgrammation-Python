
import turtle
import math


class Forme:
    def __init__(self,g, l , c ='black', epais=1, debug=False):
        self.g = g
        self.l = l
        self.c = c
        self.epais = epais
        self.debug = debug


    def _goto_G(self):
        turtle.penup() # on releve la tortue
        turtle.goto(self.g) # on deplace la tortue

        if self.debug:
            turtle.pencolor("red")
            turtle.pensize(1)
            turtle.pendown()

    def trace(self):
        self._goto_G()
        self._goto_edge()
        self._trace()


class Triangle(Forme):

    def _goto_edge(self):
        turtle.setheading(90) # on la tourne
        turtle.forward(self.l*(math.sqrt(3)/2)*2/3)


    def _trace(self):
        turtle.pencolor(self.c) # choix de la couleur
        turtle.pensize(self.epais)
        turtle.pendown() #on la pose
        turtle.setheading(-120)
        turtle.forward(self.l)
        turtle.setheading(0)
        turtle.forward(self.l)
        turtle.setheading(120)
        turtle.forward(self.l)


class Carre(Forme):
    # Le __init__ ici n'est pas obligatoire car il herite deja de la super classe
    def __init__(self,g, l , c ='black', epais=1, debug=False):
        super().__init__(g, l , c , epais, debug)

    def _goto_edge(self):
        turtle.setheading(-135)
        turtle.forward(self.l*(math.sqrt(2)/2))

    def _trace(self):
        turtle.pencolor(self.c)
        turtle.pensize(self.epais)
        turtle.pendown()
        turtle.setheading(0)
        turtle.forward(self.l)
        turtle.setheading(90)
        turtle.forward(self.l)
        turtle.setheading(180)
        turtle.forward(self.l)
        turtle.setheading(270)
        turtle.forward(self.l)

class Cercle(Forme):
    # def __init__(self,g, l , c ='black', epais=1, debug=False):
    #     super().__init__(g, l , c , epais, debug)
    def _goto_edge(self):
        turtle.setheading(-90)
        turtle.forward(self.l/2)

    def _trace(self):
        turtle.pencolor(self.c)
        turtle.pensize(self.epais)
        turtle.pendown()
        turtle.setheading(0)
        turtle.circle(self.l/2)



