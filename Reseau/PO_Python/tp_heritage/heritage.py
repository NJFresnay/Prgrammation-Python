#!/bin/env python3

import Stylo, StyloCouleur

un_stylo=Stylo.Stylo()

# for i in range(10):
#   un_stylo.print("seize caractères")

un_stylo_vert = StyloCouleur.StyloCouleur("vert")
un_stylo_vert.print("vert émeraude")


un_stylo_rouge = StyloCouleur.StyloCouleur("rouge")
un_stylo_rouge.print("rouge cerise")

#un_stylo_jaune = StyloCouleur.StyloCouleur("jaune")

if __name__ == "__main__":
    pass
