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



class Jeu:
    def __init__(self):
        super().__init__()
        self.jeu = Cartes()

        valeurs = list(range(7,11))+['Valet','Dame','Roi','As']
        couleurs = ['Coeur','Carreau','Pique','Trèfle']

        for i in valeurs:
            for j in couleurs:
                une_carte= Carte(i,j)
                self.jeu.ajoute(une_carte)
               #print(une_carte)

    def __repr__(self):
        return repr(self.jeu)
