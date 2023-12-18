import Frigo

class Recette:
    def __init__(self, dico):
        self.dico = dico

    def isPresent(self, frigo):
        for i in self.dico:
            if i not in frigo.content:
                return False
            else :
                if self.dico[i] > frigo.content[i]:
                    return False
        return True


