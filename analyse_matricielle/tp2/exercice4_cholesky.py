#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 08:08:23 2023

@author: jngouna
"""

import numpy as np
#import linalg as lg


Mat1 = np.array([[2.,1.,1.], [1.,2.,1.], [1.,1.,2.]])
M = np.reshape(Mat1, (3,3))

def QRdec(A):
    """Réalise la decomposition QR de A"""
    (n,m) = np.shape(A)
    Q = np.zeros((n,n))
    R = np.zeros_like(A)
    c = np.array([[0.,0.,0.]])
    # q = 
    # for j in range(m): 
        
        
            
        
    # return n

print(QRdec(M))