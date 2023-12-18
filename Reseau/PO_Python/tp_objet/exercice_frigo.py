#!/bin/env python3

import Frigo
import Recette

un_frigo = Frigo.Frigo({})
#print(un_frigo.etat())

un_frigo1= Frigo.Frigo({})
#print(un_frigo1.etat())

dict1 = {
        "oeufs": 6
        , "beurre": 250
        , "yaourt": 6
        , "fraise": 25
        }

un_frigo1.depose(dict1)
un_frigo1.depose({
        "oeufs": 12
        , "beurre": 250
        , "yaourt": 6
        , "prunes": 4
        })
print(un_frigo1.etat())

tarte_aux_fraises = Recette.Recette({
        "oeufs": 2
        , "beurre": 100
        , "fraise": 10
})

# for i, j in tarte_aux_fraises.items():
#     print(i, " ", j)
print("A-t-on les éléments en quantité nécessaire dans notre frigo?")
print(tarte_aux_fraises.isPresent(un_frigo1))

print(un_frigo1.extraire(tarte_aux_fraises))


if __name__=="__main__":
    pass
