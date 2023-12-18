class Stylo:
    def __init__(self):
        self.reserve = 100

    def print(self,chaine):
        m = len(chaine)
        while( self.reserve > 0):
            if self.reserve >= m:
                print(chaine)

            elif self.reserve < m :
                #for i in range(self.reserve):
                print(chaine[:self.reserve])
            self.reserve -= m
        #print("Plus d'encre disponible!")
