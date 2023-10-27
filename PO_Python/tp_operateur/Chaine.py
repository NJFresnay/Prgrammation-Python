import Domino

class Chaine:
    def __init__(self):
        self.chaine = {}


    def __str__(self):
        c = ""
        for i,j in self.chaine.items():
            c += str(i)+":"+str(j) + " "
        return c

     # def __str__(self):
  #       s=[]
  #       for i self.chaine:
  #           s += [str(i)]
  #       return "-".join(s)

    def __add__(self, d):
        self.chaine.update({d.faceA : d.faceB})
        return self



