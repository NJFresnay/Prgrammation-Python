#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 12:30:19 2023

@author: jngouna
"""

import numpy as np
import scipy.linalg as lg

def MatriceA(n, tau):
    A = np.eye(n)
    for j in range(n):
        for i in range(n-j):
          A[i,i+j] = 1 / ( 1 + (j*tau)**2 )   
          A[i+j,i] = 1 / ( 1 + (j*tau)**2 ) 
    return A

A = MatriceA(4, 1)


def MatriceToeplitz(t):
    n = len(t)
    T = np.eye(n)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if abs(j-i) == k:
                    T[i,j]= t[k]               
    return T


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


def resolution_LU(M,b):
    L,U = LU(M)
    y = descente(L, b)
    return remontee(U,y)


def LU(A) :
    (n,m)=np.shape(A)
    L=np.eye(n)
    U=np.zeros_like(A)
    for j in range(0,n):
        for k in range(j,n):  # boucle sur U
            U[j,k]=A[j,k]-np.dot(L[j,0:j],U[0:j,k])
        for k in range(j+1,n):  # boucle sur L
            L[k,j]=(A[k,j]-np.dot(L[k,0:j],U[0:j,j]))/U[j,j]
    return [L,U]  

L,U = LU(A)
#print("L : \n", L)

#print("\n\nU : \n", U

print(resolution_LU()) 





print(remontee(U, [1.,1.,1.,1.]))

#rint(lg.lu(A))


#print(remontee(A, [1.,1.,1.,1.]))

###### Matrice Toeplitz

def MatriceToeplitz(t):
    n = len(t)
    T = np.eye(n)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if abs(j-i) == k:
                    T[i,j]= t[k]               
    return T









def Etape1(t):
    T = MatriceToeplitz(t)
    n,m = np.shape((T))
    y = np.zeros(n)
    S = np.zeros_like(y)
    f = np.zeros_like(y)
    
t = np.array([1,2,3,4,5])


                    
            
    
    

