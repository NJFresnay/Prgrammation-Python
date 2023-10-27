import TicTacToe

class Joueur:
    def __init__(self, jeu, nom, pion):
        self.jeu = jeu
        self.nom = nom
        self.pion = pion

    def joue(self, x, y):
        return self.jeu.place(x, y, self.pion)


