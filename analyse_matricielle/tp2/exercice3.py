#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 08:07:41 2023

@author: jngouna
"""

import numpy as np

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


# ENTREES 
Mat1 = np.array([ [2.,1.,1.], [1.,2.,1.], [1.,1.,2.]])
M = np.reshape(Mat1, (3,3))

b = np.array([4.,4.,4.])
tb = np.reshape(b,(3,1))

def Gauss1_mod(A):
    A_c = np.copy(A)
    for k in range(0, A_c.shape[0]-1):
        for i in range(k+1, A_c.shape[0]):
            coef = - A_c[i,k]/ A_c[k,k]
            A_c[i,k] = - A_c[i,k]/ A_c[k,k]
            A_c[i,:] = A_c[i,:] +  coef* A_c[k,:]
    return A_c

def LU1(A):
    A_c = np.copy(A)
    n,m = np.shape(A_c)
    A_c = Gauss1_mod(A_c)
    U = np.triu(A_c[:,0:n])
    L = np.eye(n)
    for i in range(n):
        for j in range(n):
            if (i>j):
                L[i,j] = A_c[i,j]            
    return L,U
L,U = LU1(M)
# print("Matrice L: \n",L)
# print("\nMatrice U: \n", U)

#print(Gauss1_mod(M))
print()
#LU1(M)

# Construction de la matrice bande A (tridiagonale)
def matrice_bande(n):
    M = np.zeros((n,n))
    for i in range(6):
        for j in range(6):
            if (abs(i-j) == 1):
                M[i,j] = 1
            elif (i == j):
                    M[i,j] = 2
            else:
                M[i,j]=0
    return M

A = matrice_bande(6)

#print("\nLa décomposition LU de la matrice bande A est:\n")
#LU1(A)

# question 3

b = np.ones(4)
b1 = np.reshape(b,(4,1))

def resolution_LU(M,b):
    L,U = LU1(M)
    y = descente(L, b1)
    return remontee(U,y)

#print(resolution_LU(M,b1))


# cholesky

# Exercice4

# def CHdec1(A):
#     Ac= np.copy(A)
#     L,U = LU1(Ac)
#     for i in range(L.shape[0]):
#         #delta =  
#     B = np.dot(L,delta)
#     transposeeB = np.transpose(B)
#     return  B, transposeeB

# #B, TB = CHdec1((M))

# #print(B)
# print(CHdec1((M)))
# #print(TB)










