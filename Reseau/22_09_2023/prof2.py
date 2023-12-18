#!/bin/env python3

import fonction

def profondeur(liste):
    """
    Cette fonction renvoie la profondeur de la liste passée en argument.
    """
    def _profondeur(liste,p):
        nonlocal prof
        for i in liste:
            if type(i)==int:
                if p>prof:
                    prof = p
            else:
                _profondeur(i,p+1)

    prof = float("-inf")
    _profondeur(liste,1)
    return(prof)

if __name__=="__main__":
    # programme principal
    li = fonction.acquisition()
    print( f"{li = }")
    print( f"La profondeur de cette liste est: \t {profondeur(li)}")
