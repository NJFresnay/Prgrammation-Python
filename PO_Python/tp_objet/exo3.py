#!/bin/env python3

class C:
  """
    Ceci est classe vide
  """
  pass

if __name__=="__main__":
  c = C()
  print(f"{c.__class__.__name__=}\n", # retourne le nom de la classe
        f"{c.__dict__=}\n",
        f"{c.__init__=}\n",
        f"{c.__doc__=}\n", # récupère la documentation d'une fonction'
        f"{dir(c)=}")
