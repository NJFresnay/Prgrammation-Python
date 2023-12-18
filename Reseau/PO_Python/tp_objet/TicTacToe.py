class TicTacToe:
    def __init__(self):
        self.dict ={(1,1): ".", (1,2): ".", (1,3):".",
               (2,1): ".", (2,2): ".", (2,3):".",
               (3,1): ".", (3,2): ".", (3,3):"."}

    def __str__(self):
        s=""
        for i in range(1,4):
            for j in range(1,4):
                s += self.dict[(i,j)] + " "
            s += "\n"
        return s

    def place(self, x, y, char):
        """methode qui sert à positionner un pion sur le plateau """
        self.dict[(x,y)] = char
        return self.__str__()

    def vainqueur(self):
        """ Cette méthode permet de savoir si on a un vainqueur ou pas. Si oui elle nous retourne le pion vainqueur"""

        # Vérification sur les colonnes et les lignes
        for i in range(1,4):
            if ( self.dict[(i,1)] ==  self.dict[(i,2)] == self.dict[(i,3)] != '.'):
                return self.dict[(i,1)]
            elif ( self.dict[(1,i)] ==  self.dict[(2,i)] == self.dict[(3,i)] != '.') :
                return self.dict[(1,i)]

        #Vérification sur les diagonales
        if ( self.dict[(1,1)] ==  self.dict[(3,3)] == self.dict[(2,2)] != '.') :
            return self.dict[(1,1)]

        if ( self.dict[(1,3)] ==  self.dict[(2,2)] == self.dict[(3,1)] != '.') :
            return self.dict[(1,1)]

        return ""



