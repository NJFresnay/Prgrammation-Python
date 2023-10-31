import Carte

class Cartes(Carte):
    def __init__(self, cartes = None):
        #super().__init__()
        self.cartes = []

    def __str__(self):
        s = ""
        for c in self.cartes:
            s += str(c)
            s+= ", "
        print (s)

    def ajoute(self,carte):
        if carte:
            if not isinstance(carte, Carte.Carte):
                raise ValueError("Cet objet n'est pas de type \"Carte\"")
        else:
            return self.cartes.append([str(chaine)])
