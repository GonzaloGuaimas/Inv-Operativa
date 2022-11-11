from re import A
import nashpy as nash
import numpy as np


print("Ingrese cantidad de estrategias jugador N°1: ")
n1=int(input())

print("Ingrese cantidad de estrategias jugador N°2: ")
n2=int(input())

A=[]
B=[]

for i in range (0,n1,1):
  f1=[]
  for j in range (0,n2,1):
    print("Ingrese el valor de la posicion",i+1,j+1,"para jugador 1 o por fila")
    a=float(input())
    f1.append(a)
  A.append(f1)

for i in range (0,n1,1):
  f1=[]
  for j in range (0,n2,1):
    print("Ingrese el valor de la posicion",i+1,j+1,"para jugador 2 o por colummna")
    a=float(input())
    f1.append(a)
  B.append(f1)

A1=np.array(A)
B1=np.array(B)
matching_pennies = nash.Game(A1,B1)
matching_pennies
equilibria = matching_pennies.support_enumeration()
for eq in equilibria:
    print(eq)