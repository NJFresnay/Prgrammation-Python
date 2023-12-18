#!/bin/env python3

import TicTacToe
import Joueur

jeu = TicTacToe.TicTacToe()
alice = Joueur.Joueur(jeu, 'Alice', 'X')
bob = Joueur.Joueur(jeu, 'Bob', 'O')

## UNE PARTIE SANS GAGNANT
alice.joue(1,1)
bob.joue(1,3)
print(jeu)
alice.joue(1,2)
bob.joue(2,2)
print(jeu)
alice.joue(2,3)
bob.joue(2,1)
print(jeu)
alice.joue(3,1)
bob.joue(3,2)
print(jeu)
alice.joue(3,3)
#bob.joue(1,2)
print(jeu)

###  UNE PARTIE AVEC UN GAGNANT!
# alice.joue(1,1)
# bob.joue(1,3)
# print(jeu)
# alice.joue(2,1)
# bob.joue(1,2)
# print(jeu)
# alice.joue(2,2)
# bob.joue(2,3)
# print(jeu)
# alice.joue(3,3)
# bob.joue(3,2)
# print(jeu)

# nom1 = input("Nom du joueur 1: ")
# nom2 = input("Nom du joueur 2: ")
# pion1 = input(f"Pion du joueur {nom1}: ")
# pion2 = input(f"Pion du joueur {nom2}: ")
# alice = Joueur.Joueur(jeu, nom1, pion1)
# bob = Joueur.Joueur(jeu, nom2, pion2)
joueurs = [alice, bob]
# print("\nLe jeu peut commencer!\n\nChaque joueur spécifie la position de son pion (sous la forme x,y)\n")
#
# count = 0
# while (count < 4):
#   alice.nom = nom1
#   bob.nom = nom2
#   alice.pion = pion1
#   bob.pion = pion2
#   print(f"Tour {count+1}")
#   pos1 = input(f"Joueur {alice.nom} :  ")
#   alice.joue(pos1[0], pos1[2])
#   pos2 = input(f"Joueur {bob.nom} :  ")
#   bob.joue(pos2[0], pos2[2])
#   print(jeu)
#   count+=1
# #print(jeu)
res = jeu.vainqueur()
for i in joueurs:
    if (res == i.pion):
        print("le vainqueur de l partie est :", i.nom)
print("Aucun vainqueur pour cette manche!")


if __name__ == "__main__":
    pass

