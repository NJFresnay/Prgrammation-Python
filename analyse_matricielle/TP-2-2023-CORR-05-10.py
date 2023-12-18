# TP-2-2023 Master DS-MFA

import numpy as np
import scipy.linalg as lg
from time import time
import matplotlib.pyplot as plt

#####################   
# Exercice 1 Resolution de systemes triangulaires
#####################

###### remontee

def remontee(A,b):
    # resout le systeme triangulaire superieur Ax=b
    (n,m)=np.shape(A)
    B=np.copy(b) # pour eviter de modifier b
    for i in range (n-1,-1,-1):# attention au pas et aux extremites. On part de i=n-1 et on arrete à i=0 inclus
        B[i]=B[i]-np.dot(A[i,i+1:n],B[i+1:n]) # attention, on ne change rien quand i=n-1
        B[i]=B[i]/A[i,i]
    return(B)

####### essai en 3x3 triangulaire
A=np.array([[1.,2.,3.],[0,1.,2.],[0,0,1.]])
b=np.array([1.,3.,5.])
b=np.reshape(b,(3,1))
x=remontee(A,b)
print(np.dot(A,x)-b)
np.allclose(np.dot(A,x),b) # verifie que 2 tableaux sont egaux
lg.norm(np.dot(A,x)-b) # calcule la norme euclidienne de Ax-b
#ca marche

n=50 # avec 10 ca va, avec 50 plus du tout des fois (conditionnement) !
A =n*np.random.rand(n,n)
A=np.triu(A)# rend la matrice triangulaire superieure
b = np.random.rand(n,1)
x=remontee(A,b)
print(np.dot(A,x)-b)
np.allclose(np.dot(A,x),b) # verifie que 2 tableaux sont egaux

x2=lg.solve(A,b) # avec solve de numpy.linalg
np.allclose(np.dot(A,x2),b)
print(lg.norm(np.dot(A,x2)-b))

print(lg.norm(x-x2))# comparaison des 2 methodes 

###### descente

def descente(A,b):
    # resout le systeme triangulaire inferieur Ax=b
    (n,m)=np.shape(A)
    B=np.copy(b)
    for i in range (0,n):# attention on part de 0 on s'arrete à n-1
        B[i]=B[i]-np.dot(A[i,0:i],B[0:i])# attention on ne change rien quand i=0
        B[i]=B[i]/A[i,i]
    return B

####### essai de descente
A=np.array([[1.,0,0],[1.,2.,0],[1,2,1]])
b=np.array([1.,3.,5.])
b=np.reshape(b,(3,1))
x=descente(A,b)
np.allclose(np.dot(A,x),b)
#ca marche

