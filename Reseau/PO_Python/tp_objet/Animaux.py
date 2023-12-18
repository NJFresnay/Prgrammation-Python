class Animaux:
    def __init__(self, nom):
        self.nom = nom

    def __str__(self):
        s=""
        for i in self.__class__.__bases__:
            s+= i.__name__
        return f"Je suis {self.nom}, instance de {self.__class__.__name__}, de la famille de {s}"

    def fuite(self):
        self.bouge()
        self.crie()

    def __repr__(self):
        s=""
        for i in self.__class__.__bases__:
            s+= i.__name__
        return f"Je suis {self.nom}, instance de {self.__class__.__name__}, de la famille de {s}"

class Digitigrade(Animaux):

    # def __init__(self,nom):
    #     super().__init__(nom)

    def bouge():
        print(" je cours")

class Mammifere(Digitigrade): pass

class Ours(Mammifere):
    def crie():
        print("je grogne")

class Chat(Mammifere):
    def crie():
        print("je miaule")

class Souris(Mammifere):
    def crie():
        print("je couine")

class Dauphin(Mammifere):
    def bouge():
        print("je nage")

    def crie():
        print("siffle")

class Chauve_Souris(Mammifere):
    def crie():
        print("je grince")

class Poisson(Animaux):
    def __init__(self,nom):
        super().__init__(self)

    def bouge():
        print("je nage")

    def crie():
        print("je n'émets aucun cri")

class Poisson_crapaud(Poisson):
    def crie():
        print("je grogne")

class Saumon(Poisson):
    pass

class Exocoetidae(Poisson):
    def bouge():
        print("je vole")

class Oiseau(Animaux):
    def __init__(self,nom):
        super().__init__(self)

    def bouge():
        print("je vole")

    def crie():
        print("je siffle")

class Epervier(Oiseau):
    def crie():
        print("je piaule")

class Rossignol(Oiseau):
    pass

class Autruche(Oiseau, Digitigrade):
    def crie():
        print("je claquette")

class Gallinace(Oiseau):
    def crie():
        print("je glousse")

class Poule(Gallinace):
    pass

class Pintade(Gallinace):
    pass


class Territoire:
    def __init__(self):
        self.territoire = []

    def __str__(self):
        s = ""
        for i in self.territoire:
            s += str(i)
            s += "\n"
        return s

    def __iadd__(self, animal):
        self.territoire.append(animal)
        return self

    def alerte(self):
        for i in self.territoire:
            i.fuite()



