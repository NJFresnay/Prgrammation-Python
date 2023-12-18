#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 08:47:08 2023

@author: jngouna
"""

import numpy as np

A = np.array([ [4.0, -2.0,1.0],[1.0,-3.0, 2.0],[-1.0, 2.0, 6.0] ])
b = [1.0,2.0,3.0]

def SOR(A,b, omega, N, tol):
    n,m = np.shape(A)
    x=np.zeros_like(b)
    y=np.zeros_like(b)
    stop = tol +1
    k = 0 
    while k < N and stop > tol:
        for i in range(0,n):
            y[i] = omega*b[i] + (1-omega)*A[i,i]*x[i] - omega*np.dot(A[i,:i],y[:i]) - omega*np.dot(A[i,i+1:],x[i+1:])
            y[i] /= A[i,i]
            
        stop = np.linalg.norm(y-x)
        k=k+1
        x=y.copy()
    return k, x
k, res = SOR(A,b,0.95, 1000, 10**-6)
print("Avec la methode de relaxation")
print("Nombre d'itérations : ", k)
print('Solution :\n', res)
print()
print(np.linalg.solve(A,b))