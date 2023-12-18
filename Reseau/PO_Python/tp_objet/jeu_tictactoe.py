#!/bin/env python3

import TicTacToe
import Joueur

jeu = TicTacToe.TicTacToe()
alice = Joueur.Joueur(jeu, 'Alice', 'X')
bob = Joueur.Joueur(jeu, 'Bob', 'O')
joueurs = [alice, bob] #cette liste sera utilisée pour pouvoir afficher le nom du vainqueur

### UNE PARTIE SANS GAGNANT
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

res = jeu.vainqueur()

if ( res == ""):
  print(" Dommage! Aucun gagant.")
else:
  for i in joueurs:
    if (res == i.pion):
        print(f"Félicitations! {i.nom} remporte la partie.")
print("\n------------fin de la partie------------\n")

if __name__ == "__main__":
    pass


