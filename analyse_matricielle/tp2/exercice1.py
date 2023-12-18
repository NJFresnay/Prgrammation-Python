#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 08:09:46 2023

@author: jngouna
"""

import numpy as np
from numpy import linalg as la

#initialisation de M
# M = [ [0 for i in range(n)] for j in range(m) ]
# M = np.reshape(M,(3,3))
# M = np.zeros(shape=(m,n))

# #remplissage de M1
# for i in range(m):
#     for j in range(n):
#         M[i][j] = float(input("Saisissez l'element: "))


# Mat = np.array([ [1.,2.,3.], [0.,1.,2.], [0.,0.,1.]])
# M =np.reshape(Mat, (3,3))

Mat1 = np.array([ [1.,0.,0.], [1.,2.,0.], [1.,2.,3.]])
M1 = np.reshape(Mat1, (3,3))

#Vecteur b
b = np.array([1.,3.,3.])
#transposée de b
tb = np.reshape(b,(3,1))

print("M = ", M1)
#print(np.shape(M))
print('\nb = ', tb)    
 
def remontee(A,b):
    # resout le systeme triangulaire superieur Ax=b
    (n,m)=np.shape(A)
    B=np.copy(b) # pour eviter de modifier b
    for i in range (n-1,-1,-1):# attention au pas et aux extremites. On part de i=n-1 et on arrete à i=0 inclus
        B[i]=B[i]-np.dot(A[i,i+1:n],B[i+1:n]) # attention, on ne change rien quand i=n-1
        B[i]=B[i]/A[i,i]
    return(B)
    
def descente(M1, tb):
    l,c = np.shape(M1)
    tb2  =  np.copy(tb)
    for j in range(0,c): 
            tb2[j] = tb2[j] - np.dot(M1[j, 0:j], tb2[0:j])
            tb2[j] = tb2[j] / M1[j,j]
    return tb2


#verification
triangulaire = True
for i in range(3):
    for j in range(3):
        if( i > j):
            if ( M1[i][j] != 0):
                triangulaire = False
                break

if(triangulaire == True):
    print("\nLa matrice est bien triangulaire supérieure.")
    #print("\nLa solution du système est:\n",remontee(M, tb))
    #print("\nRésultat obtenu par python:\n", la.solve(M, tb))

else:
    print("\nLa matrice n'est pas triangulaire supérieure:")
    print("\nLa solution du système est:\n",descente(M1, tb))
    print("\nRésultat obtenu par python:\n", la.solve(M1, tb))
      
    
    
    
    
# def remontee(M, tb):
#     l,c = np.shape(M)
#     tb1  =  np.copy(tb)
#     for i in range(l-1):
#         for j in range(i,-1,-1):
#             tb1[j] = tb1[j] - (M[j][i]/M[i][i])*tb1[i]
#     return tb1  