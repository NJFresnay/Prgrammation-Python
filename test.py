import matplotlib.pyplot as plt
import numpy as np


# f(x) = x^2 -4x +3 sur [-2,5]
X = np.linspace(-2, 5, 1001) # pour avoir exactement 1000 segemnts de mm taille
Y = X**2 - 4*X + 3
Z = 5 + 3*np.cos(X)
plt.plot(X,Y, label= " f(x) = x^2 -4x +3")
plt.plot(X,Z, color='forestgreen', label= " g(x) = 5+3cos(x)")
#plt.scatter(1, 0, marker='*', linewidths=3)
#plt.scatter(3, 0, marker='*', linewidths=3)
plt.axhline(y=0, color='red')
#plt.plt(X,0*Y, color='orange)
#plt.(0,1, color='red')
plt.title("Graphiques de f et g sur [-2,5]")
plt.xlabel("abscisses")
plt.ylabel("ordonnées")
plt.legend(loc="upper center")
plt.grid()
plt.show()

