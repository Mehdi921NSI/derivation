from sympy import *

#Exercice de dérivation:

x = Symbol('x')
L=[]
def derivee(y):
    yprime = y.diff(x)
    print("la dérivée est :", yprime)

for i in range(1):
    a=(input("Entrez la fonction à derivé :"))
    L.append(a)
#print(L)
for a in L:
    print(derivee(a))
    
