import math

class Cercle:
    def initRayon(self, rayon):
        self.rayon = 10

    def circonference(self):
        return 2*math.pi*self.rayon

    def surface(self):
        return self.rayon*self.rayon* math.pi

