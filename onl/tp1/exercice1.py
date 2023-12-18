#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 08:03:44 2023

@author: jngouna
"""

import numpy as np
import matplotlib.pyplot as plt

 ## LES COURBES DE NIVEAU
 
def f(x, y):
    return np.sin(x)**10 + np.cos(x*y) * np.cos(x)
    
    
    
# X = np.linspace(0,5,1000)
# Y = np.linspace(0,5,1000)
# XX, YY = np.meshgrid(X,Y)  #construction de la grille

# # tableau contenant les valeurs de la grille
# ZZ = f(XX,YY)

# # Construction des courbes de niveau
# contour = plt.contour(XX,YY,ZZ,colors='k')

# # Interpretation des commandes
# plt.clabel(contour,inline=True, fontsize=8) # pour afficher les lignes de niveau

# plt.imshow(ZZ, extent=[0, 5, 0, 5], origin="lower",cmap="RdGy", alpha=0.5)
# plt.colorbar()
# plt.show()


# la fonction niveau
def niveau(f,a,b,c,d,ortho=False,valeur=False):
    X=np.linspace(a,b,500)
    Y=np.linspace(c,d,500)
    XX,YY=np.meshgrid(X,Y)
    ZZ=f(XX,YY)
    contour=plt.contour(XX,YY,ZZ,colors='grey')
    if valeur==True : 
        plt.clabel(contour,inline=True, fontsize=8)
    if ortho==True : 
        plt.axis("equal") # pour le repère orthonormée
    plt.xlabel('x')
    plt.ylabel('y')

print(niveau(f,0,5,0,5))


