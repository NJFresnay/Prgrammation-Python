#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 09:11:33 2023

@author: jngouna
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def f(x,y): 
    return np.log(1 + x**2 + y**2)

X=np.linspace(-1.5,1.5,500)
Y=np.linspace(-1.5,1.5,500)
XX,YY=np.meshgrid(X,Y)
ZZ=f(XX,YY)
#contour=plt.contour(XX,YY,ZZ,colors='grey')
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')


# Ajout de la ligne de niveau log(2)
plt.contour(XX,YY,ZZ,levels=[np.log(2)],colors='red')

#Ajout d'une tangente 
a=1/2**0.5
plt.arrow(a,a,-a/2,a/2,width = 0.005,head_width=0.05, head_length=0.05)
plt.axis('equal')
plt.arrow(a,a,a/2,-a/2,width = 0.005,head_width=0.05, head_length=0.05)

#gradient
plt.arrow(a,a,a/2,a/2,width = 0.05,head_width=0.05, head_length=0.4)