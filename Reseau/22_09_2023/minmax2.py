#!/bin/env python3

import fonction
import sys, re

def minmax(liste):
    """
    Cette fonction récursive retourne le minmax de la liste passée en argument.
    """
    if type(liste[0])==int:
        maximum.append(max(liste))
    else:
        for i in liste:
            minmax(i)

if __name__=="__main__":
    # programme principal
    li = fonction.acquisition()
    maximum = []
    minmax(li)
    print(min(maximum))










