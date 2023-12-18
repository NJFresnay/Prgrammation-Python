#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 08:54:26 2023

@author: jngouna
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# Z = np.linspace(0, 15, 1000)
# X = np.cos(Z)
# Y = np.sin(Z)

# ax=plt.axes(projection='3d')
# ax.plot3D(X,Y,Z, "grey")
# ax.set_xlabel('x');ax.set_ylabel('y');ax.set_zlabel('z')

# Simulation de 100 points

Z = np.random.uniform(0,15,100)
X = np.cos(Z) + np.random.randn(100)*0.1
Y = np.sin(Z)+ np.random.randn(100)*0.1
ax=plt.axes(projection='3d')
ax.scatter3D(X,Y,Z,c = Z)
ax.set_xlabel('x');ax.set_ylabel('y');ax.set_zlabel('z')

Z = np.linspace(0, 15, 1000)
X = np.cos(Z)
Y = np.sin(Z)
ax.plot3D(X,Y,Z, "red")
