from random import randrange,shuffle

class Carte():

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

    # def __str__(self):
    #     mapping = {"Carreau": "♦", "Coeur": "♥", "Pique": "♠", "Trèfle": "♣"}
    #     return f"{self.valeur} de {mapping[self.couleur]} "

    #Pour retourner la carte sous la forme d'une chaine de caractères
    def __repr__(self):
        return f"{self.valeur} de {self.couleur}"
        # mapping = {"Carreau": "♦", "Coeur": "♥", "Pique": "♠", "Trèfle": "♣"}
        # return f"{self.valeur} de {mapping[self.couleur]} "

    def __eq__(self,une_carte):
        return (self.valeur == une_carte.valeur) and (self.couleur == une_carte.couleur)


class Cartes():

    def __init__(self, cartes=None):
        if cartes == None:
            cartes = []
        if isinstance(cartes,Cartes):
            self.cartes = cartes.cartes.copy()
        else:
            self.cartes = cartes

    def __repr__(self):
        return str(self.cartes)
        #return ", ".join([str(c) for c in self.cartes])

    def __add__(self,une_carte):
        if une_carte:
            if not isinstance(une_carte, Carte):
                raise ValueError("Cet objet n'est pas de type \"Carte\"")
        else:
            car = Carte(une_carte.valeur, une_carte.couleur)
            self.cartes.append(car)
        return self.cartes

    def __isub__(self,des_cartes):
        if isinstance(des_cartes, Cartes):
            for card in des_cartes.cartes:
                self.cartes.remove(card)
        return self

    def ajoute(self,une_carte):
        self.cartes += [une_carte]

    def pioche(self):
        n = len(self.cartes)
        if  n > 0:
            pioche = self.cartes[randrange(0,n)]
            self.cartes.remove(pioche)
            return pioche
        else:
            raise ValueError("Pioche vide!")



class Jeu(Cartes):
    def __init__(self):
        super().__init__()

        valeurs = list(range(7,11))+['Valet','Dame','Roi','As']
        couleurs = ['Coeur','Carreau','Pique','Trèfle']

        for i in valeurs:
            for j in couleurs:
                une_carte = Carte(i,j)
                self.ajoute(une_carte)
        shuffle(self.cartes) # pour mélanger les cartes afin d'accéler la recherce d'un carré

class Main(Cartes):
    def __init__(self, un_jeu):
        super().__init__()
        self.jeu = un_jeu

    def complete(self):
        try:
            self.ajoute(self.jeu.pioche())
        except :
            raise ValueError(f"\nPlus de cartes pour compléter la main {self.cartes}")

class Carre(Cartes):

    def __init__(self,main):
        super().__init__()

        fin = False
        self.valeur = -1
        shuffle(main.cartes)
        k = 0
        while not fin :
            v = Carte.valeurs[k] # on choisit la valeur de la première carte comme point de départ
            un_carre = []

            for card in main.cartes:
                if card.valeur == v:
                    un_carre.append(card)

                    if len(un_carre) == 4: # c'est qu'on a obtenu notre carré
                        self.valeur = v
                        self.cartes = un_carre
                        fin = True
            k += 1
            if k == len(Carte.valeurs) : # on a parcouru toutes les cartes de notre main
                raise RuntimeError

        if self.valeur == -1 : # c'est qu'on a trouvé aucun carré dans notre main
            raise RuntimeError(f"\nIl n\'y a aucun carré dans la main:  {main} ")

    def __repr__(self):
        return f" carré de {self.valeur}"

    def __str__(self):
        return f" carré de {self.valeur}"

    def __isub__(self, carre):
        for card in carre.cartes:
            for i in range(0, len(self.cartes)):
                if card.valeur == self.cartes.valeur[i]:
                    del self.cartes[i]
        return self


class Quinte(Cartes):

    def __init__(self, main):
        super().__init__(main)

        fin = False
        self.couleur = -1
        shuffle(main.cartes)
        k = 0; p=0

        while not fin :
            c = Carte.couleurs[k] # on choisit la couleur de la première carte comme point de départ
            un_quinte = []
            while p < 5 :
                for card in main.cartes:
                    if card.couleur == c:
                        un_quinte.append(card)

                    self.couleur = c
                    self.cartes = un_quinte
                    fin = True   # fin du test
            k += 1

            if k == len(Carte.couleurs) : # on a parcouru toutes les cartes de notre main
                raise RuntimeError

        if self.couleur == -1 : # c'est qu'on a trouvé aucun quinte dans notre main
            raise RuntimeError(f"\nIl n\'y a aucun quinte dans la main: \n{main} ")


    def __repr__(self):
        return f" quinte de {self.cartes}"

    def __str__(self):
        return f" quinte de {self.cartes}"
