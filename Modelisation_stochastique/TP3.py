#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 14:06:47 2023

@author: jngouna
"""

import numpy as np
import matplotlib.pyplot as plt

def F(x,beta):
    return np.exp(beta*x)
    

def MC(beta,N):
    y = 0
    for i in range(N):
       x = np.random.randn()
       y += F(x,beta)   
    return y/N


def MC_graphe(beta,N):
    y_bar=0;y_carre=0
    y = 0 
    res = []
   #var = []
    for i in range(N):
       x = np.random.randn()
       y  +=  F(x,beta)
       res.append(y/(i+1))
       y_bar += y
       y_carre  += y**2
       
    var = (1/N)*y_carre - (y_bar/N)**2
#    plt.plot(np.arange(N),res,linestyle='--', label=f'Approximation avec beta={beta}')
#    plt.legend()
   #plt.close()
    return var
    
print(MC_graphe(1,10**4))
       
  
def MC_avec_VC(beta,N,alpha=0.05):
    # I_inf =  MC(beta,N) - 1.96*( MC_graphe(beta, N) )/np.sqrt(N)
    # I_max = MC(beta,N) + 1.96*( MC_graphe(beta, N) )/np.sqrt(N)
    k = 0; y = 0; res = []; y_bar=0;y_carre=0
    rho = 1
    # len_IC = (I_inf+I_max)/2 #taille de IC
    resVC = []
    Sk = 0
    SC = 0
    SVC = 0
    SANTIT= 0
    # s_Sk= []
    # s_SC= []
    s_SVC = []
    s_SANTIT = []
    
    # while len_IC > rho and k < N:
    k +=1
    for i in range(N):
       x = np.random.randn()
       Xk = F(x,beta)
       Xkprime = np.exp(beta*x)
       res.append(y/(i+1))
       y_bar += y
       y_carre += y**2
       Sk += Xk
       SC += Xkprime**2
       SVC = Xk - Xkprime
       SANTIT = 0.5 * ( Xk + np.exp(-beta*Xk))
       # s_Sk.append(Sk/(i+1))
       # s_SC.append(SC/(i+1))
       s_SVC.append(SVC/(i+1))
       s_SANTIT.append(SANTIT/(i+1))
       
              
    var = (1/N-1)*y_carre - N/(N-1) * (y_bar/N)**2
    var_VC = (1/N-1)*SVC- N/(N-1) *(SVC/N)**2
    var_ANTI = (1/N-1)*SANTIT- N/(N-1) *(SANTIT/N)**2
    print('Estimation :',y/N)
    print('La variance empirique est égale à',var)
    print('La RMSE est égale à',np.sqrt(var))
    estimvc=sVC/n+np.exp(beta**2/2)
    print('Estimation avec variable de controle :',estimvc)
    print('La variance empirique avec variable de controle est égale à',varVC)
    print('La RMSE avec VC est égale à',np.sqrt(varVC))
    print('Estimation avec antithétique:',santi/n)
    print('La variance empirique avec antithétique est égale à',varanti)
    print('La RMSE avec antithétique est égale à',np.sqrt(varanti))
        
    
    plt.plot(np.arange(N),res,linestyle='--', label=f'Approximation avec beta={beta}')
    
    plt.legend()    
        
    
  
      