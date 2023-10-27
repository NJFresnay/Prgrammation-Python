class Frigo:
    def __init__(self,content):
        self.content = {}

    def etat(self):
        print("\nInventaire:")
        for i,j in self.content.items():
            print(i," : ", j)
        print("******FIN*****")

    def depose(self,dic):
        self.content.update(dic)
        return self.etat

