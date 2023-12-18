#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 08:12:28 2023

@author: jngouna
"""

import numpy as np

A = np.array([ [4.0, -2.0,1.0],[1.0,-3.0, 2.0],[-1.0, 2.0, 6.0] ])
b = [1.0,2.0,3.0]

def jacobi2(A, b, N, tol):   
    x=np.zeros_like(b) #vecteur nul de même taille que b
    y=np.zeros_like(b) #vecteur nul de même taille que b
    R=np.zeros_like(b)
    p=len(x)
    r=tol+1.
    k=0 #compteur
    bb= np.linalg.norm(b) #la nomre de b
    while r > tol and k < N:
        for i in range(p):
            y[i]=(b[i]-np.dot(A[i,:i],x[:i])-np.dot(A[i,i+1:],x[i+1:]))/A[i,i]
            R[i]=A[i,i]*(x[i]-y[i])
        r=np.linalg.norm(R)/bb
        k=k+1
        x=y.copy()
    return k,x
nb_iteration, res = jacobi2(A,b, 20, 10**-6)
print("Avec Jacobi")
print("Nombre d'itérations : ", nb_iteration)
print('Solution :\n', res)
print()

def GSeidel(A, b, N, tol):
    d,m = np.shape(A)
    x = np.zeros(d)
   # r = np.zeros(d)
    s = tol + 1
    k = 0
    norm_b = np.linalg.norm(b)
    while k < N and s > tol:
        for i in range(0,d):
            x[i] = b[i] - np.dot(A[i,:i],x[:i]) - np.dot(A[i,i+1:],x[i+1:])
            x[i] /= A[i,i]
            
        r = np.dot(A,x) - b    
        s = np.linalg.norm(r) / norm_b
        k +=1
    return k,x

nb_iter, X = GSeidel(A, b, 20, 10**-6)
print("Avec Gauss-Seidel")
print("Nombre d'itérations : ",nb_iter)
print('Solution :\n',X)
#print(np.linalg.solve(A,b))