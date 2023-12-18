#!/bin/env python3

import Carte

# QUESTION 1 : CLASSE CARTE()

# print(Carte.Carte())
# print(Carte.Carte())
# print(Carte.Carte())


# QUESTION 2: CLASSE "CARTES()"
carte1=Carte.Carte(7,"Coeur")
carte2=Carte.Carte("As","Trèfle")
carte3=Carte.Carte("Valet","Pique")


des_cartes = Carte.Cartes()

#on y ajoute 3 cartes
for une_carte in [carte1,carte2,carte3]:
    des_cartes.ajoute(une_carte)

#des_cartes.ajoute(["Bonjour"]) #pour vérifier le déclenchement de l'erreur à ce niveau

#print(f"{des_cartes = } \n")


# # clonage des cartes
les_memes = Carte.Cartes(des_cartes)
print(f"{les_memes = } \n")


#  On pioche tant que faire se peut
while True:
    try :
        print(f"{des_cartes.pioche() = }")
        print(f"{des_cartes = }")
        print(f"{les_memes = }")
    except ValueError as e:
        print(e)
        break
print("----------fin de programme!----------")


# QUESTION 3: LA CLASSE JEU
un_jeu = Carte.Jeu()

#un_jeu -= Carte.Carte(7,"Coeur")
#un_jeu -= Carte.Carte("As","Pique")
#un_jeu -= Carte.Carte(10,"Trèfle")


# QUESTION 4: LA CLASSE MAIN()
le_jeu = Carte.Jeu()

ma_main = Carte.Main(le_jeu)
ta_main = Carte.Main(le_jeu)
# print(f"{ma_main = }")
# print(f"{ta_main = }")


# # On a joute 3 cartes dans chacune de nos mains
for i in range(3):
    ma_main.complete()
    ta_main.complete()
    print(f"{ma_main = }")
    print(f"{ta_main =}")
#print(f"\n {le_jeu}")

# on tente d'ajouter 25 cartes à la première
try:
    for i in range(25):
        ma_main.complete()
except ValueError as e:
    print(e)

# # on tente d'ajouter 25 cartes à la seconde
try:
    for i in range(25):
        ta_main.complete()
except ValueError as e:
    #traceback.print_exc(file=sys.stdout)
    print(e)

print(f"\n{ma_main = }")
#print(f"\n{ta_main =}")



###### QUESTION 5: CLASSE CARRE

## On recheche tous les carrés contenus dans la main
# while True:
#     try:
#         un_carre = Carte.Carre(ma_main)  # essaie de créer un carré
#         print(f"\n\n{un_carre = } ")  # si on est là, c'est qu'un carré a été créé
#         ma_main -= un_carre   # on l'enlève de la main
#         print(f"\n{ma_main = }")
#     except RuntimeError as e: # si on est là, c'est qu'aucun carré n'a pas pu être créé
#         print(e)
#         break
# print("\n---------- fin du programme! ----------\n")


## QUESTION 6: CLASS QUINTE

# Je n'ai pas bien compris comment faire pour cette question

while True:
    try:
        un_quinte = Carte.Quinte(ma_main)
        print(f"\n\n{un_quinte = } ")  # si on est là, c'est qu'un quinte a été trouvé
        #ma_main -= un_quinte   # on l'enlève de la main
        print(f"\n{ma_main = }")
    except RuntimeError as e: # si on est là, c'est qu'aucun quinte n'a pas pu être formé
        print(e)
        break

print("\n---------- fin du programme! ----------\n")




if __name__=="__main__":
    pass
