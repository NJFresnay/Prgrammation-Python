#!/bin/env python3

import fonction

def tri(liste):
    """
    Cette fonction récursive tri la liste passée en argument.
    """
    if type(liste[0])==int:
        liste.sort()
    else:
        for i in liste:
            tri(i)

if __name__=="__main__":
    # programme principal
    li = fonction.acquisition()
    print("\nListe triée : ", tri(li))
