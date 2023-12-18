#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 08:06:55 2023

@author: jngouna
"""

import numpy as np



A = np.array([ [4.0, -2.0,1.0],[1.0,-3.0, 2.0],[-1.0, 2.0, 6.0] ])
b = [1.0,2.0,3.0]


def Jacobi(A,b,n,tol): # n = nombre max d'itérations
    d,m = np.shape(A)
    k = 0
    x = np.zeros(d)
    y = np.zeros(d)
    r = np.zeros(d)
    s = 1+tol
    while k < n and  s > tol:
        for i in range(0,d):
            y[i] = ( b[i] - np.dot(A[i,:i],x[:i]) - np.dot(A[i,i+1:],x[i+1:]) )
            y[i] /=  A[i,i]
            #r[i] = A[i,i]* (x[i] - y[i])
        s = np.linalg.norm(y - x)
        #s = np.linalg.norm(r) / np.linalg.norm(b)
        k += 1
        x = np.copy(y)
        # si on x=y on fait du gauss-Sciedel
    return k,x
nb_iteration, res = Jacobi(A,b, 1000, 0.001)
print('Solution :', res)
print()
print("Nombre d'itérations : ", nb_iteration)
print(np.linalg.solve(A,b))