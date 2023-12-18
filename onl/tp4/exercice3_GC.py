#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 08:13:10 2023

@author: jngouna
"""

import numpy as np
import matplotlib.pyplot as plt


t = np.array(( 0.038 , 0.194 , 0.425 , 0.626 , 1.253 , 2.500, 3.740) )
y = np.array(( 0.050,0.127,0.094,0.2122,0.2729,0.2665,0.3317))
x_opt = np.array((0.362,0.556))
x0 = np.array((0.9,0.2))

#print(x0)

def v(t,x):
    return (x[0]*t)/(x[1]+t)


# plt.scatter(t,y)
# plt.plot(t,v(t,x0), c="green",label="xO")
# plt.plot(t, v(t,x_opt),c="red",label="x_opt")
# plt.legend()


#### question2
def r(x):
    return y - v(t,x)

def J(x):
    return np.array((-t/(x[1]+t), x[0]*t/(x[1]+t)**2)).T

def GN(x0, tol):
    x, k = x0, 0
    T = np.array([x])
    while np.linalg.norm( r(x).dot(J(x))) > tol and k <100 :
        x = x - np.linalg.inv(np.transpose(J(x)).dot(J(x))).dot(np.transpose(J(x)).dot(r(x)))
        T,k = np.append(T, [x], axis=0), k+1
    return T, k

#GN(x0, 0.00001)


t = np.arange(0,22,2)
x_opt= np.array((5,0.1,0.1))

def m(t,x):
    return x[0]*np.exp(-x[1]*t)*np.sin(x[2]*2*np.pi*t)

y = m(t,x_opt) + np.random.randn(11)*0.1


plt.scatter(t,y,c='k')
plt.plot(t, m(t,x_opt))


#### question3
def r(x):
    return y - m(t,x)

def J(x):
    return 













