from random import randrange

class Carte:
    valeurs = list(range(7,11))+['Valet','Dame','Roi','As']
    couleurs = ['Coeur','Carreau','Pique','Trèfle']

    def __init__(self, v=None, c=None):
        if v:
            if not v in Carte.valeurs:
                raise ValueError(f"{v}: valeur incorrecte!")
        else:
            v = Carte.valeurs[randrange(0,len(Carte.valeurs))]

        if c:
            if not c in Carte.couleurs:
                raise ValueError(f"{c}: couleur incorrecte!")
        else:
            c = Carte.couleurs[randrange(0,len(Carte.couleurs))]

        self.couleur = c
        self.valeur = v

    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

    #Pour retourner la carte sous forme de chaine de caractères
    def __repr__(self):
        return f"{self.valeur} de {self.couleur}"




class Cartes:
    def __init__(self, cartes=None):
        if cartes == None:
            self.cartes = []
        else:
            self.cartes = cartes

    def __repr__(self):
        return str(self.cartes)


    def __add__(self,une_carte):
        if une_carte:
            if not isinstance(une_carte, Carte):
                raise ValueError("Cet objet n'est pas de type \"Carte\"")
        else:
            car = Carte(une.valeur,une_carte.couleur)
            self.cartes.append(car)
        return self.cartes

    def ajoute(self,une_carte):
        self.cartes += [une_carte]


    # def pioche(self):
    #     n = len(self.cartes)
    #     if n == 0:
    #         print("La pioche est vide")
    #         print("fin du programme")
    #     while n > 0:
    #         pioche = self.cartes[0]
    #         self.cartes+= self.cartes[1:]
    #         print(pioche)
    #         del(pioche)













