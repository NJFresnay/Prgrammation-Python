#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 15:51:15 2023

@author: jngouna
"""

import numpy as np


# entrées 
Mat1 = np.array([ [2.,1.,1.], [1.,2.,1.], [1.,1.,2.]])
M = np.reshape(Mat1, (3,3))

#Vecteur b
b = np.array([4.,4.,4.])
tb = np.reshape(b,(3,1))

#Algorithme du pivot de gauss


def recherche_pivot(A, b, j):
    p = j
    for i in range(j+1, A.shape[0]):
        if abs(A[i, j]) > abs(A[p, j]):
            p = i
        if p != j:
            b[[p, j]] = b[[j, p]]
            A[[p, j]] = A[[j, p]]
            
def elaguation_vers_le_bas(A, b, j):
    A = np.copy(A)
    b = np.copy(b)
    for i in range(j+1, A.shape[0]):
        b[i] = b[i]  -  (A[i, j] / A[j, j]) * b[j]
        A[i,i] = A[i,i] - (A[i, j] / A[j, j]) * A[j,j]

        
def Gauss1(A, b):
    A_copie = np.copy(A)
    #b= np.transpose(b)
    for j in range(A_copie.shape[1] - 1):
        #recherche_pivot(A_copie, b, j)
        elaguation_vers_le_bas(A_copie, b, j)
    return A_copie

#print("Résultat avec Gauss1\n",  (M,tb))

def elaguation_vers_le_haut(A, b, j):
    for i in range(j):
        b[i] = b[i] - (A[i, j] / A[j, j]) * b[j]
        
def remontee(A,b):
    for j in range(A.shape[0]-1, 0,-1):
        elaguation_vers_le_haut(A, b, j)
        
def resolution_diag(A, b):
    b = np.copy(b)
    for k in range(b.shape[0]):
        b[k] = b[k] / A[k, k]
    return b
        
def Gauss2(A, b):
    A = np.copy(A)
    b = np.copy(b)
    Gauss1(A, b)
    remontee(A, b)
   
    return resolution_diag(A, b)

print("resultat avec Gauss2: \n", Gauss2(M, tb))
print(remontee(M, tb))










