#!/bin/env python3

import Carte

# print(Carte.Carte())
# print(Carte.Carte())
# print(Carte.Carte())

carte1=Carte.Carte(7,"Coeur")

carte2=Carte.Carte("As","Trèfle")

carte3=Carte.Carte("Valet","Pique")
#print(carte3.__repr__())

des_cartes = Carte.Cartes()

#on y ajoute 3 cartes
for une_carte in [carte1,carte2,carte3]:
    des_cartes.ajoute(une_carte)

#des_cartes.ajoute(["Bonjour"]) #pour vérifier le déclenchement de l'erreur à ce niveau

print(f"{des_cartes=} \n")

# clonage des cartes
les_memes = Carte.Cartes(des_cartes)
print(f"{les_memes=} \n")

# pioche
#rint(des_cartes.pioche())



if __name__=="__main__":
    pass
