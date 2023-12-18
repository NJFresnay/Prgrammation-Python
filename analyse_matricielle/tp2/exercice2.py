#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 17:01:19 2023

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

# entrées 
Mat1 = np.array([ [2.,1.,1.], [1.,2.,1.], [1.,1.,2.]])
M = np.reshape(Mat1, (3,3))

b = np.array([4.,4.,4.])
tb = np.reshape(b,(3,1))

#concatenation de la matrice et du vecteur
M_b = np.concatenate((M,tb), axis=1)
#print(M_b)

#triangularisation par la methode de Gauss
def Gauss1(A):
    A_c = np.copy(A)
    for k in range(0, A_c.shape[0]-1):
        for i in range(k+1, A_c.shape[0]):
            coef = - A_c[i,k]/ A_c[k,k]
            #A_c[i,k] = - A_c[i,k]/ A_c[k,k]
            A_c[i,:] = A_c[i,:] +  coef* A_c[k,:]
            #A_c[i,:] = A_c[i,:] +  A_c[i,k]* A_c[k,:]
    return A_c

def Gauss2(A, b):
    A_x = Gauss1(A)
    T = A_x[:, :-1]
    b = A_x[:, 3]   
    return T, remontee(T,b)
    
print(Gauss1(M_b))
print("\nResultat:")
print(Gauss2(M_b, tb))