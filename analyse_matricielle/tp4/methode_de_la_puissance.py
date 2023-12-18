#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 08:07:27 2023

@author: jngouna
"""

import numpy as np

A = np.array([ [2., 0., 0.],[0., 3., 0.],[0., 0., 7.0] ])

def Puissance(A, N, tol):
    n,m = np.shape(A)
    k = 0
    s = tol+1
    # v = np.repeat(1/np.sqrt(n), n)
    # w = np.repeat(1/np.sqrt(n), n)
    
    v = np.array([3.,0.,2.])
    w = np.array([0.,0.,7.])
    
    while s > tol and k < N:
        v_tilde = np.dot(A, v)
        w_tilde = np.dot(np.transpose(A), w)
        
        mu =  np.dot(v_tilde, v)
        
        r = v_tilde - mu*v
        
        s = np.linalg.norm(r) / abs(np.dot(w,v))
        
        v = v_tilde / np.linalg.norm(v_tilde)
        w = w_tilde / np.linalg.norm(w_tilde)
        
        k +=1
        
    return mu, v, k
        
        
mu, v, k = Puissance(A, 1000, 0.01)   
print("lambda_max :", mu)
print(" u1 : ", v)   
print("k : ",k) 
    





    