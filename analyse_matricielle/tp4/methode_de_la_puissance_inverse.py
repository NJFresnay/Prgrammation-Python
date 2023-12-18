#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 08:07:27 2023

@author: jngouna
"""

import numpy as np

A = np.array([ [2., 0., 0.],[0., 3., 0.],[0., 0. , 7.0] ])

def PuissanceInv(A, N, tol):
    n,m = np.shape(A)
    k = 0
    s = tol+1
    w_tilde = np.zeros_like(n)
    v = np.array([3.,0.,2.])
    w = np.array([0.,0.,7.])
    
    while s > tol and k < N:
        v_tilde = np.linalg.solve(A, v)
        w_tilde = np.linalg.solve(A.T, w)
        
        mu =  np.dot(v_tilde, v)
        
        r = v_tilde - mu*v
        
        s = np.linalg.norm(r) / abs(np.dot(w,v))
        
        v = v_tilde / np.linalg.norm(v_tilde)
        w = w_tilde / np.linalg.norm(w_tilde)
        
        k +=1
        
    return 1/mu, v, k
        
        
mu_inv, v, k = PuissanceInv(A, 1000, 0.01)   
print("lambda_min :", mu_inv)
print(" u1 : ", v)   
print("k : ",k) 
    





    