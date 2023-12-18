#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 08:25:30 2023

@author: jngouna
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def f(x, y):
    return np.sin((x**2 + y**2)**1/2)


# X = np.linspace(-6,6,500)
# Y = np.linspace(-6,6,500)
# XX, YY = np.meshgrid(X,Y)  #construction de la grille

# # tableau contenant les valeurs de la grille
# ZZ = f(XX,YY)

# # # Construction des courbes de niveau
# contour = plt.contour(XX,YY,ZZ,colors='k')

# # # Interpretation des commandes
# plt.clabel(contour,inline=True, fontsize=8) # pour afficher les lignes de niveau

# plt.imshow(ZZ, extent=[-6, 6, -6, 6], origin="lower",cmap="RdGy", alpha=0.5)
# #plt.colorbar()
# plt.axis('equal')
# plt.show()


# la fonction niveau pour tracer nos courbes de niveau
def niveau(f,a,b,c,d,ortho=True,valeur=False):
    X=np.linspace(a,b,500)
    Y=np.linspace(c,d,500)
    XX,YY=np.meshgrid(X,Y)
    ZZ=f(XX,YY)
    contour=plt.contour(XX,YY,ZZ,colors='grey')
    if valeur==True : 
        plt.clabel(contour,inline=True, fontsize=8)
    if ortho==True : 
        plt.axis("equal")
    plt.xlabel('x')
    plt.ylabel('y')

#print(niveau(f,-6,6,-6,6))


# représentation en 3D
#ax = plt.axes(projection='3d')

X = np.linspace(-6,6,500)
Y = np.linspace(-6,6,500)
XX, YY = np.meshgrid(X,Y)
ZZ = f(XX,YY)
# ax.plot_wireframe(XX, YY, ZZ, linewidth=0.5,color="grey") # surface en 3D
# plt.show()

ax=plt.axes(projection='3d')
ax.plot_surface(XX, YY, ZZ, cmap="viridis")
ax.plot_surface(XX, YY, ZZ, alpha=0.25, edgecolor="red", linewidth=0.3)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.contour(XX, YY, ZZ, zdir="x", offset=+7)
ax.contour(XX, YY, ZZ, zdir="y", offset=-7)
ax.contour(XX, YY, ZZ, zdir="z", offset=+1)