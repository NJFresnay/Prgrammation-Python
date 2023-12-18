# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 09:51:31 2021

@author: utilisateur
"""

#### EX 1

import numpy as np
import matplotlib.pyplot as plt
#3

def f(x): return (x-2**0.5)**2
x=np.linspace(1,2,100)
plt.plot(x,f(x))

def section(f,a0,b0,tol):
    a=a0
    b=b0
    k=0
    t=(1+5**0.5)/2
    while (b-a)>tol:
        x=a+(b-a)/t**2
        y=a+(b-a)/t
        if f(x)<f(y):
            a,b=a,y
        else :
            a,b=x,b
        k+=1
    return((a+b)/2,k)
section(f,1,2,0.001)


# 4
def f(x) : return -np.exp(np.arctan(x)-np.cos(5*x))

x=np.linspace(0,1,100)
plt.plot(x,f(x))


#5
section(f,0,1,0.001)

def section2(f,a0,b0,tol):
    a=a0
    b=b0
    k=0
    t=(1+5**0.5)/2
    x=np.linspace(a,b,100)
    plt.plot(x,f(x))
    plt.scatter([a,b],[f(a),f(b)])
    while (b-a)>tol:
        x=a+(b-a)/t**2
        y=a+(b-a)/t
        if f(x)<f(y):
            a,b=a,y
        else :
            a,b=x,b
        k+=1
        plt.pause(1)
        plt.scatter([a,b],[f(a),f(b)],c='r')                           
    return((a+b)/2,k)

section2(f,1,2,0.001)

#6 
from scipy.optimize import minimize_scalar
minimize_scalar(f,method='bounded', bounds=(0, 1))
minimize_scalar(f,method='golden',bracket=(0,1))


#ex2
import numpy as np
import matplotlib.pyplot as plt

from scipy.misc import derivative
def newton(f,a,b,h):
    t=np.linspace(a,b,1000)
    plt.plot(t,0*t,'g-')
    plt.plot(t,f(t),'b-')
    u1=b
    c=0
    e=1000
    while e>h:
        u2=u1-f(u1)/derivative(f,u1)
        plt.plot([u1,u2],[f(u1),0],'r-')
        plt.plot([u2,u2],[0,f(u2)],'r--')
        e=abs(u2-u1)
        c+=1
        u1=u2
    return(u2,c)

def f(x):return (x-2**0.5)**2
newton(f,1,2,0.01)



def newton_minimize(f,a,b,h):
    t=np.linspace(a,b,1000)
    plt.plot(t,0*t,'g-')
    plt.plot(t,f(t),'b-')
    u1=b
    c=0
    e=1000
    while e>h:
        u2=u1-derivative(f,u1,n=1)/derivative(f,u1,n=2)
        plt.scatter([u2],[f(u2)])
        e=abs(u2-u1)
        c+=1
        u1=u2
    return(u2,c)

def f(x):return (x-2**0.5)**2
newton_minimize(f,1,2,0.01)

def f(x) : return -np.exp(np.arctan(x)-np.cos(5*x))
newton_minimize(f,0.6,0.8,0.01)


