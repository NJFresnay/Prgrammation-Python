#!/bin/env python3

import Adresse

ad1 = Adresse.AdresseIP(10,0,0,1)
ad2 = Adresse.AdresseIP(171,19,45,1)
ad3 = Adresse.AdresseIP(192,168,0,1)

print("Classe ad1 : ",ad1.classe())
print("réseau ad1: ",ad1.reseau())
print("équipement ad1: ", ad1.equipement())
print("\nClasse ad2 : ",ad2.classe())
print("réseau ad2: ",ad2.reseau())
print("équipement ad2: ", ad2.equipement())
print("\nClasse ad3 : ",ad3.classe())
print("réseau ad3: ",ad3.reseau())
print("équipement ad3: ", ad3.equipement())

if __name__=="__main__":
    pass
