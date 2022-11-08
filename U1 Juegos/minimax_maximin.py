import numpy as np
def cargarValores(cant):
    v1 = []
    for i in range(cant):
        v2 = []
        for j in range(cant):
            print(
                f'ingrese el valor de [{i+1},{j+1}]:')
            pago = int(input())
            v2.append(pago)
        v1.append(v2)
    return v1

print("Ingrese cantidad de alternativas:")
j=int(input())
ma=(cargarValores(j))
minim=[]
max=[]
for i in ma:
  minimos=np.min(i)
  maximos=np.max(i)
  minim.append(minimos)
  max.append(maximos)

maximin=np.max(minim)
minimax=np.min(max)

print("Minimax: ", minimax)
print("Maximin: " ,maximin)

